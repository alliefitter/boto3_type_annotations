from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Union
from typing import List


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        """
        Check if an operation can be paginated.
        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you\'d normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator(\"create_foo\")``.
        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """
        pass

    def create_activity(self, name: str, tags: List = None) -> Dict:
        """
        Creates an activity. An activity is a task that you write in any programming language and host on any machine that has access to AWS Step Functions. Activities must poll Step Functions using the ``GetActivityTask`` API action and respond using ``SendTask*`` API actions. This function lets Step Functions know the existence of your activity and returns an identifier for use in a state machine and when polling from the activity.
        .. note::
          This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/CreateActivity>`_
        
        **Request Syntax**
        ::
          response = client.create_activity(
              name='string',
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'activityArn': 'string',
                'creationDate': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            - **activityArn** *(string) --* 
              The Amazon Resource Name (ARN) that identifies the created activity.
            - **creationDate** *(datetime) --* 
              The date the activity is created.
        :type name: string
        :param name: **[REQUIRED]**
          The name of the activity to create. This name must be unique for your AWS account and region for 90 days. For more information, see `Limits Related to State Machine Executions <https://docs.aws.amazon.com/step-functions/latest/dg/limits.html#service-limits-state-machine-executions>`__ in the *AWS Step Functions Developer Guide* .
          A name must *not* contain:
          * whitespace
          * brackets ``< > { } [ ]``
          * wildcard characters ``? *``
          * special characters ``\" # % \ ^ | ~ ` $ & , ; : /``
          * control characters (``U+0000-001F`` , ``U+007F-009F`` )
        :type tags: list
        :param tags:
          The list of tags to add to a resource.
          - *(dict) --*
            Tags are key-value pairs that can be associated with Step Functions state machines and activities.
            - **key** *(string) --*
              The key of a tag.
            - **value** *(string) --*
              The value of a tag.
        :rtype: dict
        :returns:
        """
        pass

    def create_state_machine(self, name: str, definition: str, roleArn: str, tags: List = None) -> Dict:
        """
        Creates a state machine. A state machine consists of a collection of states that can do work (``Task`` states), determine to which states to transition next (``Choice`` states), stop an execution with an error (``Fail`` states), and so on. State machines are specified using a JSON-based, structured language.
        .. note::
          This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/CreateStateMachine>`_
        
        **Request Syntax**
        ::
          response = client.create_state_machine(
              name='string',
              definition='string',
              roleArn='string',
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'stateMachineArn': 'string',
                'creationDate': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            - **stateMachineArn** *(string) --* 
              The Amazon Resource Name (ARN) that identifies the created state machine.
            - **creationDate** *(datetime) --* 
              The date the state machine is created.
        :type name: string
        :param name: **[REQUIRED]**
          The name of the state machine.
          A name must *not* contain:
          * whitespace
          * brackets ``< > { } [ ]``
          * wildcard characters ``? *``
          * special characters ``\" # % \ ^ | ~ ` $ & , ; : /``
          * control characters (``U+0000-001F`` , ``U+007F-009F`` )
        :type definition: string
        :param definition: **[REQUIRED]**
          The Amazon States Language definition of the state machine. See `Amazon States Language <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html>`__ .
        :type roleArn: string
        :param roleArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the IAM role to use for this state machine.
        :type tags: list
        :param tags:
          Tags to be added when creating a state machine.
          - *(dict) --*
            Tags are key-value pairs that can be associated with Step Functions state machines and activities.
            - **key** *(string) --*
              The key of a tag.
            - **value** *(string) --*
              The value of a tag.
        :rtype: dict
        :returns:
        """
        pass

    def delete_activity(self, activityArn: str) -> Dict:
        """
        Deletes an activity.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/DeleteActivity>`_
        
        **Request Syntax**
        ::
          response = client.delete_activity(
              activityArn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type activityArn: string
        :param activityArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the activity to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_state_machine(self, stateMachineArn: str) -> Dict:
        """
        Deletes a state machine. This is an asynchronous operation: It sets the state machine's status to ``DELETING`` and begins the deletion process. Each state machine execution is deleted the next time it makes a state transition.
        .. note::
          The state machine itself is deleted after all executions are completed or deleted.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/DeleteStateMachine>`_
        
        **Request Syntax**
        ::
          response = client.delete_state_machine(
              stateMachineArn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type stateMachineArn: string
        :param stateMachineArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the state machine to delete.
        :rtype: dict
        :returns:
        """
        pass

    def describe_activity(self, activityArn: str) -> Dict:
        """
        Describes an activity.
        .. note::
          This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/DescribeActivity>`_
        
        **Request Syntax**
        ::
          response = client.describe_activity(
              activityArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'activityArn': 'string',
                'name': 'string',
                'creationDate': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            - **activityArn** *(string) --* 
              The Amazon Resource Name (ARN) that identifies the activity.
            - **name** *(string) --* 
              The name of the activity.
              A name must *not* contain:
              * whitespace 
              * brackets ``< > { } [ ]``   
              * wildcard characters ``? *``   
              * special characters ``" # % \ ^ | ~ ` $ & , ; : /``   
              * control characters (``U+0000-001F`` , ``U+007F-009F`` ) 
            - **creationDate** *(datetime) --* 
              The date the activity is created.
        :type activityArn: string
        :param activityArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the activity to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_execution(self, executionArn: str) -> Dict:
        """
        Describes an execution.
        .. note::
          This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/DescribeExecution>`_
        
        **Request Syntax**
        ::
          response = client.describe_execution(
              executionArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'executionArn': 'string',
                'stateMachineArn': 'string',
                'name': 'string',
                'status': 'RUNNING'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'ABORTED',
                'startDate': datetime(2015, 1, 1),
                'stopDate': datetime(2015, 1, 1),
                'input': 'string',
                'output': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **executionArn** *(string) --* 
              The Amazon Resource Name (ARN) that identifies the execution.
            - **stateMachineArn** *(string) --* 
              The Amazon Resource Name (ARN) of the executed stated machine.
            - **name** *(string) --* 
              The name of the execution.
              A name must *not* contain:
              * whitespace 
              * brackets ``< > { } [ ]``   
              * wildcard characters ``? *``   
              * special characters ``" # % \ ^ | ~ ` $ & , ; : /``   
              * control characters (``U+0000-001F`` , ``U+007F-009F`` ) 
            - **status** *(string) --* 
              The current status of the execution.
            - **startDate** *(datetime) --* 
              The date the execution is started.
            - **stopDate** *(datetime) --* 
              If the execution has already ended, the date the execution stopped.
            - **input** *(string) --* 
              The string that contains the JSON input data of the execution.
            - **output** *(string) --* 
              The JSON output data of the execution.
              .. note::
                This field is set only if the execution succeeds. If the execution fails, this field is null.
        :type executionArn: string
        :param executionArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the execution to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_state_machine(self, stateMachineArn: str) -> Dict:
        """
        Describes a state machine.
        .. note::
          This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/DescribeStateMachine>`_
        
        **Request Syntax**
        ::
          response = client.describe_state_machine(
              stateMachineArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'stateMachineArn': 'string',
                'name': 'string',
                'status': 'ACTIVE'|'DELETING',
                'definition': 'string',
                'roleArn': 'string',
                'creationDate': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            - **stateMachineArn** *(string) --* 
              The Amazon Resource Name (ARN) that identifies the state machine.
            - **name** *(string) --* 
              The name of the state machine.
              A name must *not* contain:
              * whitespace 
              * brackets ``< > { } [ ]``   
              * wildcard characters ``? *``   
              * special characters ``" # % \ ^ | ~ ` $ & , ; : /``   
              * control characters (``U+0000-001F`` , ``U+007F-009F`` ) 
            - **status** *(string) --* 
              The current status of the state machine.
            - **definition** *(string) --* 
              The Amazon States Language definition of the state machine. See `Amazon States Language <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html>`__ .
            - **roleArn** *(string) --* 
              The Amazon Resource Name (ARN) of the IAM role used when creating this state machine. (The IAM role maintains security by granting Step Functions access to AWS resources.)
            - **creationDate** *(datetime) --* 
              The date the state machine is created.
        :type stateMachineArn: string
        :param stateMachineArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the state machine to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_state_machine_for_execution(self, executionArn: str) -> Dict:
        """
        Describes the state machine associated with a specific execution.
        .. note::
          This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/DescribeStateMachineForExecution>`_
        
        **Request Syntax**
        ::
          response = client.describe_state_machine_for_execution(
              executionArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'stateMachineArn': 'string',
                'name': 'string',
                'definition': 'string',
                'roleArn': 'string',
                'updateDate': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            - **stateMachineArn** *(string) --* 
              The Amazon Resource Name (ARN) of the state machine associated with the execution.
            - **name** *(string) --* 
              The name of the state machine associated with the execution.
            - **definition** *(string) --* 
              The Amazon States Language definition of the state machine. See `Amazon States Language <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html>`__ .
            - **roleArn** *(string) --* 
              The Amazon Resource Name (ARN) of the IAM role of the State Machine for the execution. 
            - **updateDate** *(datetime) --* 
              The date and time the state machine associated with an execution was updated. For a newly created state machine, this is the creation date.
        :type executionArn: string
        :param executionArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the execution you want state machine information for.
        :rtype: dict
        :returns:
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        """
        Generate a presigned url given a client, its method, and arguments
        :type ClientMethod: string
        :param ClientMethod: The client method to presign for
        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.
        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)
        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method\'s model.
        :returns: The presigned url
        """
        pass

    def get_activity_task(self, activityArn: str, workerName: str = None) -> Dict:
        """
        Used by workers to retrieve a task (with the specified activity ARN) which has been scheduled for execution by a running state machine. This initiates a long poll, where the service holds the HTTP connection open and responds as soon as a task becomes available (i.e. an execution of a task of this type is needed.) The maximum time the service holds on to the request before responding is 60 seconds. If no task is available within 60 seconds, the poll returns a ``taskToken`` with a null string.
        .. warning::
          Workers should set their client side socket timeout to at least 65 seconds (5 seconds higher than the maximum time the service may hold the poll request).
          Polling with ``GetActivityTask`` can cause latency in some implementations. See `Avoid Latency When Polling for Activity Tasks <https://docs.aws.amazon.com/step-functions/latest/dg/bp-activity-pollers.html>`__ in the Step Functions Developer Guide.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/GetActivityTask>`_
        
        **Request Syntax**
        ::
          response = client.get_activity_task(
              activityArn='string',
              workerName='string'
          )
        
        **Response Syntax**
        ::
            {
                'taskToken': 'string',
                'input': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **taskToken** *(string) --* 
              A token that identifies the scheduled task. This token must be copied and included in subsequent calls to  SendTaskHeartbeat ,  SendTaskSuccess or  SendTaskFailure in order to report the progress or completion of the task.
            - **input** *(string) --* 
              The string that contains the JSON input data for the task.
        :type activityArn: string
        :param activityArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the activity to retrieve tasks from (assigned when you create the task using  CreateActivity .)
        :type workerName: string
        :param workerName:
          You can provide an arbitrary name in order to identify the worker that the task is assigned to. This name is used when it is logged in the execution history.
        :rtype: dict
        :returns:
        """
        pass

    def get_execution_history(self, executionArn: str, maxResults: int = None, reverseOrder: bool = None, nextToken: str = None) -> Dict:
        """
        Returns the history of the specified execution as a list of events. By default, the results are returned in ascending order of the ``timeStamp`` of the events. Use the ``reverseOrder`` parameter to get the latest events first.
        If ``nextToken`` is returned, there are more results available. The value of ``nextToken`` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/GetExecutionHistory>`_
        
        **Request Syntax**
        ::
          response = client.get_execution_history(
              executionArn='string',
              maxResults=123,
              reverseOrder=True|False,
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'events': [
                    {
                        'timestamp': datetime(2015, 1, 1),
                        'type': 'ActivityFailed'|'ActivityScheduleFailed'|'ActivityScheduled'|'ActivityStarted'|'ActivitySucceeded'|'ActivityTimedOut'|'ChoiceStateEntered'|'ChoiceStateExited'|'TaskFailed'|'TaskScheduled'|'TaskStartFailed'|'TaskStarted'|'TaskSubmitFailed'|'TaskSubmitted'|'TaskSucceeded'|'TaskTimedOut'|'ExecutionFailed'|'ExecutionStarted'|'ExecutionSucceeded'|'ExecutionAborted'|'ExecutionTimedOut'|'FailStateEntered'|'LambdaFunctionFailed'|'LambdaFunctionScheduleFailed'|'LambdaFunctionScheduled'|'LambdaFunctionStartFailed'|'LambdaFunctionStarted'|'LambdaFunctionSucceeded'|'LambdaFunctionTimedOut'|'SucceedStateEntered'|'SucceedStateExited'|'TaskStateAborted'|'TaskStateEntered'|'TaskStateExited'|'PassStateEntered'|'PassStateExited'|'ParallelStateAborted'|'ParallelStateEntered'|'ParallelStateExited'|'ParallelStateFailed'|'ParallelStateStarted'|'ParallelStateSucceeded'|'WaitStateAborted'|'WaitStateEntered'|'WaitStateExited',
                        'id': 123,
                        'previousEventId': 123,
                        'activityFailedEventDetails': {
                            'error': 'string',
                            'cause': 'string'
                        },
                        'activityScheduleFailedEventDetails': {
                            'error': 'string',
                            'cause': 'string'
                        },
                        'activityScheduledEventDetails': {
                            'resource': 'string',
                            'input': 'string',
                            'timeoutInSeconds': 123,
                            'heartbeatInSeconds': 123
                        },
                        'activityStartedEventDetails': {
                            'workerName': 'string'
                        },
                        'activitySucceededEventDetails': {
                            'output': 'string'
                        },
                        'activityTimedOutEventDetails': {
                            'error': 'string',
                            'cause': 'string'
                        },
                        'taskFailedEventDetails': {
                            'resourceType': 'string',
                            'resource': 'string',
                            'error': 'string',
                            'cause': 'string'
                        },
                        'taskScheduledEventDetails': {
                            'resourceType': 'string',
                            'resource': 'string',
                            'region': 'string',
                            'parameters': 'string',
                            'timeoutInSeconds': 123
                        },
                        'taskStartFailedEventDetails': {
                            'resourceType': 'string',
                            'resource': 'string',
                            'error': 'string',
                            'cause': 'string'
                        },
                        'taskStartedEventDetails': {
                            'resourceType': 'string',
                            'resource': 'string'
                        },
                        'taskSubmitFailedEventDetails': {
                            'resourceType': 'string',
                            'resource': 'string',
                            'error': 'string',
                            'cause': 'string'
                        },
                        'taskSubmittedEventDetails': {
                            'resourceType': 'string',
                            'resource': 'string',
                            'output': 'string'
                        },
                        'taskSucceededEventDetails': {
                            'resourceType': 'string',
                            'resource': 'string',
                            'output': 'string'
                        },
                        'taskTimedOutEventDetails': {
                            'resourceType': 'string',
                            'resource': 'string',
                            'error': 'string',
                            'cause': 'string'
                        },
                        'executionFailedEventDetails': {
                            'error': 'string',
                            'cause': 'string'
                        },
                        'executionStartedEventDetails': {
                            'input': 'string',
                            'roleArn': 'string'
                        },
                        'executionSucceededEventDetails': {
                            'output': 'string'
                        },
                        'executionAbortedEventDetails': {
                            'error': 'string',
                            'cause': 'string'
                        },
                        'executionTimedOutEventDetails': {
                            'error': 'string',
                            'cause': 'string'
                        },
                        'lambdaFunctionFailedEventDetails': {
                            'error': 'string',
                            'cause': 'string'
                        },
                        'lambdaFunctionScheduleFailedEventDetails': {
                            'error': 'string',
                            'cause': 'string'
                        },
                        'lambdaFunctionScheduledEventDetails': {
                            'resource': 'string',
                            'input': 'string',
                            'timeoutInSeconds': 123
                        },
                        'lambdaFunctionStartFailedEventDetails': {
                            'error': 'string',
                            'cause': 'string'
                        },
                        'lambdaFunctionSucceededEventDetails': {
                            'output': 'string'
                        },
                        'lambdaFunctionTimedOutEventDetails': {
                            'error': 'string',
                            'cause': 'string'
                        },
                        'stateEnteredEventDetails': {
                            'name': 'string',
                            'input': 'string'
                        },
                        'stateExitedEventDetails': {
                            'name': 'string',
                            'output': 'string'
                        }
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **events** *(list) --* 
              The list of events that occurred in the execution.
              - *(dict) --* 
                Contains details about the events of an execution.
                - **timestamp** *(datetime) --* 
                  The date and time the event occurred.
                - **type** *(string) --* 
                  The type of the event.
                - **id** *(integer) --* 
                  The id of the event. Events are numbered sequentially, starting at one.
                - **previousEventId** *(integer) --* 
                  The id of the previous event.
                - **activityFailedEventDetails** *(dict) --* 
                  Contains details about an activity that failed during an execution.
                  - **error** *(string) --* 
                    The error code of the failure.
                  - **cause** *(string) --* 
                    A more detailed explanation of the cause of the failure.
                - **activityScheduleFailedEventDetails** *(dict) --* 
                  Contains details about an activity schedule event that failed during an execution.
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
                  Contains details about an activity that successfully terminated during an execution.
                  - **output** *(string) --* 
                    The JSON data output by the activity task.
                - **activityTimedOutEventDetails** *(dict) --* 
                  Contains details about an activity timeout that occurred during an execution.
                  - **error** *(string) --* 
                    The error code of the failure.
                  - **cause** *(string) --* 
                    A more detailed explanation of the cause of the timeout.
                - **taskFailedEventDetails** *(dict) --* 
                  Contains details about the failure of a task.
                  - **resourceType** *(string) --* 
                    The action of the resource called by a task state.
                  - **resource** *(string) --* 
                    The service name of the resource in a task state.
                  - **error** *(string) --* 
                    The error code of the failure.
                  - **cause** *(string) --* 
                    A more detailed explanation of the cause of the failure.
                - **taskScheduledEventDetails** *(dict) --* 
                  Contains details about a task that was scheduled.
                  - **resourceType** *(string) --* 
                    The action of the resource called by a task state.
                  - **resource** *(string) --* 
                    The service name of the resource in a task state.
                  - **region** *(string) --* 
                    The region of the scheduled task
                  - **parameters** *(string) --* 
                    The JSON data passed to the resource referenced in a task state.
                  - **timeoutInSeconds** *(integer) --* 
                    The maximum allowed duration of the task.
                - **taskStartFailedEventDetails** *(dict) --* 
                  Contains details about a task that failed to start.
                  - **resourceType** *(string) --* 
                    The action of the resource called by a task state.
                  - **resource** *(string) --* 
                    The service name of the resource in a task state.
                  - **error** *(string) --* 
                    The error code of the failure.
                  - **cause** *(string) --* 
                    A more detailed explanation of the cause of the failure.
                - **taskStartedEventDetails** *(dict) --* 
                  Contains details about a task that was started.
                  - **resourceType** *(string) --* 
                    The action of the resource called by a task state.
                  - **resource** *(string) --* 
                    The service name of the resource in a task state.
                - **taskSubmitFailedEventDetails** *(dict) --* 
                  Contains details about a task that where the submit failed.
                  - **resourceType** *(string) --* 
                    The action of the resource called by a task state.
                  - **resource** *(string) --* 
                    The service name of the resource in a task state.
                  - **error** *(string) --* 
                    The error code of the failure.
                  - **cause** *(string) --* 
                    A more detailed explanation of the cause of the failure.
                - **taskSubmittedEventDetails** *(dict) --* 
                  Contains details about a submitted task.
                  - **resourceType** *(string) --* 
                    The action of the resource called by a task state.
                  - **resource** *(string) --* 
                    The service name of the resource in a task state.
                  - **output** *(string) --* 
                    The response from a resource when a task has started.
                - **taskSucceededEventDetails** *(dict) --* 
                  Contains details about a task that succeeded.
                  - **resourceType** *(string) --* 
                    The action of the resource called by a task state.
                  - **resource** *(string) --* 
                    The service name of the resource in a task state.
                  - **output** *(string) --* 
                    The full JSON response from a resource when a task has succeeded. This response becomes the output of the related task.
                - **taskTimedOutEventDetails** *(dict) --* 
                  Contains details about a task that timed out.
                  - **resourceType** *(string) --* 
                    The action of the resource called by a task state.
                  - **resource** *(string) --* 
                    The service name of the resource in a task state.
                  - **error** *(string) --* 
                    The error code of the failure.
                  - **cause** *(string) --* 
                    A more detailed explanation of the cause of the failure.
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
                  Contains details about the execution timeout that occurred during the execution.
                  - **error** *(string) --* 
                    The error code of the failure.
                  - **cause** *(string) --* 
                    A more detailed explanation of the cause of the timeout.
                - **lambdaFunctionFailedEventDetails** *(dict) --* 
                  Contains details about a lambda function that failed during an execution.
                  - **error** *(string) --* 
                    The error code of the failure.
                  - **cause** *(string) --* 
                    A more detailed explanation of the cause of the failure.
                - **lambdaFunctionScheduleFailedEventDetails** *(dict) --* 
                  Contains details about a failed lambda function schedule event that occurred during an execution.
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
                  Contains details about a lambda function that failed to start during an execution.
                  - **error** *(string) --* 
                    The error code of the failure.
                  - **cause** *(string) --* 
                    A more detailed explanation of the cause of the failure.
                - **lambdaFunctionSucceededEventDetails** *(dict) --* 
                  Contains details about a lambda function that terminated successfully during an execution.
                  - **output** *(string) --* 
                    The JSON data output by the lambda function.
                - **lambdaFunctionTimedOutEventDetails** *(dict) --* 
                  Contains details about a lambda function timeout that occurred during an execution.
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
                    * special characters ``" # % \ ^ | ~ ` $ & , ; : /``   
                    * control characters (``U+0000-001F`` , ``U+007F-009F`` ) 
                  - **output** *(string) --* 
                    The JSON output data of the state.
            - **nextToken** *(string) --* 
              If ``nextToken`` is returned, there are more results available. The value of ``nextToken`` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
        :type executionArn: string
        :param executionArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the execution.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results that are returned per call. You can use ``nextToken`` to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.
          This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.
        :type reverseOrder: boolean
        :param reverseOrder:
          Lists events in descending order of their ``timeStamp`` .
        :type nextToken: string
        :param nextToken:
          If ``nextToken`` is returned, there are more results available. The value of ``nextToken`` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
        :rtype: dict
        :returns:
        """
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        """
        Create a paginator for an operation.
        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you\'d normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator(\"create_foo\")``.
        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.
        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        Returns an object that can wait for some condition.
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def list_activities(self, maxResults: int = None, nextToken: str = None) -> Dict:
        """
        Lists the existing activities.
        If ``nextToken`` is returned, there are more results available. The value of ``nextToken`` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
        .. note::
          This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/ListActivities>`_
        
        **Request Syntax**
        ::
          response = client.list_activities(
              maxResults=123,
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'activities': [
                    {
                        'activityArn': 'string',
                        'name': 'string',
                        'creationDate': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
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
                  * special characters ``" # % \ ^ | ~ ` $ & , ; : /``   
                  * control characters (``U+0000-001F`` , ``U+007F-009F`` ) 
                - **creationDate** *(datetime) --* 
                  The date the activity is created.
            - **nextToken** *(string) --* 
              If ``nextToken`` is returned, there are more results available. The value of ``nextToken`` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results that are returned per call. You can use ``nextToken`` to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.
          This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.
        :type nextToken: string
        :param nextToken:
          If ``nextToken`` is returned, there are more results available. The value of ``nextToken`` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
        :rtype: dict
        :returns:
        """
        pass

    def list_executions(self, stateMachineArn: str, statusFilter: str = None, maxResults: int = None, nextToken: str = None) -> Dict:
        """
        Lists the executions of a state machine that meet the filtering criteria. Results are sorted by time, with the most recent execution first.
        If ``nextToken`` is returned, there are more results available. The value of ``nextToken`` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
        .. note::
          This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/ListExecutions>`_
        
        **Request Syntax**
        ::
          response = client.list_executions(
              stateMachineArn='string',
              statusFilter='RUNNING'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'ABORTED',
              maxResults=123,
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'executions': [
                    {
                        'executionArn': 'string',
                        'stateMachineArn': 'string',
                        'name': 'string',
                        'status': 'RUNNING'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'ABORTED',
                        'startDate': datetime(2015, 1, 1),
                        'stopDate': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
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
                  * special characters ``" # % \ ^ | ~ ` $ & , ; : /``   
                  * control characters (``U+0000-001F`` , ``U+007F-009F`` ) 
                - **status** *(string) --* 
                  The current status of the execution.
                - **startDate** *(datetime) --* 
                  The date the execution started.
                - **stopDate** *(datetime) --* 
                  If the execution already ended, the date the execution stopped.
            - **nextToken** *(string) --* 
              If ``nextToken`` is returned, there are more results available. The value of ``nextToken`` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
        :type stateMachineArn: string
        :param stateMachineArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the state machine whose executions is listed.
        :type statusFilter: string
        :param statusFilter:
          If specified, only list the executions whose current execution status matches the given filter.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results that are returned per call. You can use ``nextToken`` to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.
          This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.
        :type nextToken: string
        :param nextToken:
          If ``nextToken`` is returned, there are more results available. The value of ``nextToken`` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
        :rtype: dict
        :returns:
        """
        pass

    def list_state_machines(self, maxResults: int = None, nextToken: str = None) -> Dict:
        """
        Lists the existing state machines.
        If ``nextToken`` is returned, there are more results available. The value of ``nextToken`` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
        .. note::
          This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/ListStateMachines>`_
        
        **Request Syntax**
        ::
          response = client.list_state_machines(
              maxResults=123,
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'stateMachines': [
                    {
                        'stateMachineArn': 'string',
                        'name': 'string',
                        'creationDate': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
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
                  * special characters ``" # % \ ^ | ~ ` $ & , ; : /``   
                  * control characters (``U+0000-001F`` , ``U+007F-009F`` ) 
                - **creationDate** *(datetime) --* 
                  The date the state machine is created.
            - **nextToken** *(string) --* 
              If ``nextToken`` is returned, there are more results available. The value of ``nextToken`` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results that are returned per call. You can use ``nextToken`` to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.
          This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.
        :type nextToken: string
        :param nextToken:
          If ``nextToken`` is returned, there are more results available. The value of ``nextToken`` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
        :rtype: dict
        :returns:
        """
        pass

    def list_tags_for_resource(self, resourceArn: str) -> Dict:
        """
        List tags for a given resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/ListTagsForResource>`_
        
        **Request Syntax**
        ::
          response = client.list_tags_for_resource(
              resourceArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **tags** *(list) --* 
              An array of tags associated with the resource.
              - *(dict) --* 
                Tags are key-value pairs that can be associated with Step Functions state machines and activities.
                - **key** *(string) --* 
                  The key of a tag.
                - **value** *(string) --* 
                  The value of a tag.
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) for the Step Functions state machine or activity.
        :rtype: dict
        :returns:
        """
        pass

    def send_task_failure(self, taskToken: str, error: str = None, cause: str = None) -> Dict:
        """
        Used by workers to report that the task identified by the ``taskToken`` failed.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/SendTaskFailure>`_
        
        **Request Syntax**
        ::
          response = client.send_task_failure(
              taskToken='string',
              error='string',
              cause='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type taskToken: string
        :param taskToken: **[REQUIRED]**
          The token that represents this task. Task tokens are generated by the service when the tasks are assigned to a worker (see GetActivityTask::taskToken).
        :type error: string
        :param error:
          The error code of the failure.
        :type cause: string
        :param cause:
          A more detailed explanation of the cause of the failure.
        :rtype: dict
        :returns:
        """
        pass

    def send_task_heartbeat(self, taskToken: str) -> Dict:
        """
        Used by workers to report to the service that the task represented by the specified ``taskToken`` is still making progress. This action resets the ``Heartbeat`` clock. The ``Heartbeat`` threshold is specified in the state machine's Amazon States Language definition. This action does not in itself create an event in the execution history. However, if the task times out, the execution history contains an ``ActivityTimedOut`` event.
        .. note::
          The ``Timeout`` of a task, defined in the state machine's Amazon States Language definition, is its maximum allowed duration, regardless of the number of  SendTaskHeartbeat requests received.
        .. note::
          This operation is only useful for long-lived tasks to report the liveliness of the task.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/SendTaskHeartbeat>`_
        
        **Request Syntax**
        ::
          response = client.send_task_heartbeat(
              taskToken='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type taskToken: string
        :param taskToken: **[REQUIRED]**
          The token that represents this task. Task tokens are generated by the service when the tasks are assigned to a worker (see  GetActivityTaskOutput$taskToken ).
        :rtype: dict
        :returns:
        """
        pass

    def send_task_success(self, taskToken: str, output: str) -> Dict:
        """
        Used by workers to report that the task identified by the ``taskToken`` completed successfully.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/SendTaskSuccess>`_
        
        **Request Syntax**
        ::
          response = client.send_task_success(
              taskToken='string',
              output='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type taskToken: string
        :param taskToken: **[REQUIRED]**
          The token that represents this task. Task tokens are generated by the service when the tasks are assigned to a worker (see  GetActivityTaskOutput$taskToken ).
        :type output: string
        :param output: **[REQUIRED]**
          The JSON output of the task.
        :rtype: dict
        :returns:
        """
        pass

    def start_execution(self, stateMachineArn: str, name: str = None, input: str = None) -> Dict:
        """
        Starts a state machine execution.
        .. note::
           ``StartExecution`` is idempotent. If ``StartExecution`` is called with the same name and input as a running execution, the call will succeed and return the same response as the original request. If the execution is closed or if the input is different, it will return a 400 ``ExecutionAlreadyExists`` error. Names can be reused after 90 days. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/StartExecution>`_
        
        **Request Syntax**
        ::
          response = client.start_execution(
              stateMachineArn='string',
              name='string',
              input='string'
          )
        
        **Response Syntax**
        ::
            {
                'executionArn': 'string',
                'startDate': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            - **executionArn** *(string) --* 
              The Amazon Resource Name (ARN) that identifies the execution.
            - **startDate** *(datetime) --* 
              The date the execution is started.
        :type stateMachineArn: string
        :param stateMachineArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the state machine to execute.
        :type name: string
        :param name:
          The name of the execution. This name must be unique for your AWS account, region, and state machine for 90 days. For more information, see `Limits Related to State Machine Executions <https://docs.aws.amazon.com/step-functions/latest/dg/limits.html#service-limits-state-machine-executions>`__ in the *AWS Step Functions Developer Guide* .
          A name must *not* contain:
          * whitespace
          * brackets ``< > { } [ ]``
          * wildcard characters ``? *``
          * special characters ``\" # % \ ^ | ~ ` $ & , ; : /``
          * control characters (``U+0000-001F`` , ``U+007F-009F`` )
        :type input: string
        :param input:
          The string that contains the JSON input data for the execution, for example:
           ``\"input\": \"{\\"first_name\\" : \\"test\\"}\"``
          .. note::
            If you don\'t include any JSON input data, you still must include the two braces, for example: ``\"input\": \"{}\"``
        :rtype: dict
        :returns:
        """
        pass

    def stop_execution(self, executionArn: str, error: str = None, cause: str = None) -> Dict:
        """
        Stops an execution.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/StopExecution>`_
        
        **Request Syntax**
        ::
          response = client.stop_execution(
              executionArn='string',
              error='string',
              cause='string'
          )
        
        **Response Syntax**
        ::
            {
                'stopDate': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            - **stopDate** *(datetime) --* 
              The date the execution is stopped.
        :type executionArn: string
        :param executionArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the execution to stop.
        :type error: string
        :param error:
          The error code of the failure.
        :type cause: string
        :param cause:
          A more detailed explanation of the cause of the failure.
        :rtype: dict
        :returns:
        """
        pass

    def tag_resource(self, resourceArn: str, tags: List) -> Dict:
        """
        Add a tag to a Step Functions resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/TagResource>`_
        
        **Request Syntax**
        ::
          response = client.tag_resource(
              resourceArn='string',
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) for the Step Functions state machine or activity.
        :type tags: list
        :param tags: **[REQUIRED]**
          The list of tags to add to a resource.
          Tags may only contain unicode letters, digits, whitespace, or these symbols: ``_ . : / = + - @`` .
          - *(dict) --*
            Tags are key-value pairs that can be associated with Step Functions state machines and activities.
            - **key** *(string) --*
              The key of a tag.
            - **value** *(string) --*
              The value of a tag.
        :rtype: dict
        :returns:
        """
        pass

    def untag_resource(self, resourceArn: str, tagKeys: List) -> Dict:
        """
        Remove a tag from a Step Functions resource
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/UntagResource>`_
        
        **Request Syntax**
        ::
          response = client.untag_resource(
              resourceArn='string',
              tagKeys=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) for the Step Functions state machine or activity.
        :type tagKeys: list
        :param tagKeys: **[REQUIRED]**
          The list of tags to remove from the resource.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def update_state_machine(self, stateMachineArn: str, definition: str = None, roleArn: str = None) -> Dict:
        """
        Updates an existing state machine by modifying its ``definition`` and/or ``roleArn`` . Running executions will continue to use the previous ``definition`` and ``roleArn`` . You must include at least one of ``definition`` or ``roleArn`` or you will receive a ``MissingRequiredParameter`` error.
        .. note::
          All ``StartExecution`` calls within a few seconds will use the updated ``definition`` and ``roleArn`` . Executions started immediately after calling ``UpdateStateMachine`` may use the previous state machine ``definition`` and ``roleArn`` . 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/UpdateStateMachine>`_
        
        **Request Syntax**
        ::
          response = client.update_state_machine(
              stateMachineArn='string',
              definition='string',
              roleArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'updateDate': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            - **updateDate** *(datetime) --* 
              The date and time the state machine was updated.
        :type stateMachineArn: string
        :param stateMachineArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the state machine.
        :type definition: string
        :param definition:
          The Amazon States Language definition of the state machine. See `Amazon States Language <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html>`__ .
        :type roleArn: string
        :param roleArn:
          The Amazon Resource Name (ARN) of the IAM role of the state machine.
        :rtype: dict
        :returns:
        """
        pass
