from typing import NoReturn
from typing import Dict
from botocore.waiter import Waiter


class EndpointDeleted(Waiter):
    def wait(self, EndpointName: str, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeEndpoint>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              EndpointName=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type EndpointName: string
        :param EndpointName: **[REQUIRED]** 
        
          The name of the endpoint.
        
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


class EndpointInService(Waiter):
    def wait(self, EndpointName: str, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeEndpoint>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              EndpointName=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type EndpointName: string
        :param EndpointName: **[REQUIRED]** 
        
          The name of the endpoint.
        
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


class NotebookInstanceDeleted(Waiter):
    def wait(self, NotebookInstanceName: str, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeNotebookInstance>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              NotebookInstanceName=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type NotebookInstanceName: string
        :param NotebookInstanceName: **[REQUIRED]** 
        
          The name of the notebook instance that you want information about.
        
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


class NotebookInstanceInService(Waiter):
    def wait(self, NotebookInstanceName: str, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeNotebookInstance>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              NotebookInstanceName=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type NotebookInstanceName: string
        :param NotebookInstanceName: **[REQUIRED]** 
        
          The name of the notebook instance that you want information about.
        
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


class NotebookInstanceStopped(Waiter):
    def wait(self, NotebookInstanceName: str, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeNotebookInstance>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              NotebookInstanceName=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type NotebookInstanceName: string
        :param NotebookInstanceName: **[REQUIRED]** 
        
          The name of the notebook instance that you want information about.
        
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


class TrainingJobCompletedOrStopped(Waiter):
    def wait(self, TrainingJobName: str, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeTrainingJob>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              TrainingJobName=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type TrainingJobName: string
        :param TrainingJobName: **[REQUIRED]** 
        
          The name of the training job.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 120
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 180
        
        :returns: None
        """
        pass


class TransformJobCompletedOrStopped(Waiter):
    def wait(self, TransformJobName: str, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeTransformJob>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              TransformJobName=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type TransformJobName: string
        :param TransformJobName: **[REQUIRED]** 
        
          The name of the transform job that you want to view details of.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 60
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 60
        
        :returns: None
        """
        pass
