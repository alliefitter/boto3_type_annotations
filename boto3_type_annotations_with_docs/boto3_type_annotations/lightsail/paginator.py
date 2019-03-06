from typing import Dict
from botocore.paginate import Paginator


class GetActiveNames(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_active_names`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetActiveNames>`_
        
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
                'activeNames': [
                    'string',
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **activeNames** *(list) --* 
              The list of active names returned by the get active names request.
              - *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class GetBlueprints(Paginator):
    def paginate(self, includeInactive: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_blueprints`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetBlueprints>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              includeInactive=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'blueprints': [
                    {
                        'blueprintId': 'string',
                        'name': 'string',
                        'group': 'string',
                        'type': 'os'|'app',
                        'description': 'string',
                        'isActive': True|False,
                        'minPower': 123,
                        'version': 'string',
                        'versionCode': 'string',
                        'productUrl': 'string',
                        'licenseUrl': 'string',
                        'platform': 'LINUX_UNIX'|'WINDOWS'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **blueprints** *(list) --* 
              An array of key-value pairs that contains information about the available blueprints.
              - *(dict) --* 
                Describes a blueprint (a virtual private server image).
                - **blueprintId** *(string) --* 
                  The ID for the virtual private server image (e.g., ``app_wordpress_4_4`` or ``app_lamp_7_0`` ).
                - **name** *(string) --* 
                  The friendly name of the blueprint (e.g., ``Amazon Linux`` ).
                - **group** *(string) --* 
                  The group name of the blueprint (e.g., ``amazon-linux`` ).
                - **type** *(string) --* 
                  The type of the blueprint (e.g., ``os`` or ``app`` ).
                - **description** *(string) --* 
                  The description of the blueprint.
                - **isActive** *(boolean) --* 
                  A Boolean value indicating whether the blueprint is active. Inactive blueprints are listed to support customers with existing instances but are not necessarily available for launch of new instances. Blueprints are marked inactive when they become outdated due to operating system updates or new application releases.
                - **minPower** *(integer) --* 
                  The minimum bundle power required to run this blueprint. For example, you need a bundle with a power value of 500 or more to create an instance that uses a blueprint with a minimum power value of 500. ``0`` indicates that the blueprint runs on all instance sizes. 
                - **version** *(string) --* 
                  The version number of the operating system, application, or stack (e.g., ``2016.03.0`` ).
                - **versionCode** *(string) --* 
                  The version code.
                - **productUrl** *(string) --* 
                  The product URL to learn more about the image or blueprint.
                - **licenseUrl** *(string) --* 
                  The end-user license agreement URL for the image or blueprint.
                - **platform** *(string) --* 
                  The operating system platform (either Linux/Unix-based or Windows Server-based) of the blueprint.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type includeInactive: boolean
        :param includeInactive:
          A Boolean value indicating whether to include inactive results in your request.
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


class GetBundles(Paginator):
    def paginate(self, includeInactive: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_bundles`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetBundles>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              includeInactive=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'bundles': [
                    {
                        'price': ...,
                        'cpuCount': 123,
                        'diskSizeInGb': 123,
                        'bundleId': 'string',
                        'instanceType': 'string',
                        'isActive': True|False,
                        'name': 'string',
                        'power': 123,
                        'ramSizeInGb': ...,
                        'transferPerMonthInGb': 123,
                        'supportedPlatforms': [
                            'LINUX_UNIX'|'WINDOWS',
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **bundles** *(list) --* 
              An array of key-value pairs that contains information about the available bundles.
              - *(dict) --* 
                Describes a bundle, which is a set of specs describing your virtual private server (or *instance* ).
                - **price** *(float) --* 
                  The price in US dollars (e.g., ``5.0`` ).
                - **cpuCount** *(integer) --* 
                  The number of vCPUs included in the bundle (e.g., ``2`` ).
                - **diskSizeInGb** *(integer) --* 
                  The size of the SSD (e.g., ``30`` ).
                - **bundleId** *(string) --* 
                  The bundle ID (e.g., ``micro_1_0`` ).
                - **instanceType** *(string) --* 
                  The Amazon EC2 instance type (e.g., ``t2.micro`` ).
                - **isActive** *(boolean) --* 
                  A Boolean value indicating whether the bundle is active.
                - **name** *(string) --* 
                  A friendly name for the bundle (e.g., ``Micro`` ).
                - **power** *(integer) --* 
                  A numeric value that represents the power of the bundle (e.g., ``500`` ). You can use the bundle's power value in conjunction with a blueprint's minimum power value to determine whether the blueprint will run on the bundle. For example, you need a bundle with a power value of 500 or more to create an instance that uses a blueprint with a minimum power value of 500.
                - **ramSizeInGb** *(float) --* 
                  The amount of RAM in GB (e.g., ``2.0`` ).
                - **transferPerMonthInGb** *(integer) --* 
                  The data transfer rate per month in GB (e.g., ``2000`` ).
                - **supportedPlatforms** *(list) --* 
                  The operating system platform (Linux/Unix-based or Windows Server-based) that the bundle supports. You can only launch a ``WINDOWS`` bundle on a blueprint that supports the ``WINDOWS`` platform. ``LINUX_UNIX`` blueprints require a ``LINUX_UNIX`` bundle.
                  - *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type includeInactive: boolean
        :param includeInactive:
          A Boolean value that indicates whether to include inactive bundle results in your request.
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


class GetCloudFormationStackRecords(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_cloud_formation_stack_records`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetCloudFormationStackRecords>`_
        
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
                'cloudFormationStackRecords': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'location': {
                            'availabilityZone': 'string',
                            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                        },
                        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                        'state': 'Started'|'Succeeded'|'Failed',
                        'sourceInfo': [
                            {
                                'resourceType': 'ExportSnapshotRecord',
                                'name': 'string',
                                'arn': 'string'
                            },
                        ],
                        'destinationInfo': {
                            'id': 'string',
                            'service': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **cloudFormationStackRecords** *(list) --* 
              A list of objects describing the CloudFormation stack records.
              - *(dict) --* 
                Describes a CloudFormation stack record created as a result of the ``create cloud formation stack`` operation.
                A CloudFormation stack record provides information about the AWS CloudFormation stack used to create a new Amazon Elastic Compute Cloud instance from an exported Lightsail instance snapshot.
                - **name** *(string) --* 
                  The name of the CloudFormation stack record. It starts with ``CloudFormationStackRecord`` followed by a GUID.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the CloudFormation stack record.
                - **createdAt** *(datetime) --* 
                  The date when the CloudFormation stack record was created.
                - **location** *(dict) --* 
                  A list of objects describing the Availability Zone and AWS Region of the CloudFormation stack record.
                  - **availabilityZone** *(string) --* 
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
                  - **regionName** *(string) --* 
                    The AWS Region name.
                - **resourceType** *(string) --* 
                  The Lightsail resource type (e.g., ``CloudFormationStackRecord`` ).
                - **state** *(string) --* 
                  The current state of the CloudFormation stack record.
                - **sourceInfo** *(list) --* 
                  A list of objects describing the source of the CloudFormation stack record.
                  - *(dict) --* 
                    Describes the source of a CloudFormation stack record (i.e., the export snapshot record).
                    - **resourceType** *(string) --* 
                      The Lightsail resource type (e.g., ``ExportSnapshotRecord`` ).
                    - **name** *(string) --* 
                      The name of the record.
                    - **arn** *(string) --* 
                      The Amazon Resource Name (ARN) of the export snapshot record.
                - **destinationInfo** *(dict) --* 
                  A list of objects describing the destination service, which is AWS CloudFormation, and the Amazon Resource Name (ARN) of the AWS CloudFormation stack.
                  - **id** *(string) --* 
                    The ID of the resource created at the destination.
                  - **service** *(string) --* 
                    The destination service of the record.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class GetDiskSnapshots(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_disk_snapshots`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetDiskSnapshots>`_
        
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
                'diskSnapshots': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'supportCode': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'location': {
                            'availabilityZone': 'string',
                            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                        },
                        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'sizeInGb': 123,
                        'state': 'pending'|'completed'|'error'|'unknown',
                        'progress': 'string',
                        'fromDiskName': 'string',
                        'fromDiskArn': 'string',
                        'fromInstanceName': 'string',
                        'fromInstanceArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **diskSnapshots** *(list) --* 
              An array of objects containing information about all block storage disk snapshots.
              - *(dict) --* 
                Describes a block storage disk snapshot.
                - **name** *(string) --* 
                  The name of the disk snapshot (e.g., ``my-disk-snapshot`` ).
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the disk snapshot.
                - **supportCode** *(string) --* 
                  The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
                - **createdAt** *(datetime) --* 
                  The date when the disk snapshot was created.
                - **location** *(dict) --* 
                  The AWS Region and Availability Zone where the disk snapshot was created.
                  - **availabilityZone** *(string) --* 
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
                  - **regionName** *(string) --* 
                    The AWS Region name.
                - **resourceType** *(string) --* 
                  The Lightsail resource type (e.g., ``DiskSnapshot`` ).
                - **tags** *(list) --* 
                  The tag keys and optional values for the resource. For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                  - *(dict) --* 
                    Describes a tag key and optional value assigned to an Amazon Lightsail resource.
                    For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                    - **key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                    - **value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                - **sizeInGb** *(integer) --* 
                  The size of the disk in GB.
                - **state** *(string) --* 
                  The status of the disk snapshot operation.
                - **progress** *(string) --* 
                  The progress of the disk snapshot operation.
                - **fromDiskName** *(string) --* 
                  The unique name of the source disk from which the disk snapshot was created.
                - **fromDiskArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the source disk from which the disk snapshot was created.
                - **fromInstanceName** *(string) --* 
                  The unique name of the source instance from which the disk (system volume) snapshot was created.
                - **fromInstanceArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the source instance from which the disk (system volume) snapshot was created.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class GetDisks(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_disks`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetDisks>`_
        
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
                'disks': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'supportCode': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'location': {
                            'availabilityZone': 'string',
                            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                        },
                        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'sizeInGb': 123,
                        'isSystemDisk': True|False,
                        'iops': 123,
                        'path': 'string',
                        'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                        'attachedTo': 'string',
                        'isAttached': True|False,
                        'attachmentState': 'string',
                        'gbInUse': 123
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **disks** *(list) --* 
              An array of objects containing information about all block storage disks.
              - *(dict) --* 
                Describes a system disk or an block storage disk.
                - **name** *(string) --* 
                  The unique name of the disk.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the disk.
                - **supportCode** *(string) --* 
                  The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
                - **createdAt** *(datetime) --* 
                  The date when the disk was created.
                - **location** *(dict) --* 
                  The AWS Region and Availability Zone where the disk is located.
                  - **availabilityZone** *(string) --* 
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
                  - **regionName** *(string) --* 
                    The AWS Region name.
                - **resourceType** *(string) --* 
                  The Lightsail resource type (e.g., ``Disk`` ).
                - **tags** *(list) --* 
                  The tag keys and optional values for the resource. For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                  - *(dict) --* 
                    Describes a tag key and optional value assigned to an Amazon Lightsail resource.
                    For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                    - **key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                    - **value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                - **sizeInGb** *(integer) --* 
                  The size of the disk in GB.
                - **isSystemDisk** *(boolean) --* 
                  A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).
                - **iops** *(integer) --* 
                  The input/output operations per second (IOPS) of the disk.
                - **path** *(string) --* 
                  The disk path.
                - **state** *(string) --* 
                  Describes the status of the disk.
                - **attachedTo** *(string) --* 
                  The resources to which the disk is attached.
                - **isAttached** *(boolean) --* 
                  A Boolean value indicating whether the disk is attached.
                - **attachmentState** *(string) --* 
                  (Deprecated) The attachment state of the disk.
                  .. note::
                    In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.
                - **gbInUse** *(integer) --* 
                  (Deprecated) The number of GB in use by the disk.
                  .. note::
                    In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class GetDomains(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_domains`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetDomains>`_
        
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
                'domains': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'supportCode': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'location': {
                            'availabilityZone': 'string',
                            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                        },
                        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'domainEntries': [
                            {
                                'id': 'string',
                                'name': 'string',
                                'target': 'string',
                                'isAlias': True|False,
                                'type': 'string',
                                'options': {
                                    'string': 'string'
                                }
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **domains** *(list) --* 
              An array of key-value pairs containing information about each of the domain entries in the user's account.
              - *(dict) --* 
                Describes a domain where you are storing recordsets in Lightsail.
                - **name** *(string) --* 
                  The name of the domain.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the domain recordset (e.g., ``arn:aws:lightsail:global:123456789101:Domain/824cede0-abc7-4f84-8dbc-12345EXAMPLE`` ).
                - **supportCode** *(string) --* 
                  The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
                - **createdAt** *(datetime) --* 
                  The date when the domain recordset was created.
                - **location** *(dict) --* 
                  The AWS Region and Availability Zones where the domain recordset was created.
                  - **availabilityZone** *(string) --* 
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
                  - **regionName** *(string) --* 
                    The AWS Region name.
                - **resourceType** *(string) --* 
                  The resource type. 
                - **tags** *(list) --* 
                  The tag keys and optional values for the resource. For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                  - *(dict) --* 
                    Describes a tag key and optional value assigned to an Amazon Lightsail resource.
                    For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                    - **key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                    - **value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                - **domainEntries** *(list) --* 
                  An array of key-value pairs containing information about the domain entries.
                  - *(dict) --* 
                    Describes a domain recordset entry.
                    - **id** *(string) --* 
                      The ID of the domain recordset entry.
                    - **name** *(string) --* 
                      The name of the domain.
                    - **target** *(string) --* 
                      The target AWS name server (e.g., ``ns-111.awsdns-22.com.`` ).
                      For Lightsail load balancers, the value looks like ``ab1234c56789c6b86aba6fb203d443bc-123456789.us-east-2.elb.amazonaws.com`` . Be sure to also set ``isAlias`` to ``true`` when setting up an A record for a load balancer.
                    - **isAlias** *(boolean) --* 
                      When ``true`` , specifies whether the domain entry is an alias used by the Lightsail load balancer. You can include an alias (A type) record in your request, which points to a load balancer DNS name and routes traffic to your load balancer
                    - **type** *(string) --* 
                      The type of domain entry (e.g., ``SOA`` or ``NS`` ).
                    - **options** *(dict) --* 
                      (Deprecated) The options for the domain entry.
                      .. note::
                        In releases prior to November 29, 2017, this parameter was not included in the API response. It is now deprecated.
                      - *(string) --* 
                        - *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class GetExportSnapshotRecords(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_export_snapshot_records`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetExportSnapshotRecords>`_
        
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
                'exportSnapshotRecords': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'location': {
                            'availabilityZone': 'string',
                            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                        },
                        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                        'state': 'Started'|'Succeeded'|'Failed',
                        'sourceInfo': {
                            'resourceType': 'InstanceSnapshot'|'DiskSnapshot',
                            'createdAt': datetime(2015, 1, 1),
                            'name': 'string',
                            'arn': 'string',
                            'fromResourceName': 'string',
                            'fromResourceArn': 'string',
                            'instanceSnapshotInfo': {
                                'fromBundleId': 'string',
                                'fromBlueprintId': 'string',
                                'fromDiskInfo': [
                                    {
                                        'name': 'string',
                                        'path': 'string',
                                        'sizeInGb': 123,
                                        'isSystemDisk': True|False
                                    },
                                ]
                            },
                            'diskSnapshotInfo': {
                                'sizeInGb': 123
                            }
                        },
                        'destinationInfo': {
                            'id': 'string',
                            'service': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **exportSnapshotRecords** *(list) --* 
              A list of objects describing the export snapshot records.
              - *(dict) --* 
                Describes an export snapshot record.
                - **name** *(string) --* 
                  The export snapshot record name.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the export snapshot record.
                - **createdAt** *(datetime) --* 
                  The date when the export snapshot record was created.
                - **location** *(dict) --* 
                  The AWS Region and Availability Zone where the export snapshot record is located.
                  - **availabilityZone** *(string) --* 
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
                  - **regionName** *(string) --* 
                    The AWS Region name.
                - **resourceType** *(string) --* 
                  The Lightsail resource type (e.g., ``ExportSnapshotRecord`` ).
                - **state** *(string) --* 
                  The state of the export snapshot record.
                - **sourceInfo** *(dict) --* 
                  A list of objects describing the source of the export snapshot record.
                  - **resourceType** *(string) --* 
                    The Lightsail resource type (e.g., ``InstanceSnapshot`` or ``DiskSnapshot`` ).
                  - **createdAt** *(datetime) --* 
                    The date when the source instance or disk snapshot was created.
                  - **name** *(string) --* 
                    The name of the source instance or disk snapshot.
                  - **arn** *(string) --* 
                    The Amazon Resource Name (ARN) of the source instance or disk snapshot.
                  - **fromResourceName** *(string) --* 
                    The name of the snapshot's source instance or disk.
                  - **fromResourceArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the snapshot's source instance or disk.
                  - **instanceSnapshotInfo** *(dict) --* 
                    A list of objects describing an instance snapshot.
                    - **fromBundleId** *(string) --* 
                      The bundle ID from which the source instance was created (e.g., ``micro_1_0`` ).
                    - **fromBlueprintId** *(string) --* 
                      The blueprint ID from which the source instance (e.g., ``os_debian_8_3`` ).
                    - **fromDiskInfo** *(list) --* 
                      A list of objects describing the disks that were attached to the source instance.
                      - *(dict) --* 
                        Describes a disk.
                        - **name** *(string) --* 
                          The disk name.
                        - **path** *(string) --* 
                          The disk path.
                        - **sizeInGb** *(integer) --* 
                          The size of the disk in GB (e.g., ``32`` ).
                        - **isSystemDisk** *(boolean) --* 
                          A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).
                  - **diskSnapshotInfo** *(dict) --* 
                    A list of objects describing a disk snapshot.
                    - **sizeInGb** *(integer) --* 
                      The size of the disk in GB (e.g., ``32`` ).
                - **destinationInfo** *(dict) --* 
                  A list of objects describing the destination of the export snapshot record.
                  - **id** *(string) --* 
                    The ID of the resource created at the destination.
                  - **service** *(string) --* 
                    The destination service of the record.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class GetInstanceSnapshots(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_instance_snapshots`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstanceSnapshots>`_
        
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
                'instanceSnapshots': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'supportCode': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'location': {
                            'availabilityZone': 'string',
                            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                        },
                        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'state': 'pending'|'error'|'available',
                        'progress': 'string',
                        'fromAttachedDisks': [
                            {
                                'name': 'string',
                                'arn': 'string',
                                'supportCode': 'string',
                                'createdAt': datetime(2015, 1, 1),
                                'location': {
                                    'availabilityZone': 'string',
                                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                                },
                                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                                'tags': [
                                    {
                                        'key': 'string',
                                        'value': 'string'
                                    },
                                ],
                                'sizeInGb': 123,
                                'isSystemDisk': True|False,
                                'iops': 123,
                                'path': 'string',
                                'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                                'attachedTo': 'string',
                                'isAttached': True|False,
                                'attachmentState': 'string',
                                'gbInUse': 123
                            },
                        ],
                        'fromInstanceName': 'string',
                        'fromInstanceArn': 'string',
                        'fromBlueprintId': 'string',
                        'fromBundleId': 'string',
                        'sizeInGb': 123
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **instanceSnapshots** *(list) --* 
              An array of key-value pairs containing information about the results of your get instance snapshots request.
              - *(dict) --* 
                Describes the snapshot of the virtual private server, or *instance* .
                - **name** *(string) --* 
                  The name of the snapshot.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the snapshot (e.g., ``arn:aws:lightsail:us-east-2:123456789101:InstanceSnapshot/d23b5706-3322-4d83-81e5-12345EXAMPLE`` ).
                - **supportCode** *(string) --* 
                  The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
                - **createdAt** *(datetime) --* 
                  The timestamp when the snapshot was created (e.g., ``1479907467.024`` ).
                - **location** *(dict) --* 
                  The region name and Availability Zone where you created the snapshot.
                  - **availabilityZone** *(string) --* 
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
                  - **regionName** *(string) --* 
                    The AWS Region name.
                - **resourceType** *(string) --* 
                  The type of resource (usually ``InstanceSnapshot`` ).
                - **tags** *(list) --* 
                  The tag keys and optional values for the resource. For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                  - *(dict) --* 
                    Describes a tag key and optional value assigned to an Amazon Lightsail resource.
                    For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                    - **key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                    - **value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                - **state** *(string) --* 
                  The state the snapshot is in.
                - **progress** *(string) --* 
                  The progress of the snapshot.
                - **fromAttachedDisks** *(list) --* 
                  An array of disk objects containing information about all block storage disks.
                  - *(dict) --* 
                    Describes a system disk or an block storage disk.
                    - **name** *(string) --* 
                      The unique name of the disk.
                    - **arn** *(string) --* 
                      The Amazon Resource Name (ARN) of the disk.
                    - **supportCode** *(string) --* 
                      The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
                    - **createdAt** *(datetime) --* 
                      The date when the disk was created.
                    - **location** *(dict) --* 
                      The AWS Region and Availability Zone where the disk is located.
                      - **availabilityZone** *(string) --* 
                        The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
                      - **regionName** *(string) --* 
                        The AWS Region name.
                    - **resourceType** *(string) --* 
                      The Lightsail resource type (e.g., ``Disk`` ).
                    - **tags** *(list) --* 
                      The tag keys and optional values for the resource. For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                      - *(dict) --* 
                        Describes a tag key and optional value assigned to an Amazon Lightsail resource.
                        For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                        - **key** *(string) --* 
                          The key of the tag.
                          Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                        - **value** *(string) --* 
                          The value of the tag.
                          Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                    - **sizeInGb** *(integer) --* 
                      The size of the disk in GB.
                    - **isSystemDisk** *(boolean) --* 
                      A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).
                    - **iops** *(integer) --* 
                      The input/output operations per second (IOPS) of the disk.
                    - **path** *(string) --* 
                      The disk path.
                    - **state** *(string) --* 
                      Describes the status of the disk.
                    - **attachedTo** *(string) --* 
                      The resources to which the disk is attached.
                    - **isAttached** *(boolean) --* 
                      A Boolean value indicating whether the disk is attached.
                    - **attachmentState** *(string) --* 
                      (Deprecated) The attachment state of the disk.
                      .. note::
                        In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.
                    - **gbInUse** *(integer) --* 
                      (Deprecated) The number of GB in use by the disk.
                      .. note::
                        In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.
                - **fromInstanceName** *(string) --* 
                  The instance from which the snapshot was created.
                - **fromInstanceArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the instance from which the snapshot was created (e.g., ``arn:aws:lightsail:us-east-2:123456789101:Instance/64b8404c-ccb1-430b-8daf-12345EXAMPLE`` ).
                - **fromBlueprintId** *(string) --* 
                  The blueprint ID from which you created the snapshot (e.g., ``os_debian_8_3`` ). A blueprint is a virtual private server (or *instance* ) image used to create instances quickly.
                - **fromBundleId** *(string) --* 
                  The bundle ID from which you created the snapshot (e.g., ``micro_1_0`` ).
                - **sizeInGb** *(integer) --* 
                  The size in GB of the SSD.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class GetInstances(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_instances`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstances>`_
        
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
                'instances': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'supportCode': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'location': {
                            'availabilityZone': 'string',
                            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                        },
                        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'blueprintId': 'string',
                        'blueprintName': 'string',
                        'bundleId': 'string',
                        'isStaticIp': True|False,
                        'privateIpAddress': 'string',
                        'publicIpAddress': 'string',
                        'ipv6Address': 'string',
                        'hardware': {
                            'cpuCount': 123,
                            'disks': [
                                {
                                    'name': 'string',
                                    'arn': 'string',
                                    'supportCode': 'string',
                                    'createdAt': datetime(2015, 1, 1),
                                    'location': {
                                        'availabilityZone': 'string',
                                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                                    },
                                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                                    'tags': [
                                        {
                                            'key': 'string',
                                            'value': 'string'
                                        },
                                    ],
                                    'sizeInGb': 123,
                                    'isSystemDisk': True|False,
                                    'iops': 123,
                                    'path': 'string',
                                    'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                                    'attachedTo': 'string',
                                    'isAttached': True|False,
                                    'attachmentState': 'string',
                                    'gbInUse': 123
                                },
                            ],
                            'ramSizeInGb': ...
                        },
                        'networking': {
                            'monthlyTransfer': {
                                'gbPerMonthAllocated': 123
                            },
                            'ports': [
                                {
                                    'fromPort': 123,
                                    'toPort': 123,
                                    'protocol': 'tcp'|'all'|'udp',
                                    'accessFrom': 'string',
                                    'accessType': 'Public'|'Private',
                                    'commonName': 'string',
                                    'accessDirection': 'inbound'|'outbound'
                                },
                            ]
                        },
                        'state': {
                            'code': 123,
                            'name': 'string'
                        },
                        'username': 'string',
                        'sshKeyName': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **instances** *(list) --* 
              An array of key-value pairs containing information about your instances.
              - *(dict) --* 
                Describes an instance (a virtual private server).
                - **name** *(string) --* 
                  The name the user gave the instance (e.g., ``Amazon_Linux-1GB-Ohio-1`` ).
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the instance (e.g., ``arn:aws:lightsail:us-east-2:123456789101:Instance/244ad76f-8aad-4741-809f-12345EXAMPLE`` ).
                - **supportCode** *(string) --* 
                  The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
                - **createdAt** *(datetime) --* 
                  The timestamp when the instance was created (e.g., ``1479734909.17`` ).
                - **location** *(dict) --* 
                  The region name and Availability Zone where the instance is located.
                  - **availabilityZone** *(string) --* 
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
                  - **regionName** *(string) --* 
                    The AWS Region name.
                - **resourceType** *(string) --* 
                  The type of resource (usually ``Instance`` ).
                - **tags** *(list) --* 
                  The tag keys and optional values for the resource. For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                  - *(dict) --* 
                    Describes a tag key and optional value assigned to an Amazon Lightsail resource.
                    For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                    - **key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                    - **value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                - **blueprintId** *(string) --* 
                  The blueprint ID (e.g., ``os_amlinux_2016_03`` ).
                - **blueprintName** *(string) --* 
                  The friendly name of the blueprint (e.g., ``Amazon Linux`` ).
                - **bundleId** *(string) --* 
                  The bundle for the instance (e.g., ``micro_1_0`` ).
                - **isStaticIp** *(boolean) --* 
                  A Boolean value indicating whether this instance has a static IP assigned to it.
                - **privateIpAddress** *(string) --* 
                  The private IP address of the instance.
                - **publicIpAddress** *(string) --* 
                  The public IP address of the instance.
                - **ipv6Address** *(string) --* 
                  The IPv6 address of the instance.
                - **hardware** *(dict) --* 
                  The size of the vCPU and the amount of RAM for the instance.
                  - **cpuCount** *(integer) --* 
                    The number of vCPUs the instance has.
                  - **disks** *(list) --* 
                    The disks attached to the instance.
                    - *(dict) --* 
                      Describes a system disk or an block storage disk.
                      - **name** *(string) --* 
                        The unique name of the disk.
                      - **arn** *(string) --* 
                        The Amazon Resource Name (ARN) of the disk.
                      - **supportCode** *(string) --* 
                        The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
                      - **createdAt** *(datetime) --* 
                        The date when the disk was created.
                      - **location** *(dict) --* 
                        The AWS Region and Availability Zone where the disk is located.
                        - **availabilityZone** *(string) --* 
                          The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
                        - **regionName** *(string) --* 
                          The AWS Region name.
                      - **resourceType** *(string) --* 
                        The Lightsail resource type (e.g., ``Disk`` ).
                      - **tags** *(list) --* 
                        The tag keys and optional values for the resource. For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                        - *(dict) --* 
                          Describes a tag key and optional value assigned to an Amazon Lightsail resource.
                          For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                          - **key** *(string) --* 
                            The key of the tag.
                            Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                          - **value** *(string) --* 
                            The value of the tag.
                            Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                      - **sizeInGb** *(integer) --* 
                        The size of the disk in GB.
                      - **isSystemDisk** *(boolean) --* 
                        A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).
                      - **iops** *(integer) --* 
                        The input/output operations per second (IOPS) of the disk.
                      - **path** *(string) --* 
                        The disk path.
                      - **state** *(string) --* 
                        Describes the status of the disk.
                      - **attachedTo** *(string) --* 
                        The resources to which the disk is attached.
                      - **isAttached** *(boolean) --* 
                        A Boolean value indicating whether the disk is attached.
                      - **attachmentState** *(string) --* 
                        (Deprecated) The attachment state of the disk.
                        .. note::
                          In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.
                      - **gbInUse** *(integer) --* 
                        (Deprecated) The number of GB in use by the disk.
                        .. note::
                          In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.
                  - **ramSizeInGb** *(float) --* 
                    The amount of RAM in GB on the instance (e.g., ``1.0`` ).
                - **networking** *(dict) --* 
                  Information about the public ports and monthly data transfer rates for the instance.
                  - **monthlyTransfer** *(dict) --* 
                    The amount of data in GB allocated for monthly data transfers.
                    - **gbPerMonthAllocated** *(integer) --* 
                      The amount allocated per month (in GB).
                  - **ports** *(list) --* 
                    An array of key-value pairs containing information about the ports on the instance.
                    - *(dict) --* 
                      Describes information about the instance ports.
                      - **fromPort** *(integer) --* 
                        The first port in the range.
                      - **toPort** *(integer) --* 
                        The last port in the range.
                      - **protocol** *(string) --* 
                        The protocol being used. Can be one of the following.
                        * ``tcp`` - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn't require reliable data stream service, use UDP instead. 
                        * ``all`` - All transport layer protocol types. For more general information, see `Transport layer <https://en.wikipedia.org/wiki/Transport_layer>`__ on Wikipedia. 
                        * ``udp`` - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don't require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead. 
                      - **accessFrom** *(string) --* 
                        The location from which access is allowed (e.g., ``Anywhere (0.0.0.0/0)`` ).
                      - **accessType** *(string) --* 
                        The type of access (``Public`` or ``Private`` ).
                      - **commonName** *(string) --* 
                        The common name.
                      - **accessDirection** *(string) --* 
                        The access direction (``inbound`` or ``outbound`` ).
                - **state** *(dict) --* 
                  The status code and the state (e.g., ``running`` ) for the instance.
                  - **code** *(integer) --* 
                    The status code for the instance.
                  - **name** *(string) --* 
                    The state of the instance (e.g., ``running`` or ``pending`` ).
                - **username** *(string) --* 
                  The user name for connecting to the instance (e.g., ``ec2-user`` ).
                - **sshKeyName** *(string) --* 
                  The name of the SSH key being used to connect to the instance (e.g., ``LightsailDefaultKeyPair`` ).
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class GetKeyPairs(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_key_pairs`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetKeyPairs>`_
        
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
                'keyPairs': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'supportCode': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'location': {
                            'availabilityZone': 'string',
                            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                        },
                        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'fingerprint': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **keyPairs** *(list) --* 
              An array of key-value pairs containing information about the key pairs.
              - *(dict) --* 
                Describes the SSH key pair.
                - **name** *(string) --* 
                  The friendly name of the SSH key pair.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the key pair (e.g., ``arn:aws:lightsail:us-east-2:123456789101:KeyPair/05859e3d-331d-48ba-9034-12345EXAMPLE`` ).
                - **supportCode** *(string) --* 
                  The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
                - **createdAt** *(datetime) --* 
                  The timestamp when the key pair was created (e.g., ``1479816991.349`` ).
                - **location** *(dict) --* 
                  The region name and Availability Zone where the key pair was created.
                  - **availabilityZone** *(string) --* 
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
                  - **regionName** *(string) --* 
                    The AWS Region name.
                - **resourceType** *(string) --* 
                  The resource type (usually ``KeyPair`` ).
                - **tags** *(list) --* 
                  The tag keys and optional values for the resource. For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                  - *(dict) --* 
                    Describes a tag key and optional value assigned to an Amazon Lightsail resource.
                    For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                    - **key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                    - **value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                - **fingerprint** *(string) --* 
                  The RSA fingerprint of the key pair.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class GetLoadBalancers(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_load_balancers`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetLoadBalancers>`_
        
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
                'loadBalancers': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'supportCode': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'location': {
                            'availabilityZone': 'string',
                            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                        },
                        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'dnsName': 'string',
                        'state': 'active'|'provisioning'|'active_impaired'|'failed'|'unknown',
                        'protocol': 'HTTP_HTTPS'|'HTTP',
                        'publicPorts': [
                            123,
                        ],
                        'healthCheckPath': 'string',
                        'instancePort': 123,
                        'instanceHealthSummary': [
                            {
                                'instanceName': 'string',
                                'instanceHealth': 'initial'|'healthy'|'unhealthy'|'unused'|'draining'|'unavailable',
                                'instanceHealthReason': 'Lb.RegistrationInProgress'|'Lb.InitialHealthChecking'|'Lb.InternalError'|'Instance.ResponseCodeMismatch'|'Instance.Timeout'|'Instance.FailedHealthChecks'|'Instance.NotRegistered'|'Instance.NotInUse'|'Instance.DeregistrationInProgress'|'Instance.InvalidState'|'Instance.IpUnusable'
                            },
                        ],
                        'tlsCertificateSummaries': [
                            {
                                'name': 'string',
                                'isAttached': True|False
                            },
                        ],
                        'configurationOptions': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **loadBalancers** *(list) --* 
              An array of LoadBalancer objects describing your load balancers.
              - *(dict) --* 
                Describes the Lightsail load balancer.
                - **name** *(string) --* 
                  The name of the load balancer (e.g., ``my-load-balancer`` ).
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the load balancer.
                - **supportCode** *(string) --* 
                  The support code. Include this code in your email to support when you have questions about your Lightsail load balancer. This code enables our support team to look up your Lightsail information more easily.
                - **createdAt** *(datetime) --* 
                  The date when your load balancer was created.
                - **location** *(dict) --* 
                  The AWS Region where your load balancer was created (e.g., ``us-east-2a`` ). Lightsail automatically creates your load balancer across Availability Zones.
                  - **availabilityZone** *(string) --* 
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
                  - **regionName** *(string) --* 
                    The AWS Region name.
                - **resourceType** *(string) --* 
                  The resource type (e.g., ``LoadBalancer`` .
                - **tags** *(list) --* 
                  The tag keys and optional values for the resource. For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                  - *(dict) --* 
                    Describes a tag key and optional value assigned to an Amazon Lightsail resource.
                    For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                    - **key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                    - **value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                - **dnsName** *(string) --* 
                  The DNS name of your Lightsail load balancer.
                - **state** *(string) --* 
                  The status of your load balancer. Valid values are below.
                - **protocol** *(string) --* 
                  The protocol you have enabled for your load balancer. Valid values are below.
                  You can't just have ``HTTP_HTTPS`` , but you can have just ``HTTP`` .
                - **publicPorts** *(list) --* 
                  An array of public port settings for your load balancer. For HTTP, use port 80. For HTTPS, use port 443.
                  - *(integer) --* 
                - **healthCheckPath** *(string) --* 
                  The path you specified to perform your health checks. If no path is specified, the load balancer tries to make a request to the default (root) page.
                - **instancePort** *(integer) --* 
                  The port where the load balancer will direct traffic to your Lightsail instances. For HTTP traffic, it's port 80. For HTTPS traffic, it's port 443.
                - **instanceHealthSummary** *(list) --* 
                  An array of InstanceHealthSummary objects describing the health of the load balancer.
                  - *(dict) --* 
                    Describes information about the health of the instance.
                    - **instanceName** *(string) --* 
                      The name of the Lightsail instance for which you are requesting health check data.
                    - **instanceHealth** *(string) --* 
                      Describes the overall instance health. Valid values are below.
                    - **instanceHealthReason** *(string) --* 
                      More information about the instance health. If the ``instanceHealth`` is ``healthy`` , then an ``instanceHealthReason`` value is not provided.
                      If ** ``instanceHealth`` ** is ``initial`` , the ** ``instanceHealthReason`` ** value can be one of the following:
                      * **``Lb.RegistrationInProgress`` ** - The target instance is in the process of being registered with the load balancer. 
                      * **``Lb.InitialHealthChecking`` ** - The Lightsail load balancer is still sending the target instance the minimum number of health checks required to determine its health status. 
                      If ** ``instanceHealth`` ** is ``unhealthy`` , the ** ``instanceHealthReason`` ** value can be one of the following:
                      * **``Instance.ResponseCodeMismatch`` ** - The health checks did not return an expected HTTP code. 
                      * **``Instance.Timeout`` ** - The health check requests timed out. 
                      * **``Instance.FailedHealthChecks`` ** - The health checks failed because the connection to the target instance timed out, the target instance response was malformed, or the target instance failed the health check for an unknown reason. 
                      * **``Lb.InternalError`` ** - The health checks failed due to an internal error. 
                      If ** ``instanceHealth`` ** is ``unused`` , the ** ``instanceHealthReason`` ** value can be one of the following:
                      * **``Instance.NotRegistered`` ** - The target instance is not registered with the target group. 
                      * **``Instance.NotInUse`` ** - The target group is not used by any load balancer, or the target instance is in an Availability Zone that is not enabled for its load balancer. 
                      * **``Instance.IpUnusable`` ** - The target IP address is reserved for use by a Lightsail load balancer. 
                      * **``Instance.InvalidState`` ** - The target is in the stopped or terminated state. 
                      If ** ``instanceHealth`` ** is ``draining`` , the ** ``instanceHealthReason`` ** value can be one of the following:
                      * **``Instance.DeregistrationInProgress`` ** - The target instance is in the process of being deregistered and the deregistration delay period has not expired. 
                - **tlsCertificateSummaries** *(list) --* 
                  An array of LoadBalancerTlsCertificateSummary objects that provide additional information about the SSL/TLS certificates. For example, if ``true`` , the certificate is attached to the load balancer.
                  - *(dict) --* 
                    Provides a summary of SSL/TLS certificate metadata.
                    - **name** *(string) --* 
                      The name of the SSL/TLS certificate.
                    - **isAttached** *(boolean) --* 
                      When ``true`` , the SSL/TLS certificate is attached to the Lightsail load balancer.
                - **configurationOptions** *(dict) --* 
                  A string to string map of the configuration options for your load balancer. Valid values are listed below.
                  - *(string) --* 
                    - *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class GetOperations(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_operations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetOperations>`_
        
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
                'operations': [
                    {
                        'id': 'string',
                        'resourceName': 'string',
                        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                        'createdAt': datetime(2015, 1, 1),
                        'location': {
                            'availabilityZone': 'string',
                            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                        },
                        'isTerminal': True|False,
                        'operationDetails': 'string',
                        'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                        'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                        'statusChangedAt': datetime(2015, 1, 1),
                        'errorCode': 'string',
                        'errorDetails': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **operations** *(list) --* 
              An array of key-value pairs containing information about the results of your get operations request.
              - *(dict) --* 
                Describes the API operation.
                - **id** *(string) --* 
                  The ID of the operation.
                - **resourceName** *(string) --* 
                  The resource name.
                - **resourceType** *(string) --* 
                  The resource type. 
                - **createdAt** *(datetime) --* 
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
                - **location** *(dict) --* 
                  The region and Availability Zone.
                  - **availabilityZone** *(string) --* 
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
                  - **regionName** *(string) --* 
                    The AWS Region name.
                - **isTerminal** *(boolean) --* 
                  A Boolean value indicating whether the operation is terminal.
                - **operationDetails** *(string) --* 
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
                - **operationType** *(string) --* 
                  The type of operation. 
                - **status** *(string) --* 
                  The status of the operation. 
                - **statusChangedAt** *(datetime) --* 
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
                - **errorCode** *(string) --* 
                  The error code.
                - **errorDetails** *(string) --* 
                  The error details.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class GetRelationalDatabaseBlueprints(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_relational_database_blueprints`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRelationalDatabaseBlueprints>`_
        
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
                'blueprints': [
                    {
                        'blueprintId': 'string',
                        'engine': 'mysql',
                        'engineVersion': 'string',
                        'engineDescription': 'string',
                        'engineVersionDescription': 'string',
                        'isEngineDefault': True|False
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **blueprints** *(list) --* 
              An object describing the result of your get relational database blueprints request.
              - *(dict) --* 
                Describes a database image, or blueprint. A blueprint describes the major engine version of a database.
                - **blueprintId** *(string) --* 
                  The ID for the database blueprint.
                - **engine** *(string) --* 
                  The database software of the database blueprint (for example, ``MySQL`` ).
                - **engineVersion** *(string) --* 
                  The database engine version for the database blueprint (for example, ``5.7.23`` ).
                - **engineDescription** *(string) --* 
                  The description of the database engine for the database blueprint.
                - **engineVersionDescription** *(string) --* 
                  The description of the database engine version for the database blueprint.
                - **isEngineDefault** *(boolean) --* 
                  A Boolean value indicating whether the engine version is the default for the database blueprint.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class GetRelationalDatabaseBundles(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_relational_database_bundles`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRelationalDatabaseBundles>`_
        
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
                'bundles': [
                    {
                        'bundleId': 'string',
                        'name': 'string',
                        'price': ...,
                        'ramSizeInGb': ...,
                        'diskSizeInGb': 123,
                        'transferPerMonthInGb': 123,
                        'cpuCount': 123,
                        'isEncrypted': True|False,
                        'isActive': True|False
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **bundles** *(list) --* 
              An object describing the result of your get relational database bundles request.
              - *(dict) --* 
                Describes a database bundle. A bundle describes the performance specifications of the database.
                - **bundleId** *(string) --* 
                  The ID for the database bundle.
                - **name** *(string) --* 
                  The name for the database bundle.
                - **price** *(float) --* 
                  The cost of the database bundle in US currency.
                - **ramSizeInGb** *(float) --* 
                  The amount of RAM in GB (for example, ``2.0`` ) for the database bundle.
                - **diskSizeInGb** *(integer) --* 
                  The size of the disk for the database bundle.
                - **transferPerMonthInGb** *(integer) --* 
                  The data transfer rate per month in GB for the database bundle.
                - **cpuCount** *(integer) --* 
                  The number of virtual CPUs (vCPUs) for the database bundle.
                - **isEncrypted** *(boolean) --* 
                  A Boolean value indicating whether the database bundle is encrypted.
                - **isActive** *(boolean) --* 
                  A Boolean value indicating whether the database bundle is active.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class GetRelationalDatabaseEvents(Paginator):
    def paginate(self, relationalDatabaseName: str, durationInMinutes: int = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_relational_database_events`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRelationalDatabaseEvents>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              relationalDatabaseName='string',
              durationInMinutes=123,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'relationalDatabaseEvents': [
                    {
                        'resource': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'message': 'string',
                        'eventCategories': [
                            'string',
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **relationalDatabaseEvents** *(list) --* 
              An object describing the result of your get relational database events request.
              - *(dict) --* 
                Describes an event for a database.
                - **resource** *(string) --* 
                  The database that the database event relates to.
                - **createdAt** *(datetime) --* 
                  The timestamp when the database event was created.
                - **message** *(string) --* 
                  The message of the database event.
                - **eventCategories** *(list) --* 
                  The category that the database event belongs to.
                  - *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type relationalDatabaseName: string
        :param relationalDatabaseName: **[REQUIRED]**
          The name of the database from which to get events.
        :type durationInMinutes: integer
        :param durationInMinutes:
          The number of minutes in the past from which to retrieve events. For example, to get all events from the past 2 hours, enter 120.
          Default: ``60``
          The minimum is 1 and the maximum is 14 days (20160 minutes).
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


class GetRelationalDatabaseParameters(Paginator):
    def paginate(self, relationalDatabaseName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_relational_database_parameters`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRelationalDatabaseParameters>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              relationalDatabaseName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'parameters': [
                    {
                        'allowedValues': 'string',
                        'applyMethod': 'string',
                        'applyType': 'string',
                        'dataType': 'string',
                        'description': 'string',
                        'isModifiable': True|False,
                        'parameterName': 'string',
                        'parameterValue': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **parameters** *(list) --* 
              An object describing the result of your get relational database parameters request.
              - *(dict) --* 
                Describes the parameters of a database.
                - **allowedValues** *(string) --* 
                  Specifies the valid range of values for the parameter.
                - **applyMethod** *(string) --* 
                  Indicates when parameter updates are applied.
                  Can be ``immediate`` or ``pending-reboot`` .
                - **applyType** *(string) --* 
                  Specifies the engine-specific parameter type.
                - **dataType** *(string) --* 
                  Specifies the valid data type for the parameter.
                - **description** *(string) --* 
                  Provides a description of the parameter.
                - **isModifiable** *(boolean) --* 
                  A Boolean value indicating whether the parameter can be modified.
                - **parameterName** *(string) --* 
                  Specifies the name of the parameter.
                - **parameterValue** *(string) --* 
                  Specifies the value of the parameter.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type relationalDatabaseName: string
        :param relationalDatabaseName: **[REQUIRED]**
          The name of your database for which to get parameters.
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


class GetRelationalDatabaseSnapshots(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_relational_database_snapshots`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRelationalDatabaseSnapshots>`_
        
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
                'relationalDatabaseSnapshots': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'supportCode': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'location': {
                            'availabilityZone': 'string',
                            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                        },
                        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'engine': 'string',
                        'engineVersion': 'string',
                        'sizeInGb': 123,
                        'state': 'string',
                        'fromRelationalDatabaseName': 'string',
                        'fromRelationalDatabaseArn': 'string',
                        'fromRelationalDatabaseBundleId': 'string',
                        'fromRelationalDatabaseBlueprintId': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **relationalDatabaseSnapshots** *(list) --* 
              An object describing the result of your get relational database snapshots request.
              - *(dict) --* 
                Describes a database snapshot.
                - **name** *(string) --* 
                  The name of the database snapshot.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the database snapshot.
                - **supportCode** *(string) --* 
                  The support code for the database snapshot. Include this code in your email to support when you have questions about a database snapshot in Lightsail. This code enables our support team to look up your Lightsail information more easily.
                - **createdAt** *(datetime) --* 
                  The timestamp when the database snapshot was created.
                - **location** *(dict) --* 
                  The Region name and Availability Zone where the database snapshot is located.
                  - **availabilityZone** *(string) --* 
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
                  - **regionName** *(string) --* 
                    The AWS Region name.
                - **resourceType** *(string) --* 
                  The Lightsail resource type.
                - **tags** *(list) --* 
                  The tag keys and optional values for the resource. For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                  - *(dict) --* 
                    Describes a tag key and optional value assigned to an Amazon Lightsail resource.
                    For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                    - **key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                    - **value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                - **engine** *(string) --* 
                  The software of the database snapshot (for example, ``MySQL`` )
                - **engineVersion** *(string) --* 
                  The database engine version for the database snapshot (for example, ``5.7.23`` ).
                - **sizeInGb** *(integer) --* 
                  The size of the disk in GB (for example, ``32`` ) for the database snapshot.
                - **state** *(string) --* 
                  The state of the database snapshot.
                - **fromRelationalDatabaseName** *(string) --* 
                  The name of the source database from which the database snapshot was created.
                - **fromRelationalDatabaseArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the database from which the database snapshot was created.
                - **fromRelationalDatabaseBundleId** *(string) --* 
                  The bundle ID of the database from which the database snapshot was created.
                - **fromRelationalDatabaseBlueprintId** *(string) --* 
                  The blueprint ID of the database from which the database snapshot was created. A blueprint describes the major engine version of a database.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class GetRelationalDatabases(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_relational_databases`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRelationalDatabases>`_
        
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
                'relationalDatabases': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'supportCode': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'location': {
                            'availabilityZone': 'string',
                            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                        },
                        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'relationalDatabaseBlueprintId': 'string',
                        'relationalDatabaseBundleId': 'string',
                        'masterDatabaseName': 'string',
                        'hardware': {
                            'cpuCount': 123,
                            'diskSizeInGb': 123,
                            'ramSizeInGb': ...
                        },
                        'state': 'string',
                        'secondaryAvailabilityZone': 'string',
                        'backupRetentionEnabled': True|False,
                        'pendingModifiedValues': {
                            'masterUserPassword': 'string',
                            'engineVersion': 'string',
                            'backupRetentionEnabled': True|False
                        },
                        'engine': 'string',
                        'engineVersion': 'string',
                        'latestRestorableTime': datetime(2015, 1, 1),
                        'masterUsername': 'string',
                        'parameterApplyStatus': 'string',
                        'preferredBackupWindow': 'string',
                        'preferredMaintenanceWindow': 'string',
                        'publiclyAccessible': True|False,
                        'masterEndpoint': {
                            'port': 123,
                            'address': 'string'
                        },
                        'pendingMaintenanceActions': [
                            {
                                'action': 'string',
                                'description': 'string',
                                'currentApplyDate': datetime(2015, 1, 1)
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **relationalDatabases** *(list) --* 
              An object describing the result of your get relational databases request.
              - *(dict) --* 
                Describes a database.
                - **name** *(string) --* 
                  The unique name of the database resource in Lightsail.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the database.
                - **supportCode** *(string) --* 
                  The support code for the database. Include this code in your email to support when you have questions about a database in Lightsail. This code enables our support team to look up your Lightsail information more easily.
                - **createdAt** *(datetime) --* 
                  The timestamp when the database was created. Formatted in Unix time.
                - **location** *(dict) --* 
                  The Region name and Availability Zone where the database is located.
                  - **availabilityZone** *(string) --* 
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
                  - **regionName** *(string) --* 
                    The AWS Region name.
                - **resourceType** *(string) --* 
                  The Lightsail resource type for the database (for example, ``RelationalDatabase`` ).
                - **tags** *(list) --* 
                  The tag keys and optional values for the resource. For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                  - *(dict) --* 
                    Describes a tag key and optional value assigned to an Amazon Lightsail resource.
                    For more information about tags in Lightsail, see the `Lightsail Dev Guide <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
                    - **key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                    - **value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
                - **relationalDatabaseBlueprintId** *(string) --* 
                  The blueprint ID for the database. A blueprint describes the major engine version of a database.
                - **relationalDatabaseBundleId** *(string) --* 
                  The bundle ID for the database. A bundle describes the performance specifications for your database.
                - **masterDatabaseName** *(string) --* 
                  The name of the master database created when the Lightsail database resource is created.
                - **hardware** *(dict) --* 
                  Describes the hardware of the database.
                  - **cpuCount** *(integer) --* 
                    The number of vCPUs for the database.
                  - **diskSizeInGb** *(integer) --* 
                    The size of the disk for the database.
                  - **ramSizeInGb** *(float) --* 
                    The amount of RAM in GB for the database.
                - **state** *(string) --* 
                  Describes the current state of the database.
                - **secondaryAvailabilityZone** *(string) --* 
                  Describes the secondary Availability Zone of a high availability database.
                  The secondary database is used for failover support of a high availability database.
                - **backupRetentionEnabled** *(boolean) --* 
                  A Boolean value indicating whether automated backup retention is enabled for the database.
                - **pendingModifiedValues** *(dict) --* 
                  Describes pending database value modifications.
                  - **masterUserPassword** *(string) --* 
                    The password for the master user of the database.
                  - **engineVersion** *(string) --* 
                    The database engine version.
                  - **backupRetentionEnabled** *(boolean) --* 
                    A Boolean value indicating whether automated backup retention is enabled.
                - **engine** *(string) --* 
                  The database software (for example, ``MySQL`` ).
                - **engineVersion** *(string) --* 
                  The database engine version (for example, ``5.7.23`` ).
                - **latestRestorableTime** *(datetime) --* 
                  The latest point in time to which the database can be restored. Formatted in Unix time.
                - **masterUsername** *(string) --* 
                  The master user name of the database.
                - **parameterApplyStatus** *(string) --* 
                  The status of parameter updates for the database.
                - **preferredBackupWindow** *(string) --* 
                  The daily time range during which automated backups are created for the database (for example, ``16:00-16:30`` ).
                - **preferredMaintenanceWindow** *(string) --* 
                  The weekly time range during which system maintenance can occur on the database.
                  In the format ``ddd:hh24:mi-ddd:hh24:mi`` . For example, ``Tue:17:00-Tue:17:30`` .
                - **publiclyAccessible** *(boolean) --* 
                  A Boolean value indicating whether the database is publicly accessible.
                - **masterEndpoint** *(dict) --* 
                  The master endpoint for the database.
                  - **port** *(integer) --* 
                    Specifies the port that the database is listening on.
                  - **address** *(string) --* 
                    Specifies the DNS address of the database.
                - **pendingMaintenanceActions** *(list) --* 
                  Describes the pending maintenance actions for the database.
                  - *(dict) --* 
                    Describes a pending database maintenance action.
                    - **action** *(string) --* 
                      The type of pending database maintenance action.
                    - **description** *(string) --* 
                      Additional detail about the pending database maintenance action.
                    - **currentApplyDate** *(datetime) --* 
                      The effective date of the pending database maintenance action.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class GetStaticIps(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_static_ips`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetStaticIps>`_
        
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
                'staticIps': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'supportCode': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'location': {
                            'availabilityZone': 'string',
                            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                        },
                        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                        'ipAddress': 'string',
                        'attachedTo': 'string',
                        'isAttached': True|False
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **staticIps** *(list) --* 
              An array of key-value pairs containing information about your get static IPs request.
              - *(dict) --* 
                Describes the static IP.
                - **name** *(string) --* 
                  The name of the static IP (e.g., ``StaticIP-Ohio-EXAMPLE`` ).
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the static IP (e.g., ``arn:aws:lightsail:us-east-2:123456789101:StaticIp/9cbb4a9e-f8e3-4dfe-b57e-12345EXAMPLE`` ).
                - **supportCode** *(string) --* 
                  The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
                - **createdAt** *(datetime) --* 
                  The timestamp when the static IP was created (e.g., ``1479735304.222`` ).
                - **location** *(dict) --* 
                  The region and Availability Zone where the static IP was created.
                  - **availabilityZone** *(string) --* 
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
                  - **regionName** *(string) --* 
                    The AWS Region name.
                - **resourceType** *(string) --* 
                  The resource type (usually ``StaticIp`` ).
                - **ipAddress** *(string) --* 
                  The static IP address.
                - **attachedTo** *(string) --* 
                  The instance where the static IP is attached (e.g., ``Amazon_Linux-1GB-Ohio-1`` ).
                - **isAttached** *(boolean) --* 
                  A Boolean value indicating whether the static IP is attached.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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
