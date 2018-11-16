from datetime import datetime
from typing import List
from typing import Dict
from botocore.paginate import Paginator


class LookupEvents(Paginator):
    def paginate(self, LookupAttributes: List = None, StartTime: datetime = None, EndTime: datetime = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/LookupEvents>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              LookupAttributes=[
                  {
                      \'AttributeKey\': \'EventId\'|\'EventName\'|\'ReadOnly\'|\'Username\'|\'ResourceType\'|\'ResourceName\'|\'EventSource\'|\'AccessKeyId\',
                      \'AttributeValue\': \'string\'
                  },
              ],
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type LookupAttributes: list
        :param LookupAttributes: 
        
          Contains a list of lookup attributes. Currently the list can contain only one item.
        
          - *(dict) --* 
        
            Specifies an attribute and value that filter the events returned.
        
            - **AttributeKey** *(string) --* **[REQUIRED]** 
        
              Specifies an attribute on which to filter the events returned.
        
            - **AttributeValue** *(string) --* **[REQUIRED]** 
        
              Specifies a value for the specified AttributeKey.
        
        :type StartTime: datetime
        :param StartTime: 
        
          Specifies that only events that occur after or at the specified time are returned. If the specified start time is after the specified end time, an error is returned.
        
        :type EndTime: datetime
        :param EndTime: 
        
          Specifies that only events that occur before or at the specified time are returned. If the specified end time is before the specified start time, an error is returned.
        
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
                        \'EventId\': \'string\',
                        \'EventName\': \'string\',
                        \'ReadOnly\': \'string\',
                        \'AccessKeyId\': \'string\',
                        \'EventTime\': datetime(2015, 1, 1),
                        \'EventSource\': \'string\',
                        \'Username\': \'string\',
                        \'Resources\': [
                            {
                                \'ResourceType\': \'string\',
                                \'ResourceName\': \'string\'
                            },
                        ],
                        \'CloudTrailEvent\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains a response to a LookupEvents action.
        
            - **Events** *(list) --* 
        
              A list of events returned based on the lookup attributes specified and the CloudTrail event. The events list is sorted by time. The most recent event is listed first.
        
              - *(dict) --* 
        
                Contains information about an event that was returned by a lookup request. The result includes a representation of a CloudTrail event.
        
                - **EventId** *(string) --* 
        
                  The CloudTrail ID of the event returned.
        
                - **EventName** *(string) --* 
        
                  The name of the event returned.
        
                - **ReadOnly** *(string) --* 
        
                  Information about whether the event is a write event or a read event. 
        
                - **AccessKeyId** *(string) --* 
        
                  The AWS access key ID that was used to sign the request. If the request was made with temporary security credentials, this is the access key ID of the temporary credentials.
        
                - **EventTime** *(datetime) --* 
        
                  The date and time of the event returned.
        
                - **EventSource** *(string) --* 
        
                  The AWS service that the request was made to.
        
                - **Username** *(string) --* 
        
                  A user name or role name of the requester that called the API in the event returned.
        
                - **Resources** *(list) --* 
        
                  A list of resources referenced by the event returned.
        
                  - *(dict) --* 
        
                    Specifies the type and name of a resource referenced by an event.
        
                    - **ResourceType** *(string) --* 
        
                      The type of a resource referenced by the event returned. When the resource type cannot be determined, null is returned. Some examples of resource types are: **Instance** for EC2, **Trail** for CloudTrail, **DBInstance** for RDS, and **AccessKey** for IAM. For a list of resource types supported for event lookup, see `Resource Types Supported for Event Lookup <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/lookup_supported_resourcetypes.html>`__ .
        
                    - **ResourceName** *(string) --* 
        
                      The name of the resource referenced by the event returned. These are user-created names whose values will depend on the environment. For example, the resource name might be \"auto-scaling-test-group\" for an Auto Scaling Group or \"i-1234567\" for an EC2 Instance.
        
                - **CloudTrailEvent** *(string) --* 
        
                  A JSON string that contains a representation of the event returned.
        
        """
        pass
