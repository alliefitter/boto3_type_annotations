from typing import Dict
from botocore.waiter import Waiter


class JobComplete(Waiter):
    def wait(self, Id: str, WaiterConfig: Dict = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elastictranscoder-2012-09-25/ReadJob>`_
        
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
        
          The identifier of the job for which you want to get detailed information.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 30
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 120
        
        :returns: None
        """
        pass
