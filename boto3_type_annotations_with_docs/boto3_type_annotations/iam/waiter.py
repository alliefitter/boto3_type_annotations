from typing import Dict
from botocore.waiter import Waiter


class InstanceProfileExists(Waiter):
    def wait(self, InstanceProfileName: str, WaiterConfig: Dict = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/GetInstanceProfile>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              InstanceProfileName=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type InstanceProfileName: string
        :param InstanceProfileName: **[REQUIRED]** 
        
          The name of the instance profile to get information about.
        
          This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 1
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class UserExists(Waiter):
    def wait(self, UserName: str = None, WaiterConfig: Dict = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/GetUser>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              UserName=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type UserName: string
        :param UserName: 
        
          The name of the user to get information about.
        
          This parameter is optional. If it is not included, it defaults to the user making the request. This parameter allows (per its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 1
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 20
        
        :returns: None
        """
        pass
