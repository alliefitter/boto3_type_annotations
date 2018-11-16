from typing import NoReturn
from typing import Dict
from botocore.waiter import Waiter


class TableExists(Waiter):
    def wait(self, TableName: str, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dynamodb-2012-08-10/DescribeTable>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              TableName=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type TableName: string
        :param TableName: **[REQUIRED]** 
        
          The name of the table to describe.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 20
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 25
        
        :returns: None
        """
        pass


class TableNotExists(Waiter):
    def wait(self, TableName: str, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dynamodb-2012-08-10/DescribeTable>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              TableName=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type TableName: string
        :param TableName: **[REQUIRED]** 
        
          The name of the table to describe.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 20
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 25
        
        :returns: None
        """
        pass
