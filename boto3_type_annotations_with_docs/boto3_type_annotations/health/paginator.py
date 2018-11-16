from typing import Dict
from botocore.paginate import Paginator


class DescribeAffectedEntities(Paginator):
    def paginate(self, filter: Dict, locale: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/health-2016-08-04/DescribeAffectedEntities>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              filter={
                  \'eventArns\': [
                      \'string\',
                  ],
                  \'entityArns\': [
                      \'string\',
                  ],
                  \'entityValues\': [
                      \'string\',
                  ],
                  \'lastUpdatedTimes\': [
                      {
                          \'from\': datetime(2015, 1, 1),
                          \'to\': datetime(2015, 1, 1)
                      },
                  ],
                  \'tags\': [
                      {
                          \'string\': \'string\'
                      },
                  ],
                  \'statusCodes\': [
                      \'IMPAIRED\'|\'UNIMPAIRED\'|\'UNKNOWN\',
                  ]
              },
              locale=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type filter: dict
        :param filter: **[REQUIRED]** 
        
          Values to narrow the results returned. At least one event ARN is required. 
        
          - **eventArns** *(list) --* **[REQUIRED]** 
        
            A list of event ARNs (unique identifiers). For example: ``\"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456\", \"arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101\"``  
        
            - *(string) --* 
        
          - **entityArns** *(list) --* 
        
            A list of entity ARNs (unique identifiers).
        
            - *(string) --* 
        
          - **entityValues** *(list) --* 
        
            A list of IDs for affected entities.
        
            - *(string) --* 
        
          - **lastUpdatedTimes** *(list) --* 
        
            A list of the most recent dates and times that the entity was updated.
        
            - *(dict) --* 
        
              A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` , ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from`` is set and ``to`` is not set: match items where the timestamp value is equal to or after ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is equal to or before ``to`` .
        
              - **from** *(datetime) --* 
        
                The starting date and time of a time range.
        
              - **to** *(datetime) --* 
        
                The ending date and time of a time range.
        
          - **tags** *(list) --* 
        
            A map of entity tags attached to the affected entity.
        
            - *(dict) --* 
        
              - *(string) --* 
        
                - *(string) --* 
        
          - **statusCodes** *(list) --* 
        
            A list of entity status codes (``IMPAIRED`` , ``UNIMPAIRED`` , or ``UNKNOWN`` ).
        
            - *(string) --* 
        
        :type locale: string
        :param locale: 
        
          The locale (language) to return information in. English (en) is the default and the only supported value at this time.
        
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
                \'entities\': [
                    {
                        \'entityArn\': \'string\',
                        \'eventArn\': \'string\',
                        \'entityValue\': \'string\',
                        \'awsAccountId\': \'string\',
                        \'lastUpdatedTime\': datetime(2015, 1, 1),
                        \'statusCode\': \'IMPAIRED\'|\'UNIMPAIRED\'|\'UNKNOWN\',
                        \'tags\': {
                            \'string\': \'string\'
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **entities** *(list) --* 
        
              The entities that match the filter criteria.
        
              - *(dict) --* 
        
                Information about an entity that is affected by a Health event.
        
                - **entityArn** *(string) --* 
        
                  The unique identifier for the entity. Format: ``arn:aws:health:*entity-region* :*aws-account* :entity/*entity-id* `` . Example: ``arn:aws:health:us-east-1:111222333444:entity/AVh5GGT7ul1arKr1sE1K``  
        
                - **eventArn** *(string) --* 
        
                  The unique identifier for the event. Format: ``arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example: arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456``  
        
                - **entityValue** *(string) --* 
        
                  The ID of the affected entity.
        
                - **awsAccountId** *(string) --* 
        
                  The 12-digit AWS account number that contains the affected entity.
        
                - **lastUpdatedTime** *(datetime) --* 
        
                  The most recent time that the entity was updated.
        
                - **statusCode** *(string) --* 
        
                  The most recent status of the entity affected by the event. The possible values are ``IMPAIRED`` , ``UNIMPAIRED`` , and ``UNKNOWN`` .
        
                - **tags** *(dict) --* 
        
                  A map of entity tags attached to the affected entity.
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeEventAggregates(Paginator):
    def paginate(self, aggregateField: str, filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/health-2016-08-04/DescribeEventAggregates>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              filter={
                  \'eventArns\': [
                      \'string\',
                  ],
                  \'eventTypeCodes\': [
                      \'string\',
                  ],
                  \'services\': [
                      \'string\',
                  ],
                  \'regions\': [
                      \'string\',
                  ],
                  \'availabilityZones\': [
                      \'string\',
                  ],
                  \'startTimes\': [
                      {
                          \'from\': datetime(2015, 1, 1),
                          \'to\': datetime(2015, 1, 1)
                      },
                  ],
                  \'endTimes\': [
                      {
                          \'from\': datetime(2015, 1, 1),
                          \'to\': datetime(2015, 1, 1)
                      },
                  ],
                  \'lastUpdatedTimes\': [
                      {
                          \'from\': datetime(2015, 1, 1),
                          \'to\': datetime(2015, 1, 1)
                      },
                  ],
                  \'entityArns\': [
                      \'string\',
                  ],
                  \'entityValues\': [
                      \'string\',
                  ],
                  \'eventTypeCategories\': [
                      \'issue\'|\'accountNotification\'|\'scheduledChange\',
                  ],
                  \'tags\': [
                      {
                          \'string\': \'string\'
                      },
                  ],
                  \'eventStatusCodes\': [
                      \'open\'|\'closed\'|\'upcoming\',
                  ]
              },
              aggregateField=\'eventTypeCategory\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type filter: dict
        :param filter: 
        
          Values to narrow the results returned.
        
          - **eventArns** *(list) --* 
        
            A list of event ARNs (unique identifiers). For example: ``\"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456\", \"arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101\"``  
        
            - *(string) --* 
        
          - **eventTypeCodes** *(list) --* 
        
            A list of unique identifiers for event types. For example, ``\"AWS_EC2_SYSTEM_MAINTENANCE_EVENT\",\"AWS_RDS_MAINTENANCE_SCHEDULED\"``  
        
            - *(string) --* 
        
          - **services** *(list) --* 
        
            The AWS services associated with the event. For example, ``EC2`` , ``RDS`` .
        
            - *(string) --* 
        
          - **regions** *(list) --* 
        
            A list of AWS regions.
        
            - *(string) --* 
        
          - **availabilityZones** *(list) --* 
        
            A list of AWS availability zones.
        
            - *(string) --* 
        
          - **startTimes** *(list) --* 
        
            A list of dates and times that the event began.
        
            - *(dict) --* 
        
              A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` , ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from`` is set and ``to`` is not set: match items where the timestamp value is equal to or after ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is equal to or before ``to`` .
        
              - **from** *(datetime) --* 
        
                The starting date and time of a time range.
        
              - **to** *(datetime) --* 
        
                The ending date and time of a time range.
        
          - **endTimes** *(list) --* 
        
            A list of dates and times that the event ended.
        
            - *(dict) --* 
        
              A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` , ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from`` is set and ``to`` is not set: match items where the timestamp value is equal to or after ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is equal to or before ``to`` .
        
              - **from** *(datetime) --* 
        
                The starting date and time of a time range.
        
              - **to** *(datetime) --* 
        
                The ending date and time of a time range.
        
          - **lastUpdatedTimes** *(list) --* 
        
            A list of dates and times that the event was last updated.
        
            - *(dict) --* 
        
              A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` , ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from`` is set and ``to`` is not set: match items where the timestamp value is equal to or after ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is equal to or before ``to`` .
        
              - **from** *(datetime) --* 
        
                The starting date and time of a time range.
        
              - **to** *(datetime) --* 
        
                The ending date and time of a time range.
        
          - **entityArns** *(list) --* 
        
            A list of entity ARNs (unique identifiers).
        
            - *(string) --* 
        
          - **entityValues** *(list) --* 
        
            A list of entity identifiers, such as EC2 instance IDs (``i-34ab692e`` ) or EBS volumes (``vol-426ab23e`` ).
        
            - *(string) --* 
        
          - **eventTypeCategories** *(list) --* 
        
            A list of event type category codes (``issue`` , ``scheduledChange`` , or ``accountNotification`` ).
        
            - *(string) --* 
        
          - **tags** *(list) --* 
        
            A map of entity tags attached to the affected entity.
        
            - *(dict) --* 
        
              - *(string) --* 
        
                - *(string) --* 
        
          - **eventStatusCodes** *(list) --* 
        
            A list of event status codes.
        
            - *(string) --* 
        
        :type aggregateField: string
        :param aggregateField: **[REQUIRED]** 
        
          The only currently supported value is ``eventTypeCategory`` .
        
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
                \'eventAggregates\': [
                    {
                        \'aggregateValue\': \'string\',
                        \'count\': 123
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **eventAggregates** *(list) --* 
        
              The number of events in each category that meet the optional filter criteria.
        
              - *(dict) --* 
        
                The number of events of each issue type. Returned by the  DescribeEventAggregates operation.
        
                - **aggregateValue** *(string) --* 
        
                  The issue type for the associated count.
        
                - **count** *(integer) --* 
        
                  The number of events of the associated issue type.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeEventTypes(Paginator):
    def paginate(self, filter: Dict = None, locale: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/health-2016-08-04/DescribeEventTypes>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              filter={
                  \'eventTypeCodes\': [
                      \'string\',
                  ],
                  \'services\': [
                      \'string\',
                  ],
                  \'eventTypeCategories\': [
                      \'issue\'|\'accountNotification\'|\'scheduledChange\',
                  ]
              },
              locale=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type filter: dict
        :param filter: 
        
          Values to narrow the results returned.
        
          - **eventTypeCodes** *(list) --* 
        
            A list of event type codes.
        
            - *(string) --* 
        
          - **services** *(list) --* 
        
            The AWS services associated with the event. For example, ``EC2`` , ``RDS`` .
        
            - *(string) --* 
        
          - **eventTypeCategories** *(list) --* 
        
            A list of event type category codes (``issue`` , ``scheduledChange`` , or ``accountNotification`` ).
        
            - *(string) --* 
        
        :type locale: string
        :param locale: 
        
          The locale (language) to return information in. English (en) is the default and the only supported value at this time.
        
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
                \'eventTypes\': [
                    {
                        \'service\': \'string\',
                        \'code\': \'string\',
                        \'category\': \'issue\'|\'accountNotification\'|\'scheduledChange\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **eventTypes** *(list) --* 
        
              A list of event types that match the filter criteria. Event types have a category (``issue`` , ``accountNotification`` , or ``scheduledChange`` ), a service (for example, ``EC2`` , ``RDS`` , ``DATAPIPELINE`` , ``BILLING`` ), and a code (in the format ``AWS_*SERVICE* _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` ).
        
              - *(dict) --* 
        
                Metadata about a type of event that is reported by AWS Health. Data consists of the category (for example, ``issue`` ), the service (for example, ``EC2`` ), and the event type code (for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` ).
        
                - **service** *(string) --* 
        
                  The AWS service that is affected by the event. For example, ``EC2`` , ``RDS`` .
        
                - **code** *(string) --* 
        
                  The unique identifier for the event type. The format is ``AWS_*SERVICE* _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` .
        
                - **category** *(string) --* 
        
                  A list of event type category codes (``issue`` , ``scheduledChange`` , or ``accountNotification`` ).
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeEvents(Paginator):
    def paginate(self, filter: Dict = None, locale: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/health-2016-08-04/DescribeEvents>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              filter={
                  \'eventArns\': [
                      \'string\',
                  ],
                  \'eventTypeCodes\': [
                      \'string\',
                  ],
                  \'services\': [
                      \'string\',
                  ],
                  \'regions\': [
                      \'string\',
                  ],
                  \'availabilityZones\': [
                      \'string\',
                  ],
                  \'startTimes\': [
                      {
                          \'from\': datetime(2015, 1, 1),
                          \'to\': datetime(2015, 1, 1)
                      },
                  ],
                  \'endTimes\': [
                      {
                          \'from\': datetime(2015, 1, 1),
                          \'to\': datetime(2015, 1, 1)
                      },
                  ],
                  \'lastUpdatedTimes\': [
                      {
                          \'from\': datetime(2015, 1, 1),
                          \'to\': datetime(2015, 1, 1)
                      },
                  ],
                  \'entityArns\': [
                      \'string\',
                  ],
                  \'entityValues\': [
                      \'string\',
                  ],
                  \'eventTypeCategories\': [
                      \'issue\'|\'accountNotification\'|\'scheduledChange\',
                  ],
                  \'tags\': [
                      {
                          \'string\': \'string\'
                      },
                  ],
                  \'eventStatusCodes\': [
                      \'open\'|\'closed\'|\'upcoming\',
                  ]
              },
              locale=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type filter: dict
        :param filter: 
        
          Values to narrow the results returned.
        
          - **eventArns** *(list) --* 
        
            A list of event ARNs (unique identifiers). For example: ``\"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456\", \"arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101\"``  
        
            - *(string) --* 
        
          - **eventTypeCodes** *(list) --* 
        
            A list of unique identifiers for event types. For example, ``\"AWS_EC2_SYSTEM_MAINTENANCE_EVENT\",\"AWS_RDS_MAINTENANCE_SCHEDULED\"``  
        
            - *(string) --* 
        
          - **services** *(list) --* 
        
            The AWS services associated with the event. For example, ``EC2`` , ``RDS`` .
        
            - *(string) --* 
        
          - **regions** *(list) --* 
        
            A list of AWS regions.
        
            - *(string) --* 
        
          - **availabilityZones** *(list) --* 
        
            A list of AWS availability zones.
        
            - *(string) --* 
        
          - **startTimes** *(list) --* 
        
            A list of dates and times that the event began.
        
            - *(dict) --* 
        
              A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` , ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from`` is set and ``to`` is not set: match items where the timestamp value is equal to or after ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is equal to or before ``to`` .
        
              - **from** *(datetime) --* 
        
                The starting date and time of a time range.
        
              - **to** *(datetime) --* 
        
                The ending date and time of a time range.
        
          - **endTimes** *(list) --* 
        
            A list of dates and times that the event ended.
        
            - *(dict) --* 
        
              A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` , ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from`` is set and ``to`` is not set: match items where the timestamp value is equal to or after ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is equal to or before ``to`` .
        
              - **from** *(datetime) --* 
        
                The starting date and time of a time range.
        
              - **to** *(datetime) --* 
        
                The ending date and time of a time range.
        
          - **lastUpdatedTimes** *(list) --* 
        
            A list of dates and times that the event was last updated.
        
            - *(dict) --* 
        
              A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` , ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from`` is set and ``to`` is not set: match items where the timestamp value is equal to or after ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is equal to or before ``to`` .
        
              - **from** *(datetime) --* 
        
                The starting date and time of a time range.
        
              - **to** *(datetime) --* 
        
                The ending date and time of a time range.
        
          - **entityArns** *(list) --* 
        
            A list of entity ARNs (unique identifiers).
        
            - *(string) --* 
        
          - **entityValues** *(list) --* 
        
            A list of entity identifiers, such as EC2 instance IDs (``i-34ab692e`` ) or EBS volumes (``vol-426ab23e`` ).
        
            - *(string) --* 
        
          - **eventTypeCategories** *(list) --* 
        
            A list of event type category codes (``issue`` , ``scheduledChange`` , or ``accountNotification`` ).
        
            - *(string) --* 
        
          - **tags** *(list) --* 
        
            A map of entity tags attached to the affected entity.
        
            - *(dict) --* 
        
              - *(string) --* 
        
                - *(string) --* 
        
          - **eventStatusCodes** *(list) --* 
        
            A list of event status codes.
        
            - *(string) --* 
        
        :type locale: string
        :param locale: 
        
          The locale (language) to return information in. English (en) is the default and the only supported value at this time.
        
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
                \'events\': [
                    {
                        \'arn\': \'string\',
                        \'service\': \'string\',
                        \'eventTypeCode\': \'string\',
                        \'eventTypeCategory\': \'issue\'|\'accountNotification\'|\'scheduledChange\',
                        \'region\': \'string\',
                        \'availabilityZone\': \'string\',
                        \'startTime\': datetime(2015, 1, 1),
                        \'endTime\': datetime(2015, 1, 1),
                        \'lastUpdatedTime\': datetime(2015, 1, 1),
                        \'statusCode\': \'open\'|\'closed\'|\'upcoming\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **events** *(list) --* 
        
              The events that match the specified filter criteria.
        
              - *(dict) --* 
        
                Summary information about an event, returned by the  DescribeEvents operation. The  DescribeEventDetails operation also returns this information, as well as the  EventDescription and additional event metadata.
        
                - **arn** *(string) --* 
        
                  The unique identifier for the event. Format: ``arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example: arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456``  
        
                - **service** *(string) --* 
        
                  The AWS service that is affected by the event. For example, ``EC2`` , ``RDS`` .
        
                - **eventTypeCode** *(string) --* 
        
                  The unique identifier for the event type. The format is ``AWS_*SERVICE* _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` .
        
                - **eventTypeCategory** *(string) --* 
        
                  The category of the event. Possible values are ``issue`` , ``scheduledChange`` , and ``accountNotification`` .
        
                - **region** *(string) --* 
        
                  The AWS region name of the event.
        
                - **availabilityZone** *(string) --* 
        
                  The AWS Availability Zone of the event. For example, us-east-1a.
        
                - **startTime** *(datetime) --* 
        
                  The date and time that the event began.
        
                - **endTime** *(datetime) --* 
        
                  The date and time that the event ended.
        
                - **lastUpdatedTime** *(datetime) --* 
        
                  The most recent date and time that the event was updated.
        
                - **statusCode** *(string) --* 
        
                  The most recent status of the event. Possible values are ``open`` , ``closed`` , and ``upcoming`` .
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
