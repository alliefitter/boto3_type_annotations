from typing import Dict
from botocore.paginate import Paginator


class DescribeReservedElasticsearchInstanceOfferings(Paginator):
    def paginate(self, ReservedElasticsearchInstanceOfferingId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ElasticsearchService.Client.describe_reserved_elasticsearch_instance_offerings`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/DescribeReservedElasticsearchInstanceOfferings>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ReservedElasticsearchInstanceOfferingId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ReservedElasticsearchInstanceOfferings': [
                    {
                        'ReservedElasticsearchInstanceOfferingId': 'string',
                        'ElasticsearchInstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                        'Duration': 123,
                        'FixedPrice': 123.0,
                        'UsagePrice': 123.0,
                        'CurrencyCode': 'string',
                        'PaymentOption': 'ALL_UPFRONT'|'PARTIAL_UPFRONT'|'NO_UPFRONT',
                        'RecurringCharges': [
                            {
                                'RecurringChargeAmount': 123.0,
                                'RecurringChargeFrequency': 'string'
                            },
                        ]
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Container for results from ``DescribeReservedElasticsearchInstanceOfferings`` 
            - **ReservedElasticsearchInstanceOfferings** *(list) --* 
              List of reserved Elasticsearch instance offerings
              - *(dict) --* 
                Details of a reserved Elasticsearch instance offering.
                - **ReservedElasticsearchInstanceOfferingId** *(string) --* 
                  The Elasticsearch reserved instance offering identifier.
                - **ElasticsearchInstanceType** *(string) --* 
                  The Elasticsearch instance type offered by the reserved instance offering.
                - **Duration** *(integer) --* 
                  The duration, in seconds, for which the offering will reserve the Elasticsearch instance.
                - **FixedPrice** *(float) --* 
                  The upfront fixed charge you will pay to purchase the specific reserved Elasticsearch instance offering. 
                - **UsagePrice** *(float) --* 
                  The rate you are charged for each hour the domain that is using the offering is running.
                - **CurrencyCode** *(string) --* 
                  The currency code for the reserved Elasticsearch instance offering.
                - **PaymentOption** *(string) --* 
                  Payment option for the reserved Elasticsearch instance offering
                - **RecurringCharges** *(list) --* 
                  The charge to your account regardless of whether you are creating any domains using the instance offering.
                  - *(dict) --* 
                    Contains the specific price and frequency of a recurring charges for a reserved Elasticsearch instance, or for a reserved Elasticsearch instance offering.
                    - **RecurringChargeAmount** *(float) --* 
                      The monetary amount of the recurring charge.
                    - **RecurringChargeFrequency** *(string) --* 
                      The frequency of the recurring charge.
        :type ReservedElasticsearchInstanceOfferingId: string
        :param ReservedElasticsearchInstanceOfferingId:
          The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier.
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


class DescribeReservedElasticsearchInstances(Paginator):
    def paginate(self, ReservedElasticsearchInstanceId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ElasticsearchService.Client.describe_reserved_elasticsearch_instances`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/DescribeReservedElasticsearchInstances>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ReservedElasticsearchInstanceId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ReservedElasticsearchInstances': [
                    {
                        'ReservationName': 'string',
                        'ReservedElasticsearchInstanceId': 'string',
                        'ReservedElasticsearchInstanceOfferingId': 'string',
                        'ElasticsearchInstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                        'StartTime': datetime(2015, 1, 1),
                        'Duration': 123,
                        'FixedPrice': 123.0,
                        'UsagePrice': 123.0,
                        'CurrencyCode': 'string',
                        'ElasticsearchInstanceCount': 123,
                        'State': 'string',
                        'PaymentOption': 'ALL_UPFRONT'|'PARTIAL_UPFRONT'|'NO_UPFRONT',
                        'RecurringCharges': [
                            {
                                'RecurringChargeAmount': 123.0,
                                'RecurringChargeFrequency': 'string'
                            },
                        ]
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Container for results from ``DescribeReservedElasticsearchInstances`` 
            - **ReservedElasticsearchInstances** *(list) --* 
              List of reserved Elasticsearch instances.
              - *(dict) --* 
                Details of a reserved Elasticsearch instance.
                - **ReservationName** *(string) --* 
                  The customer-specified identifier to track this reservation.
                - **ReservedElasticsearchInstanceId** *(string) --* 
                  The unique identifier for the reservation.
                - **ReservedElasticsearchInstanceOfferingId** *(string) --* 
                  The offering identifier.
                - **ElasticsearchInstanceType** *(string) --* 
                  The Elasticsearch instance type offered by the reserved instance offering.
                - **StartTime** *(datetime) --* 
                  The time the reservation started.
                - **Duration** *(integer) --* 
                  The duration, in seconds, for which the Elasticsearch instance is reserved.
                - **FixedPrice** *(float) --* 
                  The upfront fixed charge you will paid to purchase the specific reserved Elasticsearch instance offering. 
                - **UsagePrice** *(float) --* 
                  The rate you are charged for each hour for the domain that is using this reserved instance.
                - **CurrencyCode** *(string) --* 
                  The currency code for the reserved Elasticsearch instance offering.
                - **ElasticsearchInstanceCount** *(integer) --* 
                  The number of Elasticsearch instances that have been reserved.
                - **State** *(string) --* 
                  The state of the reserved Elasticsearch instance.
                - **PaymentOption** *(string) --* 
                  The payment option as defined in the reserved Elasticsearch instance offering.
                - **RecurringCharges** *(list) --* 
                  The charge to your account regardless of whether you are creating any domains using the instance offering.
                  - *(dict) --* 
                    Contains the specific price and frequency of a recurring charges for a reserved Elasticsearch instance, or for a reserved Elasticsearch instance offering.
                    - **RecurringChargeAmount** *(float) --* 
                      The monetary amount of the recurring charge.
                    - **RecurringChargeFrequency** *(string) --* 
                      The frequency of the recurring charge.
        :type ReservedElasticsearchInstanceId: string
        :param ReservedElasticsearchInstanceId:
          The reserved instance identifier filter value. Use this parameter to show only the reservation that matches the specified reserved Elasticsearch instance ID.
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


class GetUpgradeHistory(Paginator):
    def paginate(self, DomainName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ElasticsearchService.Client.get_upgrade_history`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/GetUpgradeHistory>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DomainName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'UpgradeHistories': [
                    {
                        'UpgradeName': 'string',
                        'StartTimestamp': datetime(2015, 1, 1),
                        'UpgradeStatus': 'IN_PROGRESS'|'SUCCEEDED'|'SUCCEEDED_WITH_ISSUES'|'FAILED',
                        'StepsList': [
                            {
                                'UpgradeStep': 'PRE_UPGRADE_CHECK'|'SNAPSHOT'|'UPGRADE',
                                'UpgradeStepStatus': 'IN_PROGRESS'|'SUCCEEDED'|'SUCCEEDED_WITH_ISSUES'|'FAILED',
                                'Issues': [
                                    'string',
                                ],
                                'ProgressPercent': 123.0
                            },
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Container for response returned by ``  GetUpgradeHistory `` operation. 
            - **UpgradeHistories** *(list) --* 
              A list of ``  UpgradeHistory `` objects corresponding to each Upgrade or Upgrade Eligibility Check performed on a domain returned as part of ``  GetUpgradeHistoryResponse `` object. 
              - *(dict) --* 
                History of the last 10 Upgrades and Upgrade Eligibility Checks.
                - **UpgradeName** *(string) --* 
                  A string that describes the update briefly
                - **StartTimestamp** *(datetime) --* 
                  UTC Timestamp at which the Upgrade API call was made in "yyyy-MM-ddTHH:mm:ssZ" format.
                - **UpgradeStatus** *(string) --* 
                  The overall status of the update. The status can take one of the following values: 
                  * In Progress
                  * Succeeded
                  * Succeeded with Issues
                  * Failed
                - **StepsList** *(list) --* 
                  A list of ``  UpgradeStepItem `` s representing information about each step performed as pard of a specific Upgrade or Upgrade Eligibility Check. 
                  - *(dict) --* 
                    Represents a single step of the Upgrade or Upgrade Eligibility Check workflow.
                    - **UpgradeStep** *(string) --* 
                      Represents one of 3 steps that an Upgrade or Upgrade Eligibility Check does through: 
                      * PreUpgradeCheck
                      * Snapshot
                      * Upgrade
                    - **UpgradeStepStatus** *(string) --* 
                      The status of a particular step during an upgrade. The status can take one of the following values: 
                      * In Progress
                      * Succeeded
                      * Succeeded with Issues
                      * Failed
                    - **Issues** *(list) --* 
                      A list of strings containing detailed information about the errors encountered in a particular step.
                      - *(string) --* 
                    - **ProgressPercent** *(float) --* 
                      The Floating point value representing progress percentage of a particular step.
        :type DomainName: string
        :param DomainName: **[REQUIRED]**
          The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
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


class ListElasticsearchInstanceTypes(Paginator):
    def paginate(self, ElasticsearchVersion: str, DomainName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ElasticsearchService.Client.list_elasticsearch_instance_types`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/ListElasticsearchInstanceTypes>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ElasticsearchVersion='string',
              DomainName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ElasticsearchInstanceTypes': [
                    'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Container for the parameters returned by ``  ListElasticsearchInstanceTypes `` operation. 
            - **ElasticsearchInstanceTypes** *(list) --* 
              List of instance types supported by Amazon Elasticsearch service for given ``  ElasticsearchVersion ``  
              - *(string) --* 
        :type ElasticsearchVersion: string
        :param ElasticsearchVersion: **[REQUIRED]**
          Version of Elasticsearch for which list of supported elasticsearch instance types are needed.
        :type DomainName: string
        :param DomainName:
          DomainName represents the name of the Domain that we are trying to modify. This should be present only if we are querying for list of available Elasticsearch instance types when modifying existing domain.
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


class ListElasticsearchVersions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ElasticsearchService.Client.list_elasticsearch_versions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/ListElasticsearchVersions>`_
        
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
                'ElasticsearchVersions': [
                    'string',
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Container for the parameters for response received from ``  ListElasticsearchVersions `` operation. 
            - **ElasticsearchVersions** *(list) --* 
              List of supported elastic search versions. 
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
