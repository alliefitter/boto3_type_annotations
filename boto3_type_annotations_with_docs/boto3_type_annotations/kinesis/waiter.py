from typing import NoReturn
from typing import Dict
from botocore.waiter import Waiter


class StreamExists(Waiter):
    def wait(self, StreamName: str, Limit: int = None, ExclusiveStartShardId: str = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/DescribeStream>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              StreamName=\'string\',
              Limit=123,
              ExclusiveStartShardId=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type StreamName: string
        :param StreamName: **[REQUIRED]** 
        
          The name of the stream to describe.
        
        :type Limit: integer
        :param Limit: 
        
          The maximum number of shards to return in a single call. The default value is 100. If you specify a value greater than 100, at most 100 shards are returned.
        
        :type ExclusiveStartShardId: string
        :param ExclusiveStartShardId: 
        
          The shard ID of the shard to start with.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 10
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 18
        
        :returns: None
        """
        pass


class StreamNotExists(Waiter):
    def wait(self, StreamName: str, Limit: int = None, ExclusiveStartShardId: str = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesis-2013-12-02/DescribeStream>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              StreamName=\'string\',
              Limit=123,
              ExclusiveStartShardId=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type StreamName: string
        :param StreamName: **[REQUIRED]** 
        
          The name of the stream to describe.
        
        :type Limit: integer
        :param Limit: 
        
          The maximum number of shards to return in a single call. The default value is 100. If you specify a value greater than 100, at most 100 shards are returned.
        
        :type ExclusiveStartShardId: string
        :param ExclusiveStartShardId: 
        
          The shard ID of the shard to start with.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 10
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 18
        
        :returns: None
        """
        pass
