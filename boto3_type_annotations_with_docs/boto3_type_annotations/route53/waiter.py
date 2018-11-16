from typing import Dict
from botocore.waiter import Waiter


class ResourceRecordSetsChanged(Waiter):
    def wait(self, Id: str, WaiterConfig: Dict = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetChange>`_
        
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
        
          The ID of the change batch request. The value that you specify here is the value that ``ChangeResourceRecordSets`` returned in the ``Id`` element when you submitted the request.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 30
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 60
        
        :returns: None
        """
        pass
