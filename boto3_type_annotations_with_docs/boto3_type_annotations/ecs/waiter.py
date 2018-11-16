from typing import NoReturn
from typing import List
from typing import Dict
from botocore.waiter import Waiter


class ServicesInactive(Waiter):
    def wait(self, services: List, cluster: str = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeServices>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              cluster=\'string\',
              services=[
                  \'string\',
              ],
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type cluster: string
        :param cluster: 
        
          The short name or full Amazon Resource Name (ARN)the cluster that hosts the service to describe. If you do not specify a cluster, the default cluster is assumed.
        
        :type services: list
        :param services: **[REQUIRED]** 
        
          A list of services to describe. You may specify up to 10 services to describe in a single operation.
        
          - *(string) --* 
        
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


class ServicesStable(Waiter):
    def wait(self, services: List, cluster: str = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeServices>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              cluster=\'string\',
              services=[
                  \'string\',
              ],
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type cluster: string
        :param cluster: 
        
          The short name or full Amazon Resource Name (ARN)the cluster that hosts the service to describe. If you do not specify a cluster, the default cluster is assumed.
        
        :type services: list
        :param services: **[REQUIRED]** 
        
          A list of services to describe. You may specify up to 10 services to describe in a single operation.
        
          - *(string) --* 
        
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


class TasksRunning(Waiter):
    def wait(self, tasks: List, cluster: str = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeTasks>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              cluster=\'string\',
              tasks=[
                  \'string\',
              ],
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type cluster: string
        :param cluster: 
        
          The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task to describe. If you do not specify a cluster, the default cluster is assumed.
        
        :type tasks: list
        :param tasks: **[REQUIRED]** 
        
          A list of up to 100 task IDs or full ARN entries.
        
          - *(string) --* 
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 6
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 100
        
        :returns: None
        """
        pass


class TasksStopped(Waiter):
    def wait(self, tasks: List, cluster: str = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeTasks>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              cluster=\'string\',
              tasks=[
                  \'string\',
              ],
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type cluster: string
        :param cluster: 
        
          The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task to describe. If you do not specify a cluster, the default cluster is assumed.
        
        :type tasks: list
        :param tasks: **[REQUIRED]** 
        
          A list of up to 100 task IDs or full ARN entries.
        
          - *(string) --* 
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 6
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 100
        
        :returns: None
        """
        pass
