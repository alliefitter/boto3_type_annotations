from typing import Dict
from botocore.paginate import Paginator


class DescribeBudgets(Paginator):
    def paginate(self, AccountId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Budgets.Client.describe_budgets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/DescribeBudgets>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AccountId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Budgets': [
                    {
                        'BudgetName': 'string',
                        'BudgetLimit': {
                            'Amount': 'string',
                            'Unit': 'string'
                        },
                        'CostFilters': {
                            'string': [
                                'string',
                            ]
                        },
                        'CostTypes': {
                            'IncludeTax': True|False,
                            'IncludeSubscription': True|False,
                            'UseBlended': True|False,
                            'IncludeRefund': True|False,
                            'IncludeCredit': True|False,
                            'IncludeUpfront': True|False,
                            'IncludeRecurring': True|False,
                            'IncludeOtherSubscription': True|False,
                            'IncludeSupport': True|False,
                            'IncludeDiscount': True|False,
                            'UseAmortized': True|False
                        },
                        'TimeUnit': 'DAILY'|'MONTHLY'|'QUARTERLY'|'ANNUALLY',
                        'TimePeriod': {
                            'Start': datetime(2015, 1, 1),
                            'End': datetime(2015, 1, 1)
                        },
                        'CalculatedSpend': {
                            'ActualSpend': {
                                'Amount': 'string',
                                'Unit': 'string'
                            },
                            'ForecastedSpend': {
                                'Amount': 'string',
                                'Unit': 'string'
                            }
                        },
                        'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'|'RI_COVERAGE',
                        'LastUpdatedTime': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Response of DescribeBudgets 
            - **Budgets** *(list) --* 
              A list of budgets.
              - *(dict) --* 
                Represents the output of the ``CreateBudget`` operation. The content consists of the detailed metadata and data file information, and the current status of the ``budget`` object.
                This is the ARN pattern for a budget: 
                 ``arn:aws:budgetservice::AccountId:budget/budgetName``  
                - **BudgetName** *(string) --* 
                  The name of a budget. The name must be unique within accounts. The ``:`` and ``\`` characters aren't allowed in ``BudgetName`` .
                - **BudgetLimit** *(dict) --* 
                  The total amount of cost, usage, RI utilization, or RI coverage that you want to track with your budget.
                   ``BudgetLimit`` is required for cost or usage budgets, but optional for RI utilization or coverage budgets. RI utilization or coverage budgets default to ``100`` , which is the only valid value for RI utilization or coverage budgets.
                  - **Amount** *(string) --* 
                    The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.
                  - **Unit** *(string) --* 
                    The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.
                - **CostFilters** *(dict) --* 
                  The cost filters, such as service or region, that are applied to a budget.
                  AWS Budgets supports the following services as a filter for RI budgets:
                  * Amazon Elastic Compute Cloud - Compute 
                  * Amazon Redshift 
                  * Amazon Relational Database Service 
                  * Amazon ElastiCache 
                  * Amazon Elasticsearch Service 
                  - *(string) --* 
                    A generic string.
                    - *(list) --* 
                      - *(string) --* 
                        A generic string.
                - **CostTypes** *(dict) --* 
                  The types of costs that are included in this ``COST`` budget.
                   ``USAGE`` , ``RI_UTILIZATION`` , and ``RI_COVERAGE`` budgets do not have ``CostTypes`` .
                  - **IncludeTax** *(boolean) --* 
                    Specifies whether a budget includes taxes.
                    The default value is ``true`` .
                  - **IncludeSubscription** *(boolean) --* 
                    Specifies whether a budget includes subscriptions.
                    The default value is ``true`` .
                  - **UseBlended** *(boolean) --* 
                    Specifies whether a budget uses a blended rate.
                    The default value is ``false`` .
                  - **IncludeRefund** *(boolean) --* 
                    Specifies whether a budget includes refunds.
                    The default value is ``true`` .
                  - **IncludeCredit** *(boolean) --* 
                    Specifies whether a budget includes credits.
                    The default value is ``true`` .
                  - **IncludeUpfront** *(boolean) --* 
                    Specifies whether a budget includes upfront RI costs.
                    The default value is ``true`` .
                  - **IncludeRecurring** *(boolean) --* 
                    Specifies whether a budget includes recurring fees such as monthly RI fees.
                    The default value is ``true`` .
                  - **IncludeOtherSubscription** *(boolean) --* 
                    Specifies whether a budget includes non-RI subscription costs.
                    The default value is ``true`` .
                  - **IncludeSupport** *(boolean) --* 
                    Specifies whether a budget includes support subscription fees.
                    The default value is ``true`` .
                  - **IncludeDiscount** *(boolean) --* 
                    Specifies whether a budget includes discounts.
                    The default value is ``true`` .
                  - **UseAmortized** *(boolean) --* 
                    Specifies whether a budget uses the amortized rate.
                    The default value is ``false`` .
                - **TimeUnit** *(string) --* 
                  The length of time until a budget resets the actual and forecasted spend. ``DAILY`` is available only for ``RI_UTILIZATION`` and ``RI_COVERAGE`` budgets.
                - **TimePeriod** *(dict) --* 
                  The period of time that is covered by a budget. The period has a start date and an end date. The start date must come before the end date. The end date must come before ``06/15/87 00:00 UTC`` . 
                  If you create your budget and don't specify a start date, AWS defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018, chose ``DAILY`` , and didn't set a start date, AWS set your start date to ``01/24/18 00:00 UTC`` . If you chose ``MONTHLY`` , AWS set your start date to ``01/01/18 00:00 UTC`` . If you didn't specify an end date, AWS set your end date to ``06/15/87 00:00 UTC`` . The defaults are the same for the AWS Billing and Cost Management console and the API. 
                  You can change either date with the ``UpdateBudget`` operation.
                  After the end date, AWS deletes the budget and all associated notifications and subscribers.
                  - **Start** *(datetime) --* 
                    The start date for a budget. If you created your budget and didn't specify a start date, AWS defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018, chose ``DAILY`` , and didn't set a start date, AWS set your start date to ``01/24/18 00:00 UTC`` . If you chose ``MONTHLY`` , AWS set your start date to ``01/01/18 00:00 UTC`` . The defaults are the same for the AWS Billing and Cost Management console and the API.
                    You can change your start date with the ``UpdateBudget`` operation.
                  - **End** *(datetime) --* 
                    The end date for a budget. If you didn't specify an end date, AWS set your end date to ``06/15/87 00:00 UTC`` . The defaults are the same for the AWS Billing and Cost Management console and the API.
                    After the end date, AWS deletes the budget and all associated notifications and subscribers. You can change your end date with the ``UpdateBudget`` operation.
                - **CalculatedSpend** *(dict) --* 
                  The actual and forecasted cost or usage that the budget tracks.
                  - **ActualSpend** *(dict) --* 
                    The amount of cost, usage, or RI units that you have used.
                    - **Amount** *(string) --* 
                      The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.
                    - **Unit** *(string) --* 
                      The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.
                  - **ForecastedSpend** *(dict) --* 
                    The amount of cost, usage, or RI units that you are forecasted to use.
                    - **Amount** *(string) --* 
                      The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.
                    - **Unit** *(string) --* 
                      The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.
                - **BudgetType** *(string) --* 
                  Whether this budget tracks monetary costs, usage, RI utilization, or RI coverage.
                - **LastUpdatedTime** *(datetime) --* 
                  The last time that you updated this budget.
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The ``accountId`` that is associated with the budgets that you want descriptions of.
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


class DescribeNotificationsForBudget(Paginator):
    def paginate(self, AccountId: str, BudgetName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Budgets.Client.describe_notifications_for_budget`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/DescribeNotificationsForBudget>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AccountId='string',
              BudgetName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Notifications': [
                    {
                        'NotificationType': 'ACTUAL'|'FORECASTED',
                        'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                        'Threshold': 123.0,
                        'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
                        'NotificationState': 'OK'|'ALARM'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Response of GetNotificationsForBudget 
            - **Notifications** *(list) --* 
              A list of notifications that are associated with a budget.
              - *(dict) --* 
                A notification that is associated with a budget. A budget can have up to five notifications. 
                Each notification must have at least one subscriber. A notification can have one SNS subscriber and up to 10 email subscribers, for a total of 11 subscribers.
                For example, if you have a budget for 200 dollars and you want to be notified when you go over 160 dollars, create a notification with the following parameters:
                * A notificationType of ``ACTUAL``   
                * A ``thresholdType`` of ``PERCENTAGE``   
                * A ``comparisonOperator`` of ``GREATER_THAN``   
                * A notification ``threshold`` of ``80``   
                - **NotificationType** *(string) --* 
                  Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you're forecasted to spend (``FORECASTED`` ).
                - **ComparisonOperator** *(string) --* 
                  The comparison that is used for this notification.
                - **Threshold** *(float) --* 
                  The threshold that is associated with a notification. Thresholds are always a percentage.
                - **ThresholdType** *(string) --* 
                  The type of threshold for a notification. For ``ABSOLUTE_VALUE`` thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For ``PERCENTAGE`` thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a ``PERCENTAGE`` threshold of 80%, AWS notifies you when you go over 160 dollars.
                - **NotificationState** *(string) --* 
                  Whether this notification is in alarm. If a budget notification is in the ``ALARM`` state, you have passed the set threshold for the budget.
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The ``accountId`` that is associated with the budget whose notifications you want descriptions of.
        :type BudgetName: string
        :param BudgetName: **[REQUIRED]**
          The name of the budget whose notifications you want descriptions of.
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


class DescribeSubscribersForNotification(Paginator):
    def paginate(self, AccountId: str, BudgetName: str, Notification: Dict, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Budgets.Client.describe_subscribers_for_notification`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/DescribeSubscribersForNotification>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AccountId='string',
              BudgetName='string',
              Notification={
                  'NotificationType': 'ACTUAL'|'FORECASTED',
                  'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                  'Threshold': 123.0,
                  'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
                  'NotificationState': 'OK'|'ALARM'
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Subscribers': [
                    {
                        'SubscriptionType': 'SNS'|'EMAIL',
                        'Address': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Response of DescribeSubscribersForNotification 
            - **Subscribers** *(list) --* 
              A list of subscribers that are associated with a notification.
              - *(dict) --* 
                The subscriber to a budget notification. The subscriber consists of a subscription type and either an Amazon SNS topic or an email address.
                For example, an email subscriber would have the following parameters:
                * A ``subscriptionType`` of ``EMAIL``   
                * An ``address`` of ``example@example.com``   
                - **SubscriptionType** *(string) --* 
                  The type of notification that AWS sends to a subscriber.
                - **Address** *(string) --* 
                  The address that AWS sends budget notifications to, either an SNS topic or an email.
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The ``accountId`` that is associated with the budget whose subscribers you want descriptions of.
        :type BudgetName: string
        :param BudgetName: **[REQUIRED]**
          The name of the budget whose subscribers you want descriptions of.
        :type Notification: dict
        :param Notification: **[REQUIRED]**
          The notification whose subscribers you want to list.
          - **NotificationType** *(string) --* **[REQUIRED]**
            Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you\'re forecasted to spend (``FORECASTED`` ).
          - **ComparisonOperator** *(string) --* **[REQUIRED]**
            The comparison that is used for this notification.
          - **Threshold** *(float) --* **[REQUIRED]**
            The threshold that is associated with a notification. Thresholds are always a percentage.
          - **ThresholdType** *(string) --*
            The type of threshold for a notification. For ``ABSOLUTE_VALUE`` thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For ``PERCENTAGE`` thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a ``PERCENTAGE`` threshold of 80%, AWS notifies you when you go over 160 dollars.
          - **NotificationState** *(string) --*
            Whether this notification is in alarm. If a budget notification is in the ``ALARM`` state, you have passed the set threshold for the budget.
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
