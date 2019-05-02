from typing import Dict
from typing import List
from botocore.paginate import Paginator


class DescribeDirectories(Paginator):
    def paginate(self, DirectoryIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DirectoryService.Client.describe_directories`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DescribeDirectories>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DirectoryIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'DirectoryDescriptions': [
                    {
                        'DirectoryId': 'string',
                        'Name': 'string',
                        'ShortName': 'string',
                        'Size': 'Small'|'Large',
                        'Edition': 'Enterprise'|'Standard',
                        'Alias': 'string',
                        'AccessUrl': 'string',
                        'Description': 'string',
                        'DnsIpAddrs': [
                            'string',
                        ],
                        'Stage': 'Requested'|'Creating'|'Created'|'Active'|'Inoperable'|'Impaired'|'Restoring'|'RestoreFailed'|'Deleting'|'Deleted'|'Failed',
                        'ShareStatus': 'Shared'|'PendingAcceptance'|'Rejected'|'Rejecting'|'RejectFailed'|'Sharing'|'ShareFailed'|'Deleted'|'Deleting',
                        'ShareMethod': 'ORGANIZATIONS'|'HANDSHAKE',
                        'ShareNotes': 'string',
                        'LaunchTime': datetime(2015, 1, 1),
                        'StageLastUpdatedDateTime': datetime(2015, 1, 1),
                        'Type': 'SimpleAD'|'ADConnector'|'MicrosoftAD'|'SharedMicrosoftAD',
                        'VpcSettings': {
                            'VpcId': 'string',
                            'SubnetIds': [
                                'string',
                            ],
                            'SecurityGroupId': 'string',
                            'AvailabilityZones': [
                                'string',
                            ]
                        },
                        'ConnectSettings': {
                            'VpcId': 'string',
                            'SubnetIds': [
                                'string',
                            ],
                            'CustomerUserName': 'string',
                            'SecurityGroupId': 'string',
                            'AvailabilityZones': [
                                'string',
                            ],
                            'ConnectIps': [
                                'string',
                            ]
                        },
                        'RadiusSettings': {
                            'RadiusServers': [
                                'string',
                            ],
                            'RadiusPort': 123,
                            'RadiusTimeout': 123,
                            'RadiusRetries': 123,
                            'SharedSecret': 'string',
                            'AuthenticationProtocol': 'PAP'|'CHAP'|'MS-CHAPv1'|'MS-CHAPv2',
                            'DisplayLabel': 'string',
                            'UseSameUsername': True|False
                        },
                        'RadiusStatus': 'Creating'|'Completed'|'Failed',
                        'StageReason': 'string',
                        'SsoEnabled': True|False,
                        'DesiredNumberOfDomainControllers': 123,
                        'OwnerDirectoryDescription': {
                            'DirectoryId': 'string',
                            'AccountId': 'string',
                            'DnsIpAddrs': [
                                'string',
                            ],
                            'VpcSettings': {
                                'VpcId': 'string',
                                'SubnetIds': [
                                    'string',
                                ],
                                'SecurityGroupId': 'string',
                                'AvailabilityZones': [
                                    'string',
                                ]
                            },
                            'RadiusSettings': {
                                'RadiusServers': [
                                    'string',
                                ],
                                'RadiusPort': 123,
                                'RadiusTimeout': 123,
                                'RadiusRetries': 123,
                                'SharedSecret': 'string',
                                'AuthenticationProtocol': 'PAP'|'CHAP'|'MS-CHAPv1'|'MS-CHAPv2',
                                'DisplayLabel': 'string',
                                'UseSameUsername': True|False
                            },
                            'RadiusStatus': 'Creating'|'Completed'|'Failed'
                        }
                    },
                ],
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
        :type DirectoryIds: list
        :param DirectoryIds:
          A list of identifiers of the directories for which to obtain the information. If this member is null, all directories that belong to the current account are returned.
          An empty list results in an ``InvalidParameterException`` being thrown.
          - *(string) --*
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


class DescribeDomainControllers(Paginator):
    def paginate(self, DirectoryId: str, DomainControllerIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DirectoryService.Client.describe_domain_controllers`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DescribeDomainControllers>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DirectoryId='string',
              DomainControllerIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'DomainControllers': [
                    {
                        'DirectoryId': 'string',
                        'DomainControllerId': 'string',
                        'DnsIpAddr': 'string',
                        'VpcId': 'string',
                        'SubnetId': 'string',
                        'AvailabilityZone': 'string',
                        'Status': 'Creating'|'Active'|'Impaired'|'Restoring'|'Deleting'|'Deleted'|'Failed',
                        'StatusReason': 'string',
                        'LaunchTime': datetime(2015, 1, 1),
                        'StatusLastUpdatedDateTime': datetime(2015, 1, 1)
                    },
                ],
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
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]**
          Identifier of the directory for which to retrieve the domain controller information.
        :type DomainControllerIds: list
        :param DomainControllerIds:
          A list of identifiers for the domain controllers whose information will be provided.
          - *(string) --*
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


class DescribeSharedDirectories(Paginator):
    def paginate(self, OwnerDirectoryId: str, SharedDirectoryIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DirectoryService.Client.describe_shared_directories`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DescribeSharedDirectories>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              OwnerDirectoryId='string',
              SharedDirectoryIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'SharedDirectories': [
                    {
                        'OwnerAccountId': 'string',
                        'OwnerDirectoryId': 'string',
                        'ShareMethod': 'ORGANIZATIONS'|'HANDSHAKE',
                        'SharedAccountId': 'string',
                        'SharedDirectoryId': 'string',
                        'ShareStatus': 'Shared'|'PendingAcceptance'|'Rejected'|'Rejecting'|'RejectFailed'|'Sharing'|'ShareFailed'|'Deleted'|'Deleting',
                        'ShareNotes': 'string',
                        'CreatedDateTime': datetime(2015, 1, 1),
                        'LastUpdatedDateTime': datetime(2015, 1, 1)
                    },
                ],
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
        :type OwnerDirectoryId: string
        :param OwnerDirectoryId: **[REQUIRED]**
          Returns the identifier of the directory in the directory owner account.
        :type SharedDirectoryIds: list
        :param SharedDirectoryIds:
          A list of identifiers of all shared directories in your account.
          - *(string) --*
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


class DescribeSnapshots(Paginator):
    def paginate(self, DirectoryId: str = None, SnapshotIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DirectoryService.Client.describe_snapshots`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DescribeSnapshots>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DirectoryId='string',
              SnapshotIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Snapshots': [
                    {
                        'DirectoryId': 'string',
                        'SnapshotId': 'string',
                        'Type': 'Auto'|'Manual',
                        'Name': 'string',
                        'Status': 'Creating'|'Completed'|'Failed',
                        'StartTime': datetime(2015, 1, 1)
                    },
                ],
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
        :type DirectoryId: string
        :param DirectoryId:
          The identifier of the directory for which to retrieve snapshot information.
        :type SnapshotIds: list
        :param SnapshotIds:
          A list of identifiers of the snapshots to obtain the information for. If this member is null or empty, all snapshots are returned using the *Limit* and *NextToken* members.
          - *(string) --*
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


class DescribeTrusts(Paginator):
    def paginate(self, DirectoryId: str = None, TrustIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DirectoryService.Client.describe_trusts`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/DescribeTrusts>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DirectoryId='string',
              TrustIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Trusts': [
                    {
                        'DirectoryId': 'string',
                        'TrustId': 'string',
                        'RemoteDomainName': 'string',
                        'TrustType': 'Forest'|'External',
                        'TrustDirection': 'One-Way: Outgoing'|'One-Way: Incoming'|'Two-Way',
                        'TrustState': 'Creating'|'Created'|'Verifying'|'VerifyFailed'|'Verified'|'Updating'|'UpdateFailed'|'Updated'|'Deleting'|'Deleted'|'Failed',
                        'CreatedDateTime': datetime(2015, 1, 1),
                        'LastUpdatedDateTime': datetime(2015, 1, 1),
                        'StateLastUpdatedDateTime': datetime(2015, 1, 1),
                        'TrustStateReason': 'string',
                        'SelectiveAuth': 'Enabled'|'Disabled'
                    },
                ],
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
        :type DirectoryId: string
        :param DirectoryId:
          The Directory ID of the AWS directory that is a part of the requested trust relationship.
        :type TrustIds: list
        :param TrustIds:
          A list of identifiers of the trust relationships for which to obtain the information. If this member is null, all trust relationships that belong to the current account are returned.
          An empty list results in an ``InvalidParameterException`` being thrown.
          - *(string) --*
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


class ListIpRoutes(Paginator):
    def paginate(self, DirectoryId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DirectoryService.Client.list_ip_routes`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/ListIpRoutes>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DirectoryId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'IpRoutesInfo': [
                    {
                        'DirectoryId': 'string',
                        'CidrIp': 'string',
                        'IpRouteStatusMsg': 'Adding'|'Added'|'Removing'|'Removed'|'AddFailed'|'RemoveFailed',
                        'AddedDateTime': datetime(2015, 1, 1),
                        'IpRouteStatusReason': 'string',
                        'Description': 'string'
                    },
                ],
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
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]**
          Identifier (ID) of the directory for which you want to retrieve the IP addresses.
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


class ListLogSubscriptions(Paginator):
    def paginate(self, DirectoryId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DirectoryService.Client.list_log_subscriptions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/ListLogSubscriptions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DirectoryId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'LogSubscriptions': [
                    {
                        'DirectoryId': 'string',
                        'LogGroupName': 'string',
                        'SubscriptionCreatedDateTime': datetime(2015, 1, 1)
                    },
                ],
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
        :type DirectoryId: string
        :param DirectoryId:
          If a *DirectoryID* is provided, lists only the log subscription associated with that directory. If no *DirectoryId* is provided, lists all log subscriptions associated with your AWS account. If there are no log subscriptions for the AWS account or the directory, an empty list will be returned.
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


class ListSchemaExtensions(Paginator):
    def paginate(self, DirectoryId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DirectoryService.Client.list_schema_extensions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/ListSchemaExtensions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DirectoryId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'SchemaExtensionsInfo': [
                    {
                        'DirectoryId': 'string',
                        'SchemaExtensionId': 'string',
                        'Description': 'string',
                        'SchemaExtensionStatus': 'Initializing'|'CreatingSnapshot'|'UpdatingSchema'|'Replicating'|'CancelInProgress'|'RollbackInProgress'|'Cancelled'|'Failed'|'Completed',
                        'SchemaExtensionStatusReason': 'string',
                        'StartDateTime': datetime(2015, 1, 1),
                        'EndDateTime': datetime(2015, 1, 1)
                    },
                ],
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
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]**
          The identifier of the directory from which to retrieve the schema extension information.
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


class ListTagsForResource(Paginator):
    def paginate(self, ResourceId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DirectoryService.Client.list_tags_for_resource`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/ListTagsForResource>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
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
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Tags** *(list) --* 
              List of tags returned by the ListTagsForResource operation.
              - *(dict) --* 
                Metadata assigned to a directory consisting of a key-value pair.
                - **Key** *(string) --* 
                  Required name of the tag. The string value can be Unicode characters and cannot be prefixed with "aws:". The string can contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
                - **Value** *(string) --* 
                  The optional value of the tag. The string value can be Unicode characters. The string can contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**
          Identifier (ID) of the directory for which you want to retrieve tags.
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
