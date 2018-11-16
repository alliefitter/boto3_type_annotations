from typing import NoReturn
from typing import Dict
from botocore.waiter import Waiter


class DistributionDeployed(Waiter):
    def wait(self, Id: str, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2018-06-18/GetDistribution>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Id=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Id: string
        :param Id: **[REQUIRED]** 
        
          The distribution\'s ID.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 60
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 25
        
        :returns: None
        """
        pass


class InvalidationCompleted(Waiter):
    def wait(self, DistributionId: str, Id: str, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2018-06-18/GetInvalidation>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              DistributionId=\'string\',
              Id=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type DistributionId: string
        :param DistributionId: **[REQUIRED]** 
        
          The distribution\'s ID.
        
        :type Id: string
        :param Id: **[REQUIRED]** 
        
          The identifier for the invalidation request, for example, ``IDFDVBD632BHDS5`` .
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 20
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 30
        
        :returns: None
        """
        pass


class StreamingDistributionDeployed(Waiter):
    def wait(self, Id: str, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2018-06-18/GetStreamingDistribution>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Id=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Id: string
        :param Id: **[REQUIRED]** 
        
          The streaming distribution\'s ID.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 60
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 25
        
        :returns: None
        """
        pass
