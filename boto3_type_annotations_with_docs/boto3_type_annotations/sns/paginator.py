from typing import Dict
from botocore.paginate import Paginator


class ListEndpointsByPlatformApplication(Paginator):
    def paginate(self, PlatformApplicationArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SNS.Client.list_endpoints_by_platform_application`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListEndpointsByPlatformApplication>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PlatformApplicationArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Endpoints': [
                    {
                        'EndpointArn': 'string',
                        'Attributes': {
                            'string': 'string'
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Response for ListEndpointsByPlatformApplication action.
            - **Endpoints** *(list) --* 
              Endpoints returned for ListEndpointsByPlatformApplication action.
              - *(dict) --* 
                Endpoint for mobile app and device.
                - **EndpointArn** *(string) --* 
                  EndpointArn for mobile app and device.
                - **Attributes** *(dict) --* 
                  Attributes for endpoint.
                  - *(string) --* 
                    - *(string) --* 
        :type PlatformApplicationArn: string
        :param PlatformApplicationArn: **[REQUIRED]**
          PlatformApplicationArn for ListEndpointsByPlatformApplicationInput action.
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


class ListPhoneNumbersOptedOut(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SNS.Client.list_phone_numbers_opted_out`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListPhoneNumbersOptedOut>`_
        
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
                'phoneNumbers': [
                    'string',
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The response from the ``ListPhoneNumbersOptedOut`` action.
            - **phoneNumbers** *(list) --* 
              A list of phone numbers that are opted out of receiving SMS messages. The list is paginated, and each page can contain up to 100 phone numbers.
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


class ListPlatformApplications(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SNS.Client.list_platform_applications`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListPlatformApplications>`_
        
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
                'PlatformApplications': [
                    {
                        'PlatformApplicationArn': 'string',
                        'Attributes': {
                            'string': 'string'
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Response for ListPlatformApplications action.
            - **PlatformApplications** *(list) --* 
              Platform applications returned when calling ListPlatformApplications action.
              - *(dict) --* 
                Platform application object.
                - **PlatformApplicationArn** *(string) --* 
                  PlatformApplicationArn for platform application object.
                - **Attributes** *(dict) --* 
                  Attributes for platform application object.
                  - *(string) --* 
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


class ListSubscriptions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SNS.Client.list_subscriptions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListSubscriptions>`_
        
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
                'Subscriptions': [
                    {
                        'SubscriptionArn': 'string',
                        'Owner': 'string',
                        'Protocol': 'string',
                        'Endpoint': 'string',
                        'TopicArn': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Response for ListSubscriptions action
            - **Subscriptions** *(list) --* 
              A list of subscriptions.
              - *(dict) --* 
                A wrapper type for the attributes of an Amazon SNS subscription.
                - **SubscriptionArn** *(string) --* 
                  The subscription's ARN.
                - **Owner** *(string) --* 
                  The subscription's owner.
                - **Protocol** *(string) --* 
                  The subscription's protocol.
                - **Endpoint** *(string) --* 
                  The subscription's endpoint (format depends on the protocol).
                - **TopicArn** *(string) --* 
                  The ARN of the subscription's topic.
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


class ListSubscriptionsByTopic(Paginator):
    def paginate(self, TopicArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SNS.Client.list_subscriptions_by_topic`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListSubscriptionsByTopic>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              TopicArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Subscriptions': [
                    {
                        'SubscriptionArn': 'string',
                        'Owner': 'string',
                        'Protocol': 'string',
                        'Endpoint': 'string',
                        'TopicArn': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Response for ListSubscriptionsByTopic action.
            - **Subscriptions** *(list) --* 
              A list of subscriptions.
              - *(dict) --* 
                A wrapper type for the attributes of an Amazon SNS subscription.
                - **SubscriptionArn** *(string) --* 
                  The subscription's ARN.
                - **Owner** *(string) --* 
                  The subscription's owner.
                - **Protocol** *(string) --* 
                  The subscription's protocol.
                - **Endpoint** *(string) --* 
                  The subscription's endpoint (format depends on the protocol).
                - **TopicArn** *(string) --* 
                  The ARN of the subscription's topic.
        :type TopicArn: string
        :param TopicArn: **[REQUIRED]**
          The ARN of the topic for which you wish to find subscriptions.
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


class ListTopics(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SNS.Client.list_topics`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListTopics>`_
        
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
                'Topics': [
                    {
                        'TopicArn': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Response for ListTopics action.
            - **Topics** *(list) --* 
              A list of topic ARNs.
              - *(dict) --* 
                A wrapper type for the topic's Amazon Resource Name (ARN). To retrieve a topic's attributes, use ``GetTopicAttributes`` .
                - **TopicArn** *(string) --* 
                  The topic's ARN.
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
