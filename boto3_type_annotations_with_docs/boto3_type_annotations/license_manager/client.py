from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Union
from typing import List


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        """
        Check if an operation can be paginated.
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

    def create_license_configuration(self, Name: str, LicenseCountingType: str, Description: str = None, LicenseCount: int = None, LicenseCountHardLimit: bool = None, LicenseRules: List = None, Tags: List = None) -> Dict:
        """
        Creates a new license configuration object. A license configuration is an abstraction of a customer license agreement that can be consumed and enforced by License Manager. Components include specifications for the license type (licensing by instance, socket, CPU, or VCPU), tenancy (shared tenancy, Amazon EC2 Dedicated Instance, Amazon EC2 Dedicated Host, or any of these), host affinity (how long a VM must be associated with a host), the number of licenses purchased and used.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/CreateLicenseConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.create_license_configuration(
              Name='string',
              Description='string',
              LicenseCountingType='vCPU'|'Instance'|'Core'|'Socket',
              LicenseCount=123,
              LicenseCountHardLimit=True|False,
              LicenseRules=[
                  'string',
              ],
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'LicenseConfigurationArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LicenseConfigurationArn** *(string) --* 
              ARN of the license configuration object after its creation.
        :type Name: string
        :param Name: **[REQUIRED]**
          Name of the license configuration.
        :type Description: string
        :param Description:
          Human-friendly description of the license configuration.
        :type LicenseCountingType: string
        :param LicenseCountingType: **[REQUIRED]**
          Dimension to use to track the license inventory.
        :type LicenseCount: integer
        :param LicenseCount:
          Number of licenses managed by the license configuration.
        :type LicenseCountHardLimit: boolean
        :param LicenseCountHardLimit:
          Flag indicating whether hard or soft license enforcement is used. Exceeding a hard limit results in the blocked deployment of new instances.
        :type LicenseRules: list
        :param LicenseRules:
          Array of configured License Manager rules.
          - *(string) --*
        :type Tags: list
        :param Tags:
          The tags to apply to the resources during launch. You can only tag instances and volumes on launch. The specified tags are applied to all instances or volumes that are created during launch. To tag a resource after it has been created, see CreateTags .
          - *(dict) --*
            Tag for a resource in a key-value format.
            - **Key** *(string) --*
              Key for the resource tag.
            - **Value** *(string) --*
              Value for the resource tag.
        :rtype: dict
        :returns:
        """
        pass

    def delete_license_configuration(self, LicenseConfigurationArn: str) -> Dict:
        """
        Deletes an existing license configuration. This action fails if the configuration is in use.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/DeleteLicenseConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.delete_license_configuration(
              LicenseConfigurationArn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type LicenseConfigurationArn: string
        :param LicenseConfigurationArn: **[REQUIRED]**
          Unique ID of the configuration object to delete.
        :rtype: dict
        :returns:
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        """
        Generate a presigned url given a client, its method, and arguments
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

    def get_license_configuration(self, LicenseConfigurationArn: str) -> Dict:
        """
        Returns a detailed description of a license configuration.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/GetLicenseConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.get_license_configuration(
              LicenseConfigurationArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'LicenseConfigurationId': 'string',
                'LicenseConfigurationArn': 'string',
                'Name': 'string',
                'Description': 'string',
                'LicenseCountingType': 'vCPU'|'Instance'|'Core'|'Socket',
                'LicenseRules': [
                    'string',
                ],
                'LicenseCount': 123,
                'LicenseCountHardLimit': True|False,
                'ConsumedLicenses': 123,
                'Status': 'string',
                'OwnerAccountId': 'string',
                'ConsumedLicenseSummaryList': [
                    {
                        'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI',
                        'ConsumedLicenses': 123
                    },
                ],
                'ManagedResourceSummaryList': [
                    {
                        'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI',
                        'AssociationCount': 123
                    },
                ],
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LicenseConfigurationId** *(string) --* 
              Unique ID for the license configuration.
            - **LicenseConfigurationArn** *(string) --* 
              ARN of the license configuration requested.
            - **Name** *(string) --* 
              Name of the license configuration.
            - **Description** *(string) --* 
              Description of the license configuration.
            - **LicenseCountingType** *(string) --* 
              Dimension on which the licenses are counted (for example, instances, cores, sockets, or VCPUs).
            - **LicenseRules** *(list) --* 
              List of flexible text strings designating license rules.
              - *(string) --* 
            - **LicenseCount** *(integer) --* 
              Number of available licenses.
            - **LicenseCountHardLimit** *(boolean) --* 
              Sets the number of available licenses as a hard limit.
            - **ConsumedLicenses** *(integer) --* 
              Number of licenses assigned to resources.
            - **Status** *(string) --* 
              License configuration status (active, etc.).
            - **OwnerAccountId** *(string) --* 
              Owner account ID for the license configuration.
            - **ConsumedLicenseSummaryList** *(list) --* 
              List of summaries for consumed licenses used by various resources.
              - *(dict) --* 
                Details about license consumption.
                - **ResourceType** *(string) --* 
                  Resource type of the resource consuming a license (instance, host, or AMI).
                - **ConsumedLicenses** *(integer) --* 
                  Number of licenses consumed by a resource.
            - **ManagedResourceSummaryList** *(list) --* 
              List of summaries of managed resources.
              - *(dict) --* 
                Summary for a resource.
                - **ResourceType** *(string) --* 
                  Type of resource associated with a license (instance, host, or AMI).
                - **AssociationCount** *(integer) --* 
                  Number of resources associated with licenses.
            - **Tags** *(list) --* 
              List of tags attached to the license configuration.
              - *(dict) --* 
                Tag for a resource in a key-value format.
                - **Key** *(string) --* 
                  Key for the resource tag.
                - **Value** *(string) --* 
                  Value for the resource tag.
        :type LicenseConfigurationArn: string
        :param LicenseConfigurationArn: **[REQUIRED]**
          ARN of the license configuration being requested.
        :rtype: dict
        :returns:
        """
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        """
        Create a paginator for an operation.
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

    def get_service_settings(self) -> Dict:
        """
        Gets License Manager settings for a region. Exposes the configured S3 bucket, SNS topic, etc., for inspection. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/GetServiceSettings>`_
        
        **Request Syntax**
        ::
          response = client.get_service_settings()
        
        **Response Syntax**
        ::
            {
                'S3BucketArn': 'string',
                'SnsTopicArn': 'string',
                'OrganizationConfiguration': {
                    'EnableIntegration': True|False
                },
                'EnableCrossAccountsDiscovery': True|False
            }
        
        **Response Structure**
          - *(dict) --* 
            - **S3BucketArn** *(string) --* 
              Regional S3 bucket path for storing reports, license trail event data, discovery data, etc.
            - **SnsTopicArn** *(string) --* 
              SNS topic configured to receive notifications from License Manager.
            - **OrganizationConfiguration** *(dict) --* 
              Indicates whether AWS Organizations has been integrated with License Manager for cross-account discovery.
              - **EnableIntegration** *(boolean) --* 
                Flag to activate AWS Organization integration.
            - **EnableCrossAccountsDiscovery** *(boolean) --* 
              Indicates whether cross-account discovery has been enabled.
        :rtype: dict
        :returns:
        """
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        Returns an object that can wait for some condition.
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def list_associations_for_license_configuration(self, LicenseConfigurationArn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Lists the resource associations for a license configuration. Resource associations need not consume licenses from a license configuration. For example, an AMI or a stopped instance may not consume a license (depending on the license rules). Use this operation to find all resources associated with a license configuration.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListAssociationsForLicenseConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.list_associations_for_license_configuration(
              LicenseConfigurationArn='string',
              MaxResults=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'LicenseConfigurationAssociations': [
                    {
                        'ResourceArn': 'string',
                        'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI',
                        'ResourceOwnerId': 'string',
                        'AssociationTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LicenseConfigurationAssociations** *(list) --* 
              Lists association objects for the license configuration, each containing the association time, number of consumed licenses, resource ARN, resource ID, account ID that owns the resource, resource size, and resource type.
              - *(dict) --* 
                Describes a server resource that is associated with a license configuration.
                - **ResourceArn** *(string) --* 
                  ARN of the resource associated with the license configuration.
                - **ResourceType** *(string) --* 
                  Type of server resource.
                - **ResourceOwnerId** *(string) --* 
                  ID of the AWS account that owns the resource consuming licenses.
                - **AssociationTime** *(datetime) --* 
                  Time when the license configuration was associated with the resource.
            - **NextToken** *(string) --* 
              Token for the next set of results.
        :type LicenseConfigurationArn: string
        :param LicenseConfigurationArn: **[REQUIRED]**
          ARN of a ``LicenseConfiguration`` object.
        :type MaxResults: integer
        :param MaxResults:
          Maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned ``NextToken`` value.
        :type NextToken: string
        :param NextToken:
          Token for the next set of results.
        :rtype: dict
        :returns:
        """
        pass

    def list_license_configurations(self, LicenseConfigurationArns: List = None, MaxResults: int = None, NextToken: str = None, Filters: List = None) -> Dict:
        """
        Lists license configuration objects for an account, each containing the name, description, license type, and other license terms modeled from a license agreement.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListLicenseConfigurations>`_
        
        **Request Syntax**
        ::
          response = client.list_license_configurations(
              LicenseConfigurationArns=[
                  'string',
              ],
              MaxResults=123,
              NextToken='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'LicenseConfigurations': [
                    {
                        'LicenseConfigurationId': 'string',
                        'LicenseConfigurationArn': 'string',
                        'Name': 'string',
                        'Description': 'string',
                        'LicenseCountingType': 'vCPU'|'Instance'|'Core'|'Socket',
                        'LicenseRules': [
                            'string',
                        ],
                        'LicenseCount': 123,
                        'LicenseCountHardLimit': True|False,
                        'ConsumedLicenses': 123,
                        'Status': 'string',
                        'OwnerAccountId': 'string',
                        'ConsumedLicenseSummaryList': [
                            {
                                'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI',
                                'ConsumedLicenses': 123
                            },
                        ],
                        'ManagedResourceSummaryList': [
                            {
                                'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI',
                                'AssociationCount': 123
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LicenseConfigurations** *(list) --* 
              Array of license configuration objects.
              - *(dict) --* 
                A license configuration is an abstraction of a customer license agreement that can be consumed and enforced by License Manager. Components include specifications for the license type (licensing by instance, socket, CPU, or VCPU), tenancy (shared tenancy, Amazon EC2 Dedicated Instance, Amazon EC2 Dedicated Host, or any of these), host affinity (how long a VM must be associated with a host), the number of licenses purchased and used.
                - **LicenseConfigurationId** *(string) --* 
                  Unique ID of the ``LicenseConfiguration`` object.
                - **LicenseConfigurationArn** *(string) --* 
                  ARN of the ``LicenseConfiguration`` object.
                - **Name** *(string) --* 
                  Name of the license configuration.
                - **Description** *(string) --* 
                  Description of the license configuration.
                - **LicenseCountingType** *(string) --* 
                  Dimension to use to track license inventory.
                - **LicenseRules** *(list) --* 
                  Array of configured License Manager rules.
                  - *(string) --* 
                - **LicenseCount** *(integer) --* 
                  Number of licenses managed by the license configuration.
                - **LicenseCountHardLimit** *(boolean) --* 
                  Sets the number of available licenses as a hard limit.
                - **ConsumedLicenses** *(integer) --* 
                  Number of licenses consumed. 
                - **Status** *(string) --* 
                  Status of the license configuration.
                - **OwnerAccountId** *(string) --* 
                  Account ID of the license configuration's owner.
                - **ConsumedLicenseSummaryList** *(list) --* 
                  List of summaries for licenses consumed by various resources.
                  - *(dict) --* 
                    Details about license consumption.
                    - **ResourceType** *(string) --* 
                      Resource type of the resource consuming a license (instance, host, or AMI).
                    - **ConsumedLicenses** *(integer) --* 
                      Number of licenses consumed by a resource.
                - **ManagedResourceSummaryList** *(list) --* 
                  List of summaries for managed resources.
                  - *(dict) --* 
                    Summary for a resource.
                    - **ResourceType** *(string) --* 
                      Type of resource associated with a license (instance, host, or AMI).
                    - **AssociationCount** *(integer) --* 
                      Number of resources associated with licenses.
            - **NextToken** *(string) --* 
              Token for the next set of results.
        :type LicenseConfigurationArns: list
        :param LicenseConfigurationArns:
          An array of ARNs for the calling account’s license configurations.
          - *(string) --*
        :type MaxResults: integer
        :param MaxResults:
          Maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned ``NextToken`` value.
        :type NextToken: string
        :param NextToken:
          Token for the next set of results.
        :type Filters: list
        :param Filters:
          One or more filters.
          - *(dict) --*
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a ``Describe`` operation are documented with the ``Describe`` operation.
            - **Name** *(string) --*
              Name of the filter. Filter names are case-sensitive.
            - **Values** *(list) --*
              One or more filter values. Filter values are case-sensitive.
              - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def list_license_specifications_for_resource(self, ResourceArn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Returns the license configuration for a resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListLicenseSpecificationsForResource>`_
        
        **Request Syntax**
        ::
          response = client.list_license_specifications_for_resource(
              ResourceArn='string',
              MaxResults=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'LicenseSpecifications': [
                    {
                        'LicenseConfigurationArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LicenseSpecifications** *(list) --* 
              License configurations associated with a resource.
              - *(dict) --* 
                Object used for associating a license configuration with a resource.
                - **LicenseConfigurationArn** *(string) --* 
                  ARN of the ``LicenseConfiguration`` object.
            - **NextToken** *(string) --* 
              Token for the next set of results.
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          ARN of an AMI or Amazon EC2 instance that has an associated license configuration.
        :type MaxResults: integer
        :param MaxResults:
          Maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned ``NextToken`` value.
        :type NextToken: string
        :param NextToken:
          Token for the next set of results.
        :rtype: dict
        :returns:
        """
        pass

    def list_resource_inventory(self, MaxResults: int = None, NextToken: str = None, Filters: List = None) -> Dict:
        """
        Returns a detailed list of resources.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListResourceInventory>`_
        
        **Request Syntax**
        ::
          response = client.list_resource_inventory(
              MaxResults=123,
              NextToken='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Condition': 'EQUALS'|'NOT_EQUALS'|'BEGINS_WITH'|'CONTAINS',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'ResourceInventoryList': [
                    {
                        'ResourceId': 'string',
                        'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI',
                        'ResourceArn': 'string',
                        'Platform': 'string',
                        'PlatformVersion': 'string',
                        'ResourceOwningAccountId': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ResourceInventoryList** *(list) --* 
              The detailed list of resources.
              - *(dict) --* 
                A set of attributes that describe a resource.
                - **ResourceId** *(string) --* 
                  Unique ID of the resource.
                - **ResourceType** *(string) --* 
                  The type of resource.
                - **ResourceArn** *(string) --* 
                  The ARN of the resource.
                - **Platform** *(string) --* 
                  The platform of the resource.
                - **PlatformVersion** *(string) --* 
                  Platform version of the resource in the inventory.
                - **ResourceOwningAccountId** *(string) --* 
                  Unique ID of the account that owns the resource.
            - **NextToken** *(string) --* 
              Token for the next set of results.
        :type MaxResults: integer
        :param MaxResults:
          Maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned ``NextToken`` value.
        :type NextToken: string
        :param NextToken:
          Token for the next set of results.
        :type Filters: list
        :param Filters:
          One or more filters.
          - *(dict) --*
            An inventory filter object.
            - **Name** *(string) --* **[REQUIRED]**
              The name of the filter.
            - **Condition** *(string) --* **[REQUIRED]**
              The condition of the filter.
            - **Value** *(string) --*
              Value of the filter.
        :rtype: dict
        :returns:
        """
        pass

    def list_tags_for_resource(self, ResourceArn: str) -> Dict:
        """
        Lists tags attached to a resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListTagsForResource>`_
        
        **Request Syntax**
        ::
          response = client.list_tags_for_resource(
              ResourceArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Tags** *(list) --* 
              List of tags attached to the resource.
              - *(dict) --* 
                Tag for a resource in a key-value format.
                - **Key** *(string) --* 
                  Key for the resource tag.
                - **Value** *(string) --* 
                  Value for the resource tag.
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          ARN for the resource.
        :rtype: dict
        :returns:
        """
        pass

    def list_usage_for_license_configuration(self, LicenseConfigurationArn: str, MaxResults: int = None, NextToken: str = None, Filters: List = None) -> Dict:
        """
        Lists all license usage records for a license configuration, displaying license consumption details by resource at a selected point in time. Use this action to audit the current license consumption for any license inventory and configuration.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListUsageForLicenseConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.list_usage_for_license_configuration(
              LicenseConfigurationArn='string',
              MaxResults=123,
              NextToken='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'LicenseConfigurationUsageList': [
                    {
                        'ResourceArn': 'string',
                        'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI',
                        'ResourceStatus': 'string',
                        'ResourceOwnerId': 'string',
                        'AssociationTime': datetime(2015, 1, 1),
                        'ConsumedLicenses': 123
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LicenseConfigurationUsageList** *(list) --* 
              An array of ``LicenseConfigurationUsage`` objects.
              - *(dict) --* 
                Contains details of the usage of each resource from the license pool.
                - **ResourceArn** *(string) --* 
                  ARN of the resource associated with a license configuration.
                - **ResourceType** *(string) --* 
                  Type of resource associated with athe license configuration.
                - **ResourceStatus** *(string) --* 
                  Status of a resource associated with the license configuration.
                - **ResourceOwnerId** *(string) --* 
                  ID of the account that owns a resource that is associated with the license configuration.
                - **AssociationTime** *(datetime) --* 
                  Time when the license configuration was initially associated with a resource.
                - **ConsumedLicenses** *(integer) --* 
                  Number of licenses consumed out of the total provisioned in the license configuration.
            - **NextToken** *(string) --* 
              Token for the next set of results.
        :type LicenseConfigurationArn: string
        :param LicenseConfigurationArn: **[REQUIRED]**
          ARN of the targeted ``LicenseConfiguration`` object.
        :type MaxResults: integer
        :param MaxResults:
          Maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned ``NextToken`` value.
        :type NextToken: string
        :param NextToken:
          Token for the next set of results.
        :type Filters: list
        :param Filters:
          List of filters to apply.
          - *(dict) --*
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a ``Describe`` operation are documented with the ``Describe`` operation.
            - **Name** *(string) --*
              Name of the filter. Filter names are case-sensitive.
            - **Values** *(list) --*
              One or more filter values. Filter values are case-sensitive.
              - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def tag_resource(self, ResourceArn: str, Tags: List) -> Dict:
        """
        Attach one of more tags to any resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/TagResource>`_
        
        **Request Syntax**
        ::
          response = client.tag_resource(
              ResourceArn='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          Resource of the ARN to be tagged.
        :type Tags: list
        :param Tags: **[REQUIRED]**
          Names of the tags to attach to the resource.
          - *(dict) --*
            Tag for a resource in a key-value format.
            - **Key** *(string) --*
              Key for the resource tag.
            - **Value** *(string) --*
              Value for the resource tag.
        :rtype: dict
        :returns:
        """
        pass

    def untag_resource(self, ResourceArn: str, TagKeys: List) -> Dict:
        """
        Remove tags from a resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/UntagResource>`_
        
        **Request Syntax**
        ::
          response = client.untag_resource(
              ResourceArn='string',
              TagKeys=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          ARN of the resource.
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**
          List keys identifying tags to remove.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def update_license_configuration(self, LicenseConfigurationArn: str, LicenseConfigurationStatus: str = None, LicenseRules: List = None, LicenseCount: int = None, LicenseCountHardLimit: bool = None, Name: str = None, Description: str = None) -> Dict:
        """
        Modifies the attributes of an existing license configuration object. A license configuration is an abstraction of a customer license agreement that can be consumed and enforced by License Manager. Components include specifications for the license type (Instances, cores, sockets, VCPUs), tenancy (shared or Dedicated Host), host affinity (how long a VM is associated with a host), the number of licenses purchased and used.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/UpdateLicenseConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.update_license_configuration(
              LicenseConfigurationArn='string',
              LicenseConfigurationStatus='AVAILABLE'|'DISABLED',
              LicenseRules=[
                  'string',
              ],
              LicenseCount=123,
              LicenseCountHardLimit=True|False,
              Name='string',
              Description='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type LicenseConfigurationArn: string
        :param LicenseConfigurationArn: **[REQUIRED]**
          ARN for a license configuration.
        :type LicenseConfigurationStatus: string
        :param LicenseConfigurationStatus:
          New status of the license configuration (``ACTIVE`` or ``INACTIVE`` ).
        :type LicenseRules: list
        :param LicenseRules:
          List of flexible text strings designating license rules.
          - *(string) --*
        :type LicenseCount: integer
        :param LicenseCount:
          New number of licenses managed by the license configuration.
        :type LicenseCountHardLimit: boolean
        :param LicenseCountHardLimit:
          Sets the number of available licenses as a hard limit.
        :type Name: string
        :param Name:
          New name of the license configuration.
        :type Description: string
        :param Description:
          New human-friendly description of the license configuration.
        :rtype: dict
        :returns:
        """
        pass

    def update_license_specifications_for_resource(self, ResourceArn: str, AddLicenseSpecifications: List = None, RemoveLicenseSpecifications: List = None) -> Dict:
        """
        Adds or removes license configurations for a specified AWS resource. This operation currently supports updating the license specifications of AMIs, instances, and hosts. Launch templates and AWS CloudFormation templates are not managed from this operation as those resources send the license configurations directly to a resource creation operation, such as ``RunInstances`` .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/UpdateLicenseSpecificationsForResource>`_
        
        **Request Syntax**
        ::
          response = client.update_license_specifications_for_resource(
              ResourceArn='string',
              AddLicenseSpecifications=[
                  {
                      'LicenseConfigurationArn': 'string'
                  },
              ],
              RemoveLicenseSpecifications=[
                  {
                      'LicenseConfigurationArn': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          ARN for an AWS server resource.
        :type AddLicenseSpecifications: list
        :param AddLicenseSpecifications:
          License configuration ARNs to be added to a resource.
          - *(dict) --*
            Object used for associating a license configuration with a resource.
            - **LicenseConfigurationArn** *(string) --* **[REQUIRED]**
              ARN of the ``LicenseConfiguration`` object.
        :type RemoveLicenseSpecifications: list
        :param RemoveLicenseSpecifications:
          License configuration ARNs to be removed from a resource.
          - *(dict) --*
            Object used for associating a license configuration with a resource.
            - **LicenseConfigurationArn** *(string) --* **[REQUIRED]**
              ARN of the ``LicenseConfiguration`` object.
        :rtype: dict
        :returns:
        """
        pass

    def update_service_settings(self, S3BucketArn: str = None, SnsTopicArn: str = None, OrganizationConfiguration: Dict = None, EnableCrossAccountsDiscovery: bool = None) -> Dict:
        """
        Updates License Manager service settings.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/UpdateServiceSettings>`_
        
        **Request Syntax**
        ::
          response = client.update_service_settings(
              S3BucketArn='string',
              SnsTopicArn='string',
              OrganizationConfiguration={
                  'EnableIntegration': True|False
              },
              EnableCrossAccountsDiscovery=True|False
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type S3BucketArn: string
        :param S3BucketArn:
          ARN of the Amazon S3 bucket where License Manager information is stored.
        :type SnsTopicArn: string
        :param SnsTopicArn:
          ARN of the Amazon SNS topic used for License Manager alerts.
        :type OrganizationConfiguration: dict
        :param OrganizationConfiguration:
          Integrates AWS Organizations with License Manager for cross-account discovery.
          - **EnableIntegration** *(boolean) --* **[REQUIRED]**
            Flag to activate AWS Organization integration.
        :type EnableCrossAccountsDiscovery: boolean
        :param EnableCrossAccountsDiscovery:
          Activates cross-account discovery.
        :rtype: dict
        :returns:
        """
        pass
