from typing import Dict
from botocore.waiter import Waiter


class FunctionExists(Waiter):
    def wait(self, FunctionName: str, Qualifier: str = None, WaiterConfig: Dict = None):
        """
        Polls :py:meth:`Lambda.Client.get_function` every 1 seconds until a successful state is reached. An error is returned after 20 failed checks.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetFunction>`_
        
        **Request Syntax**
        ::
          waiter.wait(
              FunctionName='string',
              Qualifier='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**
          The name of the Lambda function, version, or alias.
           **Name formats**
          * **Function name** - ``my-function`` (name-only), ``my-function:v1`` (with alias).
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .
          * **Partial ARN** - ``123456789012:function:my-function`` .
          You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        :type Qualifier: string
        :param Qualifier:
          Specify a version or alias to get details about a published version of the function.
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
