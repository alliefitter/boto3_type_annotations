from typing import NoReturn
from typing import List
from typing import Dict
from botocore.waiter import Waiter


class LoadBalancerAvailable(Waiter):
    def wait(self, LoadBalancerArns: List = None, Names: List = None, Marker: str = None, PageSize: int = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancers>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              LoadBalancerArns=[
                  \'string\',
              ],
              Names=[
                  \'string\',
              ],
              Marker=\'string\',
              PageSize=123,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type LoadBalancerArns: list
        :param LoadBalancerArns: 
        
          The Amazon Resource Names (ARN) of the load balancers. You can specify up to 20 load balancers in a single call.
        
          - *(string) --* 
        
        :type Names: list
        :param Names: 
        
          The names of the load balancers.
        
          - *(string) --* 
        
        :type Marker: string
        :param Marker: 
        
          The marker for the next set of results. (You received this marker from a previous call.)
        
        :type PageSize: integer
        :param PageSize: 
        
          The maximum number of results to return with this call.
        
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


class LoadBalancerExists(Waiter):
    def wait(self, LoadBalancerArns: List = None, Names: List = None, Marker: str = None, PageSize: int = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancers>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              LoadBalancerArns=[
                  \'string\',
              ],
              Names=[
                  \'string\',
              ],
              Marker=\'string\',
              PageSize=123,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type LoadBalancerArns: list
        :param LoadBalancerArns: 
        
          The Amazon Resource Names (ARN) of the load balancers. You can specify up to 20 load balancers in a single call.
        
          - *(string) --* 
        
        :type Names: list
        :param Names: 
        
          The names of the load balancers.
        
          - *(string) --* 
        
        :type Marker: string
        :param Marker: 
        
          The marker for the next set of results. (You received this marker from a previous call.)
        
        :type PageSize: integer
        :param PageSize: 
        
          The maximum number of results to return with this call.
        
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


class LoadBalancersDeleted(Waiter):
    def wait(self, LoadBalancerArns: List = None, Names: List = None, Marker: str = None, PageSize: int = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancers>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              LoadBalancerArns=[
                  \'string\',
              ],
              Names=[
                  \'string\',
              ],
              Marker=\'string\',
              PageSize=123,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type LoadBalancerArns: list
        :param LoadBalancerArns: 
        
          The Amazon Resource Names (ARN) of the load balancers. You can specify up to 20 load balancers in a single call.
        
          - *(string) --* 
        
        :type Names: list
        :param Names: 
        
          The names of the load balancers.
        
          - *(string) --* 
        
        :type Marker: string
        :param Marker: 
        
          The marker for the next set of results. (You received this marker from a previous call.)
        
        :type PageSize: integer
        :param PageSize: 
        
          The maximum number of results to return with this call.
        
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


class TargetDeregistered(Waiter):
    def wait(self, TargetGroupArn: str, Targets: List = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeTargetHealth>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              TargetGroupArn=\'string\',
              Targets=[
                  {
                      \'Id\': \'string\',
                      \'Port\': 123,
                      \'AvailabilityZone\': \'string\'
                  },
              ],
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type TargetGroupArn: string
        :param TargetGroupArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the target group.
        
        :type Targets: list
        :param Targets: 
        
          The targets.
        
          - *(dict) --* 
        
            Information about a target.
        
            - **Id** *(string) --* **[REQUIRED]** 
        
              The ID of the target. If the target type of the target group is ``instance`` , specify an instance ID. If the target type is ``ip`` , specify an IP address.
        
            - **Port** *(integer) --* 
        
              The port on which the target is listening.
        
            - **AvailabilityZone** *(string) --* 
        
              An Availability Zone or ``all`` . This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer.
        
              This parameter is not supported if the target type of the target group is ``instance`` . If the IP address is in a subnet of the VPC for the target group, the Availability Zone is automatically detected and this parameter is optional. If the IP address is outside the VPC, this parameter is required.
        
              With an Application Load Balancer, if the IP address is outside the VPC for the target group, the only supported value is ``all`` .
        
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


class TargetInService(Waiter):
    def wait(self, TargetGroupArn: str, Targets: List = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeTargetHealth>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              TargetGroupArn=\'string\',
              Targets=[
                  {
                      \'Id\': \'string\',
                      \'Port\': 123,
                      \'AvailabilityZone\': \'string\'
                  },
              ],
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type TargetGroupArn: string
        :param TargetGroupArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the target group.
        
        :type Targets: list
        :param Targets: 
        
          The targets.
        
          - *(dict) --* 
        
            Information about a target.
        
            - **Id** *(string) --* **[REQUIRED]** 
        
              The ID of the target. If the target type of the target group is ``instance`` , specify an instance ID. If the target type is ``ip`` , specify an IP address.
        
            - **Port** *(integer) --* 
        
              The port on which the target is listening.
        
            - **AvailabilityZone** *(string) --* 
        
              An Availability Zone or ``all`` . This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer.
        
              This parameter is not supported if the target type of the target group is ``instance`` . If the IP address is in a subnet of the VPC for the target group, the Availability Zone is automatically detected and this parameter is optional. If the IP address is outside the VPC, this parameter is required.
        
              With an Application Load Balancer, if the IP address is outside the VPC for the target group, the only supported value is ``all`` .
        
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
