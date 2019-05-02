from typing import Dict
from typing import List
from botocore.paginate import Paginator


class ListAssociationsForLicenseConfiguration(Paginator):
    def paginate(self, LicenseConfigurationArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`LicenseManager.Client.list_associations_for_license_configuration`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListAssociationsForLicenseConfiguration>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              LicenseConfigurationArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
        :type LicenseConfigurationArn: string
        :param LicenseConfigurationArn: **[REQUIRED]**
          ARN of a ``LicenseConfiguration`` object.
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


class ListLicenseConfigurations(Paginator):
    def paginate(self, LicenseConfigurationArns: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`LicenseManager.Client.list_license_configurations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListLicenseConfigurations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              LicenseConfigurationArns=[
                  'string',
              ],
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
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
        :type LicenseConfigurationArns: list
        :param LicenseConfigurationArns:
          An array of ARNs for the calling account’s license configurations.
          - *(string) --*
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


class ListLicenseSpecificationsForResource(Paginator):
    def paginate(self, ResourceArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`LicenseManager.Client.list_license_specifications_for_resource`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListLicenseSpecificationsForResource>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ResourceArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'LicenseSpecifications': [
                    {
                        'LicenseConfigurationArn': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LicenseSpecifications** *(list) --* 
              License configurations associated with a resource.
              - *(dict) --* 
                Object used for associating a license configuration with a resource.
                - **LicenseConfigurationArn** *(string) --* 
                  ARN of the ``LicenseConfiguration`` object.
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          ARN of an AMI or Amazon EC2 instance that has an associated license configuration.
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


class ListResourceInventory(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`LicenseManager.Client.list_resource_inventory`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListResourceInventory>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Condition': 'EQUALS'|'NOT_EQUALS'|'BEGINS_WITH'|'CONTAINS',
                      'Value': 'string'
                  },
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


class ListUsageForLicenseConfiguration(Paginator):
    def paginate(self, LicenseConfigurationArn: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`LicenseManager.Client.list_usage_for_license_configuration`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListUsageForLicenseConfiguration>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              LicenseConfigurationArn='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
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
        :type LicenseConfigurationArn: string
        :param LicenseConfigurationArn: **[REQUIRED]**
          ARN of the targeted ``LicenseConfiguration`` object.
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
