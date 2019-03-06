from typing import Union
from typing import List
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Optional
from typing import Dict
from botocore.client import BaseClient


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

    def get_cost_and_usage(self, TimePeriod: Dict = None, Granularity: str = None, Filter: Dict = None, Metrics: List = None, GroupBy: List = None, NextPageToken: str = None) -> Dict:
        """
        Retrieves cost and usage metrics for your account. You can specify which cost and usage-related metric, such as ``BlendedCosts`` or ``UsageQuantity`` , that you want the request to return. You can also filter and group your data by various dimensions, such as ``SERVICE`` or ``AZ`` , in a specific time range. For a complete list of valid dimensions, see the `GetDimensionValues <http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetDimensionValues.html>`__ operation. Master accounts in an organization in AWS Organizations have access to all member accounts.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetCostAndUsage>`_
        
        **Request Syntax**
        ::
          response = client.get_cost_and_usage(
              TimePeriod={
                  'Start': 'string',
                  'End': 'string'
              },
              Granularity='DAILY'|'MONTHLY'|'HOURLY',
              Filter={
                  'Or': [
                      {'... recursive ...'},
                  ],
                  'And': [
                      {'... recursive ...'},
                  ],
                  'Not': {'... recursive ...'},
                  'Dimensions': {
                      'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID',
                      'Values': [
                          'string',
                      ]
                  },
                  'Tags': {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  }
              },
              Metrics=[
                  'string',
              ],
              GroupBy=[
                  {
                      'Type': 'DIMENSION'|'TAG',
                      'Key': 'string'
                  },
              ],
              NextPageToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'NextPageToken': 'string',
                'GroupDefinitions': [
                    {
                        'Type': 'DIMENSION'|'TAG',
                        'Key': 'string'
                    },
                ],
                'ResultsByTime': [
                    {
                        'TimePeriod': {
                            'Start': 'string',
                            'End': 'string'
                        },
                        'Total': {
                            'string': {
                                'Amount': 'string',
                                'Unit': 'string'
                            }
                        },
                        'Groups': [
                            {
                                'Keys': [
                                    'string',
                                ],
                                'Metrics': {
                                    'string': {
                                        'Amount': 'string',
                                        'Unit': 'string'
                                    }
                                }
                            },
                        ],
                        'Estimated': True|False
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **NextPageToken** *(string) --* 
              The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.
            - **GroupDefinitions** *(list) --* 
              The groups that are specified by the ``Filter`` or ``GroupBy`` parameters in the request.
              - *(dict) --* 
                Represents a group when you specify a group by criteria or in the response to a query with a specific grouping.
                - **Type** *(string) --* 
                  The string that represents the type of group.
                - **Key** *(string) --* 
                  The string that represents a key for a specified group.
            - **ResultsByTime** *(list) --* 
              The time period that is covered by the results in the response.
              - *(dict) --* 
                The result that is associated with a time period.
                - **TimePeriod** *(dict) --* 
                  The time period that the result covers.
                  - **Start** *(string) --* 
                    The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data starting at ``2017-01-01`` up to the end date.
                  - **End** *(string) --* 
                    The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start date up to, but not including, ``2017-05-01`` .
                - **Total** *(dict) --* 
                  The total amount of cost or usage accrued during the time period.
                  - *(string) --* 
                    - *(dict) --* 
                      The aggregated value for a metric.
                      - **Amount** *(string) --* 
                        The actual number that represents the metric.
                      - **Unit** *(string) --* 
                        The unit that the metric is given in.
                - **Groups** *(list) --* 
                  The groups that this time period includes.
                  - *(dict) --* 
                    One level of grouped data in the results.
                    - **Keys** *(list) --* 
                      The keys that are included in this group.
                      - *(string) --* 
                    - **Metrics** *(dict) --* 
                      The metrics that are included in this group.
                      - *(string) --* 
                        - *(dict) --* 
                          The aggregated value for a metric.
                          - **Amount** *(string) --* 
                            The actual number that represents the metric.
                          - **Unit** *(string) --* 
                            The unit that the metric is given in.
                - **Estimated** *(boolean) --* 
                  Whether the result is estimated.
        :type TimePeriod: dict
        :param TimePeriod:
          Sets the start and end dates for retrieving AWS costs. The start date is inclusive, but the end date is exclusive. For example, if ``start`` is ``2017-01-01`` and ``end`` is ``2017-05-01`` , then the cost and usage data is retrieved from ``2017-01-01`` up to and including ``2017-04-30`` but not including ``2017-05-01`` .
          - **Start** *(string) --* **[REQUIRED]**
            The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data starting at ``2017-01-01`` up to the end date.
          - **End** *(string) --* **[REQUIRED]**
            The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start date up to, but not including, ``2017-05-01`` .
        :type Granularity: string
        :param Granularity:
          Sets the AWS cost granularity to ``MONTHLY`` or ``DAILY`` . If ``Granularity`` isn\'t set, the response object doesn\'t include the ``Granularity`` , either ``MONTHLY`` or ``DAILY`` .
          The ``GetCostAndUsageRequest`` operation supports only ``DAILY`` and ``MONTHLY`` granularities.
        :type Filter: dict
        :param Filter:
          Filters AWS costs by different dimensions. For example, you can specify ``SERVICE`` and ``LINKED_ACCOUNT`` and get the costs that are associated with that account\'s usage of that service. You can nest ``Expression`` objects to define any combination of dimension filters. For more information, see `Expression <http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html>`__ .
          - **Or** *(list) --*
            Return results that match either ``Dimension`` object.
            - *(dict) --*
              Use ``Expression`` to filter by cost or by usage. There are two patterns:
              * Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for ``INSTANCE_TYPE==m4.xlarge OR INSTANCE_TYPE==c4.large`` . The ``Expression`` for that looks like this:  ``{ \"Dimensions\": { \"Key\": \"INSTANCE_TYPE\", \"Values\": [ \"m4.xlarge\", “c4.large” ] } }``   The list of dimension values are OR\'d together to retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects using either ``with*`` methods or ``set*`` methods in multiple lines.
              * Compound dimension values with logical operations - You can use multiple ``Expression`` types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression`` objects. This allows you to filter on more advanced options. For example, you can filter on ``((INSTANCE_TYPE == m4.large OR INSTANCE_TYPE == m3.large) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ \"And\": [ {\"Or\": [ {\"Dimensions\": { \"Key\": \"INSTANCE_TYPE\", \"Values\": [ \"m4.x.large\", \"c4.large\" ] }}, {\"Tags\": { \"Key\": \"TagName\", \"Values\": [\"Value1\"] } } ]}, {\"Not\": {\"Dimensions\": { \"Key\": \"USAGE_TYPE\", \"Values\": [\"DataTransfer\"] }}} ] }``
              .. note::
                 Because each ``Expression`` can have only one operator, the service returns an error if more than one is specified. The following example shows an ``Expression`` object that creates an error.
                ``{ \"And\": [ ... ], \"DimensionValues\": { \"Dimension\": \"USAGE_TYPE\", \"Values\": [ \"DataTransfer\" ] } }``
          - **And** *(list) --*
            Return results that match both ``Dimension`` objects.
            - *(dict) --*
              Use ``Expression`` to filter by cost or by usage. There are two patterns:
              * Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for ``INSTANCE_TYPE==m4.xlarge OR INSTANCE_TYPE==c4.large`` . The ``Expression`` for that looks like this:  ``{ \"Dimensions\": { \"Key\": \"INSTANCE_TYPE\", \"Values\": [ \"m4.xlarge\", “c4.large” ] } }``   The list of dimension values are OR\'d together to retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects using either ``with*`` methods or ``set*`` methods in multiple lines.
              * Compound dimension values with logical operations - You can use multiple ``Expression`` types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression`` objects. This allows you to filter on more advanced options. For example, you can filter on ``((INSTANCE_TYPE == m4.large OR INSTANCE_TYPE == m3.large) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ \"And\": [ {\"Or\": [ {\"Dimensions\": { \"Key\": \"INSTANCE_TYPE\", \"Values\": [ \"m4.x.large\", \"c4.large\" ] }}, {\"Tags\": { \"Key\": \"TagName\", \"Values\": [\"Value1\"] } } ]}, {\"Not\": {\"Dimensions\": { \"Key\": \"USAGE_TYPE\", \"Values\": [\"DataTransfer\"] }}} ] }``
              .. note::
                 Because each ``Expression`` can have only one operator, the service returns an error if more than one is specified. The following example shows an ``Expression`` object that creates an error.
                ``{ \"And\": [ ... ], \"DimensionValues\": { \"Dimension\": \"USAGE_TYPE\", \"Values\": [ \"DataTransfer\" ] } }``
          - **Not** *(dict) --*
            Return results that don\'t match a ``Dimension`` object.
          - **Dimensions** *(dict) --*
            The specific ``Dimension`` to use for ``Expression`` .
            - **Key** *(string) --*
              The names of the metadata types that you can use to filter and group your results. For example, ``AZ`` returns a list of Availability Zones.
            - **Values** *(list) --*
              The metadata values that you can use to filter and group your results. You can use ``GetDimensionValues`` to find specific values.
              Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` , ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and ``Amazon Relational Database Service`` .
              - *(string) --*
          - **Tags** *(dict) --*
            The specific ``Tag`` to use for ``Expression`` .
            - **Key** *(string) --*
              The key for the tag.
            - **Values** *(list) --*
              The specific value of the tag.
              - *(string) --*
        :type Metrics: list
        :param Metrics:
          Which metrics are returned in the query. For more information about blended and unblended rates, see `Why does the \"blended\" annotation appear on some line items in my bill? <https://aws.amazon.com/premiumsupport/knowledge-center/blended-rates-intro/>`__ .
          Valid values are ``AmortizedCost`` , ``BlendedCost`` , ``NetAmortizedCost`` , ``NetUnblendedCost`` , ``NormalizedUsageAmount`` , ``UnblendedCost`` , and ``UsageQuantity`` .
          .. note::
            If you return the ``UsageQuantity`` metric, the service aggregates all usage numbers without taking into account the units. For example, if you aggregate ``usageQuantity`` across all of Amazon EC2, the results aren\'t meaningful because Amazon EC2 compute hours and data transfer are measured in different units (for example, hours vs. GB). To get more meaningful ``UsageQuantity`` metrics, filter by ``UsageType`` or ``UsageTypeGroups`` .
           ``Metrics`` is required for ``GetCostAndUsage`` requests.
          - *(string) --*
        :type GroupBy: list
        :param GroupBy:
          You can group AWS costs using up to two different groups, either dimensions, tag keys, or both.
          When you group by tag key, you get all tag values, including empty strings.
          Valid values are ``AZ`` , ``INSTANCE_TYPE`` , ``LEGAL_ENTITY_NAME`` , ``LINKED_ACCOUNT`` , ``OPERATION`` , ``PLATFORM`` , ``PURCHASE_TYPE`` , ``SERVICE`` , ``TAGS`` , ``TENANCY`` , and ``USAGE_TYPE`` .
          - *(dict) --*
            Represents a group when you specify a group by criteria or in the response to a query with a specific grouping.
            - **Type** *(string) --*
              The string that represents the type of group.
            - **Key** *(string) --*
              The string that represents a key for a specified group.
        :type NextPageToken: string
        :param NextPageToken:
          The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
        :rtype: dict
        :returns:
        """
        pass

    def get_cost_forecast(self, TimePeriod: Dict, Metric: str, Granularity: str, Filter: Dict = None, PredictionIntervalLevel: int = None) -> Dict:
        """
        Retrieves a forecast for how much Amazon Web Services predicts that you will spend over the forecast time period that you select, based on your past costs. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetCostForecast>`_
        
        **Request Syntax**
        ::
          response = client.get_cost_forecast(
              TimePeriod={
                  'Start': 'string',
                  'End': 'string'
              },
              Metric='BLENDED_COST'|'UNBLENDED_COST'|'AMORTIZED_COST'|'NET_UNBLENDED_COST'|'NET_AMORTIZED_COST'|'USAGE_QUANTITY'|'NORMALIZED_USAGE_AMOUNT',
              Granularity='DAILY'|'MONTHLY'|'HOURLY',
              Filter={
                  'Or': [
                      {'... recursive ...'},
                  ],
                  'And': [
                      {'... recursive ...'},
                  ],
                  'Not': {'... recursive ...'},
                  'Dimensions': {
                      'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID',
                      'Values': [
                          'string',
                      ]
                  },
                  'Tags': {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  }
              },
              PredictionIntervalLevel=123
          )
        
        **Response Syntax**
        ::
            {
                'Total': {
                    'Amount': 'string',
                    'Unit': 'string'
                },
                'ForecastResultsByTime': [
                    {
                        'TimePeriod': {
                            'Start': 'string',
                            'End': 'string'
                        },
                        'MeanValue': 'string',
                        'PredictionIntervalLowerBound': 'string',
                        'PredictionIntervalUpperBound': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Total** *(dict) --* 
              How much you are forecasted to spend over the forecast period, in ``USD`` .
              - **Amount** *(string) --* 
                The actual number that represents the metric.
              - **Unit** *(string) --* 
                The unit that the metric is given in.
            - **ForecastResultsByTime** *(list) --* 
              The forecasts for your query, in order. For ``DAILY`` forecasts, this is a list of days. For ``MONTHLY`` forecasts, this is a list of months.
              - *(dict) --* 
                The forecast created for your query.
                - **TimePeriod** *(dict) --* 
                  The period of time that the forecast covers.
                  - **Start** *(string) --* 
                    The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data starting at ``2017-01-01`` up to the end date.
                  - **End** *(string) --* 
                    The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start date up to, but not including, ``2017-05-01`` .
                - **MeanValue** *(string) --* 
                  The mean value of the forecast.
                - **PredictionIntervalLowerBound** *(string) --* 
                  The lower limit for the prediction interval. 
                - **PredictionIntervalUpperBound** *(string) --* 
                  The upper limit for the prediction interval. 
        :type TimePeriod: dict
        :param TimePeriod: **[REQUIRED]**
          The period of time that you want the forecast to cover.
          - **Start** *(string) --* **[REQUIRED]**
            The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data starting at ``2017-01-01`` up to the end date.
          - **End** *(string) --* **[REQUIRED]**
            The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start date up to, but not including, ``2017-05-01`` .
        :type Metric: string
        :param Metric: **[REQUIRED]**
          Which metric Cost Explorer uses to create your forecast. For more information about blended and unblended rates, see `Why does the \"blended\" annotation appear on some line items in my bill? <https://aws.amazon.com/premiumsupport/knowledge-center/blended-rates-intro/>`__ .
          Valid values for a ``GetCostForecast`` call are the following:
          * AmortizedCost
          * BlendedCost
          * NetAmortizedCost
          * NetUnblendedCost
          * UnblendedCost
        :type Granularity: string
        :param Granularity: **[REQUIRED]**
          How granular you want the forecast to be. You can get 3 months of ``DAILY`` forecasts or 12 months of ``MONTHLY`` forecasts.
          The ``GetCostForecast`` operation supports only ``DAILY`` and ``MONTHLY`` granularities.
        :type Filter: dict
        :param Filter:
          The filters that you want to use to filter your forecast. Cost Explorer API supports all of the Cost Explorer filters.
          - **Or** *(list) --*
            Return results that match either ``Dimension`` object.
            - *(dict) --*
              Use ``Expression`` to filter by cost or by usage. There are two patterns:
              * Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for ``INSTANCE_TYPE==m4.xlarge OR INSTANCE_TYPE==c4.large`` . The ``Expression`` for that looks like this:  ``{ \"Dimensions\": { \"Key\": \"INSTANCE_TYPE\", \"Values\": [ \"m4.xlarge\", “c4.large” ] } }``   The list of dimension values are OR\'d together to retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects using either ``with*`` methods or ``set*`` methods in multiple lines.
              * Compound dimension values with logical operations - You can use multiple ``Expression`` types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression`` objects. This allows you to filter on more advanced options. For example, you can filter on ``((INSTANCE_TYPE == m4.large OR INSTANCE_TYPE == m3.large) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ \"And\": [ {\"Or\": [ {\"Dimensions\": { \"Key\": \"INSTANCE_TYPE\", \"Values\": [ \"m4.x.large\", \"c4.large\" ] }}, {\"Tags\": { \"Key\": \"TagName\", \"Values\": [\"Value1\"] } } ]}, {\"Not\": {\"Dimensions\": { \"Key\": \"USAGE_TYPE\", \"Values\": [\"DataTransfer\"] }}} ] }``
              .. note::
                 Because each ``Expression`` can have only one operator, the service returns an error if more than one is specified. The following example shows an ``Expression`` object that creates an error.
                ``{ \"And\": [ ... ], \"DimensionValues\": { \"Dimension\": \"USAGE_TYPE\", \"Values\": [ \"DataTransfer\" ] } }``
          - **And** *(list) --*
            Return results that match both ``Dimension`` objects.
            - *(dict) --*
              Use ``Expression`` to filter by cost or by usage. There are two patterns:
              * Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for ``INSTANCE_TYPE==m4.xlarge OR INSTANCE_TYPE==c4.large`` . The ``Expression`` for that looks like this:  ``{ \"Dimensions\": { \"Key\": \"INSTANCE_TYPE\", \"Values\": [ \"m4.xlarge\", “c4.large” ] } }``   The list of dimension values are OR\'d together to retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects using either ``with*`` methods or ``set*`` methods in multiple lines.
              * Compound dimension values with logical operations - You can use multiple ``Expression`` types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression`` objects. This allows you to filter on more advanced options. For example, you can filter on ``((INSTANCE_TYPE == m4.large OR INSTANCE_TYPE == m3.large) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ \"And\": [ {\"Or\": [ {\"Dimensions\": { \"Key\": \"INSTANCE_TYPE\", \"Values\": [ \"m4.x.large\", \"c4.large\" ] }}, {\"Tags\": { \"Key\": \"TagName\", \"Values\": [\"Value1\"] } } ]}, {\"Not\": {\"Dimensions\": { \"Key\": \"USAGE_TYPE\", \"Values\": [\"DataTransfer\"] }}} ] }``
              .. note::
                 Because each ``Expression`` can have only one operator, the service returns an error if more than one is specified. The following example shows an ``Expression`` object that creates an error.
                ``{ \"And\": [ ... ], \"DimensionValues\": { \"Dimension\": \"USAGE_TYPE\", \"Values\": [ \"DataTransfer\" ] } }``
          - **Not** *(dict) --*
            Return results that don\'t match a ``Dimension`` object.
          - **Dimensions** *(dict) --*
            The specific ``Dimension`` to use for ``Expression`` .
            - **Key** *(string) --*
              The names of the metadata types that you can use to filter and group your results. For example, ``AZ`` returns a list of Availability Zones.
            - **Values** *(list) --*
              The metadata values that you can use to filter and group your results. You can use ``GetDimensionValues`` to find specific values.
              Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` , ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and ``Amazon Relational Database Service`` .
              - *(string) --*
          - **Tags** *(dict) --*
            The specific ``Tag`` to use for ``Expression`` .
            - **Key** *(string) --*
              The key for the tag.
            - **Values** *(list) --*
              The specific value of the tag.
              - *(string) --*
        :type PredictionIntervalLevel: integer
        :param PredictionIntervalLevel:
          Cost Explorer always returns the mean forecast as a single point. You can request a prediction interval around the mean by specifying a confidence level. The higher the confidence level, the more confident Cost Explorer is about the actual value falling in the prediction interval. Higher confidence levels result in wider prediction intervals.
        :rtype: dict
        :returns:
        """
        pass

    def get_dimension_values(self, TimePeriod: Dict, Dimension: str, SearchString: str = None, Context: str = None, NextPageToken: str = None) -> Dict:
        """
        Retrieves all available filter values for a specified filter over a period of time. You can search the dimension values for an arbitrary string. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetDimensionValues>`_
        
        **Request Syntax**
        ::
          response = client.get_dimension_values(
              SearchString='string',
              TimePeriod={
                  'Start': 'string',
                  'End': 'string'
              },
              Dimension='AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID',
              Context='COST_AND_USAGE'|'RESERVATIONS',
              NextPageToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'DimensionValues': [
                    {
                        'Value': 'string',
                        'Attributes': {
                            'string': 'string'
                        }
                    },
                ],
                'ReturnSize': 123,
                'TotalSize': 123,
                'NextPageToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DimensionValues** *(list) --* 
              The filters that you used to filter your request. Some dimensions are available only for a specific context.
              If you set the context to ``COST_AND_USAGE`` , you can use the following dimensions for searching:
              * AZ - The Availability Zone. An example is ``us-east-1a`` . 
              * DATABASE_ENGINE - The Amazon Relational Database Service database. Examples are Aurora or MySQL. 
              * INSTANCE_TYPE - The type of Amazon EC2 instance. An example is ``m4.xlarge`` . 
              * LEGAL_ENTITY_NAME - The name of the organization that sells you AWS services, such as Amazon Web Services. 
              * LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account. 
              * OPERATING_SYSTEM - The operating system. Examples are Windows or Linux. 
              * OPERATION - The action performed. Examples include ``RunInstance`` and ``CreateBucket`` . 
              * PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux. 
              * PURCHASE_TYPE - The reservation type of the purchase to which this usage is related. Examples include On-Demand Instances and Standard Reserved Instances. 
              * SERVICE - The AWS service such as Amazon DynamoDB. 
              * USAGE_TYPE - The type of usage. An example is DataTransfer-In-Bytes. The response for the ``GetDimensionValues`` operation includes a unit attribute. Examples include GB and Hrs. 
              * USAGE_TYPE_GROUP - The grouping of common usage types. An example is Amazon EC2: CloudWatch – Alarms. The response for this operation includes a unit attribute. 
              * RECORD_TYPE - The different types of charges such as RI fees, usage costs, tax refunds, and credits. 
              If you set the context to ``RESERVATIONS`` , you can use the following dimensions for searching:
              * AZ - The Availability Zone. An example is ``us-east-1a`` . 
              * CACHE_ENGINE - The Amazon ElastiCache operating system. Examples are Windows or Linux. 
              * DEPLOYMENT_OPTION - The scope of Amazon Relational Database Service deployments. Valid values are ``SingleAZ`` and ``MultiAZ`` . 
              * INSTANCE_TYPE - The type of Amazon EC2 instance. An example is ``m4.xlarge`` . 
              * LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account. 
              * PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux. 
              * REGION - The AWS Region. 
              * SCOPE (Utilization only) - The scope of a Reserved Instance (RI). Values are regional or a single Availability Zone. 
              * TAG (Coverage only) - The tags that are associated with a Reserved Instance (RI). 
              * TENANCY - The tenancy of a resource. Examples are shared or dedicated. 
              - *(dict) --* 
                The metadata of a specific type that you can use to filter and group your results. You can use ``GetDimensionValues`` to find specific values.
                - **Value** *(string) --* 
                  The value of a dimension with a specific attribute.
                - **Attributes** *(dict) --* 
                  The attribute that applies to a specific ``Dimension`` .
                  - *(string) --* 
                    - *(string) --* 
            - **ReturnSize** *(integer) --* 
              The number of results that AWS returned at one time.
            - **TotalSize** *(integer) --* 
              The total number of search results.
            - **NextPageToken** *(string) --* 
              The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.
        :type SearchString: string
        :param SearchString:
          The value that you want to search the filter values for.
        :type TimePeriod: dict
        :param TimePeriod: **[REQUIRED]**
          The start and end dates for retrieving the dimension values. The start date is inclusive, but the end date is exclusive. For example, if ``start`` is ``2017-01-01`` and ``end`` is ``2017-05-01`` , then the cost and usage data is retrieved from ``2017-01-01`` up to and including ``2017-04-30`` but not including ``2017-05-01`` .
          - **Start** *(string) --* **[REQUIRED]**
            The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data starting at ``2017-01-01`` up to the end date.
          - **End** *(string) --* **[REQUIRED]**
            The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start date up to, but not including, ``2017-05-01`` .
        :type Dimension: string
        :param Dimension: **[REQUIRED]**
          The name of the dimension. Each ``Dimension`` is available for a different ``Context`` . For more information, see ``Context`` .
        :type Context: string
        :param Context:
          The context for the call to ``GetDimensionValues`` . This can be ``RESERVATIONS`` or ``COST_AND_USAGE`` . The default value is ``COST_AND_USAGE`` . If the context is set to ``RESERVATIONS`` , the resulting dimension values can be used in the ``GetReservationUtilization`` operation. If the context is set to ``COST_AND_USAGE`` , the resulting dimension values can be used in the ``GetCostAndUsage`` operation.
          If you set the context to ``COST_AND_USAGE`` , you can use the following dimensions for searching:
          * AZ - The Availability Zone. An example is ``us-east-1a`` .
          * DATABASE_ENGINE - The Amazon Relational Database Service database. Examples are Aurora or MySQL.
          * INSTANCE_TYPE - The type of Amazon EC2 instance. An example is ``m4.xlarge`` .
          * LEGAL_ENTITY_NAME - The name of the organization that sells you AWS services, such as Amazon Web Services.
          * LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.
          * OPERATING_SYSTEM - The operating system. Examples are Windows or Linux.
          * OPERATION - The action performed. Examples include ``RunInstance`` and ``CreateBucket`` .
          * PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.
          * PURCHASE_TYPE - The reservation type of the purchase to which this usage is related. Examples include On-Demand Instances and Standard Reserved Instances.
          * SERVICE - The AWS service such as Amazon DynamoDB.
          * USAGE_TYPE - The type of usage. An example is DataTransfer-In-Bytes. The response for the ``GetDimensionValues`` operation includes a unit attribute. Examples include GB and Hrs.
          * USAGE_TYPE_GROUP - The grouping of common usage types. An example is Amazon EC2: CloudWatch – Alarms. The response for this operation includes a unit attribute.
          * RECORD_TYPE - The different types of charges such as RI fees, usage costs, tax refunds, and credits.
          If you set the context to ``RESERVATIONS`` , you can use the following dimensions for searching:
          * AZ - The Availability Zone. An example is ``us-east-1a`` .
          * CACHE_ENGINE - The Amazon ElastiCache operating system. Examples are Windows or Linux.
          * DEPLOYMENT_OPTION - The scope of Amazon Relational Database Service deployments. Valid values are ``SingleAZ`` and ``MultiAZ`` .
          * INSTANCE_TYPE - The type of Amazon EC2 instance. An example is ``m4.xlarge`` .
          * LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.
          * PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.
          * REGION - The AWS Region.
          * SCOPE (Utilization only) - The scope of a Reserved Instance (RI). Values are regional or a single Availability Zone.
          * TAG (Coverage only) - The tags that are associated with a Reserved Instance (RI).
          * TENANCY - The tenancy of a resource. Examples are shared or dedicated.
        :type NextPageToken: string
        :param NextPageToken:
          The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
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

    def get_reservation_coverage(self, TimePeriod: Dict, GroupBy: List = None, Granularity: str = None, Filter: Dict = None, Metrics: List = None, NextPageToken: str = None) -> Dict:
        """
        Retrieves the reservation coverage for your account. This enables you to see how much of your Amazon Elastic Compute Cloud, Amazon ElastiCache, Amazon Relational Database Service, or Amazon Redshift usage is covered by a reservation. An organization's master account can see the coverage of the associated member accounts. For any time period, you can filter data about reservation usage by the following dimensions:
        * AZ 
        * CACHE_ENGINE 
        * DATABASE_ENGINE 
        * DEPLOYMENT_OPTION 
        * INSTANCE_TYPE 
        * LINKED_ACCOUNT 
        * OPERATING_SYSTEM 
        * PLATFORM 
        * REGION 
        * SERVICE 
        * TAG 
        * TENANCY 
        To determine valid values for a dimension, use the ``GetDimensionValues`` operation. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetReservationCoverage>`_
        
        **Request Syntax**
        ::
          response = client.get_reservation_coverage(
              TimePeriod={
                  'Start': 'string',
                  'End': 'string'
              },
              GroupBy=[
                  {
                      'Type': 'DIMENSION'|'TAG',
                      'Key': 'string'
                  },
              ],
              Granularity='DAILY'|'MONTHLY'|'HOURLY',
              Filter={
                  'Or': [
                      {'... recursive ...'},
                  ],
                  'And': [
                      {'... recursive ...'},
                  ],
                  'Not': {'... recursive ...'},
                  'Dimensions': {
                      'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID',
                      'Values': [
                          'string',
                      ]
                  },
                  'Tags': {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  }
              },
              Metrics=[
                  'string',
              ],
              NextPageToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'CoveragesByTime': [
                    {
                        'TimePeriod': {
                            'Start': 'string',
                            'End': 'string'
                        },
                        'Groups': [
                            {
                                'Attributes': {
                                    'string': 'string'
                                },
                                'Coverage': {
                                    'CoverageHours': {
                                        'OnDemandHours': 'string',
                                        'ReservedHours': 'string',
                                        'TotalRunningHours': 'string',
                                        'CoverageHoursPercentage': 'string'
                                    },
                                    'CoverageNormalizedUnits': {
                                        'OnDemandNormalizedUnits': 'string',
                                        'ReservedNormalizedUnits': 'string',
                                        'TotalRunningNormalizedUnits': 'string',
                                        'CoverageNormalizedUnitsPercentage': 'string'
                                    },
                                    'CoverageCost': {
                                        'OnDemandCost': 'string'
                                    }
                                }
                            },
                        ],
                        'Total': {
                            'CoverageHours': {
                                'OnDemandHours': 'string',
                                'ReservedHours': 'string',
                                'TotalRunningHours': 'string',
                                'CoverageHoursPercentage': 'string'
                            },
                            'CoverageNormalizedUnits': {
                                'OnDemandNormalizedUnits': 'string',
                                'ReservedNormalizedUnits': 'string',
                                'TotalRunningNormalizedUnits': 'string',
                                'CoverageNormalizedUnitsPercentage': 'string'
                            },
                            'CoverageCost': {
                                'OnDemandCost': 'string'
                            }
                        }
                    },
                ],
                'Total': {
                    'CoverageHours': {
                        'OnDemandHours': 'string',
                        'ReservedHours': 'string',
                        'TotalRunningHours': 'string',
                        'CoverageHoursPercentage': 'string'
                    },
                    'CoverageNormalizedUnits': {
                        'OnDemandNormalizedUnits': 'string',
                        'ReservedNormalizedUnits': 'string',
                        'TotalRunningNormalizedUnits': 'string',
                        'CoverageNormalizedUnitsPercentage': 'string'
                    },
                    'CoverageCost': {
                        'OnDemandCost': 'string'
                    }
                },
                'NextPageToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CoveragesByTime** *(list) --* 
              The amount of time that your reservations covered.
              - *(dict) --* 
                Reservation coverage for a specified period, in hours.
                - **TimePeriod** *(dict) --* 
                  The period that this coverage was used over.
                  - **Start** *(string) --* 
                    The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data starting at ``2017-01-01`` up to the end date.
                  - **End** *(string) --* 
                    The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start date up to, but not including, ``2017-05-01`` .
                - **Groups** *(list) --* 
                  The groups of instances that the reservation covered.
                  - *(dict) --* 
                    A group of reservations that share a set of attributes.
                    - **Attributes** *(dict) --* 
                      The attributes for this group of reservations.
                      - *(string) --* 
                        - *(string) --* 
                    - **Coverage** *(dict) --* 
                      How much instance usage this group of reservations covered.
                      - **CoverageHours** *(dict) --* 
                        The amount of instance usage that the reservation covered, in hours.
                        - **OnDemandHours** *(string) --* 
                          The number of instance running hours that On-Demand Instances covered.
                        - **ReservedHours** *(string) --* 
                          The number of instance running hours that reservations covered.
                        - **TotalRunningHours** *(string) --* 
                          The total instance usage, in hours.
                        - **CoverageHoursPercentage** *(string) --* 
                          The percentage of instance hours that a reservation covered.
                      - **CoverageNormalizedUnits** *(dict) --* 
                        The amount of instance usage that the reservation covered, in normalized units.
                        - **OnDemandNormalizedUnits** *(string) --* 
                          The number of normalized units that are covered by On-Demand Instances instead of a reservation.
                        - **ReservedNormalizedUnits** *(string) --* 
                          The number of normalized units that a reservation covers.
                        - **TotalRunningNormalizedUnits** *(string) --* 
                          The total number of normalized units that you used.
                        - **CoverageNormalizedUnitsPercentage** *(string) --* 
                          The percentage of your used instance normalized units that a reservation covers.
                      - **CoverageCost** *(dict) --* 
                        The amount of cost that the reservation covered.
                        - **OnDemandCost** *(string) --* 
                          How much an On-Demand instance cost.
                - **Total** *(dict) --* 
                  The total reservation coverage, in hours.
                  - **CoverageHours** *(dict) --* 
                    The amount of instance usage that the reservation covered, in hours.
                    - **OnDemandHours** *(string) --* 
                      The number of instance running hours that On-Demand Instances covered.
                    - **ReservedHours** *(string) --* 
                      The number of instance running hours that reservations covered.
                    - **TotalRunningHours** *(string) --* 
                      The total instance usage, in hours.
                    - **CoverageHoursPercentage** *(string) --* 
                      The percentage of instance hours that a reservation covered.
                  - **CoverageNormalizedUnits** *(dict) --* 
                    The amount of instance usage that the reservation covered, in normalized units.
                    - **OnDemandNormalizedUnits** *(string) --* 
                      The number of normalized units that are covered by On-Demand Instances instead of a reservation.
                    - **ReservedNormalizedUnits** *(string) --* 
                      The number of normalized units that a reservation covers.
                    - **TotalRunningNormalizedUnits** *(string) --* 
                      The total number of normalized units that you used.
                    - **CoverageNormalizedUnitsPercentage** *(string) --* 
                      The percentage of your used instance normalized units that a reservation covers.
                  - **CoverageCost** *(dict) --* 
                    The amount of cost that the reservation covered.
                    - **OnDemandCost** *(string) --* 
                      How much an On-Demand instance cost.
            - **Total** *(dict) --* 
              The total amount of instance usage that a reservation covered.
              - **CoverageHours** *(dict) --* 
                The amount of instance usage that the reservation covered, in hours.
                - **OnDemandHours** *(string) --* 
                  The number of instance running hours that On-Demand Instances covered.
                - **ReservedHours** *(string) --* 
                  The number of instance running hours that reservations covered.
                - **TotalRunningHours** *(string) --* 
                  The total instance usage, in hours.
                - **CoverageHoursPercentage** *(string) --* 
                  The percentage of instance hours that a reservation covered.
              - **CoverageNormalizedUnits** *(dict) --* 
                The amount of instance usage that the reservation covered, in normalized units.
                - **OnDemandNormalizedUnits** *(string) --* 
                  The number of normalized units that are covered by On-Demand Instances instead of a reservation.
                - **ReservedNormalizedUnits** *(string) --* 
                  The number of normalized units that a reservation covers.
                - **TotalRunningNormalizedUnits** *(string) --* 
                  The total number of normalized units that you used.
                - **CoverageNormalizedUnitsPercentage** *(string) --* 
                  The percentage of your used instance normalized units that a reservation covers.
              - **CoverageCost** *(dict) --* 
                The amount of cost that the reservation covered.
                - **OnDemandCost** *(string) --* 
                  How much an On-Demand instance cost.
            - **NextPageToken** *(string) --* 
              The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.
        :type TimePeriod: dict
        :param TimePeriod: **[REQUIRED]**
          The start and end dates of the period that you want to retrieve data about reservation coverage for. You can retrieve data for a maximum of 13 months: the last 12 months and the current month. The start date is inclusive, but the end date is exclusive. For example, if ``start`` is ``2017-01-01`` and ``end`` is ``2017-05-01`` , then the cost and usage data is retrieved from ``2017-01-01`` up to and including ``2017-04-30`` but not including ``2017-05-01`` .
          - **Start** *(string) --* **[REQUIRED]**
            The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data starting at ``2017-01-01`` up to the end date.
          - **End** *(string) --* **[REQUIRED]**
            The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start date up to, but not including, ``2017-05-01`` .
        :type GroupBy: list
        :param GroupBy:
          You can group the data by the following attributes:
          * AZ
          * CACHE_ENGINE
          * DATABASE_ENGINE
          * DEPLOYMENT_OPTION
          * INSTANCE_TYPE
          * LINKED_ACCOUNT
          * OPERATING_SYSTEM
          * PLATFORM
          * REGION
          * TENANCY
          - *(dict) --*
            Represents a group when you specify a group by criteria or in the response to a query with a specific grouping.
            - **Type** *(string) --*
              The string that represents the type of group.
            - **Key** *(string) --*
              The string that represents a key for a specified group.
        :type Granularity: string
        :param Granularity:
          The granularity of the AWS cost data for the reservation. Valid values are ``MONTHLY`` and ``DAILY`` .
          If ``GroupBy`` is set, ``Granularity`` can\'t be set. If ``Granularity`` isn\'t set, the response object doesn\'t include ``Granularity`` , either ``MONTHLY`` or ``DAILY`` .
          The ``GetReservationCoverage`` operation supports only ``DAILY`` and ``MONTHLY`` granularities.
        :type Filter: dict
        :param Filter:
          Filters utilization data by dimensions. You can filter by the following dimensions:
          * AZ
          * CACHE_ENGINE
          * DATABASE_ENGINE
          * DEPLOYMENT_OPTION
          * INSTANCE_TYPE
          * LINKED_ACCOUNT
          * OPERATING_SYSTEM
          * PLATFORM
          * REGION
          * SERVICE
          * TAG
          * TENANCY
           ``GetReservationCoverage`` uses the same `Expression <http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html>`__ object as the other operations, but only ``AND`` is supported among each dimension. You can nest only one level deep. If there are multiple values for a dimension, they are OR\'d together.
          If you don\'t provide a ``SERVICE`` filter, Cost Explorer defaults to EC2.
          - **Or** *(list) --*
            Return results that match either ``Dimension`` object.
            - *(dict) --*
              Use ``Expression`` to filter by cost or by usage. There are two patterns:
              * Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for ``INSTANCE_TYPE==m4.xlarge OR INSTANCE_TYPE==c4.large`` . The ``Expression`` for that looks like this:  ``{ \"Dimensions\": { \"Key\": \"INSTANCE_TYPE\", \"Values\": [ \"m4.xlarge\", “c4.large” ] } }``   The list of dimension values are OR\'d together to retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects using either ``with*`` methods or ``set*`` methods in multiple lines.
              * Compound dimension values with logical operations - You can use multiple ``Expression`` types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression`` objects. This allows you to filter on more advanced options. For example, you can filter on ``((INSTANCE_TYPE == m4.large OR INSTANCE_TYPE == m3.large) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ \"And\": [ {\"Or\": [ {\"Dimensions\": { \"Key\": \"INSTANCE_TYPE\", \"Values\": [ \"m4.x.large\", \"c4.large\" ] }}, {\"Tags\": { \"Key\": \"TagName\", \"Values\": [\"Value1\"] } } ]}, {\"Not\": {\"Dimensions\": { \"Key\": \"USAGE_TYPE\", \"Values\": [\"DataTransfer\"] }}} ] }``
              .. note::
                 Because each ``Expression`` can have only one operator, the service returns an error if more than one is specified. The following example shows an ``Expression`` object that creates an error.
                ``{ \"And\": [ ... ], \"DimensionValues\": { \"Dimension\": \"USAGE_TYPE\", \"Values\": [ \"DataTransfer\" ] } }``
          - **And** *(list) --*
            Return results that match both ``Dimension`` objects.
            - *(dict) --*
              Use ``Expression`` to filter by cost or by usage. There are two patterns:
              * Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for ``INSTANCE_TYPE==m4.xlarge OR INSTANCE_TYPE==c4.large`` . The ``Expression`` for that looks like this:  ``{ \"Dimensions\": { \"Key\": \"INSTANCE_TYPE\", \"Values\": [ \"m4.xlarge\", “c4.large” ] } }``   The list of dimension values are OR\'d together to retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects using either ``with*`` methods or ``set*`` methods in multiple lines.
              * Compound dimension values with logical operations - You can use multiple ``Expression`` types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression`` objects. This allows you to filter on more advanced options. For example, you can filter on ``((INSTANCE_TYPE == m4.large OR INSTANCE_TYPE == m3.large) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ \"And\": [ {\"Or\": [ {\"Dimensions\": { \"Key\": \"INSTANCE_TYPE\", \"Values\": [ \"m4.x.large\", \"c4.large\" ] }}, {\"Tags\": { \"Key\": \"TagName\", \"Values\": [\"Value1\"] } } ]}, {\"Not\": {\"Dimensions\": { \"Key\": \"USAGE_TYPE\", \"Values\": [\"DataTransfer\"] }}} ] }``
              .. note::
                 Because each ``Expression`` can have only one operator, the service returns an error if more than one is specified. The following example shows an ``Expression`` object that creates an error.
                ``{ \"And\": [ ... ], \"DimensionValues\": { \"Dimension\": \"USAGE_TYPE\", \"Values\": [ \"DataTransfer\" ] } }``
          - **Not** *(dict) --*
            Return results that don\'t match a ``Dimension`` object.
          - **Dimensions** *(dict) --*
            The specific ``Dimension`` to use for ``Expression`` .
            - **Key** *(string) --*
              The names of the metadata types that you can use to filter and group your results. For example, ``AZ`` returns a list of Availability Zones.
            - **Values** *(list) --*
              The metadata values that you can use to filter and group your results. You can use ``GetDimensionValues`` to find specific values.
              Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` , ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and ``Amazon Relational Database Service`` .
              - *(string) --*
          - **Tags** *(dict) --*
            The specific ``Tag`` to use for ``Expression`` .
            - **Key** *(string) --*
              The key for the tag.
            - **Values** *(list) --*
              The specific value of the tag.
              - *(string) --*
        :type Metrics: list
        :param Metrics:
          The measurement that you want your reservation coverage reported in.
          Valid values are ``Hour`` , ``Unit`` , and ``Cost`` . You can use multiple values in a request.
          - *(string) --*
        :type NextPageToken: string
        :param NextPageToken:
          The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
        :rtype: dict
        :returns:
        """
        pass

    def get_reservation_purchase_recommendation(self, Service: str, AccountId: str = None, AccountScope: str = None, LookbackPeriodInDays: str = None, TermInYears: str = None, PaymentOption: str = None, ServiceSpecification: Dict = None, PageSize: int = None, NextPageToken: str = None) -> Dict:
        """
        Gets recommendations for which reservations to purchase. These recommendations could help you reduce your costs. Reservations provide a discounted hourly rate (up to 75%) compared to On-Demand pricing.
        AWS generates your recommendations by identifying your On-Demand usage during a specific time period and collecting your usage into categories that are eligible for a reservation. After AWS has these categories, it simulates every combination of reservations in each category of usage to identify the best number of each type of RI to purchase to maximize your estimated savings. 
        For example, AWS automatically aggregates your Amazon EC2 Linux, shared tenancy, and c4 family usage in the US West (Oregon) Region and recommends that you buy size-flexible regional reservations to apply to the c4 family usage. AWS recommends the smallest size instance in an instance family. This makes it easier to purchase a size-flexible RI. AWS also shows the equal number of normalized units so that you can purchase any instance size that you want. For this example, your RI recommendation would be for ``c4.large`` because that is the smallest size instance in the c4 instance family.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetReservationPurchaseRecommendation>`_
        
        **Request Syntax**
        ::
          response = client.get_reservation_purchase_recommendation(
              AccountId='string',
              Service='string',
              AccountScope='PAYER'|'LINKED',
              LookbackPeriodInDays='SEVEN_DAYS'|'THIRTY_DAYS'|'SIXTY_DAYS',
              TermInYears='ONE_YEAR'|'THREE_YEARS',
              PaymentOption='NO_UPFRONT'|'PARTIAL_UPFRONT'|'ALL_UPFRONT'|'LIGHT_UTILIZATION'|'MEDIUM_UTILIZATION'|'HEAVY_UTILIZATION',
              ServiceSpecification={
                  'EC2Specification': {
                      'OfferingClass': 'STANDARD'|'CONVERTIBLE'
                  }
              },
              PageSize=123,
              NextPageToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Metadata': {
                    'RecommendationId': 'string',
                    'GenerationTimestamp': 'string'
                },
                'Recommendations': [
                    {
                        'AccountScope': 'PAYER'|'LINKED',
                        'LookbackPeriodInDays': 'SEVEN_DAYS'|'THIRTY_DAYS'|'SIXTY_DAYS',
                        'TermInYears': 'ONE_YEAR'|'THREE_YEARS',
                        'PaymentOption': 'NO_UPFRONT'|'PARTIAL_UPFRONT'|'ALL_UPFRONT'|'LIGHT_UTILIZATION'|'MEDIUM_UTILIZATION'|'HEAVY_UTILIZATION',
                        'ServiceSpecification': {
                            'EC2Specification': {
                                'OfferingClass': 'STANDARD'|'CONVERTIBLE'
                            }
                        },
                        'RecommendationDetails': [
                            {
                                'AccountId': 'string',
                                'InstanceDetails': {
                                    'EC2InstanceDetails': {
                                        'Family': 'string',
                                        'InstanceType': 'string',
                                        'Region': 'string',
                                        'AvailabilityZone': 'string',
                                        'Platform': 'string',
                                        'Tenancy': 'string',
                                        'CurrentGeneration': True|False,
                                        'SizeFlexEligible': True|False
                                    },
                                    'RDSInstanceDetails': {
                                        'Family': 'string',
                                        'InstanceType': 'string',
                                        'Region': 'string',
                                        'DatabaseEngine': 'string',
                                        'DatabaseEdition': 'string',
                                        'DeploymentOption': 'string',
                                        'LicenseModel': 'string',
                                        'CurrentGeneration': True|False,
                                        'SizeFlexEligible': True|False
                                    },
                                    'RedshiftInstanceDetails': {
                                        'Family': 'string',
                                        'NodeType': 'string',
                                        'Region': 'string',
                                        'CurrentGeneration': True|False,
                                        'SizeFlexEligible': True|False
                                    },
                                    'ElastiCacheInstanceDetails': {
                                        'Family': 'string',
                                        'NodeType': 'string',
                                        'Region': 'string',
                                        'ProductDescription': 'string',
                                        'CurrentGeneration': True|False,
                                        'SizeFlexEligible': True|False
                                    },
                                    'ESInstanceDetails': {
                                        'InstanceClass': 'string',
                                        'InstanceSize': 'string',
                                        'Region': 'string',
                                        'CurrentGeneration': True|False,
                                        'SizeFlexEligible': True|False
                                    }
                                },
                                'RecommendedNumberOfInstancesToPurchase': 'string',
                                'RecommendedNormalizedUnitsToPurchase': 'string',
                                'MinimumNumberOfInstancesUsedPerHour': 'string',
                                'MinimumNormalizedUnitsUsedPerHour': 'string',
                                'MaximumNumberOfInstancesUsedPerHour': 'string',
                                'MaximumNormalizedUnitsUsedPerHour': 'string',
                                'AverageNumberOfInstancesUsedPerHour': 'string',
                                'AverageNormalizedUnitsUsedPerHour': 'string',
                                'AverageUtilization': 'string',
                                'EstimatedBreakEvenInMonths': 'string',
                                'CurrencyCode': 'string',
                                'EstimatedMonthlySavingsAmount': 'string',
                                'EstimatedMonthlySavingsPercentage': 'string',
                                'EstimatedMonthlyOnDemandCost': 'string',
                                'EstimatedReservationCostForLookbackPeriod': 'string',
                                'UpfrontCost': 'string',
                                'RecurringStandardMonthlyCost': 'string'
                            },
                        ],
                        'RecommendationSummary': {
                            'TotalEstimatedMonthlySavingsAmount': 'string',
                            'TotalEstimatedMonthlySavingsPercentage': 'string',
                            'CurrencyCode': 'string'
                        }
                    },
                ],
                'NextPageToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Metadata** *(dict) --* 
              Information about this specific recommendation call, such as the time stamp for when Cost Explorer generated this recommendation.
              - **RecommendationId** *(string) --* 
                The ID for this specific recommendation.
              - **GenerationTimestamp** *(string) --* 
                The time stamp for when AWS made this recommendation.
            - **Recommendations** *(list) --* 
              Recommendations for reservations to purchase.
              - *(dict) --* 
                A specific reservation that AWS recommends for purchase.
                - **AccountScope** *(string) --* 
                  The account scope that AWS recommends that you purchase this instance for. For example, you can purchase this reservation for an entire organization in AWS Organizations.
                - **LookbackPeriodInDays** *(string) --* 
                  How many days of previous usage that AWS considers when making this recommendation.
                - **TermInYears** *(string) --* 
                  The term of the reservation that you want recommendations for, in years.
                - **PaymentOption** *(string) --* 
                  The payment option for the reservation. For example, ``AllUpfront`` or ``NoUpfront`` .
                - **ServiceSpecification** *(dict) --* 
                  Hardware specifications for the service that you want recommendations for.
                  - **EC2Specification** *(dict) --* 
                    The Amazon EC2 hardware specifications that you want AWS to provide recommendations for.
                    - **OfferingClass** *(string) --* 
                      Whether you want a recommendation for standard or convertible reservations.
                - **RecommendationDetails** *(list) --* 
                  Details about the recommended purchases.
                  - *(dict) --* 
                    Details about your recommended reservation purchase.
                    - **AccountId** *(string) --* 
                      The account that this RI recommendation is for.
                    - **InstanceDetails** *(dict) --* 
                      Details about the instances that AWS recommends that you purchase.
                      - **EC2InstanceDetails** *(dict) --* 
                        The Amazon EC2 instances that AWS recommends that you purchase.
                        - **Family** *(string) --* 
                          The instance family of the recommended reservation.
                        - **InstanceType** *(string) --* 
                          The type of instance that AWS recommends.
                        - **Region** *(string) --* 
                          The AWS Region of the recommended reservation.
                        - **AvailabilityZone** *(string) --* 
                          The Availability Zone of the recommended reservation.
                        - **Platform** *(string) --* 
                          The platform of the recommended reservation. The platform is the specific combination of operating system, license model, and software on an instance.
                        - **Tenancy** *(string) --* 
                          Whether the recommended reservation is dedicated or shared.
                        - **CurrentGeneration** *(boolean) --* 
                          Whether the recommendation is for a current-generation instance. 
                        - **SizeFlexEligible** *(boolean) --* 
                          Whether the recommended reservation is size flexible.
                      - **RDSInstanceDetails** *(dict) --* 
                        The Amazon RDS instances that AWS recommends that you purchase.
                        - **Family** *(string) --* 
                          The instance family of the recommended reservation.
                        - **InstanceType** *(string) --* 
                          The type of instance that AWS recommends.
                        - **Region** *(string) --* 
                          The AWS Region of the recommended reservation.
                        - **DatabaseEngine** *(string) --* 
                          The database engine that the recommended reservation supports.
                        - **DatabaseEdition** *(string) --* 
                          The database edition that the recommended reservation supports.
                        - **DeploymentOption** *(string) --* 
                          Whether the recommendation is for a reservation in a single Availability Zone or a reservation with a backup in a second Availability Zone.
                        - **LicenseModel** *(string) --* 
                          The license model that the recommended reservation supports.
                        - **CurrentGeneration** *(boolean) --* 
                          Whether the recommendation is for a current-generation instance. 
                        - **SizeFlexEligible** *(boolean) --* 
                          Whether the recommended reservation is size flexible.
                      - **RedshiftInstanceDetails** *(dict) --* 
                        The Amazon Redshift instances that AWS recommends that you purchase.
                        - **Family** *(string) --* 
                          The instance family of the recommended reservation.
                        - **NodeType** *(string) --* 
                          The type of node that AWS recommends.
                        - **Region** *(string) --* 
                          The AWS Region of the recommended reservation.
                        - **CurrentGeneration** *(boolean) --* 
                          Whether the recommendation is for a current-generation instance.
                        - **SizeFlexEligible** *(boolean) --* 
                          Whether the recommended reservation is size flexible.
                      - **ElastiCacheInstanceDetails** *(dict) --* 
                        The ElastiCache instances that AWS recommends that you purchase.
                        - **Family** *(string) --* 
                          The instance family of the recommended reservation.
                        - **NodeType** *(string) --* 
                          The type of node that AWS recommends.
                        - **Region** *(string) --* 
                          The AWS Region of the recommended reservation.
                        - **ProductDescription** *(string) --* 
                          The description of the recommended reservation.
                        - **CurrentGeneration** *(boolean) --* 
                          Whether the recommendation is for a current generation instance.
                        - **SizeFlexEligible** *(boolean) --* 
                          Whether the recommended reservation is size flexible.
                      - **ESInstanceDetails** *(dict) --* 
                        The Amazon ES instances that AWS recommends that you purchase.
                        - **InstanceClass** *(string) --* 
                          The class of instance that AWS recommends.
                        - **InstanceSize** *(string) --* 
                          The size of instance that AWS recommends.
                        - **Region** *(string) --* 
                          The AWS Region of the recommended reservation.
                        - **CurrentGeneration** *(boolean) --* 
                          Whether the recommendation is for a current-generation instance.
                        - **SizeFlexEligible** *(boolean) --* 
                          Whether the recommended reservation is size flexible.
                    - **RecommendedNumberOfInstancesToPurchase** *(string) --* 
                      The number of instances that AWS recommends that you purchase.
                    - **RecommendedNormalizedUnitsToPurchase** *(string) --* 
                      The number of normalized units that AWS recommends that you purchase.
                    - **MinimumNumberOfInstancesUsedPerHour** *(string) --* 
                      The minimum number of instances that you used in an hour during the historical period. AWS uses this to calculate your recommended reservation purchases.
                    - **MinimumNormalizedUnitsUsedPerHour** *(string) --* 
                      The minimum number of normalized units that you used in an hour during the historical period. AWS uses this to calculate your recommended reservation purchases.
                    - **MaximumNumberOfInstancesUsedPerHour** *(string) --* 
                      The maximum number of instances that you used in an hour during the historical period. AWS uses this to calculate your recommended reservation purchases.
                    - **MaximumNormalizedUnitsUsedPerHour** *(string) --* 
                      The maximum number of normalized units that you used in an hour during the historical period. AWS uses this to calculate your recommended reservation purchases.
                    - **AverageNumberOfInstancesUsedPerHour** *(string) --* 
                      The average number of instances that you used in an hour during the historical period. AWS uses this to calculate your recommended reservation purchases.
                    - **AverageNormalizedUnitsUsedPerHour** *(string) --* 
                      The average number of normalized units that you used in an hour during the historical period. AWS uses this to calculate your recommended reservation purchases.
                    - **AverageUtilization** *(string) --* 
                      The average utilization of your instances. AWS uses this to calculate your recommended reservation purchases.
                    - **EstimatedBreakEvenInMonths** *(string) --* 
                      How long AWS estimates that it takes for this instance to start saving you money, in months.
                    - **CurrencyCode** *(string) --* 
                      The currency code that AWS used to calculate the costs for this instance.
                    - **EstimatedMonthlySavingsAmount** *(string) --* 
                      How much AWS estimates that this specific recommendation could save you in a month.
                    - **EstimatedMonthlySavingsPercentage** *(string) --* 
                      How much AWS estimates that this specific recommendation could save you in a month, as a percentage of your overall costs.
                    - **EstimatedMonthlyOnDemandCost** *(string) --* 
                      How much AWS estimates that you spend on On-Demand Instances in a month.
                    - **EstimatedReservationCostForLookbackPeriod** *(string) --* 
                      How much AWS estimates that you would have spent for all usage during the specified historical period if you had had a reservation.
                    - **UpfrontCost** *(string) --* 
                      How much purchasing this instance costs you upfront.
                    - **RecurringStandardMonthlyCost** *(string) --* 
                      How much purchasing this instance costs you on a monthly basis.
                - **RecommendationSummary** *(dict) --* 
                  A summary about the recommended purchase.
                  - **TotalEstimatedMonthlySavingsAmount** *(string) --* 
                    The total amount that AWS estimates that this recommendation could save you in a month.
                  - **TotalEstimatedMonthlySavingsPercentage** *(string) --* 
                    The total amount that AWS estimates that this recommendation could save you in a month, as a percentage of your costs.
                  - **CurrencyCode** *(string) --* 
                    The currency code used for this recommendation.
            - **NextPageToken** *(string) --* 
              The pagination token for the next set of retrievable results.
        :type AccountId: string
        :param AccountId:
          The account ID that is associated with the recommendation.
        :type Service: string
        :param Service: **[REQUIRED]**
          The specific service that you want recommendations for.
        :type AccountScope: string
        :param AccountScope:
          The account scope that you want recommendations for. ``PAYER`` means that AWS includes the master account and any member accounts when it calculates its recommendations. ``LINKED`` means that AWS includes only member accounts when it calculates its recommendations.
          Valid values are ``PAYER`` and ``LINKED`` .
        :type LookbackPeriodInDays: string
        :param LookbackPeriodInDays:
          The number of previous days that you want AWS to consider when it calculates your recommendations.
        :type TermInYears: string
        :param TermInYears:
          The reservation term that you want recommendations for.
        :type PaymentOption: string
        :param PaymentOption:
          The reservation purchase option that you want recommendations for.
        :type ServiceSpecification: dict
        :param ServiceSpecification:
          The hardware specifications for the service instances that you want recommendations for, such as standard or convertible Amazon EC2 instances.
          - **EC2Specification** *(dict) --*
            The Amazon EC2 hardware specifications that you want AWS to provide recommendations for.
            - **OfferingClass** *(string) --*
              Whether you want a recommendation for standard or convertible reservations.
        :type PageSize: integer
        :param PageSize:
          The number of recommendations that you want returned in a single response object.
        :type NextPageToken: string
        :param NextPageToken:
          The pagination token that indicates the next set of results that you want to retrieve.
        :rtype: dict
        :returns:
        """
        pass

    def get_reservation_utilization(self, TimePeriod: Dict, GroupBy: List = None, Granularity: str = None, Filter: Dict = None, NextPageToken: str = None) -> Dict:
        """
        Retrieves the reservation utilization for your account. Master accounts in an organization have access to member accounts. You can filter data by dimensions in a time period. You can use ``GetDimensionValues`` to determine the possible dimension values. Currently, you can group only by ``SUBSCRIPTION_ID`` . 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetReservationUtilization>`_
        
        **Request Syntax**
        ::
          response = client.get_reservation_utilization(
              TimePeriod={
                  'Start': 'string',
                  'End': 'string'
              },
              GroupBy=[
                  {
                      'Type': 'DIMENSION'|'TAG',
                      'Key': 'string'
                  },
              ],
              Granularity='DAILY'|'MONTHLY'|'HOURLY',
              Filter={
                  'Or': [
                      {'... recursive ...'},
                  ],
                  'And': [
                      {'... recursive ...'},
                  ],
                  'Not': {'... recursive ...'},
                  'Dimensions': {
                      'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID',
                      'Values': [
                          'string',
                      ]
                  },
                  'Tags': {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  }
              },
              NextPageToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'UtilizationsByTime': [
                    {
                        'TimePeriod': {
                            'Start': 'string',
                            'End': 'string'
                        },
                        'Groups': [
                            {
                                'Key': 'string',
                                'Value': 'string',
                                'Attributes': {
                                    'string': 'string'
                                },
                                'Utilization': {
                                    'UtilizationPercentage': 'string',
                                    'UtilizationPercentageInUnits': 'string',
                                    'PurchasedHours': 'string',
                                    'PurchasedUnits': 'string',
                                    'TotalActualHours': 'string',
                                    'TotalActualUnits': 'string',
                                    'UnusedHours': 'string',
                                    'UnusedUnits': 'string',
                                    'OnDemandCostOfRIHoursUsed': 'string',
                                    'NetRISavings': 'string',
                                    'TotalPotentialRISavings': 'string',
                                    'AmortizedUpfrontFee': 'string',
                                    'AmortizedRecurringFee': 'string',
                                    'TotalAmortizedFee': 'string'
                                }
                            },
                        ],
                        'Total': {
                            'UtilizationPercentage': 'string',
                            'UtilizationPercentageInUnits': 'string',
                            'PurchasedHours': 'string',
                            'PurchasedUnits': 'string',
                            'TotalActualHours': 'string',
                            'TotalActualUnits': 'string',
                            'UnusedHours': 'string',
                            'UnusedUnits': 'string',
                            'OnDemandCostOfRIHoursUsed': 'string',
                            'NetRISavings': 'string',
                            'TotalPotentialRISavings': 'string',
                            'AmortizedUpfrontFee': 'string',
                            'AmortizedRecurringFee': 'string',
                            'TotalAmortizedFee': 'string'
                        }
                    },
                ],
                'Total': {
                    'UtilizationPercentage': 'string',
                    'UtilizationPercentageInUnits': 'string',
                    'PurchasedHours': 'string',
                    'PurchasedUnits': 'string',
                    'TotalActualHours': 'string',
                    'TotalActualUnits': 'string',
                    'UnusedHours': 'string',
                    'UnusedUnits': 'string',
                    'OnDemandCostOfRIHoursUsed': 'string',
                    'NetRISavings': 'string',
                    'TotalPotentialRISavings': 'string',
                    'AmortizedUpfrontFee': 'string',
                    'AmortizedRecurringFee': 'string',
                    'TotalAmortizedFee': 'string'
                },
                'NextPageToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **UtilizationsByTime** *(list) --* 
              The amount of time that you used your RIs.
              - *(dict) --* 
                The amount of utilization, in hours.
                - **TimePeriod** *(dict) --* 
                  The period of time that this utilization was used for.
                  - **Start** *(string) --* 
                    The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data starting at ``2017-01-01`` up to the end date.
                  - **End** *(string) --* 
                    The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start date up to, but not including, ``2017-05-01`` .
                - **Groups** *(list) --* 
                  The groups that this utilization result uses.
                  - *(dict) --* 
                    A group of reservations that share a set of attributes.
                    - **Key** *(string) --* 
                      The key for a specific reservation attribute.
                    - **Value** *(string) --* 
                      The value of a specific reservation attribute.
                    - **Attributes** *(dict) --* 
                      The attributes for this group of reservations.
                      - *(string) --* 
                        - *(string) --* 
                    - **Utilization** *(dict) --* 
                      How much you used this group of reservations.
                      - **UtilizationPercentage** *(string) --* 
                        The percentage of reservation time that you used.
                      - **UtilizationPercentageInUnits** *(string) --* 
                        The percentage of Amazon EC2 reservation time that you used, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.
                      - **PurchasedHours** *(string) --* 
                        How many reservation hours that you purchased.
                      - **PurchasedUnits** *(string) --* 
                        How many Amazon EC2 reservation hours that you purchased, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.
                      - **TotalActualHours** *(string) --* 
                        The total number of reservation hours that you used.
                      - **TotalActualUnits** *(string) --* 
                        The total number of Amazon EC2 reservation hours that you used, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.
                      - **UnusedHours** *(string) --* 
                        The number of reservation hours that you didn't use.
                      - **UnusedUnits** *(string) --* 
                        The number of Amazon EC2 reservation hours that you didn't use, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.
                      - **OnDemandCostOfRIHoursUsed** *(string) --* 
                        How much your reservation would cost if charged On-Demand rates.
                      - **NetRISavings** *(string) --* 
                        How much you saved due to purchasing and utilizing reservation. AWS calculates this by subtracting ``TotalAmortizedFee`` from ``OnDemandCostOfRIHoursUsed`` .
                      - **TotalPotentialRISavings** *(string) --* 
                        How much you could save if you use your entire reservation.
                      - **AmortizedUpfrontFee** *(string) --* 
                        The upfront cost of your reservation, amortized over the reservation period.
                      - **AmortizedRecurringFee** *(string) --* 
                        The monthly cost of your reservation, amortized over the reservation period.
                      - **TotalAmortizedFee** *(string) --* 
                        The total cost of your reservation, amortized over the reservation period.
                - **Total** *(dict) --* 
                  The total number of reservation hours that were used.
                  - **UtilizationPercentage** *(string) --* 
                    The percentage of reservation time that you used.
                  - **UtilizationPercentageInUnits** *(string) --* 
                    The percentage of Amazon EC2 reservation time that you used, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.
                  - **PurchasedHours** *(string) --* 
                    How many reservation hours that you purchased.
                  - **PurchasedUnits** *(string) --* 
                    How many Amazon EC2 reservation hours that you purchased, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.
                  - **TotalActualHours** *(string) --* 
                    The total number of reservation hours that you used.
                  - **TotalActualUnits** *(string) --* 
                    The total number of Amazon EC2 reservation hours that you used, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.
                  - **UnusedHours** *(string) --* 
                    The number of reservation hours that you didn't use.
                  - **UnusedUnits** *(string) --* 
                    The number of Amazon EC2 reservation hours that you didn't use, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.
                  - **OnDemandCostOfRIHoursUsed** *(string) --* 
                    How much your reservation would cost if charged On-Demand rates.
                  - **NetRISavings** *(string) --* 
                    How much you saved due to purchasing and utilizing reservation. AWS calculates this by subtracting ``TotalAmortizedFee`` from ``OnDemandCostOfRIHoursUsed`` .
                  - **TotalPotentialRISavings** *(string) --* 
                    How much you could save if you use your entire reservation.
                  - **AmortizedUpfrontFee** *(string) --* 
                    The upfront cost of your reservation, amortized over the reservation period.
                  - **AmortizedRecurringFee** *(string) --* 
                    The monthly cost of your reservation, amortized over the reservation period.
                  - **TotalAmortizedFee** *(string) --* 
                    The total cost of your reservation, amortized over the reservation period.
            - **Total** *(dict) --* 
              The total amount of time that you used your RIs.
              - **UtilizationPercentage** *(string) --* 
                The percentage of reservation time that you used.
              - **UtilizationPercentageInUnits** *(string) --* 
                The percentage of Amazon EC2 reservation time that you used, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.
              - **PurchasedHours** *(string) --* 
                How many reservation hours that you purchased.
              - **PurchasedUnits** *(string) --* 
                How many Amazon EC2 reservation hours that you purchased, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.
              - **TotalActualHours** *(string) --* 
                The total number of reservation hours that you used.
              - **TotalActualUnits** *(string) --* 
                The total number of Amazon EC2 reservation hours that you used, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.
              - **UnusedHours** *(string) --* 
                The number of reservation hours that you didn't use.
              - **UnusedUnits** *(string) --* 
                The number of Amazon EC2 reservation hours that you didn't use, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.
              - **OnDemandCostOfRIHoursUsed** *(string) --* 
                How much your reservation would cost if charged On-Demand rates.
              - **NetRISavings** *(string) --* 
                How much you saved due to purchasing and utilizing reservation. AWS calculates this by subtracting ``TotalAmortizedFee`` from ``OnDemandCostOfRIHoursUsed`` .
              - **TotalPotentialRISavings** *(string) --* 
                How much you could save if you use your entire reservation.
              - **AmortizedUpfrontFee** *(string) --* 
                The upfront cost of your reservation, amortized over the reservation period.
              - **AmortizedRecurringFee** *(string) --* 
                The monthly cost of your reservation, amortized over the reservation period.
              - **TotalAmortizedFee** *(string) --* 
                The total cost of your reservation, amortized over the reservation period.
            - **NextPageToken** *(string) --* 
              The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.
        :type TimePeriod: dict
        :param TimePeriod: **[REQUIRED]**
          Sets the start and end dates for retrieving RI utilization. The start date is inclusive, but the end date is exclusive. For example, if ``start`` is ``2017-01-01`` and ``end`` is ``2017-05-01`` , then the cost and usage data is retrieved from ``2017-01-01`` up to and including ``2017-04-30`` but not including ``2017-05-01`` .
          - **Start** *(string) --* **[REQUIRED]**
            The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data starting at ``2017-01-01`` up to the end date.
          - **End** *(string) --* **[REQUIRED]**
            The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start date up to, but not including, ``2017-05-01`` .
        :type GroupBy: list
        :param GroupBy:
          Groups only by ``SUBSCRIPTION_ID`` . Metadata is included.
          - *(dict) --*
            Represents a group when you specify a group by criteria or in the response to a query with a specific grouping.
            - **Type** *(string) --*
              The string that represents the type of group.
            - **Key** *(string) --*
              The string that represents a key for a specified group.
        :type Granularity: string
        :param Granularity:
          If ``GroupBy`` is set, ``Granularity`` can\'t be set. If ``Granularity`` isn\'t set, the response object doesn\'t include ``Granularity`` , either ``MONTHLY`` or ``DAILY`` . If both ``GroupBy`` and ``Granularity`` aren\'t set, ``GetReservationUtilization`` defaults to ``DAILY`` .
          The ``GetReservationUtilization`` operation supports only ``DAILY`` and ``MONTHLY`` granularities.
        :type Filter: dict
        :param Filter:
          Filters utilization data by dimensions. You can filter by the following dimensions:
          * AZ
          * CACHE_ENGINE
          * DATABASE_ENGINE
          * DEPLOYMENT_OPTION
          * INSTANCE_TYPE
          * LINKED_ACCOUNT
          * OPERATING_SYSTEM
          * PLATFORM
          * REGION
          * SERVICE
          * SCOPE
          * TENANCY
           ``GetReservationUtilization`` uses the same `Expression <http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html>`__ object as the other operations, but only ``AND`` is supported among each dimension, and nesting is supported up to only one level deep. If there are multiple values for a dimension, they are OR\'d together.
          - **Or** *(list) --*
            Return results that match either ``Dimension`` object.
            - *(dict) --*
              Use ``Expression`` to filter by cost or by usage. There are two patterns:
              * Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for ``INSTANCE_TYPE==m4.xlarge OR INSTANCE_TYPE==c4.large`` . The ``Expression`` for that looks like this:  ``{ \"Dimensions\": { \"Key\": \"INSTANCE_TYPE\", \"Values\": [ \"m4.xlarge\", “c4.large” ] } }``   The list of dimension values are OR\'d together to retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects using either ``with*`` methods or ``set*`` methods in multiple lines.
              * Compound dimension values with logical operations - You can use multiple ``Expression`` types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression`` objects. This allows you to filter on more advanced options. For example, you can filter on ``((INSTANCE_TYPE == m4.large OR INSTANCE_TYPE == m3.large) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ \"And\": [ {\"Or\": [ {\"Dimensions\": { \"Key\": \"INSTANCE_TYPE\", \"Values\": [ \"m4.x.large\", \"c4.large\" ] }}, {\"Tags\": { \"Key\": \"TagName\", \"Values\": [\"Value1\"] } } ]}, {\"Not\": {\"Dimensions\": { \"Key\": \"USAGE_TYPE\", \"Values\": [\"DataTransfer\"] }}} ] }``
              .. note::
                 Because each ``Expression`` can have only one operator, the service returns an error if more than one is specified. The following example shows an ``Expression`` object that creates an error.
                ``{ \"And\": [ ... ], \"DimensionValues\": { \"Dimension\": \"USAGE_TYPE\", \"Values\": [ \"DataTransfer\" ] } }``
          - **And** *(list) --*
            Return results that match both ``Dimension`` objects.
            - *(dict) --*
              Use ``Expression`` to filter by cost or by usage. There are two patterns:
              * Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for ``INSTANCE_TYPE==m4.xlarge OR INSTANCE_TYPE==c4.large`` . The ``Expression`` for that looks like this:  ``{ \"Dimensions\": { \"Key\": \"INSTANCE_TYPE\", \"Values\": [ \"m4.xlarge\", “c4.large” ] } }``   The list of dimension values are OR\'d together to retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects using either ``with*`` methods or ``set*`` methods in multiple lines.
              * Compound dimension values with logical operations - You can use multiple ``Expression`` types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression`` objects. This allows you to filter on more advanced options. For example, you can filter on ``((INSTANCE_TYPE == m4.large OR INSTANCE_TYPE == m3.large) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ \"And\": [ {\"Or\": [ {\"Dimensions\": { \"Key\": \"INSTANCE_TYPE\", \"Values\": [ \"m4.x.large\", \"c4.large\" ] }}, {\"Tags\": { \"Key\": \"TagName\", \"Values\": [\"Value1\"] } } ]}, {\"Not\": {\"Dimensions\": { \"Key\": \"USAGE_TYPE\", \"Values\": [\"DataTransfer\"] }}} ] }``
              .. note::
                 Because each ``Expression`` can have only one operator, the service returns an error if more than one is specified. The following example shows an ``Expression`` object that creates an error.
                ``{ \"And\": [ ... ], \"DimensionValues\": { \"Dimension\": \"USAGE_TYPE\", \"Values\": [ \"DataTransfer\" ] } }``
          - **Not** *(dict) --*
            Return results that don\'t match a ``Dimension`` object.
          - **Dimensions** *(dict) --*
            The specific ``Dimension`` to use for ``Expression`` .
            - **Key** *(string) --*
              The names of the metadata types that you can use to filter and group your results. For example, ``AZ`` returns a list of Availability Zones.
            - **Values** *(list) --*
              The metadata values that you can use to filter and group your results. You can use ``GetDimensionValues`` to find specific values.
              Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` , ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and ``Amazon Relational Database Service`` .
              - *(string) --*
          - **Tags** *(dict) --*
            The specific ``Tag`` to use for ``Expression`` .
            - **Key** *(string) --*
              The key for the tag.
            - **Values** *(list) --*
              The specific value of the tag.
              - *(string) --*
        :type NextPageToken: string
        :param NextPageToken:
          The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
        :rtype: dict
        :returns:
        """
        pass

    def get_tags(self, TimePeriod: Dict, SearchString: str = None, TagKey: str = None, NextPageToken: str = None) -> Dict:
        """
        Queries for available tag keys and tag values for a specified period. You can search the tag values for an arbitrary string. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetTags>`_
        
        **Request Syntax**
        ::
          response = client.get_tags(
              SearchString='string',
              TimePeriod={
                  'Start': 'string',
                  'End': 'string'
              },
              TagKey='string',
              NextPageToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'NextPageToken': 'string',
                'Tags': [
                    'string',
                ],
                'ReturnSize': 123,
                'TotalSize': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **NextPageToken** *(string) --* 
              The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.
            - **Tags** *(list) --* 
              The tags that match your request.
              - *(string) --* 
            - **ReturnSize** *(integer) --* 
              The number of query results that AWS returns at a time.
            - **TotalSize** *(integer) --* 
              The total number of query results.
        :type SearchString: string
        :param SearchString:
          The value that you want to search for.
        :type TimePeriod: dict
        :param TimePeriod: **[REQUIRED]**
          The start and end dates for retrieving the dimension values. The start date is inclusive, but the end date is exclusive. For example, if ``start`` is ``2017-01-01`` and ``end`` is ``2017-05-01`` , then the cost and usage data is retrieved from ``2017-01-01`` up to and including ``2017-04-30`` but not including ``2017-05-01`` .
          - **Start** *(string) --* **[REQUIRED]**
            The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data starting at ``2017-01-01`` up to the end date.
          - **End** *(string) --* **[REQUIRED]**
            The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start date up to, but not including, ``2017-05-01`` .
        :type TagKey: string
        :param TagKey:
          The key of the tag that you want to return values for.
        :type NextPageToken: string
        :param NextPageToken:
          The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
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
