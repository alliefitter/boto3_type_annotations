from typing import Dict
from botocore.paginate import Paginator


class DescribeStream(Paginator):
    def paginate(self, StreamName: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/DescribeStream>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              StreamName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type StreamName: string
        :param StreamName: **[REQUIRED]** 
        
          The name of the stream to describe.
        
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
                \'StreamDescription\': {
                    \'StreamName\': \'string\',
                    \'StreamARN\': \'string\',
                    \'StreamStatus\': \'CREATING\'|\'DELETING\'|\'ACTIVE\'|\'UPDATING\',
                    \'Shards\': [
                        {
                            \'ShardId\': \'string\',
                            \'ParentShardId\': \'string\',
                            \'AdjacentParentShardId\': \'string\',
                            \'HashKeyRange\': {
                                \'StartingHashKey\': \'string\',
                                \'EndingHashKey\': \'string\'
                            },
                            \'SequenceNumberRange\': {
                                \'StartingSequenceNumber\': \'string\',
                                \'EndingSequenceNumber\': \'string\'
                            }
                        },
                    ],
                    \'HasMoreShards\': True|False,
                    \'RetentionPeriodHours\': 123,
                    \'StreamCreationTimestamp\': datetime(2015, 1, 1),
                    \'EnhancedMonitoring\': [
                        {
                            \'ShardLevelMetrics\': [
                                \'IncomingBytes\'|\'IncomingRecords\'|\'OutgoingBytes\'|\'OutgoingRecords\'|\'WriteProvisionedThroughputExceeded\'|\'ReadProvisionedThroughputExceeded\'|\'IteratorAgeMilliseconds\'|\'ALL\',
                            ]
                        },
                    ],
                    \'EncryptionType\': \'NONE\'|\'KMS\',
                    \'KeyId\': \'string\'
                },
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output for ``DescribeStream`` .
        
            - **StreamDescription** *(dict) --* 
        
              The current status of the stream, the stream Amazon Resource Name (ARN), an array of shard objects that comprise the stream, and whether there are more shards available.
        
              - **StreamName** *(string) --* 
        
                The name of the stream being described.
        
              - **StreamARN** *(string) --* 
        
                The Amazon Resource Name (ARN) for the stream being described.
        
              - **StreamStatus** *(string) --* 
        
                The current status of the stream being described. The stream status is one of the following states:
        
                * ``CREATING`` - The stream is being created. Kinesis Data Streams immediately returns and sets ``StreamStatus`` to ``CREATING`` . 
                 
                * ``DELETING`` - The stream is being deleted. The specified stream is in the ``DELETING`` state until Kinesis Data Streams completes the deletion. 
                 
                * ``ACTIVE`` - The stream exists and is ready for read and write operations or deletion. You should perform read and write operations only on an ``ACTIVE`` stream. 
                 
                * ``UPDATING`` - Shards in the stream are being merged or split. Read and write operations continue to work while the stream is in the ``UPDATING`` state. 
                 
              - **Shards** *(list) --* 
        
                The shards that comprise the stream.
        
                - *(dict) --* 
        
                  A uniquely identified group of data records in a Kinesis data stream.
        
                  - **ShardId** *(string) --* 
        
                    The unique identifier of the shard within the stream.
        
                  - **ParentShardId** *(string) --* 
        
                    The shard ID of the shard\'s parent.
        
                  - **AdjacentParentShardId** *(string) --* 
        
                    The shard ID of the shard adjacent to the shard\'s parent.
        
                  - **HashKeyRange** *(dict) --* 
        
                    The range of possible hash key values for the shard, which is a set of ordered contiguous positive integers.
        
                    - **StartingHashKey** *(string) --* 
        
                      The starting hash key of the hash key range.
        
                    - **EndingHashKey** *(string) --* 
        
                      The ending hash key of the hash key range.
        
                  - **SequenceNumberRange** *(dict) --* 
        
                    The range of possible sequence numbers for the shard.
        
                    - **StartingSequenceNumber** *(string) --* 
        
                      The starting sequence number for the range.
        
                    - **EndingSequenceNumber** *(string) --* 
        
                      The ending sequence number for the range. Shards that are in the OPEN state have an ending sequence number of ``null`` .
        
              - **HasMoreShards** *(boolean) --* 
        
                If set to ``true`` , more shards in the stream are available to describe.
        
              - **RetentionPeriodHours** *(integer) --* 
        
                The current retention period, in hours.
        
              - **StreamCreationTimestamp** *(datetime) --* 
        
                The approximate time that the stream was created.
        
              - **EnhancedMonitoring** *(list) --* 
        
                Represents the current enhanced monitoring settings of the stream.
        
                - *(dict) --* 
        
                  Represents enhanced metrics types.
        
                  - **ShardLevelMetrics** *(list) --* 
        
                    List of shard-level metrics.
        
                    The following are the valid shard-level metrics. The value \"``ALL`` \" enhances every metric.
        
                    * ``IncomingBytes``   
                     
                    * ``IncomingRecords``   
                     
                    * ``OutgoingBytes``   
                     
                    * ``OutgoingRecords``   
                     
                    * ``WriteProvisionedThroughputExceeded``   
                     
                    * ``ReadProvisionedThroughputExceeded``   
                     
                    * ``IteratorAgeMilliseconds``   
                     
                    * ``ALL``   
                     
                    For more information, see `Monitoring the Amazon Kinesis Data Streams Service with Amazon CloudWatch <http://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html>`__ in the *Amazon Kinesis Data Streams Developer Guide* .
        
                    - *(string) --* 
                
              - **EncryptionType** *(string) --* 
        
                The server-side encryption type used on the stream. This parameter can be one of the following values:
        
                * ``NONE`` : Do not encrypt the records in the stream. 
                 
                * ``KMS`` : Use server-side encryption on the records in the stream using a customer-managed AWS KMS key. 
                 
              - **KeyId** *(string) --* 
        
                The GUID for the customer-managed AWS KMS key to use for encryption. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by \"alias/\".You can also use a master key owned by Kinesis Data Streams by specifying the alias ``aws/kinesis`` .
        
                * Key ARN example: ``arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012``   
                 
                * Alias ARN example: ``arn:aws:kms:us-east-1:123456789012:alias/MyAliasName``   
                 
                * Globally unique key ID example: ``12345678-1234-1234-1234-123456789012``   
                 
                * Alias name example: ``alias/MyAliasName``   
                 
                * Master key owned by Kinesis Data Streams: ``alias/aws/kinesis``   
                 
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListStreams(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/ListStreams>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'StreamNames\': [
                    \'string\',
                ],
                \'HasMoreStreams\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output for ``ListStreams`` .
        
            - **StreamNames** *(list) --* 
        
              The names of the streams that are associated with the AWS account making the ``ListStreams`` request.
        
              - *(string) --* 
          
            - **HasMoreStreams** *(boolean) --* 
        
              If set to ``true`` , there are more streams available to list.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
