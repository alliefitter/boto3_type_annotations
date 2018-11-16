from typing import Dict
from botocore.paginate import Paginator


class GetActiveNames(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetActiveNames>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'activeNames\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **activeNames** *(list) --* 
        
              The list of active names returned by the get active names request.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class GetBlueprints(Paginator):
    def paginate(self, includeInactive: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetBlueprints>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              includeInactive=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'blueprints\': [
                    {
                        \'blueprintId\': \'string\',
                        \'name\': \'string\',
                        \'group\': \'string\',
                        \'type\': \'os\'|\'app\',
                        \'description\': \'string\',
                        \'isActive\': True|False,
                        \'minPower\': 123,
                        \'version\': \'string\',
                        \'versionCode\': \'string\',
                        \'productUrl\': \'string\',
                        \'licenseUrl\': \'string\',
                        \'platform\': \'LINUX_UNIX\'|\'WINDOWS\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
        """
        pass


class GetBundles(Paginator):
    def paginate(self, includeInactive: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetBundles>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              includeInactive=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'bundles\': [
                    {
                        \'price\': ...,
                        \'cpuCount\': 123,
                        \'diskSizeInGb\': 123,
                        \'bundleId\': \'string\',
                        \'instanceType\': \'string\',
                        \'isActive\': True|False,
                        \'name\': \'string\',
                        \'power\': 123,
                        \'ramSizeInGb\': ...,
                        \'transferPerMonthInGb\': 123,
                        \'supportedPlatforms\': [
                            \'LINUX_UNIX\'|\'WINDOWS\',
                        ]
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  A numeric value that represents the power of the bundle (e.g., ``500`` ). You can use the bundle\'s power value in conjunction with a blueprint\'s minimum power value to determine whether the blueprint will run on the bundle. For example, you need a bundle with a power value of 500 or more to create an instance that uses a blueprint with a minimum power value of 500.
        
                - **ramSizeInGb** *(float) --* 
        
                  The amount of RAM in GB (e.g., ``2.0`` ).
        
                - **transferPerMonthInGb** *(integer) --* 
        
                  The data transfer rate per month in GB (e.g., ``2000`` ).
        
                - **supportedPlatforms** *(list) --* 
        
                  The operating system platform (Linux/Unix-based or Windows Server-based) that the bundle supports. You can only launch a ``WINDOWS`` bundle on a blueprint that supports the ``WINDOWS`` platform. ``LINUX_UNIX`` blueprints require a ``LINUX_UNIX`` bundle.
        
                  - *(string) --* 
              
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class GetDomains(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetDomains>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'domains\': [
                    {
                        \'name\': \'string\',
                        \'arn\': \'string\',
                        \'supportCode\': \'string\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'domainEntries\': [
                            {
                                \'id\': \'string\',
                                \'name\': \'string\',
                                \'target\': \'string\',
                                \'isAlias\': True|False,
                                \'type\': \'string\',
                                \'options\': {
                                    \'string\': \'string\'
                                }
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **domains** *(list) --* 
        
              An array of key-value pairs containing information about each of the domain entries in the user\'s account.
        
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
        
        """
        pass


class GetInstanceSnapshots(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstanceSnapshots>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'instanceSnapshots\': [
                    {
                        \'name\': \'string\',
                        \'arn\': \'string\',
                        \'supportCode\': \'string\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'state\': \'pending\'|\'error\'|\'available\',
                        \'progress\': \'string\',
                        \'fromAttachedDisks\': [
                            {
                                \'name\': \'string\',
                                \'arn\': \'string\',
                                \'supportCode\': \'string\',
                                \'createdAt\': datetime(2015, 1, 1),
                                \'location\': {
                                    \'availabilityZone\': \'string\',
                                    \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                                },
                                \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                                \'sizeInGb\': 123,
                                \'isSystemDisk\': True|False,
                                \'iops\': 123,
                                \'path\': \'string\',
                                \'state\': \'pending\'|\'error\'|\'available\'|\'in-use\'|\'unknown\',
                                \'attachedTo\': \'string\',
                                \'isAttached\': True|False,
                                \'attachmentState\': \'string\',
                                \'gbInUse\': 123
                            },
                        ],
                        \'fromInstanceName\': \'string\',
                        \'fromInstanceArn\': \'string\',
                        \'fromBlueprintId\': \'string\',
                        \'fromBundleId\': \'string\',
                        \'sizeInGb\': 123
                    },
                ],
                \'NextToken\': \'string\'
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
        
        """
        pass


class GetInstances(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstances>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'instances\': [
                    {
                        \'name\': \'string\',
                        \'arn\': \'string\',
                        \'supportCode\': \'string\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'blueprintId\': \'string\',
                        \'blueprintName\': \'string\',
                        \'bundleId\': \'string\',
                        \'isStaticIp\': True|False,
                        \'privateIpAddress\': \'string\',
                        \'publicIpAddress\': \'string\',
                        \'ipv6Address\': \'string\',
                        \'hardware\': {
                            \'cpuCount\': 123,
                            \'disks\': [
                                {
                                    \'name\': \'string\',
                                    \'arn\': \'string\',
                                    \'supportCode\': \'string\',
                                    \'createdAt\': datetime(2015, 1, 1),
                                    \'location\': {
                                        \'availabilityZone\': \'string\',
                                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                                    },
                                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                                    \'sizeInGb\': 123,
                                    \'isSystemDisk\': True|False,
                                    \'iops\': 123,
                                    \'path\': \'string\',
                                    \'state\': \'pending\'|\'error\'|\'available\'|\'in-use\'|\'unknown\',
                                    \'attachedTo\': \'string\',
                                    \'isAttached\': True|False,
                                    \'attachmentState\': \'string\',
                                    \'gbInUse\': 123
                                },
                            ],
                            \'ramSizeInGb\': ...
                        },
                        \'networking\': {
                            \'monthlyTransfer\': {
                                \'gbPerMonthAllocated\': 123
                            },
                            \'ports\': [
                                {
                                    \'fromPort\': 123,
                                    \'toPort\': 123,
                                    \'protocol\': \'tcp\'|\'all\'|\'udp\',
                                    \'accessFrom\': \'string\',
                                    \'accessType\': \'Public\'|\'Private\',
                                    \'commonName\': \'string\',
                                    \'accessDirection\': \'inbound\'|\'outbound\'
                                },
                            ]
                        },
                        \'state\': {
                            \'code\': 123,
                            \'name\': \'string\'
                        },
                        \'username\': \'string\',
                        \'sshKeyName\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
                        * ``tcp`` - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn\'t require reliable data stream service, use UDP instead. 
                         
                        * ``all`` - All transport layer protocol types. For more general information, see `Transport layer <https://en.wikipedia.org/wiki/Transport_layer>`__ on Wikipedia. 
                         
                        * ``udp`` - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don\'t require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead. 
                         
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
        
        """
        pass


class GetKeyPairs(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetKeyPairs>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'keyPairs\': [
                    {
                        \'name\': \'string\',
                        \'arn\': \'string\',
                        \'supportCode\': \'string\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'fingerprint\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
                - **fingerprint** *(string) --* 
        
                  The RSA fingerprint of the key pair.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class GetOperations(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetOperations>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
        """
        pass


class GetStaticIps(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetStaticIps>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'staticIps\': [
                    {
                        \'name\': \'string\',
                        \'arn\': \'string\',
                        \'supportCode\': \'string\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'ipAddress\': \'string\',
                        \'attachedTo\': \'string\',
                        \'isAttached\': True|False
                    },
                ],
                \'NextToken\': \'string\'
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
        
        """
        pass
