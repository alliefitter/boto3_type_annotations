from typing import Dict
from botocore.paginate import Paginator


class ListStreams(Paginator):
    def paginate(self, StreamNameCondition: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`KinesisVideo.Client.list_streams`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisvideo-2017-09-30/ListStreams>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              StreamNameCondition={
                  'ComparisonOperator': 'BEGINS_WITH',
                  'ComparisonValue': 'string'
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
                'StreamInfoList': [
                    {
                        'DeviceName': 'string',
                        'StreamName': 'string',
                        'StreamARN': 'string',
                        'MediaType': 'string',
                        'KmsKeyId': 'string',
                        'Version': 'string',
                        'Status': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING',
                        'CreationTime': datetime(2015, 1, 1),
                        'DataRetentionInHours': 123
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **StreamInfoList** *(list) --* 
              An array of ``StreamInfo`` objects.
              - *(dict) --* 
                An object describing a Kinesis video stream.
                - **DeviceName** *(string) --* 
                  The name of the device that is associated with the stream.
                - **StreamName** *(string) --* 
                  The name of the stream.
                - **StreamARN** *(string) --* 
                  The Amazon Resource Name (ARN) of the stream.
                - **MediaType** *(string) --* 
                  The ``MediaType`` of the stream. 
                - **KmsKeyId** *(string) --* 
                  The ID of the AWS Key Management Service (AWS KMS) key that Kinesis Video Streams uses to encrypt data on the stream.
                - **Version** *(string) --* 
                  The version of the stream.
                - **Status** *(string) --* 
                  The status of the stream.
                - **CreationTime** *(datetime) --* 
                  A time stamp that indicates when the stream was created.
                - **DataRetentionInHours** *(integer) --* 
                  How long the stream retains data, in hours.
        :type StreamNameCondition: dict
        :param StreamNameCondition:
          Optional: Returns only streams that satisfy a specific condition. Currently, you can specify only the prefix of a stream name as a condition.
          - **ComparisonOperator** *(string) --*
            A comparison operator. Currently, you can specify only the ``BEGINS_WITH`` operator, which finds streams whose names start with a given prefix.
          - **ComparisonValue** *(string) --*
            A value to compare.
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
