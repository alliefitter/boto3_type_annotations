from typing import Dict
from botocore.paginate import Paginator


class GetExecutionHistory(Paginator):
    def paginate(self, executionArn: str, reverseOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/GetExecutionHistory>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              executionArn=\'string\',
              reverseOrder=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type executionArn: string
        :param executionArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the execution.
        
        :type reverseOrder: boolean
        :param reverseOrder: 
        
          Lists events in descending order of their ``timeStamp`` .
        
        :type PaginationConfig: dict
        :param PaginationConfig: 
        
          A dictionary that provides parameters to control pagination.
        
          - **MaxItems** *(integer) --* 
        
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
        
          - **PageSize** *(integer) --* 
        
            The size of each page.
        
          - **StartingToken** *(string) --* 
        
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'events\': [
                    {
                        \'timestamp\': datetime(2015, 1, 1),
                        \'type\': \'ActivityFailed\'|\'ActivityScheduleFailed\'|\'ActivityScheduled\'|\'ActivityStarted\'|\'ActivitySucceeded\'|\'ActivityTimedOut\'|\'ChoiceStateEntered\'|\'ChoiceStateExited\'|\'ExecutionFailed\'|\'ExecutionStarted\'|\'ExecutionSucceeded\'|\'ExecutionAborted\'|\'ExecutionTimedOut\'|\'FailStateEntered\'|\'LambdaFunctionFailed\'|\'LambdaFunctionScheduleFailed\'|\'LambdaFunctionScheduled\'|\'LambdaFunctionStartFailed\'|\'LambdaFunctionStarted\'|\'LambdaFunctionSucceeded\'|\'LambdaFunctionTimedOut\'|\'SucceedStateEntered\'|\'SucceedStateExited\'|\'TaskStateAborted\'|\'TaskStateEntered\'|\'TaskStateExited\'|\'PassStateEntered\'|\'PassStateExited\'|\'ParallelStateAborted\'|\'ParallelStateEntered\'|\'ParallelStateExited\'|\'ParallelStateFailed\'|\'ParallelStateStarted\'|\'ParallelStateSucceeded\'|\'WaitStateAborted\'|\'WaitStateEntered\'|\'WaitStateExited\',
                        \'id\': 123,
                        \'previousEventId\': 123,
                        \'activityFailedEventDetails\': {
                            \'error\': \'string\',
                            \'cause\': \'string\'
                        },
                        \'activityScheduleFailedEventDetails\': {
                            \'error\': \'string\',
                            \'cause\': \'string\'
                        },
                        \'activityScheduledEventDetails\': {
                            \'resource\': \'string\',
                            \'input\': \'string\',
                            \'timeoutInSeconds\': 123,
                            \'heartbeatInSeconds\': 123
                        },
                        \'activityStartedEventDetails\': {
                            \'workerName\': \'string\'
                        },
                        \'activitySucceededEventDetails\': {
                            \'output\': \'string\'
                        },
                        \'activityTimedOutEventDetails\': {
                            \'error\': \'string\',
                            \'cause\': \'string\'
                        },
                        \'executionFailedEventDetails\': {
                            \'error\': \'string\',
                            \'cause\': \'string\'
                        },
                        \'executionStartedEventDetails\': {
                            \'input\': \'string\',
                            \'roleArn\': \'string\'
                        },
                        \'executionSucceededEventDetails\': {
                            \'output\': \'string\'
                        },
                        \'executionAbortedEventDetails\': {
                            \'error\': \'string\',
                            \'cause\': \'string\'
                        },
                        \'executionTimedOutEventDetails\': {
                            \'error\': \'string\',
                            \'cause\': \'string\'
                        },
                        \'lambdaFunctionFailedEventDetails\': {
                            \'error\': \'string\',
                            \'cause\': \'string\'
                        },
                        \'lambdaFunctionScheduleFailedEventDetails\': {
                            \'error\': \'string\',
                            \'cause\': \'string\'
                        },
                        \'lambdaFunctionScheduledEventDetails\': {
                            \'resource\': \'string\',
                            \'input\': \'string\',
                            \'timeoutInSeconds\': 123
                        },
                        \'lambdaFunctionStartFailedEventDetails\': {
                            \'error\': \'string\',
                            \'cause\': \'string\'
                        },
                        \'lambdaFunctionSucceededEventDetails\': {
                            \'output\': \'string\'
                        },
                        \'lambdaFunctionTimedOutEventDetails\': {
                            \'error\': \'string\',
                            \'cause\': \'string\'
                        },
                        \'stateEnteredEventDetails\': {
                            \'name\': \'string\',
                            \'input\': \'string\'
                        },
                        \'stateExitedEventDetails\': {
                            \'name\': \'string\',
                            \'output\': \'string\'
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **events** *(list) --* 
        
              The list of events that occurred in the execution.
        
              - *(dict) --* 
        
                Contains details about the events of an execution.
        
                - **timestamp** *(datetime) --* 
        
                  The date the event occurred.
        
                - **type** *(string) --* 
        
                  The type of the event.
        
                - **id** *(integer) --* 
        
                  The id of the event. Events are numbered sequentially, starting at one.
        
                - **previousEventId** *(integer) --* 
        
                  The id of the previous event.
        
                - **activityFailedEventDetails** *(dict) --* 
        
                  Contains details about an activity which failed during an execution.
        
                  - **error** *(string) --* 
        
                    The error code of the failure.
        
                  - **cause** *(string) --* 
        
                    A more detailed explanation of the cause of the failure.
        
                - **activityScheduleFailedEventDetails** *(dict) --* 
        
                  Contains details about an activity schedule event which failed during an execution.
        
                  - **error** *(string) --* 
        
                    The error code of the failure.
        
                  - **cause** *(string) --* 
        
                    A more detailed explanation of the cause of the failure.
        
                - **activityScheduledEventDetails** *(dict) --* 
        
                  Contains details about an activity scheduled during an execution.
        
                  - **resource** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the scheduled activity.
        
                  - **input** *(string) --* 
        
                    The JSON data input to the activity task.
        
                  - **timeoutInSeconds** *(integer) --* 
        
                    The maximum allowed duration of the activity task.
        
                  - **heartbeatInSeconds** *(integer) --* 
        
                    The maximum allowed duration between two heartbeats for the activity task.
        
                - **activityStartedEventDetails** *(dict) --* 
        
                  Contains details about the start of an activity during an execution.
        
                  - **workerName** *(string) --* 
        
                    The name of the worker that the task is assigned to. These names are provided by the workers when calling  GetActivityTask .
        
                - **activitySucceededEventDetails** *(dict) --* 
        
                  Contains details about an activity which successfully terminated during an execution.
        
                  - **output** *(string) --* 
        
                    The JSON data output by the activity task.
        
                - **activityTimedOutEventDetails** *(dict) --* 
        
                  Contains details about an activity timeout which occurred during an execution.
        
                  - **error** *(string) --* 
        
                    The error code of the failure.
        
                  - **cause** *(string) --* 
        
                    A more detailed explanation of the cause of the timeout.
        
                - **executionFailedEventDetails** *(dict) --* 
        
                  Contains details about an execution failure event.
        
                  - **error** *(string) --* 
        
                    The error code of the failure.
        
                  - **cause** *(string) --* 
        
                    A more detailed explanation of the cause of the failure.
        
                - **executionStartedEventDetails** *(dict) --* 
        
                  Contains details about the start of the execution.
        
                  - **input** *(string) --* 
        
                    The JSON data input to the execution.
        
                  - **roleArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the IAM role used for executing AWS Lambda tasks.
        
                - **executionSucceededEventDetails** *(dict) --* 
        
                  Contains details about the successful termination of the execution.
        
                  - **output** *(string) --* 
        
                    The JSON data output by the execution.
        
                - **executionAbortedEventDetails** *(dict) --* 
        
                  Contains details about an abort of an execution.
        
                  - **error** *(string) --* 
        
                    The error code of the failure.
        
                  - **cause** *(string) --* 
        
                    A more detailed explanation of the cause of the failure.
        
                - **executionTimedOutEventDetails** *(dict) --* 
        
                  Contains details about the execution timeout which occurred during the execution.
        
                  - **error** *(string) --* 
        
                    The error code of the failure.
        
                  - **cause** *(string) --* 
        
                    A more detailed explanation of the cause of the timeout.
        
                - **lambdaFunctionFailedEventDetails** *(dict) --* 
        
                  Contains details about a lambda function which failed during an execution.
        
                  - **error** *(string) --* 
        
                    The error code of the failure.
        
                  - **cause** *(string) --* 
        
                    A more detailed explanation of the cause of the failure.
        
                - **lambdaFunctionScheduleFailedEventDetails** *(dict) --* 
        
                  Contains details about a failed lambda function schedule event which occurred during an execution.
        
                  - **error** *(string) --* 
        
                    The error code of the failure.
        
                  - **cause** *(string) --* 
        
                    A more detailed explanation of the cause of the failure.
        
                - **lambdaFunctionScheduledEventDetails** *(dict) --* 
        
                  Contains details about a lambda function scheduled during an execution.
        
                  - **resource** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the scheduled lambda function.
        
                  - **input** *(string) --* 
        
                    The JSON data input to the lambda function.
        
                  - **timeoutInSeconds** *(integer) --* 
        
                    The maximum allowed duration of the lambda function.
        
                - **lambdaFunctionStartFailedEventDetails** *(dict) --* 
        
                  Contains details about a lambda function which failed to start during an execution.
        
                  - **error** *(string) --* 
        
                    The error code of the failure.
        
                  - **cause** *(string) --* 
        
                    A more detailed explanation of the cause of the failure.
        
                - **lambdaFunctionSucceededEventDetails** *(dict) --* 
        
                  Contains details about a lambda function which terminated successfully during an execution.
        
                  - **output** *(string) --* 
        
                    The JSON data output by the lambda function.
        
                - **lambdaFunctionTimedOutEventDetails** *(dict) --* 
        
                  Contains details about a lambda function timeout which occurred during an execution.
        
                  - **error** *(string) --* 
        
                    The error code of the failure.
        
                  - **cause** *(string) --* 
        
                    A more detailed explanation of the cause of the timeout.
        
                - **stateEnteredEventDetails** *(dict) --* 
        
                  Contains details about a state entered during an execution.
        
                  - **name** *(string) --* 
        
                    The name of the state.
        
                  - **input** *(string) --* 
        
                    The string that contains the JSON input data for the state.
        
                - **stateExitedEventDetails** *(dict) --* 
        
                  Contains details about an exit from a state during an execution.
        
                  - **name** *(string) --* 
        
                    The name of the state.
        
                    A name must *not* contain:
        
                    * whitespace 
                     
                    * brackets ``< > { } [ ]``   
                     
                    * wildcard characters ``? *``   
                     
                    * special characters ``\" # % \ ^ | ~ ` $ & , ; : /``   
                     
                    * control characters (``U+0000-001F`` , ``U+007F-009F`` ) 
                     
                  - **output** *(string) --* 
        
                    The JSON output data of the state.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListActivities(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/ListActivities>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig: 
        
          A dictionary that provides parameters to control pagination.
        
          - **MaxItems** *(integer) --* 
        
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
        
          - **PageSize** *(integer) --* 
        
            The size of each page.
        
          - **StartingToken** *(string) --* 
        
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'activities\': [
                    {
                        \'activityArn\': \'string\',
                        \'name\': \'string\',
                        \'creationDate\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **activities** *(list) --* 
        
              The list of activities.
        
              - *(dict) --* 
        
                Contains details about an activity.
        
                - **activityArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that identifies the activity.
        
                - **name** *(string) --* 
        
                  The name of the activity.
        
                  A name must *not* contain:
        
                  * whitespace 
                   
                  * brackets ``< > { } [ ]``   
                   
                  * wildcard characters ``? *``   
                   
                  * special characters ``\" # % \ ^ | ~ ` $ & , ; : /``   
                   
                  * control characters (``U+0000-001F`` , ``U+007F-009F`` ) 
                   
                - **creationDate** *(datetime) --* 
        
                  The date the activity is created.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListExecutions(Paginator):
    def paginate(self, stateMachineArn: str, statusFilter: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/ListExecutions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              stateMachineArn=\'string\',
              statusFilter=\'RUNNING\'|\'SUCCEEDED\'|\'FAILED\'|\'TIMED_OUT\'|\'ABORTED\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type stateMachineArn: string
        :param stateMachineArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the state machine whose executions is listed.
        
        :type statusFilter: string
        :param statusFilter: 
        
          If specified, only list the executions whose current execution status matches the given filter.
        
        :type PaginationConfig: dict
        :param PaginationConfig: 
        
          A dictionary that provides parameters to control pagination.
        
          - **MaxItems** *(integer) --* 
        
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
        
          - **PageSize** *(integer) --* 
        
            The size of each page.
        
          - **StartingToken** *(string) --* 
        
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'executions\': [
                    {
                        \'executionArn\': \'string\',
                        \'stateMachineArn\': \'string\',
                        \'name\': \'string\',
                        \'status\': \'RUNNING\'|\'SUCCEEDED\'|\'FAILED\'|\'TIMED_OUT\'|\'ABORTED\',
                        \'startDate\': datetime(2015, 1, 1),
                        \'stopDate\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **executions** *(list) --* 
        
              The list of matching executions.
        
              - *(dict) --* 
        
                Contains details about an execution.
        
                - **executionArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that identifies the execution.
        
                - **stateMachineArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the executed state machine.
        
                - **name** *(string) --* 
        
                  The name of the execution.
        
                  A name must *not* contain:
        
                  * whitespace 
                   
                  * brackets ``< > { } [ ]``   
                   
                  * wildcard characters ``? *``   
                   
                  * special characters ``\" # % \ ^ | ~ ` $ & , ; : /``   
                   
                  * control characters (``U+0000-001F`` , ``U+007F-009F`` ) 
                   
                - **status** *(string) --* 
        
                  The current status of the execution.
        
                - **startDate** *(datetime) --* 
        
                  The date the execution started.
        
                - **stopDate** *(datetime) --* 
        
                  If the execution already ended, the date the execution stopped.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListStateMachines(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/ListStateMachines>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig: 
        
          A dictionary that provides parameters to control pagination.
        
          - **MaxItems** *(integer) --* 
        
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
        
          - **PageSize** *(integer) --* 
        
            The size of each page.
        
          - **StartingToken** *(string) --* 
        
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'stateMachines\': [
                    {
                        \'stateMachineArn\': \'string\',
                        \'name\': \'string\',
                        \'creationDate\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **stateMachines** *(list) --* 
              
              - *(dict) --* 
        
                Contains details about the state machine.
        
                - **stateMachineArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that identifies the state machine.
        
                - **name** *(string) --* 
        
                  The name of the state machine.
        
                  A name must *not* contain:
        
                  * whitespace 
                   
                  * brackets ``< > { } [ ]``   
                   
                  * wildcard characters ``? *``   
                   
                  * special characters ``\" # % \ ^ | ~ ` $ & , ; : /``   
                   
                  * control characters (``U+0000-001F`` , ``U+007F-009F`` ) 
                   
                - **creationDate** *(datetime) --* 
        
                  The date the state machine is created.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
