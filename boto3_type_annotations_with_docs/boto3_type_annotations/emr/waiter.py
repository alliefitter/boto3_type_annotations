from typing import Dict
from botocore.waiter import Waiter


class ClusterRunning(Waiter):
    def wait(self, ClusterId: str, WaiterConfig: Dict = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/DescribeCluster>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              ClusterId=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type ClusterId: string
        :param ClusterId: **[REQUIRED]** 
        
          The identifier of the cluster to describe.
        
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


class ClusterTerminated(Waiter):
    def wait(self, ClusterId: str, WaiterConfig: Dict = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/DescribeCluster>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              ClusterId=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type ClusterId: string
        :param ClusterId: **[REQUIRED]** 
        
          The identifier of the cluster to describe.
        
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


class StepComplete(Waiter):
    def wait(self, ClusterId: str, StepId: str, WaiterConfig: Dict = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/DescribeStep>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              ClusterId=\'string\',
              StepId=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type ClusterId: string
        :param ClusterId: **[REQUIRED]** 
        
          The identifier of the cluster with steps to describe.
        
        :type StepId: string
        :param StepId: **[REQUIRED]** 
        
          The identifier of the step to describe.
        
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
