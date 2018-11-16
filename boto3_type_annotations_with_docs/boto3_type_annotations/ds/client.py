from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def accept_shared_directory(self, SharedDirectoryId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/AcceptSharedDirectory>`_
        
        **Request Syntax** 
        ::
        
          response = client.accept_shared_directory(
              SharedDirectoryId=\'string\'
          )
        :type SharedDirectoryId: string
        :param SharedDirectoryId: **[REQUIRED]** 
        
          Identifier of the shared directory in the directory consumer account. This identifier is different for each directory owner account. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SharedDirectory\': {
                    \'OwnerAccountId\': \'string\',
                    \'OwnerDirectoryId\': \'string\',
                    \'ShareMethod\': \'ORGANIZATIONS\'|\'HANDSHAKE\',
                    \'SharedAccountId\': \'string\',
                    \'SharedDirectoryId\': \'string\',
                    \'ShareStatus\': \'Shared\'|\'PendingAcceptance\'|\'Rejected\'|\'Rejecting\'|\'RejectFailed\'|\'Sharing\'|\'ShareFailed\'|\'Deleted\'|\'Deleting\',
                    \'ShareNotes\': \'string\',
                    \'CreatedDateTime\': datetime(2015, 1, 1),
                    \'LastUpdatedDateTime\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SharedDirectory** *(dict) --* 
        
              The shared directory in the directory consumer account.
        
              - **OwnerAccountId** *(string) --* 
        
                Identifier of the directory owner account, which contains the directory that has been shared to the consumer account.
        
              - **OwnerDirectoryId** *(string) --* 
        
                Identifier of the directory in the directory owner account. 
        
              - **ShareMethod** *(string) --* 
        
                The method used when sharing a directory to determine whether the directory should be shared within your AWS organization (``ORGANIZATIONS`` ) or with any AWS account by sending a shared directory request (``HANDSHAKE`` ).
        
              - **SharedAccountId** *(string) --* 
        
                Identifier of the directory consumer account that has access to the shared directory (``OwnerDirectoryId`` ) in the directory owner account.
        
              - **SharedDirectoryId** *(string) --* 
        
                Identifier of the shared directory in the directory consumer account. This identifier is different for each directory owner account.
        
              - **ShareStatus** *(string) --* 
        
                Current directory status of the shared AWS Managed Microsoft AD directory.
        
              - **ShareNotes** *(string) --* 
        
                A directory share request that is sent by the directory owner to the directory consumer. The request includes a typed message to help the directory consumer administrator determine whether to approve or reject the share invitation.
        
              - **CreatedDateTime** *(datetime) --* 
        
                The date and time that the shared directory was created.
        
              - **LastUpdatedDateTime** *(datetime) --* 
        
                The date and time that the shared directory was last updated.
        
        """
        pass

    def add_ip_routes(self, DirectoryId: str, IpRoutes: List, UpdateSecurityGroupForDirectoryControllers: bool = None) -> Dict:
        """
        
        Before you call *AddIpRoutes* , ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the *AddIpRoutes* operation, see `AWS Directory Service API Permissions\: Actions, Resources, and Conditions Reference <http://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/AddIpRoutes>`_
        
        **Request Syntax** 
        ::
        
          response = client.add_ip_routes(
              DirectoryId=\'string\',
              IpRoutes=[
                  {
                      \'CidrIp\': \'string\',
                      \'Description\': \'string\'
                  },
              ],
              UpdateSecurityGroupForDirectoryControllers=True|False
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          Identifier (ID) of the directory to which to add the address block.
        
        :type IpRoutes: list
        :param IpRoutes: **[REQUIRED]** 
        
          IP address blocks, using CIDR format, of the traffic to route. This is often the IP address block of the DNS server used for your on-premises domain.
        
          - *(dict) --* 
        
            IP address block. This is often the address block of the DNS server used for your on-premises domain. 
        
            - **CidrIp** *(string) --* 
        
              IP address block using CIDR format, for example 10.0.0.0/24. This is often the address block of the DNS server used for your on-premises domain. For a single IP address use a CIDR address block with /32. For example 10.0.0.0/32.
        
            - **Description** *(string) --* 
        
              Description of the address block.
        
        :type UpdateSecurityGroupForDirectoryControllers: boolean
        :param UpdateSecurityGroupForDirectoryControllers: 
        
          If set to true, updates the inbound and outbound rules of the security group that has the description: \"AWS created security group for *directory ID* directory controllers.\" Following are the new rules: 
        
          Inbound:
        
          * Type: Custom UDP Rule, Protocol: UDP, Range: 88, Source: 0.0.0.0/0 
           
          * Type: Custom UDP Rule, Protocol: UDP, Range: 123, Source: 0.0.0.0/0 
           
          * Type: Custom UDP Rule, Protocol: UDP, Range: 138, Source: 0.0.0.0/0 
           
          * Type: Custom UDP Rule, Protocol: UDP, Range: 389, Source: 0.0.0.0/0 
           
          * Type: Custom UDP Rule, Protocol: UDP, Range: 464, Source: 0.0.0.0/0 
           
          * Type: Custom UDP Rule, Protocol: UDP, Range: 445, Source: 0.0.0.0/0 
           
          * Type: Custom TCP Rule, Protocol: TCP, Range: 88, Source: 0.0.0.0/0 
           
          * Type: Custom TCP Rule, Protocol: TCP, Range: 135, Source: 0.0.0.0/0 
           
          * Type: Custom TCP Rule, Protocol: TCP, Range: 445, Source: 0.0.0.0/0 
           
          * Type: Custom TCP Rule, Protocol: TCP, Range: 464, Source: 0.0.0.0/0 
           
          * Type: Custom TCP Rule, Protocol: TCP, Range: 636, Source: 0.0.0.0/0 
           
          * Type: Custom TCP Rule, Protocol: TCP, Range: 1024-65535, Source: 0.0.0.0/0 
           
          * Type: Custom TCP Rule, Protocol: TCP, Range: 3268-33269, Source: 0.0.0.0/0 
           
          * Type: DNS (UDP), Protocol: UDP, Range: 53, Source: 0.0.0.0/0 
           
          * Type: DNS (TCP), Protocol: TCP, Range: 53, Source: 0.0.0.0/0 
           
          * Type: LDAP, Protocol: TCP, Range: 389, Source: 0.0.0.0/0 
           
          * Type: All ICMP, Protocol: All, Range: N/A, Source: 0.0.0.0/0 
           
          Outbound:
        
          * Type: All traffic, Protocol: All, Range: All, Destination: 0.0.0.0/0 
           
          These security rules impact an internal network interface that is not exposed publicly.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def add_tags_to_resource(self, ResourceId: str, Tags: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/AddTagsToResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.add_tags_to_resource(
              ResourceId=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          Identifier (ID) for the directory to which to add the tag.
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          The tags to be assigned to the directory.
        
          - *(dict) --* 
        
            Metadata assigned to a directory consisting of a key-value pair.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              Required name of the tag. The string value can be Unicode characters and cannot be prefixed with \"aws:\". The string can contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The optional value of the tag. The string value can be Unicode characters. The string can contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
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

    def cancel_schema_extension(self, DirectoryId: str, SchemaExtensionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/CancelSchemaExtension>`_
        
        **Request Syntax** 
        ::
        
          response = client.cancel_schema_extension(
              DirectoryId=\'string\',
              SchemaExtensionId=\'string\'
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The identifier of the directory whose schema extension will be canceled.
        
        :type SchemaExtensionId: string
        :param SchemaExtensionId: **[REQUIRED]** 
        
          The identifier of the schema extension that will be canceled.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def connect_directory(self, Name: str, Password: str, Size: str, ConnectSettings: Dict, ShortName: str = None, Description: str = None) -> Dict:
        """
        
        Before you call ``ConnectDirectory`` , ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the ``ConnectDirectory`` operation, see `AWS Directory Service API Permissions\: Actions, Resources, and Conditions Reference <http://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/ConnectDirectory>`_
        
        **Request Syntax** 
        ::
        
          response = client.connect_directory(
              Name=\'string\',
              ShortName=\'string\',
              Password=\'string\',
              Description=\'string\',
              Size=\'Small\'|\'Large\',
              ConnectSettings={
                  \'VpcId\': \'string\',
                  \'SubnetIds\': [
                      \'string\',
                  ],
                  \'CustomerDnsIps\': [
                      \'string\',
                  ],
                  \'CustomerUserName\': \'string\'
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The fully qualified name of the on-premises directory, such as ``corp.example.com`` .
        
        :type ShortName: string
        :param ShortName: 
        
          The NetBIOS name of the on-premises directory, such as ``CORP`` .
        
        :type Password: string
        :param Password: **[REQUIRED]** 
        
          The password for the on-premises user account.
        
        :type Description: string
        :param Description: 
        
          A textual description for the directory.
        
        :type Size: string
        :param Size: **[REQUIRED]** 
        
          The size of the directory.
        
        :type ConnectSettings: dict
        :param ConnectSettings: **[REQUIRED]** 
        
          A  DirectoryConnectSettings object that contains additional information for the operation.
        
          - **VpcId** *(string) --* **[REQUIRED]** 
        
            The identifier of the VPC in which the AD Connector is created.
        
          - **SubnetIds** *(list) --* **[REQUIRED]** 
        
            A list of subnet identifiers in the VPC in which the AD Connector is created.
        
            - *(string) --* 
        
          - **CustomerDnsIps** *(list) --* **[REQUIRED]** 
        
            A list of one or more IP addresses of DNS servers or domain controllers in the on-premises directory.
        
            - *(string) --* 
        
          - **CustomerUserName** *(string) --* **[REQUIRED]** 
        
            The user name of an account in the on-premises directory that is used to connect to the directory. This account must have the following permissions:
        
            * Read users and groups 
             
            * Create computer objects 
             
            * Join computers to the domain 
             
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DirectoryId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the results of the  ConnectDirectory operation.
        
            - **DirectoryId** *(string) --* 
        
              The identifier of the new directory.
        
        """
        pass

    def create_alias(self, DirectoryId: str, Alias: str) -> Dict:
        """
        
        .. warning::
        
          After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/CreateAlias>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_alias(
              DirectoryId=\'string\',
              Alias=\'string\'
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The identifier of the directory for which to create the alias.
        
        :type Alias: string
        :param Alias: **[REQUIRED]** 
        
          The requested alias.
        
          The alias must be unique amongst all aliases in AWS. This operation throws an ``EntityAlreadyExistsException`` error if the alias already exists.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DirectoryId\': \'string\',
                \'Alias\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the results of the  CreateAlias operation.
        
            - **DirectoryId** *(string) --* 
        
              The identifier of the directory.
        
            - **Alias** *(string) --* 
        
              The alias for the directory.
        
        """
        pass

    def create_computer(self, DirectoryId: str, ComputerName: str, Password: str, OrganizationalUnitDistinguishedName: str = None, ComputerAttributes: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/CreateComputer>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_computer(
              DirectoryId=\'string\',
              ComputerName=\'string\',
              Password=\'string\',
              OrganizationalUnitDistinguishedName=\'string\',
              ComputerAttributes=[
                  {
                      \'Name\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The identifier of the directory in which to create the computer account.
        
        :type ComputerName: string
        :param ComputerName: **[REQUIRED]** 
        
          The name of the computer account.
        
        :type Password: string
        :param Password: **[REQUIRED]** 
        
          A one-time password that is used to join the computer to the directory. You should generate a random, strong password to use for this parameter.
        
        :type OrganizationalUnitDistinguishedName: string
        :param OrganizationalUnitDistinguishedName: 
        
          The fully-qualified distinguished name of the organizational unit to place the computer account in.
        
        :type ComputerAttributes: list
        :param ComputerAttributes: 
        
          An array of  Attribute objects that contain any LDAP attributes to apply to the computer account.
        
          - *(dict) --* 
        
            Represents a named directory attribute.
        
            - **Name** *(string) --* 
        
              The name of the attribute.
        
            - **Value** *(string) --* 
        
              The value of the attribute.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Computer\': {
                    \'ComputerId\': \'string\',
                    \'ComputerName\': \'string\',
                    \'ComputerAttributes\': [
                        {
                            \'Name\': \'string\',
                            \'Value\': \'string\'
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the results for the  CreateComputer operation.
        
            - **Computer** *(dict) --* 
        
              A  Computer object that represents the computer account.
        
              - **ComputerId** *(string) --* 
        
                The identifier of the computer.
        
              - **ComputerName** *(string) --* 
        
                The computer name.
        
              - **ComputerAttributes** *(list) --* 
        
                An array of  Attribute objects containing the LDAP attributes that belong to the computer account.
        
                - *(dict) --* 
        
                  Represents a named directory attribute.
        
                  - **Name** *(string) --* 
        
                    The name of the attribute.
        
                  - **Value** *(string) --* 
        
                    The value of the attribute.
        
        """
        pass

    def create_conditional_forwarder(self, DirectoryId: str, RemoteDomainName: str, DnsIpAddrs: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/CreateConditionalForwarder>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_conditional_forwarder(
              DirectoryId=\'string\',
              RemoteDomainName=\'string\',
              DnsIpAddrs=[
                  \'string\',
              ]
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The directory ID of the AWS directory for which you are creating the conditional forwarder.
        
        :type RemoteDomainName: string
        :param RemoteDomainName: **[REQUIRED]** 
        
          The fully qualified domain name (FQDN) of the remote domain with which you will set up a trust relationship.
        
        :type DnsIpAddrs: list
        :param DnsIpAddrs: **[REQUIRED]** 
        
          The IP addresses of the remote DNS server associated with RemoteDomainName.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            The result of a CreateConditinalForwarder request.
        
        """
        pass

    def create_directory(self, Name: str, Password: str, Size: str, ShortName: str = None, Description: str = None, VpcSettings: Dict = None) -> Dict:
        """
        
        Before you call ``CreateDirectory`` , ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the ``CreateDirectory`` operation, see `AWS Directory Service API Permissions\: Actions, Resources, and Conditions Reference <http://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/CreateDirectory>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_directory(
              Name=\'string\',
              ShortName=\'string\',
              Password=\'string\',
              Description=\'string\',
              Size=\'Small\'|\'Large\',
              VpcSettings={
                  \'VpcId\': \'string\',
                  \'SubnetIds\': [
                      \'string\',
                  ]
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The fully qualified name for the directory, such as ``corp.example.com`` .
        
        :type ShortName: string
        :param ShortName: 
        
          The short name of the directory, such as ``CORP`` .
        
        :type Password: string
        :param Password: **[REQUIRED]** 
        
          The password for the directory administrator. The directory creation process creates a directory administrator account with the user name ``Administrator`` and this password.
        
        :type Description: string
        :param Description: 
        
          A textual description for the directory.
        
        :type Size: string
        :param Size: **[REQUIRED]** 
        
          The size of the directory.
        
        :type VpcSettings: dict
        :param VpcSettings: 
        
          A  DirectoryVpcSettings object that contains additional information for the operation.
        
          - **VpcId** *(string) --* **[REQUIRED]** 
        
            The identifier of the VPC in which to create the directory.
        
          - **SubnetIds** *(list) --* **[REQUIRED]** 
        
            The identifiers of the subnets for the directory servers. The two subnets must be in different Availability Zones. AWS Directory Service creates a directory server and a DNS server in each of these subnets.
        
            - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DirectoryId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the results of the  CreateDirectory operation.
        
            - **DirectoryId** *(string) --* 
        
              The identifier of the directory that was created.
        
        """
        pass

    def create_log_subscription(self, DirectoryId: str, LogGroupName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/CreateLogSubscription>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_log_subscription(
              DirectoryId=\'string\',
              LogGroupName=\'string\'
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          Identifier (ID) of the directory to which you want to subscribe and receive real-time logs to your specified CloudWatch log group.
        
        :type LogGroupName: string
        :param LogGroupName: **[REQUIRED]** 
        
          The name of the CloudWatch log group where the real-time domain controller logs are forwarded.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def create_microsoft_ad(self, Name: str, Password: str, VpcSettings: Dict, ShortName: str = None, Description: str = None, Edition: str = None) -> Dict:
        """
        
        Before you call *CreateMicrosoftAD* , ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the *CreateMicrosoftAD* operation, see `AWS Directory Service API Permissions\: Actions, Resources, and Conditions Reference <http://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/CreateMicrosoftAD>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_microsoft_ad(
              Name=\'string\',
              ShortName=\'string\',
              Password=\'string\',
              Description=\'string\',
              VpcSettings={
                  \'VpcId\': \'string\',
                  \'SubnetIds\': [
                      \'string\',
                  ]
              },
              Edition=\'Enterprise\'|\'Standard\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The fully qualified domain name for the directory, such as ``corp.example.com`` . This name will resolve inside your VPC only. It does not need to be publicly resolvable.
        
        :type ShortName: string
        :param ShortName: 
        
          The NetBIOS name for your domain. A short identifier for your domain, such as ``CORP`` . If you don\'t specify a NetBIOS name, it will default to the first part of your directory DNS. For example, ``CORP`` for the directory DNS ``corp.example.com`` . 
        
        :type Password: string
        :param Password: **[REQUIRED]** 
        
          The password for the default administrative user named ``Admin`` .
        
        :type Description: string
        :param Description: 
        
          A textual description for the directory. This label will appear on the AWS console ``Directory Details`` page after the directory is created.
        
        :type VpcSettings: dict
        :param VpcSettings: **[REQUIRED]** 
        
          Contains VPC information for the  CreateDirectory or  CreateMicrosoftAD operation.
        
          - **VpcId** *(string) --* **[REQUIRED]** 
        
            The identifier of the VPC in which to create the directory.
        
          - **SubnetIds** *(list) --* **[REQUIRED]** 
        
            The identifiers of the subnets for the directory servers. The two subnets must be in different Availability Zones. AWS Directory Service creates a directory server and a DNS server in each of these subnets.
        
            - *(string) --* 
        
        :type Edition: string
        :param Edition: 
        
          AWS Managed Microsoft AD is available in two editions: Standard and Enterprise. Enterprise is the default.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DirectoryId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Result of a CreateMicrosoftAD request.
        
            - **DirectoryId** *(string) --* 
        
              The identifier of the directory that was created.
        
        """
        pass

    def create_snapshot(self, DirectoryId: str, Name: str = None) -> Dict:
        """
        
        .. note::
        
          You cannot take snapshots of AD Connector directories.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/CreateSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_snapshot(
              DirectoryId=\'string\',
              Name=\'string\'
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The identifier of the directory of which to take a snapshot.
        
        :type Name: string
        :param Name: 
        
          The descriptive name to apply to the snapshot.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SnapshotId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the results of the  CreateSnapshot operation.
        
            - **SnapshotId** *(string) --* 
        
              The identifier of the snapshot that was created.
        
        """
        pass

    def create_trust(self, DirectoryId: str, RemoteDomainName: str, TrustPassword: str, TrustDirection: str, TrustType: str = None, ConditionalForwarderIpAddrs: List = None, SelectiveAuth: str = None) -> Dict:
        """
        
        This action initiates the creation of the AWS side of a trust relationship between an AWS Managed Microsoft AD directory and an external domain. You can create either a forest trust or an external trust.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/CreateTrust>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_trust(
              DirectoryId=\'string\',
              RemoteDomainName=\'string\',
              TrustPassword=\'string\',
              TrustDirection=\'One-Way: Outgoing\'|\'One-Way: Incoming\'|\'Two-Way\',
              TrustType=\'Forest\'|\'External\',
              ConditionalForwarderIpAddrs=[
                  \'string\',
              ],
              SelectiveAuth=\'Enabled\'|\'Disabled\'
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The Directory ID of the AWS Managed Microsoft AD directory for which to establish the trust relationship.
        
        :type RemoteDomainName: string
        :param RemoteDomainName: **[REQUIRED]** 
        
          The Fully Qualified Domain Name (FQDN) of the external domain for which to create the trust relationship.
        
        :type TrustPassword: string
        :param TrustPassword: **[REQUIRED]** 
        
          The trust password. The must be the same password that was used when creating the trust relationship on the external domain.
        
        :type TrustDirection: string
        :param TrustDirection: **[REQUIRED]** 
        
          The direction of the trust relationship.
        
        :type TrustType: string
        :param TrustType: 
        
          The trust relationship type. ``Forest`` is the default.
        
        :type ConditionalForwarderIpAddrs: list
        :param ConditionalForwarderIpAddrs: 
        
          The IP addresses of the remote DNS server associated with RemoteDomainName.
        
          - *(string) --* 
        
        :type SelectiveAuth: string
        :param SelectiveAuth: 
        
          Optional parameter to enable selective authentication for the trust.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TrustId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The result of a CreateTrust request.
        
            - **TrustId** *(string) --* 
        
              A unique identifier for the trust relationship that was created.
        
        """
        pass

    def delete_conditional_forwarder(self, DirectoryId: str, RemoteDomainName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DeleteConditionalForwarder>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_conditional_forwarder(
              DirectoryId=\'string\',
              RemoteDomainName=\'string\'
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The directory ID for which you are deleting the conditional forwarder.
        
        :type RemoteDomainName: string
        :param RemoteDomainName: **[REQUIRED]** 
        
          The fully qualified domain name (FQDN) of the remote domain with which you are deleting the conditional forwarder.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            The result of a DeleteConditionalForwarder request.
        
        """
        pass

    def delete_directory(self, DirectoryId: str) -> Dict:
        """
        
        Before you call ``DeleteDirectory`` , ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the ``DeleteDirectory`` operation, see `AWS Directory Service API Permissions\: Actions, Resources, and Conditions Reference <http://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DeleteDirectory>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_directory(
              DirectoryId=\'string\'
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The identifier of the directory to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DirectoryId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the results of the  DeleteDirectory operation.
        
            - **DirectoryId** *(string) --* 
        
              The directory identifier.
        
        """
        pass

    def delete_log_subscription(self, DirectoryId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DeleteLogSubscription>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_log_subscription(
              DirectoryId=\'string\'
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          Identifier (ID) of the directory whose log subscription you want to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_snapshot(self, SnapshotId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DeleteSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_snapshot(
              SnapshotId=\'string\'
          )
        :type SnapshotId: string
        :param SnapshotId: **[REQUIRED]** 
        
          The identifier of the directory snapshot to be deleted.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SnapshotId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the results of the  DeleteSnapshot operation.
        
            - **SnapshotId** *(string) --* 
        
              The identifier of the directory snapshot that was deleted.
        
        """
        pass

    def delete_trust(self, TrustId: str, DeleteAssociatedConditionalForwarder: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DeleteTrust>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_trust(
              TrustId=\'string\',
              DeleteAssociatedConditionalForwarder=True|False
          )
        :type TrustId: string
        :param TrustId: **[REQUIRED]** 
        
          The Trust ID of the trust relationship to be deleted.
        
        :type DeleteAssociatedConditionalForwarder: boolean
        :param DeleteAssociatedConditionalForwarder: 
        
          Delete a conditional forwarder as part of a DeleteTrustRequest.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TrustId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The result of a DeleteTrust request.
        
            - **TrustId** *(string) --* 
        
              The Trust ID of the trust relationship that was deleted.
        
        """
        pass

    def deregister_event_topic(self, DirectoryId: str, TopicName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DeregisterEventTopic>`_
        
        **Request Syntax** 
        ::
        
          response = client.deregister_event_topic(
              DirectoryId=\'string\',
              TopicName=\'string\'
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The Directory ID to remove as a publisher. This directory will no longer send messages to the specified SNS topic.
        
        :type TopicName: string
        :param TopicName: **[REQUIRED]** 
        
          The name of the SNS topic from which to remove the directory as a publisher.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            The result of a DeregisterEventTopic request.
        
        """
        pass

    def describe_conditional_forwarders(self, DirectoryId: str, RemoteDomainNames: List = None) -> Dict:
        """
        
        If no input parameters are provided for RemoteDomainNames, this request describes all conditional forwarders for the specified directory ID.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DescribeConditionalForwarders>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_conditional_forwarders(
              DirectoryId=\'string\',
              RemoteDomainNames=[
                  \'string\',
              ]
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The directory ID for which to get the list of associated conditional forwarders.
        
        :type RemoteDomainNames: list
        :param RemoteDomainNames: 
        
          The fully qualified domain names (FQDN) of the remote domains for which to get the list of associated conditional forwarders. If this member is null, all conditional forwarders are returned.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ConditionalForwarders\': [
                    {
                        \'RemoteDomainName\': \'string\',
                        \'DnsIpAddrs\': [
                            \'string\',
                        ],
                        \'ReplicationScope\': \'Domain\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The result of a DescribeConditionalForwarder request.
        
            - **ConditionalForwarders** *(list) --* 
        
              The list of conditional forwarders that have been created.
        
              - *(dict) --* 
        
                Points to a remote domain with which you are setting up a trust relationship. Conditional forwarders are required in order to set up a trust relationship with another domain.
        
                - **RemoteDomainName** *(string) --* 
        
                  The fully qualified domain name (FQDN) of the remote domains pointed to by the conditional forwarder.
        
                - **DnsIpAddrs** *(list) --* 
        
                  The IP addresses of the remote DNS server associated with RemoteDomainName. This is the IP address of the DNS server that your conditional forwarder points to.
        
                  - *(string) --* 
              
                - **ReplicationScope** *(string) --* 
        
                  The replication scope of the conditional forwarder. The only allowed value is ``Domain`` , which will replicate the conditional forwarder to all of the domain controllers for your AWS directory.
        
        """
        pass

    def describe_directories(self, DirectoryIds: List = None, NextToken: str = None, Limit: int = None) -> Dict:
        """
        
        You can retrieve information about specific directories by passing the directory identifiers in the ``DirectoryIds`` parameter. Otherwise, all directories that belong to the current account are returned.
        
        This operation supports pagination with the use of the ``NextToken`` request and response parameters. If more results are available, the ``DescribeDirectoriesResult.NextToken`` member contains a token that you pass in the next call to  DescribeDirectories to retrieve the next set of items.
        
        You can also specify a maximum number of return results with the ``Limit`` parameter.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DescribeDirectories>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_directories(
              DirectoryIds=[
                  \'string\',
              ],
              NextToken=\'string\',
              Limit=123
          )
        :type DirectoryIds: list
        :param DirectoryIds: 
        
          A list of identifiers of the directories for which to obtain the information. If this member is null, all directories that belong to the current account are returned.
        
          An empty list results in an ``InvalidParameterException`` being thrown.
        
          - *(string) --* 
        
        :type NextToken: string
        :param NextToken: 
        
          The ``DescribeDirectoriesResult.NextToken`` value from a previous call to  DescribeDirectories . Pass null if this is the first call.
        
        :type Limit: integer
        :param Limit: 
        
          The maximum number of items to return. If this value is zero, the maximum number of items is specified by the limitations of the operation.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DirectoryDescriptions\': [
                    {
                        \'DirectoryId\': \'string\',
                        \'Name\': \'string\',
                        \'ShortName\': \'string\',
                        \'Size\': \'Small\'|\'Large\',
                        \'Edition\': \'Enterprise\'|\'Standard\',
                        \'Alias\': \'string\',
                        \'AccessUrl\': \'string\',
                        \'Description\': \'string\',
                        \'DnsIpAddrs\': [
                            \'string\',
                        ],
                        \'Stage\': \'Requested\'|\'Creating\'|\'Created\'|\'Active\'|\'Inoperable\'|\'Impaired\'|\'Restoring\'|\'RestoreFailed\'|\'Deleting\'|\'Deleted\'|\'Failed\',
                        \'ShareStatus\': \'Shared\'|\'PendingAcceptance\'|\'Rejected\'|\'Rejecting\'|\'RejectFailed\'|\'Sharing\'|\'ShareFailed\'|\'Deleted\'|\'Deleting\',
                        \'ShareMethod\': \'ORGANIZATIONS\'|\'HANDSHAKE\',
                        \'ShareNotes\': \'string\',
                        \'LaunchTime\': datetime(2015, 1, 1),
                        \'StageLastUpdatedDateTime\': datetime(2015, 1, 1),
                        \'Type\': \'SimpleAD\'|\'ADConnector\'|\'MicrosoftAD\'|\'SharedMicrosoftAD\',
                        \'VpcSettings\': {
                            \'VpcId\': \'string\',
                            \'SubnetIds\': [
                                \'string\',
                            ],
                            \'SecurityGroupId\': \'string\',
                            \'AvailabilityZones\': [
                                \'string\',
                            ]
                        },
                        \'ConnectSettings\': {
                            \'VpcId\': \'string\',
                            \'SubnetIds\': [
                                \'string\',
                            ],
                            \'CustomerUserName\': \'string\',
                            \'SecurityGroupId\': \'string\',
                            \'AvailabilityZones\': [
                                \'string\',
                            ],
                            \'ConnectIps\': [
                                \'string\',
                            ]
                        },
                        \'RadiusSettings\': {
                            \'RadiusServers\': [
                                \'string\',
                            ],
                            \'RadiusPort\': 123,
                            \'RadiusTimeout\': 123,
                            \'RadiusRetries\': 123,
                            \'SharedSecret\': \'string\',
                            \'AuthenticationProtocol\': \'PAP\'|\'CHAP\'|\'MS-CHAPv1\'|\'MS-CHAPv2\',
                            \'DisplayLabel\': \'string\',
                            \'UseSameUsername\': True|False
                        },
                        \'RadiusStatus\': \'Creating\'|\'Completed\'|\'Failed\',
                        \'StageReason\': \'string\',
                        \'SsoEnabled\': True|False,
                        \'DesiredNumberOfDomainControllers\': 123,
                        \'OwnerDirectoryDescription\': {
                            \'DirectoryId\': \'string\',
                            \'AccountId\': \'string\',
                            \'DnsIpAddrs\': [
                                \'string\',
                            ],
                            \'VpcSettings\': {
                                \'VpcId\': \'string\',
                                \'SubnetIds\': [
                                    \'string\',
                                ],
                                \'SecurityGroupId\': \'string\',
                                \'AvailabilityZones\': [
                                    \'string\',
                                ]
                            },
                            \'RadiusSettings\': {
                                \'RadiusServers\': [
                                    \'string\',
                                ],
                                \'RadiusPort\': 123,
                                \'RadiusTimeout\': 123,
                                \'RadiusRetries\': 123,
                                \'SharedSecret\': \'string\',
                                \'AuthenticationProtocol\': \'PAP\'|\'CHAP\'|\'MS-CHAPv1\'|\'MS-CHAPv2\',
                                \'DisplayLabel\': \'string\',
                                \'UseSameUsername\': True|False
                            },
                            \'RadiusStatus\': \'Creating\'|\'Completed\'|\'Failed\'
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the results of the  DescribeDirectories operation.
        
            - **DirectoryDescriptions** *(list) --* 
        
              The list of  DirectoryDescription objects that were retrieved.
        
              It is possible that this list contains less than the number of items specified in the ``Limit`` member of the request. This occurs if there are less than the requested number of items left to retrieve, or if the limitations of the operation have been exceeded.
        
              - *(dict) --* 
        
                Contains information about an AWS Directory Service directory.
        
                - **DirectoryId** *(string) --* 
        
                  The directory identifier.
        
                - **Name** *(string) --* 
        
                  The fully qualified name of the directory.
        
                - **ShortName** *(string) --* 
        
                  The short name of the directory.
        
                - **Size** *(string) --* 
        
                  The directory size.
        
                - **Edition** *(string) --* 
        
                  The edition associated with this directory.
        
                - **Alias** *(string) --* 
        
                  The alias for the directory. If no alias has been created for the directory, the alias is the directory identifier, such as ``d-XXXXXXXXXX`` .
        
                - **AccessUrl** *(string) --* 
        
                  The access URL for the directory, such as ``http://<alias>.awsapps.com`` . If no alias has been created for the directory, ``<alias>`` is the directory identifier, such as ``d-XXXXXXXXXX`` .
        
                - **Description** *(string) --* 
        
                  The textual description for the directory.
        
                - **DnsIpAddrs** *(list) --* 
        
                  The IP addresses of the DNS servers for the directory. For a Simple AD or Microsoft AD directory, these are the IP addresses of the Simple AD or Microsoft AD directory servers. For an AD Connector directory, these are the IP addresses of the DNS servers or domain controllers in the on-premises directory to which the AD Connector is connected.
        
                  - *(string) --* 
              
                - **Stage** *(string) --* 
        
                  The current stage of the directory.
        
                - **ShareStatus** *(string) --* 
        
                  Current directory status of the shared AWS Managed Microsoft AD directory.
        
                - **ShareMethod** *(string) --* 
        
                  The method used when sharing a directory to determine whether the directory should be shared within your AWS organization (``ORGANIZATIONS`` ) or with any AWS account by sending a shared directory request (``HANDSHAKE`` ).
        
                - **ShareNotes** *(string) --* 
        
                  A directory share request that is sent by the directory owner to the directory consumer. The request includes a typed message to help the directory consumer administrator determine whether to approve or reject the share invitation.
        
                - **LaunchTime** *(datetime) --* 
        
                  Specifies when the directory was created.
        
                - **StageLastUpdatedDateTime** *(datetime) --* 
        
                  The date and time that the stage was last updated.
        
                - **Type** *(string) --* 
        
                  The directory size.
        
                - **VpcSettings** *(dict) --* 
        
                  A  DirectoryVpcSettingsDescription object that contains additional information about a directory. This member is only present if the directory is a Simple AD or Managed AD directory.
        
                  - **VpcId** *(string) --* 
        
                    The identifier of the VPC that the directory is in.
        
                  - **SubnetIds** *(list) --* 
        
                    The identifiers of the subnets for the directory servers.
        
                    - *(string) --* 
                
                  - **SecurityGroupId** *(string) --* 
        
                    The domain controller security group identifier for the directory.
        
                  - **AvailabilityZones** *(list) --* 
        
                    The list of Availability Zones that the directory is in.
        
                    - *(string) --* 
                
                - **ConnectSettings** *(dict) --* 
        
                  A  DirectoryConnectSettingsDescription object that contains additional information about an AD Connector directory. This member is only present if the directory is an AD Connector directory.
        
                  - **VpcId** *(string) --* 
        
                    The identifier of the VPC that the AD Connector is in.
        
                  - **SubnetIds** *(list) --* 
        
                    A list of subnet identifiers in the VPC that the AD connector is in.
        
                    - *(string) --* 
                
                  - **CustomerUserName** *(string) --* 
        
                    The user name of the service account in the on-premises directory.
        
                  - **SecurityGroupId** *(string) --* 
        
                    The security group identifier for the AD Connector directory.
        
                  - **AvailabilityZones** *(list) --* 
        
                    A list of the Availability Zones that the directory is in.
        
                    - *(string) --* 
                
                  - **ConnectIps** *(list) --* 
        
                    The IP addresses of the AD Connector servers.
        
                    - *(string) --* 
                
                - **RadiusSettings** *(dict) --* 
        
                  A  RadiusSettings object that contains information about the RADIUS server configured for this directory.
        
                  - **RadiusServers** *(list) --* 
        
                    An array of strings that contains the IP addresses of the RADIUS server endpoints, or the IP addresses of your RADIUS server load balancer.
        
                    - *(string) --* 
                
                  - **RadiusPort** *(integer) --* 
        
                    The port that your RADIUS server is using for communications. Your on-premises network must allow inbound traffic over this port from the AWS Directory Service servers.
        
                  - **RadiusTimeout** *(integer) --* 
        
                    The amount of time, in seconds, to wait for the RADIUS server to respond.
        
                  - **RadiusRetries** *(integer) --* 
        
                    The maximum number of times that communication with the RADIUS server is attempted.
        
                  - **SharedSecret** *(string) --* 
        
                    Required for enabling RADIUS on the directory.
        
                  - **AuthenticationProtocol** *(string) --* 
        
                    The protocol specified for your RADIUS endpoints.
        
                  - **DisplayLabel** *(string) --* 
        
                    Not currently used.
        
                  - **UseSameUsername** *(boolean) --* 
        
                    Not currently used.
        
                - **RadiusStatus** *(string) --* 
        
                  The status of the RADIUS MFA server connection.
        
                - **StageReason** *(string) --* 
        
                  Additional information about the directory stage.
        
                - **SsoEnabled** *(boolean) --* 
        
                  Indicates if single sign-on is enabled for the directory. For more information, see  EnableSso and  DisableSso .
        
                - **DesiredNumberOfDomainControllers** *(integer) --* 
        
                  The desired number of domain controllers in the directory if the directory is Microsoft AD.
        
                - **OwnerDirectoryDescription** *(dict) --* 
        
                  Describes the AWS Managed Microsoft AD directory in the directory owner account.
        
                  - **DirectoryId** *(string) --* 
        
                    Identifier of the AWS Managed Microsoft AD directory in the directory owner account.
        
                  - **AccountId** *(string) --* 
        
                    Identifier of the directory owner account.
        
                  - **DnsIpAddrs** *(list) --* 
        
                    IP address of the directory’s domain controllers.
        
                    - *(string) --* 
                
                  - **VpcSettings** *(dict) --* 
        
                    Information about the VPC settings for the directory.
        
                    - **VpcId** *(string) --* 
        
                      The identifier of the VPC that the directory is in.
        
                    - **SubnetIds** *(list) --* 
        
                      The identifiers of the subnets for the directory servers.
        
                      - *(string) --* 
                  
                    - **SecurityGroupId** *(string) --* 
        
                      The domain controller security group identifier for the directory.
        
                    - **AvailabilityZones** *(list) --* 
        
                      The list of Availability Zones that the directory is in.
        
                      - *(string) --* 
                  
                  - **RadiusSettings** *(dict) --* 
        
                    A  RadiusSettings object that contains information about the RADIUS server.
        
                    - **RadiusServers** *(list) --* 
        
                      An array of strings that contains the IP addresses of the RADIUS server endpoints, or the IP addresses of your RADIUS server load balancer.
        
                      - *(string) --* 
                  
                    - **RadiusPort** *(integer) --* 
        
                      The port that your RADIUS server is using for communications. Your on-premises network must allow inbound traffic over this port from the AWS Directory Service servers.
        
                    - **RadiusTimeout** *(integer) --* 
        
                      The amount of time, in seconds, to wait for the RADIUS server to respond.
        
                    - **RadiusRetries** *(integer) --* 
        
                      The maximum number of times that communication with the RADIUS server is attempted.
        
                    - **SharedSecret** *(string) --* 
        
                      Required for enabling RADIUS on the directory.
        
                    - **AuthenticationProtocol** *(string) --* 
        
                      The protocol specified for your RADIUS endpoints.
        
                    - **DisplayLabel** *(string) --* 
        
                      Not currently used.
        
                    - **UseSameUsername** *(boolean) --* 
        
                      Not currently used.
        
                  - **RadiusStatus** *(string) --* 
        
                    Information about the status of the RADIUS server.
        
            - **NextToken** *(string) --* 
        
              If not null, more results are available. Pass this value for the ``NextToken`` parameter in a subsequent call to  DescribeDirectories to retrieve the next set of items.
        
        """
        pass

    def describe_domain_controllers(self, DirectoryId: str, DomainControllerIds: List = None, NextToken: str = None, Limit: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DescribeDomainControllers>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_domain_controllers(
              DirectoryId=\'string\',
              DomainControllerIds=[
                  \'string\',
              ],
              NextToken=\'string\',
              Limit=123
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          Identifier of the directory for which to retrieve the domain controller information.
        
        :type DomainControllerIds: list
        :param DomainControllerIds: 
        
          A list of identifiers for the domain controllers whose information will be provided.
        
          - *(string) --* 
        
        :type NextToken: string
        :param NextToken: 
        
          The *DescribeDomainControllers.NextToken* value from a previous call to  DescribeDomainControllers . Pass null if this is the first call. 
        
        :type Limit: integer
        :param Limit: 
        
          The maximum number of items to return.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DomainControllers\': [
                    {
                        \'DirectoryId\': \'string\',
                        \'DomainControllerId\': \'string\',
                        \'DnsIpAddr\': \'string\',
                        \'VpcId\': \'string\',
                        \'SubnetId\': \'string\',
                        \'AvailabilityZone\': \'string\',
                        \'Status\': \'Creating\'|\'Active\'|\'Impaired\'|\'Restoring\'|\'Deleting\'|\'Deleted\'|\'Failed\',
                        \'StatusReason\': \'string\',
                        \'LaunchTime\': datetime(2015, 1, 1),
                        \'StatusLastUpdatedDateTime\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DomainControllers** *(list) --* 
        
              List of the  DomainController objects that were retrieved.
        
              - *(dict) --* 
        
                Contains information about the domain controllers for a specified directory.
        
                - **DirectoryId** *(string) --* 
        
                  Identifier of the directory where the domain controller resides.
        
                - **DomainControllerId** *(string) --* 
        
                  Identifies a specific domain controller in the directory.
        
                - **DnsIpAddr** *(string) --* 
        
                  The IP address of the domain controller.
        
                - **VpcId** *(string) --* 
        
                  The identifier of the VPC that contains the domain controller.
        
                - **SubnetId** *(string) --* 
        
                  Identifier of the subnet in the VPC that contains the domain controller.
        
                - **AvailabilityZone** *(string) --* 
        
                  The Availability Zone where the domain controller is located.
        
                - **Status** *(string) --* 
        
                  The status of the domain controller.
        
                - **StatusReason** *(string) --* 
        
                  A description of the domain controller state.
        
                - **LaunchTime** *(datetime) --* 
        
                  Specifies when the domain controller was created.
        
                - **StatusLastUpdatedDateTime** *(datetime) --* 
        
                  The date and time that the status was last updated.
        
            - **NextToken** *(string) --* 
        
              If not null, more results are available. Pass this value for the ``NextToken`` parameter in a subsequent call to  DescribeDomainControllers retrieve the next set of items.
        
        """
        pass

    def describe_event_topics(self, DirectoryId: str = None, TopicNames: List = None) -> Dict:
        """
        
        If no input parameters are provided, such as DirectoryId or TopicName, this request describes all of the associations in the account.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DescribeEventTopics>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_event_topics(
              DirectoryId=\'string\',
              TopicNames=[
                  \'string\',
              ]
          )
        :type DirectoryId: string
        :param DirectoryId: 
        
          The Directory ID for which to get the list of associated SNS topics. If this member is null, associations for all Directory IDs are returned.
        
        :type TopicNames: list
        :param TopicNames: 
        
          A list of SNS topic names for which to obtain the information. If this member is null, all associations for the specified Directory ID are returned.
        
          An empty list results in an ``InvalidParameterException`` being thrown.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EventTopics\': [
                    {
                        \'DirectoryId\': \'string\',
                        \'TopicName\': \'string\',
                        \'TopicArn\': \'string\',
                        \'CreatedDateTime\': datetime(2015, 1, 1),
                        \'Status\': \'Registered\'|\'Topic not found\'|\'Failed\'|\'Deleted\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The result of a DescribeEventTopic request.
        
            - **EventTopics** *(list) --* 
        
              A list of SNS topic names that receive status messages from the specified Directory ID.
        
              - *(dict) --* 
        
                Information about SNS topic and AWS Directory Service directory associations.
        
                - **DirectoryId** *(string) --* 
        
                  The Directory ID of an AWS Directory Service directory that will publish status messages to an SNS topic.
        
                - **TopicName** *(string) --* 
        
                  The name of an AWS SNS topic the receives status messages from the directory.
        
                - **TopicArn** *(string) --* 
        
                  The SNS topic ARN (Amazon Resource Name).
        
                - **CreatedDateTime** *(datetime) --* 
        
                  The date and time of when you associated your directory with the SNS topic.
        
                - **Status** *(string) --* 
        
                  The topic registration status.
        
        """
        pass

    def describe_shared_directories(self, OwnerDirectoryId: str, SharedDirectoryIds: List = None, NextToken: str = None, Limit: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DescribeSharedDirectories>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_shared_directories(
              OwnerDirectoryId=\'string\',
              SharedDirectoryIds=[
                  \'string\',
              ],
              NextToken=\'string\',
              Limit=123
          )
        :type OwnerDirectoryId: string
        :param OwnerDirectoryId: **[REQUIRED]** 
        
          Returns the identifier of the directory in the directory owner account. 
        
        :type SharedDirectoryIds: list
        :param SharedDirectoryIds: 
        
          A list of identifiers of all shared directories in your account. 
        
          - *(string) --* 
        
        :type NextToken: string
        :param NextToken: 
        
          The ``DescribeSharedDirectoriesResult.NextToken`` value from a previous call to  DescribeSharedDirectories . Pass null if this is the first call. 
        
        :type Limit: integer
        :param Limit: 
        
          The number of shared directories to return in the response object.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SharedDirectories\': [
                    {
                        \'OwnerAccountId\': \'string\',
                        \'OwnerDirectoryId\': \'string\',
                        \'ShareMethod\': \'ORGANIZATIONS\'|\'HANDSHAKE\',
                        \'SharedAccountId\': \'string\',
                        \'SharedDirectoryId\': \'string\',
                        \'ShareStatus\': \'Shared\'|\'PendingAcceptance\'|\'Rejected\'|\'Rejecting\'|\'RejectFailed\'|\'Sharing\'|\'ShareFailed\'|\'Deleted\'|\'Deleting\',
                        \'ShareNotes\': \'string\',
                        \'CreatedDateTime\': datetime(2015, 1, 1),
                        \'LastUpdatedDateTime\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SharedDirectories** *(list) --* 
        
              A list of all shared directories in your account.
        
              - *(dict) --* 
        
                Details about the shared directory in the directory owner account for which the share request in the directory consumer account has been accepted.
        
                - **OwnerAccountId** *(string) --* 
        
                  Identifier of the directory owner account, which contains the directory that has been shared to the consumer account.
        
                - **OwnerDirectoryId** *(string) --* 
        
                  Identifier of the directory in the directory owner account. 
        
                - **ShareMethod** *(string) --* 
        
                  The method used when sharing a directory to determine whether the directory should be shared within your AWS organization (``ORGANIZATIONS`` ) or with any AWS account by sending a shared directory request (``HANDSHAKE`` ).
        
                - **SharedAccountId** *(string) --* 
        
                  Identifier of the directory consumer account that has access to the shared directory (``OwnerDirectoryId`` ) in the directory owner account.
        
                - **SharedDirectoryId** *(string) --* 
        
                  Identifier of the shared directory in the directory consumer account. This identifier is different for each directory owner account.
        
                - **ShareStatus** *(string) --* 
        
                  Current directory status of the shared AWS Managed Microsoft AD directory.
        
                - **ShareNotes** *(string) --* 
        
                  A directory share request that is sent by the directory owner to the directory consumer. The request includes a typed message to help the directory consumer administrator determine whether to approve or reject the share invitation.
        
                - **CreatedDateTime** *(datetime) --* 
        
                  The date and time that the shared directory was created.
        
                - **LastUpdatedDateTime** *(datetime) --* 
        
                  The date and time that the shared directory was last updated.
        
            - **NextToken** *(string) --* 
        
              If not null, token that indicates that more results are available. Pass this value for the ``NextToken`` parameter in a subsequent call to  DescribeSharedDirectories to retrieve the next set of items.
        
        """
        pass

    def describe_snapshots(self, DirectoryId: str = None, SnapshotIds: List = None, NextToken: str = None, Limit: int = None) -> Dict:
        """
        
        This operation supports pagination with the use of the *NextToken* request and response parameters. If more results are available, the *DescribeSnapshots.NextToken* member contains a token that you pass in the next call to  DescribeSnapshots to retrieve the next set of items.
        
        You can also specify a maximum number of return results with the *Limit* parameter.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DescribeSnapshots>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_snapshots(
              DirectoryId=\'string\',
              SnapshotIds=[
                  \'string\',
              ],
              NextToken=\'string\',
              Limit=123
          )
        :type DirectoryId: string
        :param DirectoryId: 
        
          The identifier of the directory for which to retrieve snapshot information.
        
        :type SnapshotIds: list
        :param SnapshotIds: 
        
          A list of identifiers of the snapshots to obtain the information for. If this member is null or empty, all snapshots are returned using the *Limit* and *NextToken* members.
        
          - *(string) --* 
        
        :type NextToken: string
        :param NextToken: 
        
          The *DescribeSnapshotsResult.NextToken* value from a previous call to  DescribeSnapshots . Pass null if this is the first call.
        
        :type Limit: integer
        :param Limit: 
        
          The maximum number of objects to return.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Snapshots\': [
                    {
                        \'DirectoryId\': \'string\',
                        \'SnapshotId\': \'string\',
                        \'Type\': \'Auto\'|\'Manual\',
                        \'Name\': \'string\',
                        \'Status\': \'Creating\'|\'Completed\'|\'Failed\',
                        \'StartTime\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the results of the  DescribeSnapshots operation.
        
            - **Snapshots** *(list) --* 
        
              The list of  Snapshot objects that were retrieved.
        
              It is possible that this list contains less than the number of items specified in the *Limit* member of the request. This occurs if there are less than the requested number of items left to retrieve, or if the limitations of the operation have been exceeded.
        
              - *(dict) --* 
        
                Describes a directory snapshot.
        
                - **DirectoryId** *(string) --* 
        
                  The directory identifier.
        
                - **SnapshotId** *(string) --* 
        
                  The snapshot identifier.
        
                - **Type** *(string) --* 
        
                  The snapshot type.
        
                - **Name** *(string) --* 
        
                  The descriptive name of the snapshot.
        
                - **Status** *(string) --* 
        
                  The snapshot status.
        
                - **StartTime** *(datetime) --* 
        
                  The date and time that the snapshot was taken.
        
            - **NextToken** *(string) --* 
        
              If not null, more results are available. Pass this value in the *NextToken* member of a subsequent call to  DescribeSnapshots .
        
        """
        pass

    def describe_trusts(self, DirectoryId: str = None, TrustIds: List = None, NextToken: str = None, Limit: int = None) -> Dict:
        """
        
        If no input parameters are provided, such as DirectoryId or TrustIds, this request describes all the trust relationships belonging to the account.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DescribeTrusts>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_trusts(
              DirectoryId=\'string\',
              TrustIds=[
                  \'string\',
              ],
              NextToken=\'string\',
              Limit=123
          )
        :type DirectoryId: string
        :param DirectoryId: 
        
          The Directory ID of the AWS directory that is a part of the requested trust relationship.
        
        :type TrustIds: list
        :param TrustIds: 
        
          A list of identifiers of the trust relationships for which to obtain the information. If this member is null, all trust relationships that belong to the current account are returned.
        
          An empty list results in an ``InvalidParameterException`` being thrown.
        
          - *(string) --* 
        
        :type NextToken: string
        :param NextToken: 
        
          The *DescribeTrustsResult.NextToken* value from a previous call to  DescribeTrusts . Pass null if this is the first call.
        
        :type Limit: integer
        :param Limit: 
        
          The maximum number of objects to return.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Trusts\': [
                    {
                        \'DirectoryId\': \'string\',
                        \'TrustId\': \'string\',
                        \'RemoteDomainName\': \'string\',
                        \'TrustType\': \'Forest\'|\'External\',
                        \'TrustDirection\': \'One-Way: Outgoing\'|\'One-Way: Incoming\'|\'Two-Way\',
                        \'TrustState\': \'Creating\'|\'Created\'|\'Verifying\'|\'VerifyFailed\'|\'Verified\'|\'Updating\'|\'UpdateFailed\'|\'Updated\'|\'Deleting\'|\'Deleted\'|\'Failed\',
                        \'CreatedDateTime\': datetime(2015, 1, 1),
                        \'LastUpdatedDateTime\': datetime(2015, 1, 1),
                        \'StateLastUpdatedDateTime\': datetime(2015, 1, 1),
                        \'TrustStateReason\': \'string\',
                        \'SelectiveAuth\': \'Enabled\'|\'Disabled\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The result of a DescribeTrust request.
        
            - **Trusts** *(list) --* 
        
              The list of Trust objects that were retrieved.
        
              It is possible that this list contains less than the number of items specified in the *Limit* member of the request. This occurs if there are less than the requested number of items left to retrieve, or if the limitations of the operation have been exceeded.
        
              - *(dict) --* 
        
                Describes a trust relationship between an AWS Managed Microsoft AD directory and an external domain.
        
                - **DirectoryId** *(string) --* 
        
                  The Directory ID of the AWS directory involved in the trust relationship.
        
                - **TrustId** *(string) --* 
        
                  The unique ID of the trust relationship.
        
                - **RemoteDomainName** *(string) --* 
        
                  The Fully Qualified Domain Name (FQDN) of the external domain involved in the trust relationship.
        
                - **TrustType** *(string) --* 
        
                  The trust relationship type. ``Forest`` is the default.
        
                - **TrustDirection** *(string) --* 
        
                  The trust relationship direction.
        
                - **TrustState** *(string) --* 
        
                  The trust relationship state.
        
                - **CreatedDateTime** *(datetime) --* 
        
                  The date and time that the trust relationship was created.
        
                - **LastUpdatedDateTime** *(datetime) --* 
        
                  The date and time that the trust relationship was last updated.
        
                - **StateLastUpdatedDateTime** *(datetime) --* 
        
                  The date and time that the TrustState was last updated.
        
                - **TrustStateReason** *(string) --* 
        
                  The reason for the TrustState.
        
                - **SelectiveAuth** *(string) --* 
        
                  Current state of selective authentication for the trust.
        
            - **NextToken** *(string) --* 
        
              If not null, more results are available. Pass this value for the *NextToken* parameter in a subsequent call to  DescribeTrusts to retrieve the next set of items.
        
        """
        pass

    def disable_radius(self, DirectoryId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DisableRadius>`_
        
        **Request Syntax** 
        ::
        
          response = client.disable_radius(
              DirectoryId=\'string\'
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The identifier of the directory for which to disable MFA.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the results of the  DisableRadius operation.
        
        """
        pass

    def disable_sso(self, DirectoryId: str, UserName: str = None, Password: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DisableSso>`_
        
        **Request Syntax** 
        ::
        
          response = client.disable_sso(
              DirectoryId=\'string\',
              UserName=\'string\',
              Password=\'string\'
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The identifier of the directory for which to disable single-sign on.
        
        :type UserName: string
        :param UserName: 
        
          The username of an alternate account to use to disable single-sign on. This is only used for AD Connector directories. This account must have privileges to remove a service principal name.
        
          If the AD Connector service account does not have privileges to remove a service principal name, you can specify an alternate account with the *UserName* and *Password* parameters. These credentials are only used to disable single sign-on and are not stored by the service. The AD Connector service account is not changed.
        
        :type Password: string
        :param Password: 
        
          The password of an alternate account to use to disable single-sign on. This is only used for AD Connector directories. For more information, see the *UserName* parameter.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the results of the  DisableSso operation.
        
        """
        pass

    def enable_radius(self, DirectoryId: str, RadiusSettings: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/EnableRadius>`_
        
        **Request Syntax** 
        ::
        
          response = client.enable_radius(
              DirectoryId=\'string\',
              RadiusSettings={
                  \'RadiusServers\': [
                      \'string\',
                  ],
                  \'RadiusPort\': 123,
                  \'RadiusTimeout\': 123,
                  \'RadiusRetries\': 123,
                  \'SharedSecret\': \'string\',
                  \'AuthenticationProtocol\': \'PAP\'|\'CHAP\'|\'MS-CHAPv1\'|\'MS-CHAPv2\',
                  \'DisplayLabel\': \'string\',
                  \'UseSameUsername\': True|False
              }
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The identifier of the directory for which to enable MFA.
        
        :type RadiusSettings: dict
        :param RadiusSettings: **[REQUIRED]** 
        
          A  RadiusSettings object that contains information about the RADIUS server.
        
          - **RadiusServers** *(list) --* 
        
            An array of strings that contains the IP addresses of the RADIUS server endpoints, or the IP addresses of your RADIUS server load balancer.
        
            - *(string) --* 
        
          - **RadiusPort** *(integer) --* 
        
            The port that your RADIUS server is using for communications. Your on-premises network must allow inbound traffic over this port from the AWS Directory Service servers.
        
          - **RadiusTimeout** *(integer) --* 
        
            The amount of time, in seconds, to wait for the RADIUS server to respond.
        
          - **RadiusRetries** *(integer) --* 
        
            The maximum number of times that communication with the RADIUS server is attempted.
        
          - **SharedSecret** *(string) --* 
        
            Required for enabling RADIUS on the directory.
        
          - **AuthenticationProtocol** *(string) --* 
        
            The protocol specified for your RADIUS endpoints.
        
          - **DisplayLabel** *(string) --* 
        
            Not currently used.
        
          - **UseSameUsername** *(boolean) --* 
        
            Not currently used.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the results of the  EnableRadius operation.
        
        """
        pass

    def enable_sso(self, DirectoryId: str, UserName: str = None, Password: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/EnableSso>`_
        
        **Request Syntax** 
        ::
        
          response = client.enable_sso(
              DirectoryId=\'string\',
              UserName=\'string\',
              Password=\'string\'
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The identifier of the directory for which to enable single-sign on.
        
        :type UserName: string
        :param UserName: 
        
          The username of an alternate account to use to enable single-sign on. This is only used for AD Connector directories. This account must have privileges to add a service principal name.
        
          If the AD Connector service account does not have privileges to add a service principal name, you can specify an alternate account with the *UserName* and *Password* parameters. These credentials are only used to enable single sign-on and are not stored by the service. The AD Connector service account is not changed.
        
        :type Password: string
        :param Password: 
        
          The password of an alternate account to use to enable single-sign on. This is only used for AD Connector directories. For more information, see the *UserName* parameter.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the results of the  EnableSso operation.
        
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

    def get_directory_limits(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/GetDirectoryLimits>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_directory_limits()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DirectoryLimits\': {
                    \'CloudOnlyDirectoriesLimit\': 123,
                    \'CloudOnlyDirectoriesCurrentCount\': 123,
                    \'CloudOnlyDirectoriesLimitReached\': True|False,
                    \'CloudOnlyMicrosoftADLimit\': 123,
                    \'CloudOnlyMicrosoftADCurrentCount\': 123,
                    \'CloudOnlyMicrosoftADLimitReached\': True|False,
                    \'ConnectedDirectoriesLimit\': 123,
                    \'ConnectedDirectoriesCurrentCount\': 123,
                    \'ConnectedDirectoriesLimitReached\': True|False
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the results of the  GetDirectoryLimits operation.
        
            - **DirectoryLimits** *(dict) --* 
        
              A  DirectoryLimits object that contains the directory limits for the current region.
        
              - **CloudOnlyDirectoriesLimit** *(integer) --* 
        
                The maximum number of cloud directories allowed in the region.
        
              - **CloudOnlyDirectoriesCurrentCount** *(integer) --* 
        
                The current number of cloud directories in the region.
        
              - **CloudOnlyDirectoriesLimitReached** *(boolean) --* 
        
                Indicates if the cloud directory limit has been reached.
        
              - **CloudOnlyMicrosoftADLimit** *(integer) --* 
        
                The maximum number of AWS Managed Microsoft AD directories allowed in the region.
        
              - **CloudOnlyMicrosoftADCurrentCount** *(integer) --* 
        
                The current number of AWS Managed Microsoft AD directories in the region.
        
              - **CloudOnlyMicrosoftADLimitReached** *(boolean) --* 
        
                Indicates if the AWS Managed Microsoft AD directory limit has been reached.
        
              - **ConnectedDirectoriesLimit** *(integer) --* 
        
                The maximum number of connected directories allowed in the region.
        
              - **ConnectedDirectoriesCurrentCount** *(integer) --* 
        
                The current number of connected directories in the region.
        
              - **ConnectedDirectoriesLimitReached** *(boolean) --* 
        
                Indicates if the connected directory limit has been reached.
        
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

    def get_snapshot_limits(self, DirectoryId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/GetSnapshotLimits>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_snapshot_limits(
              DirectoryId=\'string\'
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          Contains the identifier of the directory to obtain the limits for.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SnapshotLimits\': {
                    \'ManualSnapshotsLimit\': 123,
                    \'ManualSnapshotsCurrentCount\': 123,
                    \'ManualSnapshotsLimitReached\': True|False
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the results of the  GetSnapshotLimits operation.
        
            - **SnapshotLimits** *(dict) --* 
        
              A  SnapshotLimits object that contains the manual snapshot limits for the specified directory.
        
              - **ManualSnapshotsLimit** *(integer) --* 
        
                The maximum number of manual snapshots allowed.
        
              - **ManualSnapshotsCurrentCount** *(integer) --* 
        
                The current number of manual snapshots of the directory.
        
              - **ManualSnapshotsLimitReached** *(boolean) --* 
        
                Indicates if the manual snapshot limit has been reached.
        
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

    def list_ip_routes(self, DirectoryId: str, NextToken: str = None, Limit: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/ListIpRoutes>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_ip_routes(
              DirectoryId=\'string\',
              NextToken=\'string\',
              Limit=123
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          Identifier (ID) of the directory for which you want to retrieve the IP addresses.
        
        :type NextToken: string
        :param NextToken: 
        
          The *ListIpRoutes.NextToken* value from a previous call to  ListIpRoutes . Pass null if this is the first call.
        
        :type Limit: integer
        :param Limit: 
        
          Maximum number of items to return. If this value is zero, the maximum number of items is specified by the limitations of the operation.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IpRoutesInfo\': [
                    {
                        \'DirectoryId\': \'string\',
                        \'CidrIp\': \'string\',
                        \'IpRouteStatusMsg\': \'Adding\'|\'Added\'|\'Removing\'|\'Removed\'|\'AddFailed\'|\'RemoveFailed\',
                        \'AddedDateTime\': datetime(2015, 1, 1),
                        \'IpRouteStatusReason\': \'string\',
                        \'Description\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **IpRoutesInfo** *(list) --* 
        
              A list of  IpRoute s.
        
              - *(dict) --* 
        
                Information about one or more IP address blocks.
        
                - **DirectoryId** *(string) --* 
        
                  Identifier (ID) of the directory associated with the IP addresses.
        
                - **CidrIp** *(string) --* 
        
                  IP address block in the  IpRoute .
        
                - **IpRouteStatusMsg** *(string) --* 
        
                  The status of the IP address block.
        
                - **AddedDateTime** *(datetime) --* 
        
                  The date and time the address block was added to the directory.
        
                - **IpRouteStatusReason** *(string) --* 
        
                  The reason for the IpRouteStatusMsg.
        
                - **Description** *(string) --* 
        
                  Description of the  IpRouteInfo .
        
            - **NextToken** *(string) --* 
        
              If not null, more results are available. Pass this value for the *NextToken* parameter in a subsequent call to  ListIpRoutes to retrieve the next set of items.
        
        """
        pass

    def list_log_subscriptions(self, DirectoryId: str = None, NextToken: str = None, Limit: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/ListLogSubscriptions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_log_subscriptions(
              DirectoryId=\'string\',
              NextToken=\'string\',
              Limit=123
          )
        :type DirectoryId: string
        :param DirectoryId: 
        
          If a *DirectoryID* is provided, lists only the log subscription associated with that directory. If no *DirectoryId* is provided, lists all log subscriptions associated with your AWS account. If there are no log subscriptions for the AWS account or the directory, an empty list will be returned.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return.
        
        :type Limit: integer
        :param Limit: 
        
          The maximum number of items returned.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'LogSubscriptions\': [
                    {
                        \'DirectoryId\': \'string\',
                        \'LogGroupName\': \'string\',
                        \'SubscriptionCreatedDateTime\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **LogSubscriptions** *(list) --* 
        
              A list of active  LogSubscription objects for calling the AWS account.
        
              - *(dict) --* 
        
                Represents a log subscription, which tracks real-time data from a chosen log group to a specified destination.
        
                - **DirectoryId** *(string) --* 
        
                  Identifier (ID) of the directory that you want to associate with the log subscription.
        
                - **LogGroupName** *(string) --* 
        
                  The name of the log group.
        
                - **SubscriptionCreatedDateTime** *(datetime) --* 
        
                  The date and time that the log subscription was created.
        
            - **NextToken** *(string) --* 
        
              The token for the next set of items to return.
        
        """
        pass

    def list_schema_extensions(self, DirectoryId: str, NextToken: str = None, Limit: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/ListSchemaExtensions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_schema_extensions(
              DirectoryId=\'string\',
              NextToken=\'string\',
              Limit=123
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The identifier of the directory from which to retrieve the schema extension information.
        
        :type NextToken: string
        :param NextToken: 
        
          The ``ListSchemaExtensions.NextToken`` value from a previous call to ``ListSchemaExtensions`` . Pass null if this is the first call.
        
        :type Limit: integer
        :param Limit: 
        
          The maximum number of items to return.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SchemaExtensionsInfo\': [
                    {
                        \'DirectoryId\': \'string\',
                        \'SchemaExtensionId\': \'string\',
                        \'Description\': \'string\',
                        \'SchemaExtensionStatus\': \'Initializing\'|\'CreatingSnapshot\'|\'UpdatingSchema\'|\'Replicating\'|\'CancelInProgress\'|\'RollbackInProgress\'|\'Cancelled\'|\'Failed\'|\'Completed\',
                        \'SchemaExtensionStatusReason\': \'string\',
                        \'StartDateTime\': datetime(2015, 1, 1),
                        \'EndDateTime\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SchemaExtensionsInfo** *(list) --* 
        
              Information about the schema extensions applied to the directory.
        
              - *(dict) --* 
        
                Information about a schema extension.
        
                - **DirectoryId** *(string) --* 
        
                  The identifier of the directory to which the schema extension is applied.
        
                - **SchemaExtensionId** *(string) --* 
        
                  The identifier of the schema extension.
        
                - **Description** *(string) --* 
        
                  A description of the schema extension.
        
                - **SchemaExtensionStatus** *(string) --* 
        
                  The current status of the schema extension.
        
                - **SchemaExtensionStatusReason** *(string) --* 
        
                  The reason for the ``SchemaExtensionStatus`` .
        
                - **StartDateTime** *(datetime) --* 
        
                  The date and time that the schema extension started being applied to the directory.
        
                - **EndDateTime** *(datetime) --* 
        
                  The date and time that the schema extension was completed.
        
            - **NextToken** *(string) --* 
        
              If not null, more results are available. Pass this value for the ``NextToken`` parameter in a subsequent call to ``ListSchemaExtensions`` to retrieve the next set of items.
        
        """
        pass

    def list_tags_for_resource(self, ResourceId: str, NextToken: str = None, Limit: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/ListTagsForResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_tags_for_resource(
              ResourceId=\'string\',
              NextToken=\'string\',
              Limit=123
          )
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          Identifier (ID) of the directory for which you want to retrieve tags.
        
        :type NextToken: string
        :param NextToken: 
        
          Reserved for future use.
        
        :type Limit: integer
        :param Limit: 
        
          Reserved for future use.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Tags\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Tags** *(list) --* 
        
              List of tags returned by the ListTagsForResource operation.
        
              - *(dict) --* 
        
                Metadata assigned to a directory consisting of a key-value pair.
        
                - **Key** *(string) --* 
        
                  Required name of the tag. The string value can be Unicode characters and cannot be prefixed with \"aws:\". The string can contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
                - **Value** *(string) --* 
        
                  The optional value of the tag. The string value can be Unicode characters. The string can contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **NextToken** *(string) --* 
        
              Reserved for future use.
        
        """
        pass

    def register_event_topic(self, DirectoryId: str, TopicName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/RegisterEventTopic>`_
        
        **Request Syntax** 
        ::
        
          response = client.register_event_topic(
              DirectoryId=\'string\',
              TopicName=\'string\'
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The Directory ID that will publish status messages to the SNS topic.
        
        :type TopicName: string
        :param TopicName: **[REQUIRED]** 
        
          The SNS topic name to which the directory will publish status messages. This SNS topic must be in the same region as the specified Directory ID.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            The result of a RegisterEventTopic request.
        
        """
        pass

    def reject_shared_directory(self, SharedDirectoryId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/RejectSharedDirectory>`_
        
        **Request Syntax** 
        ::
        
          response = client.reject_shared_directory(
              SharedDirectoryId=\'string\'
          )
        :type SharedDirectoryId: string
        :param SharedDirectoryId: **[REQUIRED]** 
        
          Identifier of the shared directory in the directory consumer account. This identifier is different for each directory owner account.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SharedDirectoryId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SharedDirectoryId** *(string) --* 
        
              Identifier of the shared directory in the directory consumer account.
        
        """
        pass

    def remove_ip_routes(self, DirectoryId: str, CidrIps: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/RemoveIpRoutes>`_
        
        **Request Syntax** 
        ::
        
          response = client.remove_ip_routes(
              DirectoryId=\'string\',
              CidrIps=[
                  \'string\',
              ]
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          Identifier (ID) of the directory from which you want to remove the IP addresses.
        
        :type CidrIps: list
        :param CidrIps: **[REQUIRED]** 
        
          IP address blocks that you want to remove.
        
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

    def remove_tags_from_resource(self, ResourceId: str, TagKeys: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/RemoveTagsFromResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.remove_tags_from_resource(
              ResourceId=\'string\',
              TagKeys=[
                  \'string\',
              ]
          )
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          Identifier (ID) of the directory from which to remove the tag.
        
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]** 
        
          The tag key (name) of the tag to be removed.
        
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

    def reset_user_password(self, DirectoryId: str, UserName: str, NewPassword: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/ResetUserPassword>`_
        
        **Request Syntax** 
        ::
        
          response = client.reset_user_password(
              DirectoryId=\'string\',
              UserName=\'string\',
              NewPassword=\'string\'
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          Identifier of the AWS Managed Microsoft AD or Simple AD directory in which the user resides.
        
        :type UserName: string
        :param UserName: **[REQUIRED]** 
        
          The user name of the user whose password will be reset.
        
        :type NewPassword: string
        :param NewPassword: **[REQUIRED]** 
        
          The new password that will be reset.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def restore_from_snapshot(self, SnapshotId: str) -> Dict:
        """
        
        When you restore a directory from a snapshot, any changes made to the directory after the snapshot date are overwritten.
        
        This action returns as soon as the restore operation is initiated. You can monitor the progress of the restore operation by calling the  DescribeDirectories operation with the directory identifier. When the **DirectoryDescription.Stage** value changes to ``Active`` , the restore operation is complete.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/RestoreFromSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.restore_from_snapshot(
              SnapshotId=\'string\'
          )
        :type SnapshotId: string
        :param SnapshotId: **[REQUIRED]** 
        
          The identifier of the snapshot to restore from.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the results of the  RestoreFromSnapshot operation.
        
        """
        pass

    def share_directory(self, DirectoryId: str, ShareTarget: Dict, ShareMethod: str, ShareNotes: str = None) -> Dict:
        """
        
        When you share your AWS Managed Microsoft AD directory, AWS Directory Service creates a shared directory in the directory consumer account. This shared directory contains the metadata to provide access to the directory within the directory owner account. The shared directory is visible in all VPCs in the directory consumer account.
        
        The ``ShareMethod`` parameter determines whether the specified directory can be shared between AWS accounts inside the same AWS organization (``ORGANIZATIONS`` ). It also determines whether you can share the directory with any other AWS account either inside or outside of the organization (``HANDSHAKE`` ).
        
        The ``ShareNotes`` parameter is only used when ``HANDSHAKE`` is called, which sends a directory sharing request to the directory consumer. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/ShareDirectory>`_
        
        **Request Syntax** 
        ::
        
          response = client.share_directory(
              DirectoryId=\'string\',
              ShareNotes=\'string\',
              ShareTarget={
                  \'Id\': \'string\',
                  \'Type\': \'ACCOUNT\'
              },
              ShareMethod=\'ORGANIZATIONS\'|\'HANDSHAKE\'
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          Identifier of the AWS Managed Microsoft AD directory that you want to share with other AWS accounts.
        
        :type ShareNotes: string
        :param ShareNotes: 
        
          A directory share request that is sent by the directory owner to the directory consumer. The request includes a typed message to help the directory consumer administrator determine whether to approve or reject the share invitation.
        
        :type ShareTarget: dict
        :param ShareTarget: **[REQUIRED]** 
        
          Identifier for the directory consumer account with whom the directory is to be shared.
        
          - **Id** *(string) --* **[REQUIRED]** 
        
            Identifier of the directory consumer account.
        
          - **Type** *(string) --* **[REQUIRED]** 
        
            Type of identifier to be used in the ``Id`` field.
        
        :type ShareMethod: string
        :param ShareMethod: **[REQUIRED]** 
        
          The method used when sharing a directory to determine whether the directory should be shared within your AWS organization (``ORGANIZATIONS`` ) or with any AWS account by sending a directory sharing request (``HANDSHAKE`` ).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SharedDirectoryId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SharedDirectoryId** *(string) --* 
        
              Identifier of the directory that is stored in the directory consumer account that is shared from the specified directory (``DirectoryId`` ).
        
        """
        pass

    def start_schema_extension(self, DirectoryId: str, CreateSnapshotBeforeSchemaExtension: bool, LdifContent: str, Description: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/StartSchemaExtension>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_schema_extension(
              DirectoryId=\'string\',
              CreateSnapshotBeforeSchemaExtension=True|False,
              LdifContent=\'string\',
              Description=\'string\'
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The identifier of the directory for which the schema extension will be applied to.
        
        :type CreateSnapshotBeforeSchemaExtension: boolean
        :param CreateSnapshotBeforeSchemaExtension: **[REQUIRED]** 
        
          If true, creates a snapshot of the directory before applying the schema extension.
        
        :type LdifContent: string
        :param LdifContent: **[REQUIRED]** 
        
          The LDIF file represented as a string. To construct the LdifContent string, precede each line as it would be formatted in an ldif file with \n. See the example request below for more details. The file size can be no larger than 1MB.
        
        :type Description: string
        :param Description: **[REQUIRED]** 
        
          A description of the schema extension.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SchemaExtensionId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SchemaExtensionId** *(string) --* 
        
              The identifier of the schema extension that will be applied.
        
        """
        pass

    def unshare_directory(self, DirectoryId: str, UnshareTarget: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/UnshareDirectory>`_
        
        **Request Syntax** 
        ::
        
          response = client.unshare_directory(
              DirectoryId=\'string\',
              UnshareTarget={
                  \'Id\': \'string\',
                  \'Type\': \'ACCOUNT\'
              }
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The identifier of the AWS Managed Microsoft AD directory that you want to stop sharing.
        
        :type UnshareTarget: dict
        :param UnshareTarget: **[REQUIRED]** 
        
          Identifier for the directory consumer account with whom the directory has to be unshared.
        
          - **Id** *(string) --* **[REQUIRED]** 
        
            Identifier of the directory consumer account.
        
          - **Type** *(string) --* **[REQUIRED]** 
        
            Type of identifier to be used in the *Id* field.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SharedDirectoryId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SharedDirectoryId** *(string) --* 
        
              Identifier of the directory stored in the directory consumer account that is to be unshared from the specified directory (``DirectoryId`` ).
        
        """
        pass

    def update_conditional_forwarder(self, DirectoryId: str, RemoteDomainName: str, DnsIpAddrs: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/UpdateConditionalForwarder>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_conditional_forwarder(
              DirectoryId=\'string\',
              RemoteDomainName=\'string\',
              DnsIpAddrs=[
                  \'string\',
              ]
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The directory ID of the AWS directory for which to update the conditional forwarder.
        
        :type RemoteDomainName: string
        :param RemoteDomainName: **[REQUIRED]** 
        
          The fully qualified domain name (FQDN) of the remote domain with which you will set up a trust relationship.
        
        :type DnsIpAddrs: list
        :param DnsIpAddrs: **[REQUIRED]** 
        
          The updated IP addresses of the remote DNS server associated with the conditional forwarder.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            The result of an UpdateConditionalForwarder request.
        
        """
        pass

    def update_number_of_domain_controllers(self, DirectoryId: str, DesiredNumber: int) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/UpdateNumberOfDomainControllers>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_number_of_domain_controllers(
              DirectoryId=\'string\',
              DesiredNumber=123
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          Identifier of the directory to which the domain controllers will be added or removed.
        
        :type DesiredNumber: integer
        :param DesiredNumber: **[REQUIRED]** 
        
          The number of domain controllers desired in the directory.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_radius(self, DirectoryId: str, RadiusSettings: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/UpdateRadius>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_radius(
              DirectoryId=\'string\',
              RadiusSettings={
                  \'RadiusServers\': [
                      \'string\',
                  ],
                  \'RadiusPort\': 123,
                  \'RadiusTimeout\': 123,
                  \'RadiusRetries\': 123,
                  \'SharedSecret\': \'string\',
                  \'AuthenticationProtocol\': \'PAP\'|\'CHAP\'|\'MS-CHAPv1\'|\'MS-CHAPv2\',
                  \'DisplayLabel\': \'string\',
                  \'UseSameUsername\': True|False
              }
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The identifier of the directory for which to update the RADIUS server information.
        
        :type RadiusSettings: dict
        :param RadiusSettings: **[REQUIRED]** 
        
          A  RadiusSettings object that contains information about the RADIUS server.
        
          - **RadiusServers** *(list) --* 
        
            An array of strings that contains the IP addresses of the RADIUS server endpoints, or the IP addresses of your RADIUS server load balancer.
        
            - *(string) --* 
        
          - **RadiusPort** *(integer) --* 
        
            The port that your RADIUS server is using for communications. Your on-premises network must allow inbound traffic over this port from the AWS Directory Service servers.
        
          - **RadiusTimeout** *(integer) --* 
        
            The amount of time, in seconds, to wait for the RADIUS server to respond.
        
          - **RadiusRetries** *(integer) --* 
        
            The maximum number of times that communication with the RADIUS server is attempted.
        
          - **SharedSecret** *(string) --* 
        
            Required for enabling RADIUS on the directory.
        
          - **AuthenticationProtocol** *(string) --* 
        
            The protocol specified for your RADIUS endpoints.
        
          - **DisplayLabel** *(string) --* 
        
            Not currently used.
        
          - **UseSameUsername** *(boolean) --* 
        
            Not currently used.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the results of the  UpdateRadius operation.
        
        """
        pass

    def update_trust(self, TrustId: str, SelectiveAuth: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/UpdateTrust>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_trust(
              TrustId=\'string\',
              SelectiveAuth=\'Enabled\'|\'Disabled\'
          )
        :type TrustId: string
        :param TrustId: **[REQUIRED]** 
        
          Identifier of the trust relationship.
        
        :type SelectiveAuth: string
        :param SelectiveAuth: 
        
          Updates selective authentication for the trust.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'RequestId\': \'string\',
                \'TrustId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **RequestId** *(string) --* 
        
              The AWS request identifier.
        
            - **TrustId** *(string) --* 
        
              Identifier of the trust relationship.
        
        """
        pass

    def verify_trust(self, TrustId: str) -> Dict:
        """
        
        This action verifies a trust relationship between your AWS Managed Microsoft AD directory and an external domain.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/VerifyTrust>`_
        
        **Request Syntax** 
        ::
        
          response = client.verify_trust(
              TrustId=\'string\'
          )
        :type TrustId: string
        :param TrustId: **[REQUIRED]** 
        
          The unique Trust ID of the trust relationship to verify.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TrustId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Result of a VerifyTrust request.
        
            - **TrustId** *(string) --* 
        
              The unique Trust ID of the trust relationship that was verified.
        
        """
        pass
