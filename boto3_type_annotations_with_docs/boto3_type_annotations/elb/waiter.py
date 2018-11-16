from typing import List
from typing import Dict
from botocore.waiter import Waiter


class AnyInstanceInService(Waiter):
    def wait(self, LoadBalancerName: str, Instances: List = None, WaiterConfig: Dict = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/DescribeInstanceHealth>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              LoadBalancerName=\'string\',
              Instances=[
                  {
                      \'InstanceId\': \'string\'
                  },
              ],
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type Instances: list
        :param Instances: 
        
          The IDs of the instances.
        
          - *(dict) --* 
        
            The ID of an EC2 instance.
        
            - **InstanceId** *(string) --* 
        
              The instance ID.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class InstanceDeregistered(Waiter):
    def wait(self, LoadBalancerName: str, Instances: List = None, WaiterConfig: Dict = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/DescribeInstanceHealth>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              LoadBalancerName=\'string\',
              Instances=[
                  {
                      \'InstanceId\': \'string\'
                  },
              ],
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type Instances: list
        :param Instances: 
        
          The IDs of the instances.
        
          - *(dict) --* 
        
            The ID of an EC2 instance.
        
            - **InstanceId** *(string) --* 
        
              The instance ID.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class InstanceInService(Waiter):
    def wait(self, LoadBalancerName: str, Instances: List = None, WaiterConfig: Dict = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/DescribeInstanceHealth>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              LoadBalancerName=\'string\',
              Instances=[
                  {
                      \'InstanceId\': \'string\'
                  },
              ],
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type Instances: list
        :param Instances: 
        
          The IDs of the instances.
        
          - *(dict) --* 
        
            The ID of an EC2 instance.
        
            - **InstanceId** *(string) --* 
        
              The instance ID.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass
