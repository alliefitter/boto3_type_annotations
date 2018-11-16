from typing import List
from typing import Dict
from botocore.waiter import Waiter


class FleetStarted(Waiter):
    def wait(self, Names: List = None, NextToken: str = None, WaiterConfig: Dict = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeFleets>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Names=[
                  \'string\',
              ],
              NextToken=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Names: list
        :param Names: 
        
          The names of the fleets to describe.
        
          - *(string) --* 
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 30
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class FleetStopped(Waiter):
    def wait(self, Names: List = None, NextToken: str = None, WaiterConfig: Dict = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeFleets>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Names=[
                  \'string\',
              ],
              NextToken=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Names: list
        :param Names: 
        
          The names of the fleets to describe.
        
          - *(string) --* 
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 30
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass
