from datetime import datetime
from typing import Dict
from botocore.paginate import Paginator


class DescribeEvents(Paginator):
    def paginate(self, ApplicationName: str = None, VersionLabel: str = None, TemplateName: str = None, EnvironmentId: str = None, EnvironmentName: str = None, PlatformArn: str = None, RequestId: str = None, Severity: str = None, StartTime: datetime = None, EndTime: datetime = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribeEvents>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ApplicationName=\'string\',
              VersionLabel=\'string\',
              TemplateName=\'string\',
              EnvironmentId=\'string\',
              EnvironmentName=\'string\',
              PlatformArn=\'string\',
              RequestId=\'string\',
              Severity=\'TRACE\'|\'DEBUG\'|\'INFO\'|\'WARN\'|\'ERROR\'|\'FATAL\',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ApplicationName: string
        :param ApplicationName: 
        
          If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those associated with this application.
        
        :type VersionLabel: string
        :param VersionLabel: 
        
          If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this application version.
        
        :type TemplateName: string
        :param TemplateName: 
        
          If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that are associated with this environment configuration.
        
        :type EnvironmentId: string
        :param EnvironmentId: 
        
          If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this environment.
        
        :type EnvironmentName: string
        :param EnvironmentName: 
        
          If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this environment.
        
        :type PlatformArn: string
        :param PlatformArn: 
        
          The ARN of the version of the custom platform.
        
        :type RequestId: string
        :param RequestId: 
        
          If specified, AWS Elastic Beanstalk restricts the described events to include only those associated with this request ID.
        
        :type Severity: string
        :param Severity: 
        
          If specified, limits the events returned from this call to include only those with the specified severity or higher.
        
        :type StartTime: datetime
        :param StartTime: 
        
          If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that occur on or after this time.
        
        :type EndTime: datetime
        :param EndTime: 
        
          If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that occur up to, but not including, the ``EndTime`` . 
        
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
                \'Events\': [
                    {
                        \'EventDate\': datetime(2015, 1, 1),
                        \'Message\': \'string\',
                        \'ApplicationName\': \'string\',
                        \'VersionLabel\': \'string\',
                        \'TemplateName\': \'string\',
                        \'EnvironmentName\': \'string\',
                        \'PlatformArn\': \'string\',
                        \'RequestId\': \'string\',
                        \'Severity\': \'TRACE\'|\'DEBUG\'|\'INFO\'|\'WARN\'|\'ERROR\'|\'FATAL\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Result message wrapping a list of event descriptions.
        
            - **Events** *(list) --* 
        
              A list of  EventDescription . 
        
              - *(dict) --* 
        
                Describes an event.
        
                - **EventDate** *(datetime) --* 
        
                  The date when the event occurred.
        
                - **Message** *(string) --* 
        
                  The event message.
        
                - **ApplicationName** *(string) --* 
        
                  The application associated with the event.
        
                - **VersionLabel** *(string) --* 
        
                  The release label for the application version associated with this event.
        
                - **TemplateName** *(string) --* 
        
                  The name of the configuration associated with this event.
        
                - **EnvironmentName** *(string) --* 
        
                  The name of the environment associated with this event.
        
                - **PlatformArn** *(string) --* 
        
                  The ARN of the platform.
        
                - **RequestId** *(string) --* 
        
                  The web service request ID for the activity of this event.
        
                - **Severity** *(string) --* 
        
                  The severity level of this event.
        
        """
        pass
