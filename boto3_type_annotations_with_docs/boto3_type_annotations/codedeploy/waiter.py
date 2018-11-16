from typing import NoReturn
from typing import Dict
from botocore.waiter import Waiter


class DeploymentSuccessful(Waiter):
    def wait(self, deploymentId: str, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/GetDeployment>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              deploymentId=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type deploymentId: string
        :param deploymentId: **[REQUIRED]** 
        
          A deployment ID associated with the applicable IAM user or AWS account.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 120
        
        :returns: None
        """
        pass
