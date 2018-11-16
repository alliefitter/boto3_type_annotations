from typing import NoReturn
from typing import Dict
from botocore.waiter import Waiter


class SuccessfulSigningJob(Waiter):
    def wait(self, jobId: str, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/signer-2017-08-25/DescribeSigningJob>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              jobId=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type jobId: string
        :param jobId: **[REQUIRED]** 
        
          The ID of the signing job on input.
        
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
