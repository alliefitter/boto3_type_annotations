from typing import Dict
from botocore.paginate import Paginator


class GetWorkflowExecutionHistory(Paginator):
    def paginate(self, domain: str, execution: Dict, reverseOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/swf-2012-01-25/GetWorkflowExecutionHistory>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              domain=\'string\',
              execution={
                  \'workflowId\': \'string\',
                  \'runId\': \'string\'
              },
              reverseOrder=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type domain: string
        :param domain: **[REQUIRED]** 
        
          The name of the domain containing the workflow execution.
        
        :type execution: dict
        :param execution: **[REQUIRED]** 
        
          Specifies the workflow execution for which to return the history.
        
          - **workflowId** *(string) --* **[REQUIRED]** 
        
            The user defined identifier associated with the workflow execution.
        
          - **runId** *(string) --* **[REQUIRED]** 
        
            A system-generated unique identifier for the workflow execution.
        
        :type reverseOrder: boolean
        :param reverseOrder: 
        
          When set to ``true`` , returns the events in reverse order. By default the results are returned in ascending order of the ``eventTimeStamp`` of the events.
        
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
                        \'eventTimestamp\': datetime(2015, 1, 1),
                        \'eventType\': \'WorkflowExecutionStarted\'|\'WorkflowExecutionCancelRequested\'|\'WorkflowExecutionCompleted\'|\'CompleteWorkflowExecutionFailed\'|\'WorkflowExecutionFailed\'|\'FailWorkflowExecutionFailed\'|\'WorkflowExecutionTimedOut\'|\'WorkflowExecutionCanceled\'|\'CancelWorkflowExecutionFailed\'|\'WorkflowExecutionContinuedAsNew\'|\'ContinueAsNewWorkflowExecutionFailed\'|\'WorkflowExecutionTerminated\'|\'DecisionTaskScheduled\'|\'DecisionTaskStarted\'|\'DecisionTaskCompleted\'|\'DecisionTaskTimedOut\'|\'ActivityTaskScheduled\'|\'ScheduleActivityTaskFailed\'|\'ActivityTaskStarted\'|\'ActivityTaskCompleted\'|\'ActivityTaskFailed\'|\'ActivityTaskTimedOut\'|\'ActivityTaskCanceled\'|\'ActivityTaskCancelRequested\'|\'RequestCancelActivityTaskFailed\'|\'WorkflowExecutionSignaled\'|\'MarkerRecorded\'|\'RecordMarkerFailed\'|\'TimerStarted\'|\'StartTimerFailed\'|\'TimerFired\'|\'TimerCanceled\'|\'CancelTimerFailed\'|\'StartChildWorkflowExecutionInitiated\'|\'StartChildWorkflowExecutionFailed\'|\'ChildWorkflowExecutionStarted\'|\'ChildWorkflowExecutionCompleted\'|\'ChildWorkflowExecutionFailed\'|\'ChildWorkflowExecutionTimedOut\'|\'ChildWorkflowExecutionCanceled\'|\'ChildWorkflowExecutionTerminated\'|\'SignalExternalWorkflowExecutionInitiated\'|\'SignalExternalWorkflowExecutionFailed\'|\'ExternalWorkflowExecutionSignaled\'|\'RequestCancelExternalWorkflowExecutionInitiated\'|\'RequestCancelExternalWorkflowExecutionFailed\'|\'ExternalWorkflowExecutionCancelRequested\'|\'LambdaFunctionScheduled\'|\'LambdaFunctionStarted\'|\'LambdaFunctionCompleted\'|\'LambdaFunctionFailed\'|\'LambdaFunctionTimedOut\'|\'ScheduleLambdaFunctionFailed\'|\'StartLambdaFunctionFailed\',
                        \'eventId\': 123,
                        \'workflowExecutionStartedEventAttributes\': {
                            \'input\': \'string\',
                            \'executionStartToCloseTimeout\': \'string\',
                            \'taskStartToCloseTimeout\': \'string\',
                            \'childPolicy\': \'TERMINATE\'|\'REQUEST_CANCEL\'|\'ABANDON\',
                            \'taskList\': {
                                \'name\': \'string\'
                            },
                            \'taskPriority\': \'string\',
                            \'workflowType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'tagList\': [
                                \'string\',
                            ],
                            \'continuedExecutionRunId\': \'string\',
                            \'parentWorkflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'parentInitiatedEventId\': 123,
                            \'lambdaRole\': \'string\'
                        },
                        \'workflowExecutionCompletedEventAttributes\': {
                            \'result\': \'string\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'completeWorkflowExecutionFailedEventAttributes\': {
                            \'cause\': \'UNHANDLED_DECISION\'|\'OPERATION_NOT_PERMITTED\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'workflowExecutionFailedEventAttributes\': {
                            \'reason\': \'string\',
                            \'details\': \'string\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'failWorkflowExecutionFailedEventAttributes\': {
                            \'cause\': \'UNHANDLED_DECISION\'|\'OPERATION_NOT_PERMITTED\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'workflowExecutionTimedOutEventAttributes\': {
                            \'timeoutType\': \'START_TO_CLOSE\',
                            \'childPolicy\': \'TERMINATE\'|\'REQUEST_CANCEL\'|\'ABANDON\'
                        },
                        \'workflowExecutionCanceledEventAttributes\': {
                            \'details\': \'string\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'cancelWorkflowExecutionFailedEventAttributes\': {
                            \'cause\': \'UNHANDLED_DECISION\'|\'OPERATION_NOT_PERMITTED\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'workflowExecutionContinuedAsNewEventAttributes\': {
                            \'input\': \'string\',
                            \'decisionTaskCompletedEventId\': 123,
                            \'newExecutionRunId\': \'string\',
                            \'executionStartToCloseTimeout\': \'string\',
                            \'taskList\': {
                                \'name\': \'string\'
                            },
                            \'taskPriority\': \'string\',
                            \'taskStartToCloseTimeout\': \'string\',
                            \'childPolicy\': \'TERMINATE\'|\'REQUEST_CANCEL\'|\'ABANDON\',
                            \'tagList\': [
                                \'string\',
                            ],
                            \'workflowType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'lambdaRole\': \'string\'
                        },
                        \'continueAsNewWorkflowExecutionFailedEventAttributes\': {
                            \'cause\': \'UNHANDLED_DECISION\'|\'WORKFLOW_TYPE_DEPRECATED\'|\'WORKFLOW_TYPE_DOES_NOT_EXIST\'|\'DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED\'|\'DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED\'|\'DEFAULT_TASK_LIST_UNDEFINED\'|\'DEFAULT_CHILD_POLICY_UNDEFINED\'|\'CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED\'|\'OPERATION_NOT_PERMITTED\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'workflowExecutionTerminatedEventAttributes\': {
                            \'reason\': \'string\',
                            \'details\': \'string\',
                            \'childPolicy\': \'TERMINATE\'|\'REQUEST_CANCEL\'|\'ABANDON\',
                            \'cause\': \'CHILD_POLICY_APPLIED\'|\'EVENT_LIMIT_EXCEEDED\'|\'OPERATOR_INITIATED\'
                        },
                        \'workflowExecutionCancelRequestedEventAttributes\': {
                            \'externalWorkflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'externalInitiatedEventId\': 123,
                            \'cause\': \'CHILD_POLICY_APPLIED\'
                        },
                        \'decisionTaskScheduledEventAttributes\': {
                            \'taskList\': {
                                \'name\': \'string\'
                            },
                            \'taskPriority\': \'string\',
                            \'startToCloseTimeout\': \'string\'
                        },
                        \'decisionTaskStartedEventAttributes\': {
                            \'identity\': \'string\',
                            \'scheduledEventId\': 123
                        },
                        \'decisionTaskCompletedEventAttributes\': {
                            \'executionContext\': \'string\',
                            \'scheduledEventId\': 123,
                            \'startedEventId\': 123
                        },
                        \'decisionTaskTimedOutEventAttributes\': {
                            \'timeoutType\': \'START_TO_CLOSE\',
                            \'scheduledEventId\': 123,
                            \'startedEventId\': 123
                        },
                        \'activityTaskScheduledEventAttributes\': {
                            \'activityType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'activityId\': \'string\',
                            \'input\': \'string\',
                            \'control\': \'string\',
                            \'scheduleToStartTimeout\': \'string\',
                            \'scheduleToCloseTimeout\': \'string\',
                            \'startToCloseTimeout\': \'string\',
                            \'taskList\': {
                                \'name\': \'string\'
                            },
                            \'taskPriority\': \'string\',
                            \'decisionTaskCompletedEventId\': 123,
                            \'heartbeatTimeout\': \'string\'
                        },
                        \'activityTaskStartedEventAttributes\': {
                            \'identity\': \'string\',
                            \'scheduledEventId\': 123
                        },
                        \'activityTaskCompletedEventAttributes\': {
                            \'result\': \'string\',
                            \'scheduledEventId\': 123,
                            \'startedEventId\': 123
                        },
                        \'activityTaskFailedEventAttributes\': {
                            \'reason\': \'string\',
                            \'details\': \'string\',
                            \'scheduledEventId\': 123,
                            \'startedEventId\': 123
                        },
                        \'activityTaskTimedOutEventAttributes\': {
                            \'timeoutType\': \'START_TO_CLOSE\'|\'SCHEDULE_TO_START\'|\'SCHEDULE_TO_CLOSE\'|\'HEARTBEAT\',
                            \'scheduledEventId\': 123,
                            \'startedEventId\': 123,
                            \'details\': \'string\'
                        },
                        \'activityTaskCanceledEventAttributes\': {
                            \'details\': \'string\',
                            \'scheduledEventId\': 123,
                            \'startedEventId\': 123,
                            \'latestCancelRequestedEventId\': 123
                        },
                        \'activityTaskCancelRequestedEventAttributes\': {
                            \'decisionTaskCompletedEventId\': 123,
                            \'activityId\': \'string\'
                        },
                        \'workflowExecutionSignaledEventAttributes\': {
                            \'signalName\': \'string\',
                            \'input\': \'string\',
                            \'externalWorkflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'externalInitiatedEventId\': 123
                        },
                        \'markerRecordedEventAttributes\': {
                            \'markerName\': \'string\',
                            \'details\': \'string\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'recordMarkerFailedEventAttributes\': {
                            \'markerName\': \'string\',
                            \'cause\': \'OPERATION_NOT_PERMITTED\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'timerStartedEventAttributes\': {
                            \'timerId\': \'string\',
                            \'control\': \'string\',
                            \'startToFireTimeout\': \'string\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'timerFiredEventAttributes\': {
                            \'timerId\': \'string\',
                            \'startedEventId\': 123
                        },
                        \'timerCanceledEventAttributes\': {
                            \'timerId\': \'string\',
                            \'startedEventId\': 123,
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'startChildWorkflowExecutionInitiatedEventAttributes\': {
                            \'workflowId\': \'string\',
                            \'workflowType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'control\': \'string\',
                            \'input\': \'string\',
                            \'executionStartToCloseTimeout\': \'string\',
                            \'taskList\': {
                                \'name\': \'string\'
                            },
                            \'taskPriority\': \'string\',
                            \'decisionTaskCompletedEventId\': 123,
                            \'childPolicy\': \'TERMINATE\'|\'REQUEST_CANCEL\'|\'ABANDON\',
                            \'taskStartToCloseTimeout\': \'string\',
                            \'tagList\': [
                                \'string\',
                            ],
                            \'lambdaRole\': \'string\'
                        },
                        \'childWorkflowExecutionStartedEventAttributes\': {
                            \'workflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'workflowType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'initiatedEventId\': 123
                        },
                        \'childWorkflowExecutionCompletedEventAttributes\': {
                            \'workflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'workflowType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'result\': \'string\',
                            \'initiatedEventId\': 123,
                            \'startedEventId\': 123
                        },
                        \'childWorkflowExecutionFailedEventAttributes\': {
                            \'workflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'workflowType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'reason\': \'string\',
                            \'details\': \'string\',
                            \'initiatedEventId\': 123,
                            \'startedEventId\': 123
                        },
                        \'childWorkflowExecutionTimedOutEventAttributes\': {
                            \'workflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'workflowType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'timeoutType\': \'START_TO_CLOSE\',
                            \'initiatedEventId\': 123,
                            \'startedEventId\': 123
                        },
                        \'childWorkflowExecutionCanceledEventAttributes\': {
                            \'workflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'workflowType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'details\': \'string\',
                            \'initiatedEventId\': 123,
                            \'startedEventId\': 123
                        },
                        \'childWorkflowExecutionTerminatedEventAttributes\': {
                            \'workflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'workflowType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'initiatedEventId\': 123,
                            \'startedEventId\': 123
                        },
                        \'signalExternalWorkflowExecutionInitiatedEventAttributes\': {
                            \'workflowId\': \'string\',
                            \'runId\': \'string\',
                            \'signalName\': \'string\',
                            \'input\': \'string\',
                            \'decisionTaskCompletedEventId\': 123,
                            \'control\': \'string\'
                        },
                        \'externalWorkflowExecutionSignaledEventAttributes\': {
                            \'workflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'initiatedEventId\': 123
                        },
                        \'signalExternalWorkflowExecutionFailedEventAttributes\': {
                            \'workflowId\': \'string\',
                            \'runId\': \'string\',
                            \'cause\': \'UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION\'|\'SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED\'|\'OPERATION_NOT_PERMITTED\',
                            \'initiatedEventId\': 123,
                            \'decisionTaskCompletedEventId\': 123,
                            \'control\': \'string\'
                        },
                        \'externalWorkflowExecutionCancelRequestedEventAttributes\': {
                            \'workflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'initiatedEventId\': 123
                        },
                        \'requestCancelExternalWorkflowExecutionInitiatedEventAttributes\': {
                            \'workflowId\': \'string\',
                            \'runId\': \'string\',
                            \'decisionTaskCompletedEventId\': 123,
                            \'control\': \'string\'
                        },
                        \'requestCancelExternalWorkflowExecutionFailedEventAttributes\': {
                            \'workflowId\': \'string\',
                            \'runId\': \'string\',
                            \'cause\': \'UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION\'|\'REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED\'|\'OPERATION_NOT_PERMITTED\',
                            \'initiatedEventId\': 123,
                            \'decisionTaskCompletedEventId\': 123,
                            \'control\': \'string\'
                        },
                        \'scheduleActivityTaskFailedEventAttributes\': {
                            \'activityType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'activityId\': \'string\',
                            \'cause\': \'ACTIVITY_TYPE_DEPRECATED\'|\'ACTIVITY_TYPE_DOES_NOT_EXIST\'|\'ACTIVITY_ID_ALREADY_IN_USE\'|\'OPEN_ACTIVITIES_LIMIT_EXCEEDED\'|\'ACTIVITY_CREATION_RATE_EXCEEDED\'|\'DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED\'|\'DEFAULT_TASK_LIST_UNDEFINED\'|\'DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED\'|\'DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED\'|\'DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED\'|\'OPERATION_NOT_PERMITTED\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'requestCancelActivityTaskFailedEventAttributes\': {
                            \'activityId\': \'string\',
                            \'cause\': \'ACTIVITY_ID_UNKNOWN\'|\'OPERATION_NOT_PERMITTED\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'startTimerFailedEventAttributes\': {
                            \'timerId\': \'string\',
                            \'cause\': \'TIMER_ID_ALREADY_IN_USE\'|\'OPEN_TIMERS_LIMIT_EXCEEDED\'|\'TIMER_CREATION_RATE_EXCEEDED\'|\'OPERATION_NOT_PERMITTED\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'cancelTimerFailedEventAttributes\': {
                            \'timerId\': \'string\',
                            \'cause\': \'TIMER_ID_UNKNOWN\'|\'OPERATION_NOT_PERMITTED\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'startChildWorkflowExecutionFailedEventAttributes\': {
                            \'workflowType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'cause\': \'WORKFLOW_TYPE_DOES_NOT_EXIST\'|\'WORKFLOW_TYPE_DEPRECATED\'|\'OPEN_CHILDREN_LIMIT_EXCEEDED\'|\'OPEN_WORKFLOWS_LIMIT_EXCEEDED\'|\'CHILD_CREATION_RATE_EXCEEDED\'|\'WORKFLOW_ALREADY_RUNNING\'|\'DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED\'|\'DEFAULT_TASK_LIST_UNDEFINED\'|\'DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED\'|\'DEFAULT_CHILD_POLICY_UNDEFINED\'|\'OPERATION_NOT_PERMITTED\',
                            \'workflowId\': \'string\',
                            \'initiatedEventId\': 123,
                            \'decisionTaskCompletedEventId\': 123,
                            \'control\': \'string\'
                        },
                        \'lambdaFunctionScheduledEventAttributes\': {
                            \'id\': \'string\',
                            \'name\': \'string\',
                            \'control\': \'string\',
                            \'input\': \'string\',
                            \'startToCloseTimeout\': \'string\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'lambdaFunctionStartedEventAttributes\': {
                            \'scheduledEventId\': 123
                        },
                        \'lambdaFunctionCompletedEventAttributes\': {
                            \'scheduledEventId\': 123,
                            \'startedEventId\': 123,
                            \'result\': \'string\'
                        },
                        \'lambdaFunctionFailedEventAttributes\': {
                            \'scheduledEventId\': 123,
                            \'startedEventId\': 123,
                            \'reason\': \'string\',
                            \'details\': \'string\'
                        },
                        \'lambdaFunctionTimedOutEventAttributes\': {
                            \'scheduledEventId\': 123,
                            \'startedEventId\': 123,
                            \'timeoutType\': \'START_TO_CLOSE\'
                        },
                        \'scheduleLambdaFunctionFailedEventAttributes\': {
                            \'id\': \'string\',
                            \'name\': \'string\',
                            \'cause\': \'ID_ALREADY_IN_USE\'|\'OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED\'|\'LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED\'|\'LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'startLambdaFunctionFailedEventAttributes\': {
                            \'scheduledEventId\': 123,
                            \'cause\': \'ASSUME_ROLE_FAILED\',
                            \'message\': \'string\'
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Paginated representation of a workflow history for a workflow execution. This is the up to date, complete and authoritative record of the events related to all tasks and events in the life of the workflow execution.
        
            - **events** *(list) --* 
        
              The list of history events.
        
              - *(dict) --* 
        
                Event within a workflow execution. A history event can be one of these types:
        
                * ``ActivityTaskCancelRequested`` – A ``RequestCancelActivityTask`` decision was received by the system. 
                 
                * ``ActivityTaskCanceled`` – The activity task was successfully canceled. 
                 
                * ``ActivityTaskCompleted`` – An activity worker successfully completed an activity task by calling  RespondActivityTaskCompleted . 
                 
                * ``ActivityTaskFailed`` – An activity worker failed an activity task by calling  RespondActivityTaskFailed . 
                 
                * ``ActivityTaskScheduled`` – An activity task was scheduled for execution. 
                 
                * ``ActivityTaskStarted`` – The scheduled activity task was dispatched to a worker. 
                 
                * ``ActivityTaskTimedOut`` – The activity task timed out. 
                 
                * ``CancelTimerFailed`` – Failed to process CancelTimer decision. This happens when the decision isn\'t configured properly, for example no timer exists with the specified timer Id. 
                 
                * ``CancelWorkflowExecutionFailed`` – A request to cancel a workflow execution failed. 
                 
                * ``ChildWorkflowExecutionCanceled`` – A child workflow execution, started by this workflow execution, was canceled and closed. 
                 
                * ``ChildWorkflowExecutionCompleted`` – A child workflow execution, started by this workflow execution, completed successfully and was closed. 
                 
                * ``ChildWorkflowExecutionFailed`` – A child workflow execution, started by this workflow execution, failed to complete successfully and was closed. 
                 
                * ``ChildWorkflowExecutionStarted`` – A child workflow execution was successfully started. 
                 
                * ``ChildWorkflowExecutionTerminated`` – A child workflow execution, started by this workflow execution, was terminated. 
                 
                * ``ChildWorkflowExecutionTimedOut`` – A child workflow execution, started by this workflow execution, timed out and was closed. 
                 
                * ``CompleteWorkflowExecutionFailed`` – The workflow execution failed to complete. 
                 
                * ``ContinueAsNewWorkflowExecutionFailed`` – The workflow execution failed to complete after being continued as a new workflow execution. 
                 
                * ``DecisionTaskCompleted`` – The decider successfully completed a decision task by calling  RespondDecisionTaskCompleted . 
                 
                * ``DecisionTaskScheduled`` – A decision task was scheduled for the workflow execution. 
                 
                * ``DecisionTaskStarted`` – The decision task was dispatched to a decider. 
                 
                * ``DecisionTaskTimedOut`` – The decision task timed out. 
                 
                * ``ExternalWorkflowExecutionCancelRequested`` – Request to cancel an external workflow execution was successfully delivered to the target execution. 
                 
                * ``ExternalWorkflowExecutionSignaled`` – A signal, requested by this workflow execution, was successfully delivered to the target external workflow execution. 
                 
                * ``FailWorkflowExecutionFailed`` – A request to mark a workflow execution as failed, itself failed. 
                 
                * ``MarkerRecorded`` – A marker was recorded in the workflow history as the result of a ``RecordMarker`` decision. 
                 
                * ``RecordMarkerFailed`` – A ``RecordMarker`` decision was returned as failed. 
                 
                * ``RequestCancelActivityTaskFailed`` – Failed to process RequestCancelActivityTask decision. This happens when the decision isn\'t configured properly. 
                 
                * ``RequestCancelExternalWorkflowExecutionFailed`` – Request to cancel an external workflow execution failed. 
                 
                * ``RequestCancelExternalWorkflowExecutionInitiated`` – A request was made to request the cancellation of an external workflow execution. 
                 
                * ``ScheduleActivityTaskFailed`` – Failed to process ScheduleActivityTask decision. This happens when the decision isn\'t configured properly, for example the activity type specified isn\'t registered. 
                 
                * ``SignalExternalWorkflowExecutionFailed`` – The request to signal an external workflow execution failed. 
                 
                * ``SignalExternalWorkflowExecutionInitiated`` – A request to signal an external workflow was made. 
                 
                * ``StartActivityTaskFailed`` – A scheduled activity task failed to start. 
                 
                * ``StartChildWorkflowExecutionFailed`` – Failed to process StartChildWorkflowExecution decision. This happens when the decision isn\'t configured properly, for example the workflow type specified isn\'t registered. 
                 
                * ``StartChildWorkflowExecutionInitiated`` – A request was made to start a child workflow execution. 
                 
                * ``StartTimerFailed`` – Failed to process StartTimer decision. This happens when the decision isn\'t configured properly, for example a timer already exists with the specified timer Id. 
                 
                * ``TimerCanceled`` – A timer, previously started for this workflow execution, was successfully canceled. 
                 
                * ``TimerFired`` – A timer, previously started for this workflow execution, fired. 
                 
                * ``TimerStarted`` – A timer was started for the workflow execution due to a ``StartTimer`` decision. 
                 
                * ``WorkflowExecutionCancelRequested`` – A request to cancel this workflow execution was made. 
                 
                * ``WorkflowExecutionCanceled`` – The workflow execution was successfully canceled and closed. 
                 
                * ``WorkflowExecutionCompleted`` – The workflow execution was closed due to successful completion. 
                 
                * ``WorkflowExecutionContinuedAsNew`` – The workflow execution was closed and a new execution of the same type was created with the same workflowId. 
                 
                * ``WorkflowExecutionFailed`` – The workflow execution closed due to a failure. 
                 
                * ``WorkflowExecutionSignaled`` – An external signal was received for the workflow execution. 
                 
                * ``WorkflowExecutionStarted`` – The workflow execution was started. 
                 
                * ``WorkflowExecutionTerminated`` – The workflow execution was terminated. 
                 
                * ``WorkflowExecutionTimedOut`` – The workflow execution was closed because a time out was exceeded. 
                 
                - **eventTimestamp** *(datetime) --* 
        
                  The date and time when the event occurred.
        
                - **eventType** *(string) --* 
        
                  The type of the history event.
        
                - **eventId** *(integer) --* 
        
                  The system generated ID of the event. This ID uniquely identifies the event with in the workflow execution history.
        
                - **workflowExecutionStartedEventAttributes** *(dict) --* 
        
                  If the event is of type ``WorkflowExecutionStarted`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **input** *(string) --* 
        
                    The input provided to the workflow execution.
        
                  - **executionStartToCloseTimeout** *(string) --* 
        
                    The maximum duration for this workflow execution.
        
                    The duration is specified in seconds, an integer greater than or equal to ``0`` . You can use ``NONE`` to specify unlimited duration.
        
                  - **taskStartToCloseTimeout** *(string) --* 
        
                    The maximum duration of decision tasks for this workflow type.
        
                    The duration is specified in seconds, an integer greater than or equal to ``0`` . You can use ``NONE`` to specify unlimited duration.
        
                  - **childPolicy** *(string) --* 
        
                    The policy to use for the child workflow executions if this workflow execution is terminated, by calling the  TerminateWorkflowExecution action explicitly or due to an expired timeout.
        
                    The supported child policies are:
        
                    * ``TERMINATE`` – The child executions are terminated. 
                     
                    * ``REQUEST_CANCEL`` – A request to cancel is attempted for each child execution by recording a ``WorkflowExecutionCancelRequested`` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event. 
                     
                    * ``ABANDON`` – No action is taken. The child executions continue to run. 
                     
                  - **taskList** *(dict) --* 
        
                    The name of the task list for scheduling the decision tasks for this workflow execution.
        
                    - **name** *(string) --* 
        
                      The name of the task list.
        
                  - **taskPriority** *(string) --* 
        
                    The priority of the decision tasks in the workflow execution.
        
                  - **workflowType** *(dict) --* 
        
                    The workflow type of this execution.
        
                    - **name** *(string) --* 
        
                      The name of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                    - **version** *(string) --* 
        
                      The version of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                  - **tagList** *(list) --* 
        
                    The list of tags associated with this workflow execution. An execution can have up to 5 tags.
        
                    - *(string) --* 
                
                  - **continuedExecutionRunId** *(string) --* 
        
                    If this workflow execution was started due to a ``ContinueAsNewWorkflowExecution`` decision, then it contains the ``runId`` of the previous workflow execution that was closed and continued as this execution.
        
                  - **parentWorkflowExecution** *(dict) --* 
        
                    The source workflow execution that started this workflow execution. The member isn\'t set if the workflow execution was not started by a workflow.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **parentInitiatedEventId** *(integer) --* 
        
                    The ID of the ``StartChildWorkflowExecutionInitiated`` event corresponding to the ``StartChildWorkflowExecution``   Decision to start this workflow execution. The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **lambdaRole** *(string) --* 
        
                    The IAM role attached to the workflow execution.
        
                - **workflowExecutionCompletedEventAttributes** *(dict) --* 
        
                  If the event is of type ``WorkflowExecutionCompleted`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **result** *(string) --* 
        
                    The result produced by the workflow execution upon successful completion.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``CompleteWorkflowExecution`` decision to complete this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **completeWorkflowExecutionFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``CompleteWorkflowExecutionFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``CompleteWorkflowExecution`` decision to complete this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **workflowExecutionFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``WorkflowExecutionFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **reason** *(string) --* 
        
                    The descriptive reason provided for the failure.
        
                  - **details** *(string) --* 
        
                    The details of the failure.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``FailWorkflowExecution`` decision to fail this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **failWorkflowExecutionFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``FailWorkflowExecutionFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``FailWorkflowExecution`` decision to fail this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **workflowExecutionTimedOutEventAttributes** *(dict) --* 
        
                  If the event is of type ``WorkflowExecutionTimedOut`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **timeoutType** *(string) --* 
        
                    The type of timeout that caused this event.
        
                  - **childPolicy** *(string) --* 
        
                    The policy used for the child workflow executions of this workflow execution.
        
                    The supported child policies are:
        
                    * ``TERMINATE`` – The child executions are terminated. 
                     
                    * ``REQUEST_CANCEL`` – A request to cancel is attempted for each child execution by recording a ``WorkflowExecutionCancelRequested`` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event. 
                     
                    * ``ABANDON`` – No action is taken. The child executions continue to run. 
                     
                - **workflowExecutionCanceledEventAttributes** *(dict) --* 
        
                  If the event is of type ``WorkflowExecutionCanceled`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **details** *(string) --* 
        
                    The details of the cancellation.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``CancelWorkflowExecution`` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **cancelWorkflowExecutionFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``CancelWorkflowExecutionFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``CancelWorkflowExecution`` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **workflowExecutionContinuedAsNewEventAttributes** *(dict) --* 
        
                  If the event is of type ``WorkflowExecutionContinuedAsNew`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **input** *(string) --* 
        
                    The input provided to the new workflow execution.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``ContinueAsNewWorkflowExecution`` decision that started this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **newExecutionRunId** *(string) --* 
        
                    The ``runId`` of the new workflow execution.
        
                  - **executionStartToCloseTimeout** *(string) --* 
        
                    The total duration allowed for the new workflow execution.
        
                    The duration is specified in seconds, an integer greater than or equal to ``0`` . You can use ``NONE`` to specify unlimited duration.
        
                  - **taskList** *(dict) --* 
        
                    The task list to use for the decisions of the new (continued) workflow execution.
        
                    - **name** *(string) --* 
        
                      The name of the task list.
        
                  - **taskPriority** *(string) --* 
        
                    The priority of the task to use for the decisions of the new (continued) workflow execution.
        
                  - **taskStartToCloseTimeout** *(string) --* 
        
                    The maximum duration of decision tasks for the new workflow execution.
        
                    The duration is specified in seconds, an integer greater than or equal to ``0`` . You can use ``NONE`` to specify unlimited duration.
        
                  - **childPolicy** *(string) --* 
        
                    The policy to use for the child workflow executions of the new execution if it is terminated by calling the  TerminateWorkflowExecution action explicitly or due to an expired timeout.
        
                    The supported child policies are:
        
                    * ``TERMINATE`` – The child executions are terminated. 
                     
                    * ``REQUEST_CANCEL`` – A request to cancel is attempted for each child execution by recording a ``WorkflowExecutionCancelRequested`` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event. 
                     
                    * ``ABANDON`` – No action is taken. The child executions continue to run. 
                     
                  - **tagList** *(list) --* 
        
                    The list of tags associated with the new workflow execution.
        
                    - *(string) --* 
                
                  - **workflowType** *(dict) --* 
        
                    The workflow type of this execution.
        
                    - **name** *(string) --* 
        
                      The name of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                    - **version** *(string) --* 
        
                      The version of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                  - **lambdaRole** *(string) --* 
        
                    The IAM role to attach to the new (continued) workflow execution.
        
                - **continueAsNewWorkflowExecutionFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ContinueAsNewWorkflowExecutionFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``ContinueAsNewWorkflowExecution`` decision that started this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **workflowExecutionTerminatedEventAttributes** *(dict) --* 
        
                  If the event is of type ``WorkflowExecutionTerminated`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **reason** *(string) --* 
        
                    The reason provided for the termination.
        
                  - **details** *(string) --* 
        
                    The details provided for the termination.
        
                  - **childPolicy** *(string) --* 
        
                    The policy used for the child workflow executions of this workflow execution.
        
                    The supported child policies are:
        
                    * ``TERMINATE`` – The child executions are terminated. 
                     
                    * ``REQUEST_CANCEL`` – A request to cancel is attempted for each child execution by recording a ``WorkflowExecutionCancelRequested`` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event. 
                     
                    * ``ABANDON`` – No action is taken. The child executions continue to run. 
                     
                  - **cause** *(string) --* 
        
                    If set, indicates that the workflow execution was automatically terminated, and specifies the cause. This happens if the parent workflow execution times out or is terminated and the child policy is set to terminate child executions.
        
                - **workflowExecutionCancelRequestedEventAttributes** *(dict) --* 
        
                  If the event is of type ``WorkflowExecutionCancelRequested`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **externalWorkflowExecution** *(dict) --* 
        
                    The external workflow execution for which the cancellation was requested.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **externalInitiatedEventId** *(integer) --* 
        
                    The ID of the ``RequestCancelExternalWorkflowExecutionInitiated`` event corresponding to the ``RequestCancelExternalWorkflowExecution`` decision to cancel this workflow execution.The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **cause** *(string) --* 
        
                    If set, indicates that the request to cancel the workflow execution was automatically generated, and specifies the cause. This happens if the parent workflow execution times out or is terminated, and the child policy is set to cancel child executions.
        
                - **decisionTaskScheduledEventAttributes** *(dict) --* 
        
                  If the event is of type ``DecisionTaskScheduled`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **taskList** *(dict) --* 
        
                    The name of the task list in which the decision task was scheduled.
        
                    - **name** *(string) --* 
        
                      The name of the task list.
        
                  - **taskPriority** *(string) --* 
        
                    A task priority that, if set, specifies the priority for this decision task. Valid values are integers that range from Java\'s ``Integer.MIN_VALUE`` (-2147483648) to ``Integer.MAX_VALUE`` (2147483647). Higher numbers indicate higher priority.
        
                    For more information about setting task priority, see `Setting Task Priority <http://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **startToCloseTimeout** *(string) --* 
        
                    The maximum duration for this decision task. The task is considered timed out if it doesn\'t completed within this duration.
        
                    The duration is specified in seconds, an integer greater than or equal to ``0`` . You can use ``NONE`` to specify unlimited duration.
        
                - **decisionTaskStartedEventAttributes** *(dict) --* 
        
                  If the event is of type ``DecisionTaskStarted`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **identity** *(string) --* 
        
                    Identity of the decider making the request. This enables diagnostic tracing when problems arise. The form of this identity is user defined.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskScheduled`` event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **decisionTaskCompletedEventAttributes** *(dict) --* 
        
                  If the event is of type ``DecisionTaskCompleted`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **executionContext** *(string) --* 
        
                    User defined context for the workflow execution.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskScheduled`` event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskStarted`` event recorded when this decision task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **decisionTaskTimedOutEventAttributes** *(dict) --* 
        
                  If the event is of type ``DecisionTaskTimedOut`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **timeoutType** *(string) --* 
        
                    The type of timeout that expired before the decision task could be completed.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskScheduled`` event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskStarted`` event recorded when this decision task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **activityTaskScheduledEventAttributes** *(dict) --* 
        
                  If the event is of type ``ActivityTaskScheduled`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **activityType** *(dict) --* 
        
                    The type of the activity task.
        
                    - **name** *(string) --* 
        
                      The name of this activity.
        
                      .. note::
        
                        The combination of activity type name and version must be unique within a domain.
        
                    - **version** *(string) --* 
        
                      The version of this activity.
        
                      .. note::
        
                        The combination of activity type name and version must be unique with in a domain.
        
                  - **activityId** *(string) --* 
        
                    The unique ID of the activity task.
        
                  - **input** *(string) --* 
        
                    The input provided to the activity task.
        
                  - **control** *(string) --* 
        
                    Data attached to the event that can be used by the decider in subsequent workflow tasks. This data isn\'t sent to the activity.
        
                  - **scheduleToStartTimeout** *(string) --* 
        
                    The maximum amount of time the activity task can wait to be assigned to a worker.
        
                  - **scheduleToCloseTimeout** *(string) --* 
        
                    The maximum amount of time for this activity task.
        
                  - **startToCloseTimeout** *(string) --* 
        
                    The maximum amount of time a worker may take to process the activity task.
        
                  - **taskList** *(dict) --* 
        
                    The task list in which the activity task has been scheduled.
        
                    - **name** *(string) --* 
        
                      The name of the task list.
        
                  - **taskPriority** *(string) --* 
        
                    The priority to assign to the scheduled activity task. If set, this overrides any default priority value that was assigned when the activity type was registered.
        
                    Valid values are integers that range from Java\'s ``Integer.MIN_VALUE`` (-2147483648) to ``Integer.MAX_VALUE`` (2147483647). Higher numbers indicate higher priority.
        
                    For more information about setting task priority, see `Setting Task Priority <http://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision that resulted in the scheduling of this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **heartbeatTimeout** *(string) --* 
        
                    The maximum time before which the worker processing this task must report progress by calling  RecordActivityTaskHeartbeat . If the timeout is exceeded, the activity task is automatically timed out. If the worker subsequently attempts to record a heartbeat or return a result, it is ignored.
        
                - **activityTaskStartedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ActivityTaskStarted`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **identity** *(string) --* 
        
                    Identity of the worker that was assigned this task. This aids diagnostics when problems arise. The form of this identity is user defined.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskScheduled`` event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **activityTaskCompletedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ActivityTaskCompleted`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **result** *(string) --* 
        
                    The results of the activity task.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskScheduled`` event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskStarted`` event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **activityTaskFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ActivityTaskFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **reason** *(string) --* 
        
                    The reason provided for the failure.
        
                  - **details** *(string) --* 
        
                    The details of the failure.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskScheduled`` event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskStarted`` event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **activityTaskTimedOutEventAttributes** *(dict) --* 
        
                  If the event is of type ``ActivityTaskTimedOut`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **timeoutType** *(string) --* 
        
                    The type of the timeout that caused this event.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskScheduled`` event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskStarted`` event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **details** *(string) --* 
        
                    Contains the content of the ``details`` parameter for the last call made by the activity to ``RecordActivityTaskHeartbeat`` .
        
                - **activityTaskCanceledEventAttributes** *(dict) --* 
        
                  If the event is of type ``ActivityTaskCanceled`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **details** *(string) --* 
        
                    Details of the cancellation.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskScheduled`` event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskStarted`` event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **latestCancelRequestedEventId** *(integer) --* 
        
                    If set, contains the ID of the last ``ActivityTaskCancelRequested`` event recorded for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **activityTaskCancelRequestedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ActivityTaskcancelRequested`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``RequestCancelActivityTask`` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **activityId** *(string) --* 
        
                    The unique ID of the task.
        
                - **workflowExecutionSignaledEventAttributes** *(dict) --* 
        
                  If the event is of type ``WorkflowExecutionSignaled`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **signalName** *(string) --* 
        
                    The name of the signal received. The decider can use the signal name and inputs to determine how to the process the signal.
        
                  - **input** *(string) --* 
        
                    The inputs provided with the signal. The decider can use the signal name and inputs to determine how to process the signal.
        
                  - **externalWorkflowExecution** *(dict) --* 
        
                    The workflow execution that sent the signal. This is set only of the signal was sent by another workflow execution.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **externalInitiatedEventId** *(integer) --* 
        
                    The ID of the ``SignalExternalWorkflowExecutionInitiated`` event corresponding to the ``SignalExternalWorkflow`` decision to signal this workflow execution.The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event. This field is set only if the signal was initiated by another workflow execution.
        
                - **markerRecordedEventAttributes** *(dict) --* 
        
                  If the event is of type ``MarkerRecorded`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **markerName** *(string) --* 
        
                    The name of the marker.
        
                  - **details** *(string) --* 
        
                    The details of the marker.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``RecordMarker`` decision that requested this marker. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **recordMarkerFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``DecisionTaskFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **markerName** *(string) --* 
        
                    The marker\'s name.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``RecordMarkerFailed`` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **timerStartedEventAttributes** *(dict) --* 
        
                  If the event is of type ``TimerStarted`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **timerId** *(string) --* 
        
                    The unique ID of the timer that was started.
        
                  - **control** *(string) --* 
        
                    Data attached to the event that can be used by the decider in subsequent workflow tasks.
        
                  - **startToFireTimeout** *(string) --* 
        
                    The duration of time after which the timer fires.
        
                    The duration is specified in seconds, an integer greater than or equal to ``0`` .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``StartTimer`` decision for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **timerFiredEventAttributes** *(dict) --* 
        
                  If the event is of type ``TimerFired`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **timerId** *(string) --* 
        
                    The unique ID of the timer that fired.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``TimerStarted`` event that was recorded when this timer was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **timerCanceledEventAttributes** *(dict) --* 
        
                  If the event is of type ``TimerCanceled`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **timerId** *(string) --* 
        
                    The unique ID of the timer that was canceled.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``TimerStarted`` event that was recorded when this timer was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``CancelTimer`` decision to cancel this timer. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **startChildWorkflowExecutionInitiatedEventAttributes** *(dict) --* 
        
                  If the event is of type ``StartChildWorkflowExecutionInitiated`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowId** *(string) --* 
        
                    The ``workflowId`` of the child workflow execution.
        
                  - **workflowType** *(dict) --* 
        
                    The type of the child workflow execution.
        
                    - **name** *(string) --* 
        
                      The name of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                    - **version** *(string) --* 
        
                      The version of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                  - **control** *(string) --* 
        
                    Data attached to the event that can be used by the decider in subsequent decision tasks. This data isn\'t sent to the activity.
        
                  - **input** *(string) --* 
        
                    The inputs provided to the child workflow execution.
        
                  - **executionStartToCloseTimeout** *(string) --* 
        
                    The maximum duration for the child workflow execution. If the workflow execution isn\'t closed within this duration, it is timed out and force-terminated.
        
                    The duration is specified in seconds, an integer greater than or equal to ``0`` . You can use ``NONE`` to specify unlimited duration.
        
                  - **taskList** *(dict) --* 
        
                    The name of the task list used for the decision tasks of the child workflow execution.
        
                    - **name** *(string) --* 
        
                      The name of the task list.
        
                  - **taskPriority** *(string) --* 
        
                    The priority assigned for the decision tasks for this workflow execution. Valid values are integers that range from Java\'s ``Integer.MIN_VALUE`` (-2147483648) to ``Integer.MAX_VALUE`` (2147483647). Higher numbers indicate higher priority.
        
                    For more information about setting task priority, see `Setting Task Priority <http://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``StartChildWorkflowExecution``   Decision to request this child workflow execution. This information can be useful for diagnosing problems by tracing back the cause of events.
        
                  - **childPolicy** *(string) --* 
        
                    The policy to use for the child workflow executions if this execution gets terminated by explicitly calling the  TerminateWorkflowExecution action or due to an expired timeout.
        
                    The supported child policies are:
        
                    * ``TERMINATE`` – The child executions are terminated. 
                     
                    * ``REQUEST_CANCEL`` – A request to cancel is attempted for each child execution by recording a ``WorkflowExecutionCancelRequested`` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event. 
                     
                    * ``ABANDON`` – No action is taken. The child executions continue to run. 
                     
                  - **taskStartToCloseTimeout** *(string) --* 
        
                    The maximum duration allowed for the decision tasks for this workflow execution.
        
                    The duration is specified in seconds, an integer greater than or equal to ``0`` . You can use ``NONE`` to specify unlimited duration.
        
                  - **tagList** *(list) --* 
        
                    The list of tags to associated with the child workflow execution.
        
                    - *(string) --* 
                
                  - **lambdaRole** *(string) --* 
        
                    The IAM role to attach to the child workflow execution.
        
                - **childWorkflowExecutionStartedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ChildWorkflowExecutionStarted`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowExecution** *(dict) --* 
        
                    The child workflow execution that was started.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **workflowType** *(dict) --* 
        
                    The type of the child workflow execution.
        
                    - **name** *(string) --* 
        
                      The name of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                    - **version** *(string) --* 
        
                      The version of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                  - **initiatedEventId** *(integer) --* 
        
                    The ID of the ``StartChildWorkflowExecutionInitiated`` event corresponding to the ``StartChildWorkflowExecution``   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **childWorkflowExecutionCompletedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ChildWorkflowExecutionCompleted`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowExecution** *(dict) --* 
        
                    The child workflow execution that was completed.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **workflowType** *(dict) --* 
        
                    The type of the child workflow execution.
        
                    - **name** *(string) --* 
        
                      The name of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                    - **version** *(string) --* 
        
                      The version of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                  - **result** *(string) --* 
        
                    The result of the child workflow execution.
        
                  - **initiatedEventId** *(integer) --* 
        
                    The ID of the ``StartChildWorkflowExecutionInitiated`` event corresponding to the ``StartChildWorkflowExecution``   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``ChildWorkflowExecutionStarted`` event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **childWorkflowExecutionFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ChildWorkflowExecutionFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowExecution** *(dict) --* 
        
                    The child workflow execution that failed.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **workflowType** *(dict) --* 
        
                    The type of the child workflow execution.
        
                    - **name** *(string) --* 
        
                      The name of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                    - **version** *(string) --* 
        
                      The version of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                  - **reason** *(string) --* 
        
                    The reason for the failure (if provided).
        
                  - **details** *(string) --* 
        
                    The details of the failure (if provided).
        
                  - **initiatedEventId** *(integer) --* 
        
                    The ID of the ``StartChildWorkflowExecutionInitiated`` event corresponding to the ``StartChildWorkflowExecution``   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``ChildWorkflowExecutionStarted`` event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **childWorkflowExecutionTimedOutEventAttributes** *(dict) --* 
        
                  If the event is of type ``ChildWorkflowExecutionTimedOut`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowExecution** *(dict) --* 
        
                    The child workflow execution that timed out.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **workflowType** *(dict) --* 
        
                    The type of the child workflow execution.
        
                    - **name** *(string) --* 
        
                      The name of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                    - **version** *(string) --* 
        
                      The version of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                  - **timeoutType** *(string) --* 
        
                    The type of the timeout that caused the child workflow execution to time out.
        
                  - **initiatedEventId** *(integer) --* 
        
                    The ID of the ``StartChildWorkflowExecutionInitiated`` event corresponding to the ``StartChildWorkflowExecution``   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``ChildWorkflowExecutionStarted`` event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **childWorkflowExecutionCanceledEventAttributes** *(dict) --* 
        
                  If the event is of type ``ChildWorkflowExecutionCanceled`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowExecution** *(dict) --* 
        
                    The child workflow execution that was canceled.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **workflowType** *(dict) --* 
        
                    The type of the child workflow execution.
        
                    - **name** *(string) --* 
        
                      The name of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                    - **version** *(string) --* 
        
                      The version of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                  - **details** *(string) --* 
        
                    Details of the cancellation (if provided).
        
                  - **initiatedEventId** *(integer) --* 
        
                    The ID of the ``StartChildWorkflowExecutionInitiated`` event corresponding to the ``StartChildWorkflowExecution``   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``ChildWorkflowExecutionStarted`` event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **childWorkflowExecutionTerminatedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ChildWorkflowExecutionTerminated`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowExecution** *(dict) --* 
        
                    The child workflow execution that was terminated.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **workflowType** *(dict) --* 
        
                    The type of the child workflow execution.
        
                    - **name** *(string) --* 
        
                      The name of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                    - **version** *(string) --* 
        
                      The version of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                  - **initiatedEventId** *(integer) --* 
        
                    The ID of the ``StartChildWorkflowExecutionInitiated`` event corresponding to the ``StartChildWorkflowExecution``   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``ChildWorkflowExecutionStarted`` event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **signalExternalWorkflowExecutionInitiatedEventAttributes** *(dict) --* 
        
                  If the event is of type ``SignalExternalWorkflowExecutionInitiated`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowId** *(string) --* 
        
                    The ``workflowId`` of the external workflow execution.
        
                  - **runId** *(string) --* 
        
                    The ``runId`` of the external workflow execution to send the signal to.
        
                  - **signalName** *(string) --* 
        
                    The name of the signal.
        
                  - **input** *(string) --* 
        
                    The input provided to the signal.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``SignalExternalWorkflowExecution`` decision for this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **control** *(string) --* 
        
                    Data attached to the event that can be used by the decider in subsequent decision tasks.
        
                - **externalWorkflowExecutionSignaledEventAttributes** *(dict) --* 
        
                  If the event is of type ``ExternalWorkflowExecutionSignaled`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowExecution** *(dict) --* 
        
                    The external workflow execution that the signal was delivered to.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **initiatedEventId** *(integer) --* 
        
                    The ID of the ``SignalExternalWorkflowExecutionInitiated`` event corresponding to the ``SignalExternalWorkflowExecution`` decision to request this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **signalExternalWorkflowExecutionFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``SignalExternalWorkflowExecutionFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowId** *(string) --* 
        
                    The ``workflowId`` of the external workflow execution that the signal was being delivered to.
        
                  - **runId** *(string) --* 
        
                    The ``runId`` of the external workflow execution that the signal was being delivered to.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **initiatedEventId** *(integer) --* 
        
                    The ID of the ``SignalExternalWorkflowExecutionInitiated`` event corresponding to the ``SignalExternalWorkflowExecution`` decision to request this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``SignalExternalWorkflowExecution`` decision for this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **control** *(string) --* 
        
                    The data attached to the event that the decider can use in subsequent workflow tasks. This data isn\'t sent to the workflow execution.
        
                - **externalWorkflowExecutionCancelRequestedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ExternalWorkflowExecutionCancelRequested`` then this member is set and provides detailed information about the event. It isn\'t set for other event types. 
        
                  - **workflowExecution** *(dict) --* 
        
                    The external workflow execution to which the cancellation request was delivered.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **initiatedEventId** *(integer) --* 
        
                    The ID of the ``RequestCancelExternalWorkflowExecutionInitiated`` event corresponding to the ``RequestCancelExternalWorkflowExecution`` decision to cancel this external workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **requestCancelExternalWorkflowExecutionInitiatedEventAttributes** *(dict) --* 
        
                  If the event is of type ``RequestCancelExternalWorkflowExecutionInitiated`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowId** *(string) --* 
        
                    The ``workflowId`` of the external workflow execution to be canceled.
        
                  - **runId** *(string) --* 
        
                    The ``runId`` of the external workflow execution to be canceled.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``RequestCancelExternalWorkflowExecution`` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **control** *(string) --* 
        
                    Data attached to the event that can be used by the decider in subsequent workflow tasks.
        
                - **requestCancelExternalWorkflowExecutionFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``RequestCancelExternalWorkflowExecutionFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowId** *(string) --* 
        
                    The ``workflowId`` of the external workflow to which the cancel request was to be delivered.
        
                  - **runId** *(string) --* 
        
                    The ``runId`` of the external workflow execution.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **initiatedEventId** *(integer) --* 
        
                    The ID of the ``RequestCancelExternalWorkflowExecutionInitiated`` event corresponding to the ``RequestCancelExternalWorkflowExecution`` decision to cancel this external workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``RequestCancelExternalWorkflowExecution`` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **control** *(string) --* 
        
                    The data attached to the event that the decider can use in subsequent workflow tasks. This data isn\'t sent to the workflow execution.
        
                - **scheduleActivityTaskFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ScheduleActivityTaskFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **activityType** *(dict) --* 
        
                    The activity type provided in the ``ScheduleActivityTask`` decision that failed.
        
                    - **name** *(string) --* 
        
                      The name of this activity.
        
                      .. note::
        
                        The combination of activity type name and version must be unique within a domain.
        
                    - **version** *(string) --* 
        
                      The version of this activity.
        
                      .. note::
        
                        The combination of activity type name and version must be unique with in a domain.
        
                  - **activityId** *(string) --* 
        
                    The activityId provided in the ``ScheduleActivityTask`` decision that failed.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision that resulted in the scheduling of this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **requestCancelActivityTaskFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``RequestCancelActivityTaskFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **activityId** *(string) --* 
        
                    The activityId provided in the ``RequestCancelActivityTask`` decision that failed.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``RequestCancelActivityTask`` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **startTimerFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``StartTimerFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **timerId** *(string) --* 
        
                    The timerId provided in the ``StartTimer`` decision that failed.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``StartTimer`` decision for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **cancelTimerFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``CancelTimerFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **timerId** *(string) --* 
        
                    The timerId provided in the ``CancelTimer`` decision that failed.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``CancelTimer`` decision to cancel this timer. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **startChildWorkflowExecutionFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``StartChildWorkflowExecutionFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowType** *(dict) --* 
        
                    The workflow type provided in the ``StartChildWorkflowExecution``   Decision that failed.
        
                    - **name** *(string) --* 
        
                      The name of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                    - **version** *(string) --* 
        
                      The version of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      When ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision fails because it lacks sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **workflowId** *(string) --* 
        
                    The ``workflowId`` of the child workflow execution.
        
                  - **initiatedEventId** *(integer) --* 
        
                    When the ``cause`` is ``WORKFLOW_ALREADY_RUNNING`` , ``initiatedEventId`` is the ID of the ``StartChildWorkflowExecutionInitiated`` event that corresponds to the ``StartChildWorkflowExecution``   Decision to start the workflow execution. You can use this information to diagnose problems by tracing back the chain of events leading up to this event.
        
                    When the ``cause`` isn\'t ``WORKFLOW_ALREADY_RUNNING`` , ``initiatedEventId`` is set to ``0`` because the ``StartChildWorkflowExecutionInitiated`` event doesn\'t exist.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``StartChildWorkflowExecution``   Decision to request this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events.
        
                  - **control** *(string) --* 
        
                    The data attached to the event that the decider can use in subsequent workflow tasks. This data isn\'t sent to the child workflow execution.
        
                - **lambdaFunctionScheduledEventAttributes** *(dict) --* 
        
                  Provides the details of the ``LambdaFunctionScheduled`` event. It isn\'t set for other event types.
        
                  - **id** *(string) --* 
        
                    The unique ID of the Lambda task.
        
                  - **name** *(string) --* 
        
                    The name of the Lambda function.
        
                  - **control** *(string) --* 
        
                    Data attached to the event that the decider can use in subsequent workflow tasks. This data isn\'t sent to the Lambda task.
        
                  - **input** *(string) --* 
        
                    The input provided to the Lambda task.
        
                  - **startToCloseTimeout** *(string) --* 
        
                    The maximum amount of time a worker can take to process the Lambda task.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``LambdaFunctionCompleted`` event corresponding to the decision that resulted in scheduling this activity task. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                - **lambdaFunctionStartedEventAttributes** *(dict) --* 
        
                  Provides the details of the ``LambdaFunctionStarted`` event. It isn\'t set for other event types.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``LambdaFunctionScheduled`` event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                - **lambdaFunctionCompletedEventAttributes** *(dict) --* 
        
                  Provides the details of the ``LambdaFunctionCompleted`` event. It isn\'t set for other event types.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``LambdaFunctionScheduled`` event that was recorded when this Lambda task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``LambdaFunctionStarted`` event recorded when this activity task started. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                  - **result** *(string) --* 
        
                    The results of the Lambda task.
        
                - **lambdaFunctionFailedEventAttributes** *(dict) --* 
        
                  Provides the details of the ``LambdaFunctionFailed`` event. It isn\'t set for other event types.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``LambdaFunctionScheduled`` event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``LambdaFunctionStarted`` event recorded when this activity task started. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                  - **reason** *(string) --* 
        
                    The reason provided for the failure.
        
                  - **details** *(string) --* 
        
                    The details of the failure.
        
                - **lambdaFunctionTimedOutEventAttributes** *(dict) --* 
        
                  Provides the details of the ``LambdaFunctionTimedOut`` event. It isn\'t set for other event types.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``LambdaFunctionScheduled`` event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskStarted`` event that was recorded when this activity task started. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                  - **timeoutType** *(string) --* 
        
                    The type of the timeout that caused this event.
        
                - **scheduleLambdaFunctionFailedEventAttributes** *(dict) --* 
        
                  Provides the details of the ``ScheduleLambdaFunctionFailed`` event. It isn\'t set for other event types.
        
                  - **id** *(string) --* 
        
                    The ID provided in the ``ScheduleLambdaFunction`` decision that failed. 
        
                  - **name** *(string) --* 
        
                    The name of the Lambda function.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``LambdaFunctionCompleted`` event corresponding to the decision that resulted in scheduling this Lambda task. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                - **startLambdaFunctionFailedEventAttributes** *(dict) --* 
        
                  Provides the details of the ``StartLambdaFunctionFailed`` event. It isn\'t set for other event types.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskScheduled`` event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because the IAM role attached to the execution lacked sufficient permissions. For details and example IAM policies, see `Lambda Tasks <http://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **message** *(string) --* 
        
                    A description that can help diagnose the cause of the fault.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListActivityTypes(Paginator):
    def paginate(self, domain: str, registrationStatus: str, name: str = None, reverseOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/swf-2012-01-25/ListActivityTypes>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              domain=\'string\',
              name=\'string\',
              registrationStatus=\'REGISTERED\'|\'DEPRECATED\',
              reverseOrder=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type domain: string
        :param domain: **[REQUIRED]** 
        
          The name of the domain in which the activity types have been registered.
        
        :type name: string
        :param name: 
        
          If specified, only lists the activity types that have this name.
        
        :type registrationStatus: string
        :param registrationStatus: **[REQUIRED]** 
        
          Specifies the registration status of the activity types to list.
        
        :type reverseOrder: boolean
        :param reverseOrder: 
        
          When set to ``true`` , returns the results in reverse order. By default, the results are returned in ascending alphabetical order by ``name`` of the activity types.
        
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
                \'typeInfos\': [
                    {
                        \'activityType\': {
                            \'name\': \'string\',
                            \'version\': \'string\'
                        },
                        \'status\': \'REGISTERED\'|\'DEPRECATED\',
                        \'description\': \'string\',
                        \'creationDate\': datetime(2015, 1, 1),
                        \'deprecationDate\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains a paginated list of activity type information structures.
        
            - **typeInfos** *(list) --* 
        
              List of activity type information.
        
              - *(dict) --* 
        
                Detailed information about an activity type.
        
                - **activityType** *(dict) --* 
        
                  The  ActivityType type structure representing the activity type.
        
                  - **name** *(string) --* 
        
                    The name of this activity.
        
                    .. note::
        
                      The combination of activity type name and version must be unique within a domain.
        
                  - **version** *(string) --* 
        
                    The version of this activity.
        
                    .. note::
        
                      The combination of activity type name and version must be unique with in a domain.
        
                - **status** *(string) --* 
        
                  The current status of the activity type.
        
                - **description** *(string) --* 
        
                  The description of the activity type provided in  RegisterActivityType .
        
                - **creationDate** *(datetime) --* 
        
                  The date and time this activity type was created through  RegisterActivityType .
        
                - **deprecationDate** *(datetime) --* 
        
                  If DEPRECATED, the date and time  DeprecateActivityType was called.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListClosedWorkflowExecutions(Paginator):
    def paginate(self, domain: str, startTimeFilter: Dict = None, closeTimeFilter: Dict = None, executionFilter: Dict = None, closeStatusFilter: Dict = None, typeFilter: Dict = None, tagFilter: Dict = None, reverseOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/swf-2012-01-25/ListClosedWorkflowExecutions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              domain=\'string\',
              startTimeFilter={
                  \'oldestDate\': datetime(2015, 1, 1),
                  \'latestDate\': datetime(2015, 1, 1)
              },
              closeTimeFilter={
                  \'oldestDate\': datetime(2015, 1, 1),
                  \'latestDate\': datetime(2015, 1, 1)
              },
              executionFilter={
                  \'workflowId\': \'string\'
              },
              closeStatusFilter={
                  \'status\': \'COMPLETED\'|\'FAILED\'|\'CANCELED\'|\'TERMINATED\'|\'CONTINUED_AS_NEW\'|\'TIMED_OUT\'
              },
              typeFilter={
                  \'name\': \'string\',
                  \'version\': \'string\'
              },
              tagFilter={
                  \'tag\': \'string\'
              },
              reverseOrder=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type domain: string
        :param domain: **[REQUIRED]** 
        
          The name of the domain that contains the workflow executions to list.
        
        :type startTimeFilter: dict
        :param startTimeFilter: 
        
          If specified, the workflow executions are included in the returned results based on whether their start times are within the range specified by this filter. Also, if this parameter is specified, the returned results are ordered by their start times.
        
          .. note::
        
             ``startTimeFilter`` and ``closeTimeFilter`` are mutually exclusive. You must specify one of these in a request but not both.
        
          - **oldestDate** *(datetime) --* **[REQUIRED]** 
        
            Specifies the oldest start or close date and time to return.
        
          - **latestDate** *(datetime) --* 
        
            Specifies the latest start or close date and time to return.
        
        :type closeTimeFilter: dict
        :param closeTimeFilter: 
        
          If specified, the workflow executions are included in the returned results based on whether their close times are within the range specified by this filter. Also, if this parameter is specified, the returned results are ordered by their close times.
        
          .. note::
        
             ``startTimeFilter`` and ``closeTimeFilter`` are mutually exclusive. You must specify one of these in a request but not both.
        
          - **oldestDate** *(datetime) --* **[REQUIRED]** 
        
            Specifies the oldest start or close date and time to return.
        
          - **latestDate** *(datetime) --* 
        
            Specifies the latest start or close date and time to return.
        
        :type executionFilter: dict
        :param executionFilter: 
        
          If specified, only workflow executions matching the workflow ID specified in the filter are returned.
        
          .. note::
        
             ``closeStatusFilter`` , ``executionFilter`` , ``typeFilter`` and ``tagFilter`` are mutually exclusive. You can specify at most one of these in a request.
        
          - **workflowId** *(string) --* **[REQUIRED]** 
        
            The workflowId to pass of match the criteria of this filter.
        
        :type closeStatusFilter: dict
        :param closeStatusFilter: 
        
          If specified, only workflow executions that match this *close status* are listed. For example, if TERMINATED is specified, then only TERMINATED workflow executions are listed.
        
          .. note::
        
             ``closeStatusFilter`` , ``executionFilter`` , ``typeFilter`` and ``tagFilter`` are mutually exclusive. You can specify at most one of these in a request.
        
          - **status** *(string) --* **[REQUIRED]** 
        
            The close status that must match the close status of an execution for it to meet the criteria of this filter.
        
        :type typeFilter: dict
        :param typeFilter: 
        
          If specified, only executions of the type specified in the filter are returned.
        
          .. note::
        
             ``closeStatusFilter`` , ``executionFilter`` , ``typeFilter`` and ``tagFilter`` are mutually exclusive. You can specify at most one of these in a request.
        
          - **name** *(string) --* **[REQUIRED]** 
        
            Name of the workflow type.
        
          - **version** *(string) --* 
        
            Version of the workflow type.
        
        :type tagFilter: dict
        :param tagFilter: 
        
          If specified, only executions that have the matching tag are listed.
        
          .. note::
        
             ``closeStatusFilter`` , ``executionFilter`` , ``typeFilter`` and ``tagFilter`` are mutually exclusive. You can specify at most one of these in a request.
        
          - **tag** *(string) --* **[REQUIRED]** 
        
            Specifies the tag that must be associated with the execution for it to meet the filter criteria.
        
        :type reverseOrder: boolean
        :param reverseOrder: 
        
          When set to ``true`` , returns the results in reverse order. By default the results are returned in descending order of the start or the close time of the executions.
        
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
                \'executionInfos\': [
                    {
                        \'execution\': {
                            \'workflowId\': \'string\',
                            \'runId\': \'string\'
                        },
                        \'workflowType\': {
                            \'name\': \'string\',
                            \'version\': \'string\'
                        },
                        \'startTimestamp\': datetime(2015, 1, 1),
                        \'closeTimestamp\': datetime(2015, 1, 1),
                        \'executionStatus\': \'OPEN\'|\'CLOSED\',
                        \'closeStatus\': \'COMPLETED\'|\'FAILED\'|\'CANCELED\'|\'TERMINATED\'|\'CONTINUED_AS_NEW\'|\'TIMED_OUT\',
                        \'parent\': {
                            \'workflowId\': \'string\',
                            \'runId\': \'string\'
                        },
                        \'tagList\': [
                            \'string\',
                        ],
                        \'cancelRequested\': True|False
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains a paginated list of information about workflow executions.
        
            - **executionInfos** *(list) --* 
        
              The list of workflow information structures.
        
              - *(dict) --* 
        
                Contains information about a workflow execution.
        
                - **execution** *(dict) --* 
        
                  The workflow execution this information is about.
        
                  - **workflowId** *(string) --* 
        
                    The user defined identifier associated with the workflow execution.
        
                  - **runId** *(string) --* 
        
                    A system-generated unique identifier for the workflow execution.
        
                - **workflowType** *(dict) --* 
        
                  The type of the workflow execution.
        
                  - **name** *(string) --* 
        
                    The name of the workflow type.
        
                    .. note::
        
                      The combination of workflow type name and version must be unique with in a domain.
        
                  - **version** *(string) --* 
        
                    The version of the workflow type.
        
                    .. note::
        
                      The combination of workflow type name and version must be unique with in a domain.
        
                - **startTimestamp** *(datetime) --* 
        
                  The time when the execution was started.
        
                - **closeTimestamp** *(datetime) --* 
        
                  The time when the workflow execution was closed. Set only if the execution status is CLOSED.
        
                - **executionStatus** *(string) --* 
        
                  The current status of the execution.
        
                - **closeStatus** *(string) --* 
        
                  If the execution status is closed then this specifies how the execution was closed:
        
                  * ``COMPLETED`` – the execution was successfully completed. 
                   
                  * ``CANCELED`` – the execution was canceled.Cancellation allows the implementation to gracefully clean up before the execution is closed. 
                   
                  * ``TERMINATED`` – the execution was force terminated. 
                   
                  * ``FAILED`` – the execution failed to complete. 
                   
                  * ``TIMED_OUT`` – the execution did not complete in the alloted time and was automatically timed out. 
                   
                  * ``CONTINUED_AS_NEW`` – the execution is logically continued. This means the current execution was completed and a new execution was started to carry on the workflow. 
                   
                - **parent** *(dict) --* 
        
                  If this workflow execution is a child of another execution then contains the workflow execution that started this execution.
        
                  - **workflowId** *(string) --* 
        
                    The user defined identifier associated with the workflow execution.
        
                  - **runId** *(string) --* 
        
                    A system-generated unique identifier for the workflow execution.
        
                - **tagList** *(list) --* 
        
                  The list of tags associated with the workflow execution. Tags can be used to identify and list workflow executions of interest through the visibility APIs. A workflow execution can have a maximum of 5 tags.
        
                  - *(string) --* 
              
                - **cancelRequested** *(boolean) --* 
        
                  Set to true if a cancellation is requested for this workflow execution.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListDomains(Paginator):
    def paginate(self, registrationStatus: str, reverseOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/swf-2012-01-25/ListDomains>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              registrationStatus=\'REGISTERED\'|\'DEPRECATED\',
              reverseOrder=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type registrationStatus: string
        :param registrationStatus: **[REQUIRED]** 
        
          Specifies the registration status of the domains to list.
        
        :type reverseOrder: boolean
        :param reverseOrder: 
        
          When set to ``true`` , returns the results in reverse order. By default, the results are returned in ascending alphabetical order by ``name`` of the domains.
        
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
                \'domainInfos\': [
                    {
                        \'name\': \'string\',
                        \'status\': \'REGISTERED\'|\'DEPRECATED\',
                        \'description\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains a paginated collection of DomainInfo structures.
        
            - **domainInfos** *(list) --* 
        
              A list of DomainInfo structures.
        
              - *(dict) --* 
        
                Contains general information about a domain.
        
                - **name** *(string) --* 
        
                  The name of the domain. This name is unique within the account.
        
                - **status** *(string) --* 
        
                  The status of the domain:
        
                  * ``REGISTERED`` – The domain is properly registered and available. You can use this domain for registering types and creating new workflow executions.  
                   
                  * ``DEPRECATED`` – The domain was deprecated using  DeprecateDomain , but is still in use. You should not create new workflow executions in this domain.  
                   
                - **description** *(string) --* 
        
                  The description of the domain provided through  RegisterDomain .
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListOpenWorkflowExecutions(Paginator):
    def paginate(self, domain: str, startTimeFilter: Dict, typeFilter: Dict = None, tagFilter: Dict = None, reverseOrder: bool = None, executionFilter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/swf-2012-01-25/ListOpenWorkflowExecutions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              domain=\'string\',
              startTimeFilter={
                  \'oldestDate\': datetime(2015, 1, 1),
                  \'latestDate\': datetime(2015, 1, 1)
              },
              typeFilter={
                  \'name\': \'string\',
                  \'version\': \'string\'
              },
              tagFilter={
                  \'tag\': \'string\'
              },
              reverseOrder=True|False,
              executionFilter={
                  \'workflowId\': \'string\'
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type domain: string
        :param domain: **[REQUIRED]** 
        
          The name of the domain that contains the workflow executions to list.
        
        :type startTimeFilter: dict
        :param startTimeFilter: **[REQUIRED]** 
        
          Workflow executions are included in the returned results based on whether their start times are within the range specified by this filter.
        
          - **oldestDate** *(datetime) --* **[REQUIRED]** 
        
            Specifies the oldest start or close date and time to return.
        
          - **latestDate** *(datetime) --* 
        
            Specifies the latest start or close date and time to return.
        
        :type typeFilter: dict
        :param typeFilter: 
        
          If specified, only executions of the type specified in the filter are returned.
        
          .. note::
        
             ``executionFilter`` , ``typeFilter`` and ``tagFilter`` are mutually exclusive. You can specify at most one of these in a request.
        
          - **name** *(string) --* **[REQUIRED]** 
        
            Name of the workflow type.
        
          - **version** *(string) --* 
        
            Version of the workflow type.
        
        :type tagFilter: dict
        :param tagFilter: 
        
          If specified, only executions that have the matching tag are listed.
        
          .. note::
        
             ``executionFilter`` , ``typeFilter`` and ``tagFilter`` are mutually exclusive. You can specify at most one of these in a request.
        
          - **tag** *(string) --* **[REQUIRED]** 
        
            Specifies the tag that must be associated with the execution for it to meet the filter criteria.
        
        :type reverseOrder: boolean
        :param reverseOrder: 
        
          When set to ``true`` , returns the results in reverse order. By default the results are returned in descending order of the start time of the executions.
        
        :type executionFilter: dict
        :param executionFilter: 
        
          If specified, only workflow executions matching the workflow ID specified in the filter are returned.
        
          .. note::
        
             ``executionFilter`` , ``typeFilter`` and ``tagFilter`` are mutually exclusive. You can specify at most one of these in a request.
        
          - **workflowId** *(string) --* **[REQUIRED]** 
        
            The workflowId to pass of match the criteria of this filter.
        
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
                \'executionInfos\': [
                    {
                        \'execution\': {
                            \'workflowId\': \'string\',
                            \'runId\': \'string\'
                        },
                        \'workflowType\': {
                            \'name\': \'string\',
                            \'version\': \'string\'
                        },
                        \'startTimestamp\': datetime(2015, 1, 1),
                        \'closeTimestamp\': datetime(2015, 1, 1),
                        \'executionStatus\': \'OPEN\'|\'CLOSED\',
                        \'closeStatus\': \'COMPLETED\'|\'FAILED\'|\'CANCELED\'|\'TERMINATED\'|\'CONTINUED_AS_NEW\'|\'TIMED_OUT\',
                        \'parent\': {
                            \'workflowId\': \'string\',
                            \'runId\': \'string\'
                        },
                        \'tagList\': [
                            \'string\',
                        ],
                        \'cancelRequested\': True|False
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains a paginated list of information about workflow executions.
        
            - **executionInfos** *(list) --* 
        
              The list of workflow information structures.
        
              - *(dict) --* 
        
                Contains information about a workflow execution.
        
                - **execution** *(dict) --* 
        
                  The workflow execution this information is about.
        
                  - **workflowId** *(string) --* 
        
                    The user defined identifier associated with the workflow execution.
        
                  - **runId** *(string) --* 
        
                    A system-generated unique identifier for the workflow execution.
        
                - **workflowType** *(dict) --* 
        
                  The type of the workflow execution.
        
                  - **name** *(string) --* 
        
                    The name of the workflow type.
        
                    .. note::
        
                      The combination of workflow type name and version must be unique with in a domain.
        
                  - **version** *(string) --* 
        
                    The version of the workflow type.
        
                    .. note::
        
                      The combination of workflow type name and version must be unique with in a domain.
        
                - **startTimestamp** *(datetime) --* 
        
                  The time when the execution was started.
        
                - **closeTimestamp** *(datetime) --* 
        
                  The time when the workflow execution was closed. Set only if the execution status is CLOSED.
        
                - **executionStatus** *(string) --* 
        
                  The current status of the execution.
        
                - **closeStatus** *(string) --* 
        
                  If the execution status is closed then this specifies how the execution was closed:
        
                  * ``COMPLETED`` – the execution was successfully completed. 
                   
                  * ``CANCELED`` – the execution was canceled.Cancellation allows the implementation to gracefully clean up before the execution is closed. 
                   
                  * ``TERMINATED`` – the execution was force terminated. 
                   
                  * ``FAILED`` – the execution failed to complete. 
                   
                  * ``TIMED_OUT`` – the execution did not complete in the alloted time and was automatically timed out. 
                   
                  * ``CONTINUED_AS_NEW`` – the execution is logically continued. This means the current execution was completed and a new execution was started to carry on the workflow. 
                   
                - **parent** *(dict) --* 
        
                  If this workflow execution is a child of another execution then contains the workflow execution that started this execution.
        
                  - **workflowId** *(string) --* 
        
                    The user defined identifier associated with the workflow execution.
        
                  - **runId** *(string) --* 
        
                    A system-generated unique identifier for the workflow execution.
        
                - **tagList** *(list) --* 
        
                  The list of tags associated with the workflow execution. Tags can be used to identify and list workflow executions of interest through the visibility APIs. A workflow execution can have a maximum of 5 tags.
        
                  - *(string) --* 
              
                - **cancelRequested** *(boolean) --* 
        
                  Set to true if a cancellation is requested for this workflow execution.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListWorkflowTypes(Paginator):
    def paginate(self, domain: str, registrationStatus: str, name: str = None, reverseOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/swf-2012-01-25/ListWorkflowTypes>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              domain=\'string\',
              name=\'string\',
              registrationStatus=\'REGISTERED\'|\'DEPRECATED\',
              reverseOrder=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type domain: string
        :param domain: **[REQUIRED]** 
        
          The name of the domain in which the workflow types have been registered.
        
        :type name: string
        :param name: 
        
          If specified, lists the workflow type with this name.
        
        :type registrationStatus: string
        :param registrationStatus: **[REQUIRED]** 
        
          Specifies the registration status of the workflow types to list.
        
        :type reverseOrder: boolean
        :param reverseOrder: 
        
          When set to ``true`` , returns the results in reverse order. By default the results are returned in ascending alphabetical order of the ``name`` of the workflow types.
        
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
                \'typeInfos\': [
                    {
                        \'workflowType\': {
                            \'name\': \'string\',
                            \'version\': \'string\'
                        },
                        \'status\': \'REGISTERED\'|\'DEPRECATED\',
                        \'description\': \'string\',
                        \'creationDate\': datetime(2015, 1, 1),
                        \'deprecationDate\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains a paginated list of information structures about workflow types.
        
            - **typeInfos** *(list) --* 
        
              The list of workflow type information.
        
              - *(dict) --* 
        
                Contains information about a workflow type.
        
                - **workflowType** *(dict) --* 
        
                  The workflow type this information is about.
        
                  - **name** *(string) --* 
        
                    The name of the workflow type.
        
                    .. note::
        
                      The combination of workflow type name and version must be unique with in a domain.
        
                  - **version** *(string) --* 
        
                    The version of the workflow type.
        
                    .. note::
        
                      The combination of workflow type name and version must be unique with in a domain.
        
                - **status** *(string) --* 
        
                  The current status of the workflow type.
        
                - **description** *(string) --* 
        
                  The description of the type registered through  RegisterWorkflowType .
        
                - **creationDate** *(datetime) --* 
        
                  The date when this type was registered.
        
                - **deprecationDate** *(datetime) --* 
        
                  If the type is in deprecated state, then it is set to the date when the type was deprecated.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class PollForDecisionTask(Paginator):
    def paginate(self, domain: str, taskList: Dict, identity: str = None, reverseOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/swf-2012-01-25/PollForDecisionTask>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              domain=\'string\',
              taskList={
                  \'name\': \'string\'
              },
              identity=\'string\',
              reverseOrder=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type domain: string
        :param domain: **[REQUIRED]** 
        
          The name of the domain containing the task lists to poll.
        
        :type taskList: dict
        :param taskList: **[REQUIRED]** 
        
          Specifies the task list to poll for decision tasks.
        
          The specified string must not start or end with whitespace. It must not contain a ``:`` (colon), ``/`` (slash), ``|`` (vertical bar), or any control characters (``\u0000-\u001f`` | ``\u007f-\u009f`` ). Also, it must not contain the literal string ``arn`` .
        
          - **name** *(string) --* **[REQUIRED]** 
        
            The name of the task list.
        
        :type identity: string
        :param identity: 
        
          Identity of the decider making the request, which is recorded in the DecisionTaskStarted event in the workflow history. This enables diagnostic tracing when problems arise. The form of this identity is user defined.
        
        :type reverseOrder: boolean
        :param reverseOrder: 
        
          When set to ``true`` , returns the events in reverse order. By default the results are returned in ascending order of the ``eventTimestamp`` of the events.
        
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
                \'taskToken\': \'string\',
                \'startedEventId\': 123,
                \'workflowExecution\': {
                    \'workflowId\': \'string\',
                    \'runId\': \'string\'
                },
                \'workflowType\': {
                    \'name\': \'string\',
                    \'version\': \'string\'
                },
                \'events\': [
                    {
                        \'eventTimestamp\': datetime(2015, 1, 1),
                        \'eventType\': \'WorkflowExecutionStarted\'|\'WorkflowExecutionCancelRequested\'|\'WorkflowExecutionCompleted\'|\'CompleteWorkflowExecutionFailed\'|\'WorkflowExecutionFailed\'|\'FailWorkflowExecutionFailed\'|\'WorkflowExecutionTimedOut\'|\'WorkflowExecutionCanceled\'|\'CancelWorkflowExecutionFailed\'|\'WorkflowExecutionContinuedAsNew\'|\'ContinueAsNewWorkflowExecutionFailed\'|\'WorkflowExecutionTerminated\'|\'DecisionTaskScheduled\'|\'DecisionTaskStarted\'|\'DecisionTaskCompleted\'|\'DecisionTaskTimedOut\'|\'ActivityTaskScheduled\'|\'ScheduleActivityTaskFailed\'|\'ActivityTaskStarted\'|\'ActivityTaskCompleted\'|\'ActivityTaskFailed\'|\'ActivityTaskTimedOut\'|\'ActivityTaskCanceled\'|\'ActivityTaskCancelRequested\'|\'RequestCancelActivityTaskFailed\'|\'WorkflowExecutionSignaled\'|\'MarkerRecorded\'|\'RecordMarkerFailed\'|\'TimerStarted\'|\'StartTimerFailed\'|\'TimerFired\'|\'TimerCanceled\'|\'CancelTimerFailed\'|\'StartChildWorkflowExecutionInitiated\'|\'StartChildWorkflowExecutionFailed\'|\'ChildWorkflowExecutionStarted\'|\'ChildWorkflowExecutionCompleted\'|\'ChildWorkflowExecutionFailed\'|\'ChildWorkflowExecutionTimedOut\'|\'ChildWorkflowExecutionCanceled\'|\'ChildWorkflowExecutionTerminated\'|\'SignalExternalWorkflowExecutionInitiated\'|\'SignalExternalWorkflowExecutionFailed\'|\'ExternalWorkflowExecutionSignaled\'|\'RequestCancelExternalWorkflowExecutionInitiated\'|\'RequestCancelExternalWorkflowExecutionFailed\'|\'ExternalWorkflowExecutionCancelRequested\'|\'LambdaFunctionScheduled\'|\'LambdaFunctionStarted\'|\'LambdaFunctionCompleted\'|\'LambdaFunctionFailed\'|\'LambdaFunctionTimedOut\'|\'ScheduleLambdaFunctionFailed\'|\'StartLambdaFunctionFailed\',
                        \'eventId\': 123,
                        \'workflowExecutionStartedEventAttributes\': {
                            \'input\': \'string\',
                            \'executionStartToCloseTimeout\': \'string\',
                            \'taskStartToCloseTimeout\': \'string\',
                            \'childPolicy\': \'TERMINATE\'|\'REQUEST_CANCEL\'|\'ABANDON\',
                            \'taskList\': {
                                \'name\': \'string\'
                            },
                            \'taskPriority\': \'string\',
                            \'workflowType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'tagList\': [
                                \'string\',
                            ],
                            \'continuedExecutionRunId\': \'string\',
                            \'parentWorkflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'parentInitiatedEventId\': 123,
                            \'lambdaRole\': \'string\'
                        },
                        \'workflowExecutionCompletedEventAttributes\': {
                            \'result\': \'string\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'completeWorkflowExecutionFailedEventAttributes\': {
                            \'cause\': \'UNHANDLED_DECISION\'|\'OPERATION_NOT_PERMITTED\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'workflowExecutionFailedEventAttributes\': {
                            \'reason\': \'string\',
                            \'details\': \'string\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'failWorkflowExecutionFailedEventAttributes\': {
                            \'cause\': \'UNHANDLED_DECISION\'|\'OPERATION_NOT_PERMITTED\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'workflowExecutionTimedOutEventAttributes\': {
                            \'timeoutType\': \'START_TO_CLOSE\',
                            \'childPolicy\': \'TERMINATE\'|\'REQUEST_CANCEL\'|\'ABANDON\'
                        },
                        \'workflowExecutionCanceledEventAttributes\': {
                            \'details\': \'string\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'cancelWorkflowExecutionFailedEventAttributes\': {
                            \'cause\': \'UNHANDLED_DECISION\'|\'OPERATION_NOT_PERMITTED\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'workflowExecutionContinuedAsNewEventAttributes\': {
                            \'input\': \'string\',
                            \'decisionTaskCompletedEventId\': 123,
                            \'newExecutionRunId\': \'string\',
                            \'executionStartToCloseTimeout\': \'string\',
                            \'taskList\': {
                                \'name\': \'string\'
                            },
                            \'taskPriority\': \'string\',
                            \'taskStartToCloseTimeout\': \'string\',
                            \'childPolicy\': \'TERMINATE\'|\'REQUEST_CANCEL\'|\'ABANDON\',
                            \'tagList\': [
                                \'string\',
                            ],
                            \'workflowType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'lambdaRole\': \'string\'
                        },
                        \'continueAsNewWorkflowExecutionFailedEventAttributes\': {
                            \'cause\': \'UNHANDLED_DECISION\'|\'WORKFLOW_TYPE_DEPRECATED\'|\'WORKFLOW_TYPE_DOES_NOT_EXIST\'|\'DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED\'|\'DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED\'|\'DEFAULT_TASK_LIST_UNDEFINED\'|\'DEFAULT_CHILD_POLICY_UNDEFINED\'|\'CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED\'|\'OPERATION_NOT_PERMITTED\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'workflowExecutionTerminatedEventAttributes\': {
                            \'reason\': \'string\',
                            \'details\': \'string\',
                            \'childPolicy\': \'TERMINATE\'|\'REQUEST_CANCEL\'|\'ABANDON\',
                            \'cause\': \'CHILD_POLICY_APPLIED\'|\'EVENT_LIMIT_EXCEEDED\'|\'OPERATOR_INITIATED\'
                        },
                        \'workflowExecutionCancelRequestedEventAttributes\': {
                            \'externalWorkflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'externalInitiatedEventId\': 123,
                            \'cause\': \'CHILD_POLICY_APPLIED\'
                        },
                        \'decisionTaskScheduledEventAttributes\': {
                            \'taskList\': {
                                \'name\': \'string\'
                            },
                            \'taskPriority\': \'string\',
                            \'startToCloseTimeout\': \'string\'
                        },
                        \'decisionTaskStartedEventAttributes\': {
                            \'identity\': \'string\',
                            \'scheduledEventId\': 123
                        },
                        \'decisionTaskCompletedEventAttributes\': {
                            \'executionContext\': \'string\',
                            \'scheduledEventId\': 123,
                            \'startedEventId\': 123
                        },
                        \'decisionTaskTimedOutEventAttributes\': {
                            \'timeoutType\': \'START_TO_CLOSE\',
                            \'scheduledEventId\': 123,
                            \'startedEventId\': 123
                        },
                        \'activityTaskScheduledEventAttributes\': {
                            \'activityType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'activityId\': \'string\',
                            \'input\': \'string\',
                            \'control\': \'string\',
                            \'scheduleToStartTimeout\': \'string\',
                            \'scheduleToCloseTimeout\': \'string\',
                            \'startToCloseTimeout\': \'string\',
                            \'taskList\': {
                                \'name\': \'string\'
                            },
                            \'taskPriority\': \'string\',
                            \'decisionTaskCompletedEventId\': 123,
                            \'heartbeatTimeout\': \'string\'
                        },
                        \'activityTaskStartedEventAttributes\': {
                            \'identity\': \'string\',
                            \'scheduledEventId\': 123
                        },
                        \'activityTaskCompletedEventAttributes\': {
                            \'result\': \'string\',
                            \'scheduledEventId\': 123,
                            \'startedEventId\': 123
                        },
                        \'activityTaskFailedEventAttributes\': {
                            \'reason\': \'string\',
                            \'details\': \'string\',
                            \'scheduledEventId\': 123,
                            \'startedEventId\': 123
                        },
                        \'activityTaskTimedOutEventAttributes\': {
                            \'timeoutType\': \'START_TO_CLOSE\'|\'SCHEDULE_TO_START\'|\'SCHEDULE_TO_CLOSE\'|\'HEARTBEAT\',
                            \'scheduledEventId\': 123,
                            \'startedEventId\': 123,
                            \'details\': \'string\'
                        },
                        \'activityTaskCanceledEventAttributes\': {
                            \'details\': \'string\',
                            \'scheduledEventId\': 123,
                            \'startedEventId\': 123,
                            \'latestCancelRequestedEventId\': 123
                        },
                        \'activityTaskCancelRequestedEventAttributes\': {
                            \'decisionTaskCompletedEventId\': 123,
                            \'activityId\': \'string\'
                        },
                        \'workflowExecutionSignaledEventAttributes\': {
                            \'signalName\': \'string\',
                            \'input\': \'string\',
                            \'externalWorkflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'externalInitiatedEventId\': 123
                        },
                        \'markerRecordedEventAttributes\': {
                            \'markerName\': \'string\',
                            \'details\': \'string\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'recordMarkerFailedEventAttributes\': {
                            \'markerName\': \'string\',
                            \'cause\': \'OPERATION_NOT_PERMITTED\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'timerStartedEventAttributes\': {
                            \'timerId\': \'string\',
                            \'control\': \'string\',
                            \'startToFireTimeout\': \'string\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'timerFiredEventAttributes\': {
                            \'timerId\': \'string\',
                            \'startedEventId\': 123
                        },
                        \'timerCanceledEventAttributes\': {
                            \'timerId\': \'string\',
                            \'startedEventId\': 123,
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'startChildWorkflowExecutionInitiatedEventAttributes\': {
                            \'workflowId\': \'string\',
                            \'workflowType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'control\': \'string\',
                            \'input\': \'string\',
                            \'executionStartToCloseTimeout\': \'string\',
                            \'taskList\': {
                                \'name\': \'string\'
                            },
                            \'taskPriority\': \'string\',
                            \'decisionTaskCompletedEventId\': 123,
                            \'childPolicy\': \'TERMINATE\'|\'REQUEST_CANCEL\'|\'ABANDON\',
                            \'taskStartToCloseTimeout\': \'string\',
                            \'tagList\': [
                                \'string\',
                            ],
                            \'lambdaRole\': \'string\'
                        },
                        \'childWorkflowExecutionStartedEventAttributes\': {
                            \'workflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'workflowType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'initiatedEventId\': 123
                        },
                        \'childWorkflowExecutionCompletedEventAttributes\': {
                            \'workflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'workflowType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'result\': \'string\',
                            \'initiatedEventId\': 123,
                            \'startedEventId\': 123
                        },
                        \'childWorkflowExecutionFailedEventAttributes\': {
                            \'workflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'workflowType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'reason\': \'string\',
                            \'details\': \'string\',
                            \'initiatedEventId\': 123,
                            \'startedEventId\': 123
                        },
                        \'childWorkflowExecutionTimedOutEventAttributes\': {
                            \'workflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'workflowType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'timeoutType\': \'START_TO_CLOSE\',
                            \'initiatedEventId\': 123,
                            \'startedEventId\': 123
                        },
                        \'childWorkflowExecutionCanceledEventAttributes\': {
                            \'workflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'workflowType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'details\': \'string\',
                            \'initiatedEventId\': 123,
                            \'startedEventId\': 123
                        },
                        \'childWorkflowExecutionTerminatedEventAttributes\': {
                            \'workflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'workflowType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'initiatedEventId\': 123,
                            \'startedEventId\': 123
                        },
                        \'signalExternalWorkflowExecutionInitiatedEventAttributes\': {
                            \'workflowId\': \'string\',
                            \'runId\': \'string\',
                            \'signalName\': \'string\',
                            \'input\': \'string\',
                            \'decisionTaskCompletedEventId\': 123,
                            \'control\': \'string\'
                        },
                        \'externalWorkflowExecutionSignaledEventAttributes\': {
                            \'workflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'initiatedEventId\': 123
                        },
                        \'signalExternalWorkflowExecutionFailedEventAttributes\': {
                            \'workflowId\': \'string\',
                            \'runId\': \'string\',
                            \'cause\': \'UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION\'|\'SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED\'|\'OPERATION_NOT_PERMITTED\',
                            \'initiatedEventId\': 123,
                            \'decisionTaskCompletedEventId\': 123,
                            \'control\': \'string\'
                        },
                        \'externalWorkflowExecutionCancelRequestedEventAttributes\': {
                            \'workflowExecution\': {
                                \'workflowId\': \'string\',
                                \'runId\': \'string\'
                            },
                            \'initiatedEventId\': 123
                        },
                        \'requestCancelExternalWorkflowExecutionInitiatedEventAttributes\': {
                            \'workflowId\': \'string\',
                            \'runId\': \'string\',
                            \'decisionTaskCompletedEventId\': 123,
                            \'control\': \'string\'
                        },
                        \'requestCancelExternalWorkflowExecutionFailedEventAttributes\': {
                            \'workflowId\': \'string\',
                            \'runId\': \'string\',
                            \'cause\': \'UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION\'|\'REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED\'|\'OPERATION_NOT_PERMITTED\',
                            \'initiatedEventId\': 123,
                            \'decisionTaskCompletedEventId\': 123,
                            \'control\': \'string\'
                        },
                        \'scheduleActivityTaskFailedEventAttributes\': {
                            \'activityType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'activityId\': \'string\',
                            \'cause\': \'ACTIVITY_TYPE_DEPRECATED\'|\'ACTIVITY_TYPE_DOES_NOT_EXIST\'|\'ACTIVITY_ID_ALREADY_IN_USE\'|\'OPEN_ACTIVITIES_LIMIT_EXCEEDED\'|\'ACTIVITY_CREATION_RATE_EXCEEDED\'|\'DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED\'|\'DEFAULT_TASK_LIST_UNDEFINED\'|\'DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED\'|\'DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED\'|\'DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED\'|\'OPERATION_NOT_PERMITTED\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'requestCancelActivityTaskFailedEventAttributes\': {
                            \'activityId\': \'string\',
                            \'cause\': \'ACTIVITY_ID_UNKNOWN\'|\'OPERATION_NOT_PERMITTED\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'startTimerFailedEventAttributes\': {
                            \'timerId\': \'string\',
                            \'cause\': \'TIMER_ID_ALREADY_IN_USE\'|\'OPEN_TIMERS_LIMIT_EXCEEDED\'|\'TIMER_CREATION_RATE_EXCEEDED\'|\'OPERATION_NOT_PERMITTED\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'cancelTimerFailedEventAttributes\': {
                            \'timerId\': \'string\',
                            \'cause\': \'TIMER_ID_UNKNOWN\'|\'OPERATION_NOT_PERMITTED\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'startChildWorkflowExecutionFailedEventAttributes\': {
                            \'workflowType\': {
                                \'name\': \'string\',
                                \'version\': \'string\'
                            },
                            \'cause\': \'WORKFLOW_TYPE_DOES_NOT_EXIST\'|\'WORKFLOW_TYPE_DEPRECATED\'|\'OPEN_CHILDREN_LIMIT_EXCEEDED\'|\'OPEN_WORKFLOWS_LIMIT_EXCEEDED\'|\'CHILD_CREATION_RATE_EXCEEDED\'|\'WORKFLOW_ALREADY_RUNNING\'|\'DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED\'|\'DEFAULT_TASK_LIST_UNDEFINED\'|\'DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED\'|\'DEFAULT_CHILD_POLICY_UNDEFINED\'|\'OPERATION_NOT_PERMITTED\',
                            \'workflowId\': \'string\',
                            \'initiatedEventId\': 123,
                            \'decisionTaskCompletedEventId\': 123,
                            \'control\': \'string\'
                        },
                        \'lambdaFunctionScheduledEventAttributes\': {
                            \'id\': \'string\',
                            \'name\': \'string\',
                            \'control\': \'string\',
                            \'input\': \'string\',
                            \'startToCloseTimeout\': \'string\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'lambdaFunctionStartedEventAttributes\': {
                            \'scheduledEventId\': 123
                        },
                        \'lambdaFunctionCompletedEventAttributes\': {
                            \'scheduledEventId\': 123,
                            \'startedEventId\': 123,
                            \'result\': \'string\'
                        },
                        \'lambdaFunctionFailedEventAttributes\': {
                            \'scheduledEventId\': 123,
                            \'startedEventId\': 123,
                            \'reason\': \'string\',
                            \'details\': \'string\'
                        },
                        \'lambdaFunctionTimedOutEventAttributes\': {
                            \'scheduledEventId\': 123,
                            \'startedEventId\': 123,
                            \'timeoutType\': \'START_TO_CLOSE\'
                        },
                        \'scheduleLambdaFunctionFailedEventAttributes\': {
                            \'id\': \'string\',
                            \'name\': \'string\',
                            \'cause\': \'ID_ALREADY_IN_USE\'|\'OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED\'|\'LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED\'|\'LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION\',
                            \'decisionTaskCompletedEventId\': 123
                        },
                        \'startLambdaFunctionFailedEventAttributes\': {
                            \'scheduledEventId\': 123,
                            \'cause\': \'ASSUME_ROLE_FAILED\',
                            \'message\': \'string\'
                        }
                    },
                ],
                \'previousStartedEventId\': 123,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            A structure that represents a decision task. Decision tasks are sent to deciders in order for them to make decisions.
        
            - **taskToken** *(string) --* 
        
              The opaque string used as a handle on the task. This token is used by workers to communicate progress and response information back to the system about the task.
        
            - **startedEventId** *(integer) --* 
        
              The ID of the ``DecisionTaskStarted`` event recorded in the history.
        
            - **workflowExecution** *(dict) --* 
        
              The workflow execution for which this decision task was created.
        
              - **workflowId** *(string) --* 
        
                The user defined identifier associated with the workflow execution.
        
              - **runId** *(string) --* 
        
                A system-generated unique identifier for the workflow execution.
        
            - **workflowType** *(dict) --* 
        
              The type of the workflow execution for which this decision task was created.
        
              - **name** *(string) --* 
        
                The name of the workflow type.
        
                .. note::
        
                  The combination of workflow type name and version must be unique with in a domain.
        
              - **version** *(string) --* 
        
                The version of the workflow type.
        
                .. note::
        
                  The combination of workflow type name and version must be unique with in a domain.
        
            - **events** *(list) --* 
        
              A paginated list of history events of the workflow execution. The decider uses this during the processing of the decision task.
        
              - *(dict) --* 
        
                Event within a workflow execution. A history event can be one of these types:
        
                * ``ActivityTaskCancelRequested`` – A ``RequestCancelActivityTask`` decision was received by the system. 
                 
                * ``ActivityTaskCanceled`` – The activity task was successfully canceled. 
                 
                * ``ActivityTaskCompleted`` – An activity worker successfully completed an activity task by calling  RespondActivityTaskCompleted . 
                 
                * ``ActivityTaskFailed`` – An activity worker failed an activity task by calling  RespondActivityTaskFailed . 
                 
                * ``ActivityTaskScheduled`` – An activity task was scheduled for execution. 
                 
                * ``ActivityTaskStarted`` – The scheduled activity task was dispatched to a worker. 
                 
                * ``ActivityTaskTimedOut`` – The activity task timed out. 
                 
                * ``CancelTimerFailed`` – Failed to process CancelTimer decision. This happens when the decision isn\'t configured properly, for example no timer exists with the specified timer Id. 
                 
                * ``CancelWorkflowExecutionFailed`` – A request to cancel a workflow execution failed. 
                 
                * ``ChildWorkflowExecutionCanceled`` – A child workflow execution, started by this workflow execution, was canceled and closed. 
                 
                * ``ChildWorkflowExecutionCompleted`` – A child workflow execution, started by this workflow execution, completed successfully and was closed. 
                 
                * ``ChildWorkflowExecutionFailed`` – A child workflow execution, started by this workflow execution, failed to complete successfully and was closed. 
                 
                * ``ChildWorkflowExecutionStarted`` – A child workflow execution was successfully started. 
                 
                * ``ChildWorkflowExecutionTerminated`` – A child workflow execution, started by this workflow execution, was terminated. 
                 
                * ``ChildWorkflowExecutionTimedOut`` – A child workflow execution, started by this workflow execution, timed out and was closed. 
                 
                * ``CompleteWorkflowExecutionFailed`` – The workflow execution failed to complete. 
                 
                * ``ContinueAsNewWorkflowExecutionFailed`` – The workflow execution failed to complete after being continued as a new workflow execution. 
                 
                * ``DecisionTaskCompleted`` – The decider successfully completed a decision task by calling  RespondDecisionTaskCompleted . 
                 
                * ``DecisionTaskScheduled`` – A decision task was scheduled for the workflow execution. 
                 
                * ``DecisionTaskStarted`` – The decision task was dispatched to a decider. 
                 
                * ``DecisionTaskTimedOut`` – The decision task timed out. 
                 
                * ``ExternalWorkflowExecutionCancelRequested`` – Request to cancel an external workflow execution was successfully delivered to the target execution. 
                 
                * ``ExternalWorkflowExecutionSignaled`` – A signal, requested by this workflow execution, was successfully delivered to the target external workflow execution. 
                 
                * ``FailWorkflowExecutionFailed`` – A request to mark a workflow execution as failed, itself failed. 
                 
                * ``MarkerRecorded`` – A marker was recorded in the workflow history as the result of a ``RecordMarker`` decision. 
                 
                * ``RecordMarkerFailed`` – A ``RecordMarker`` decision was returned as failed. 
                 
                * ``RequestCancelActivityTaskFailed`` – Failed to process RequestCancelActivityTask decision. This happens when the decision isn\'t configured properly. 
                 
                * ``RequestCancelExternalWorkflowExecutionFailed`` – Request to cancel an external workflow execution failed. 
                 
                * ``RequestCancelExternalWorkflowExecutionInitiated`` – A request was made to request the cancellation of an external workflow execution. 
                 
                * ``ScheduleActivityTaskFailed`` – Failed to process ScheduleActivityTask decision. This happens when the decision isn\'t configured properly, for example the activity type specified isn\'t registered. 
                 
                * ``SignalExternalWorkflowExecutionFailed`` – The request to signal an external workflow execution failed. 
                 
                * ``SignalExternalWorkflowExecutionInitiated`` – A request to signal an external workflow was made. 
                 
                * ``StartActivityTaskFailed`` – A scheduled activity task failed to start. 
                 
                * ``StartChildWorkflowExecutionFailed`` – Failed to process StartChildWorkflowExecution decision. This happens when the decision isn\'t configured properly, for example the workflow type specified isn\'t registered. 
                 
                * ``StartChildWorkflowExecutionInitiated`` – A request was made to start a child workflow execution. 
                 
                * ``StartTimerFailed`` – Failed to process StartTimer decision. This happens when the decision isn\'t configured properly, for example a timer already exists with the specified timer Id. 
                 
                * ``TimerCanceled`` – A timer, previously started for this workflow execution, was successfully canceled. 
                 
                * ``TimerFired`` – A timer, previously started for this workflow execution, fired. 
                 
                * ``TimerStarted`` – A timer was started for the workflow execution due to a ``StartTimer`` decision. 
                 
                * ``WorkflowExecutionCancelRequested`` – A request to cancel this workflow execution was made. 
                 
                * ``WorkflowExecutionCanceled`` – The workflow execution was successfully canceled and closed. 
                 
                * ``WorkflowExecutionCompleted`` – The workflow execution was closed due to successful completion. 
                 
                * ``WorkflowExecutionContinuedAsNew`` – The workflow execution was closed and a new execution of the same type was created with the same workflowId. 
                 
                * ``WorkflowExecutionFailed`` – The workflow execution closed due to a failure. 
                 
                * ``WorkflowExecutionSignaled`` – An external signal was received for the workflow execution. 
                 
                * ``WorkflowExecutionStarted`` – The workflow execution was started. 
                 
                * ``WorkflowExecutionTerminated`` – The workflow execution was terminated. 
                 
                * ``WorkflowExecutionTimedOut`` – The workflow execution was closed because a time out was exceeded. 
                 
                - **eventTimestamp** *(datetime) --* 
        
                  The date and time when the event occurred.
        
                - **eventType** *(string) --* 
        
                  The type of the history event.
        
                - **eventId** *(integer) --* 
        
                  The system generated ID of the event. This ID uniquely identifies the event with in the workflow execution history.
        
                - **workflowExecutionStartedEventAttributes** *(dict) --* 
        
                  If the event is of type ``WorkflowExecutionStarted`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **input** *(string) --* 
        
                    The input provided to the workflow execution.
        
                  - **executionStartToCloseTimeout** *(string) --* 
        
                    The maximum duration for this workflow execution.
        
                    The duration is specified in seconds, an integer greater than or equal to ``0`` . You can use ``NONE`` to specify unlimited duration.
        
                  - **taskStartToCloseTimeout** *(string) --* 
        
                    The maximum duration of decision tasks for this workflow type.
        
                    The duration is specified in seconds, an integer greater than or equal to ``0`` . You can use ``NONE`` to specify unlimited duration.
        
                  - **childPolicy** *(string) --* 
        
                    The policy to use for the child workflow executions if this workflow execution is terminated, by calling the  TerminateWorkflowExecution action explicitly or due to an expired timeout.
        
                    The supported child policies are:
        
                    * ``TERMINATE`` – The child executions are terminated. 
                     
                    * ``REQUEST_CANCEL`` – A request to cancel is attempted for each child execution by recording a ``WorkflowExecutionCancelRequested`` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event. 
                     
                    * ``ABANDON`` – No action is taken. The child executions continue to run. 
                     
                  - **taskList** *(dict) --* 
        
                    The name of the task list for scheduling the decision tasks for this workflow execution.
        
                    - **name** *(string) --* 
        
                      The name of the task list.
        
                  - **taskPriority** *(string) --* 
        
                    The priority of the decision tasks in the workflow execution.
        
                  - **workflowType** *(dict) --* 
        
                    The workflow type of this execution.
        
                    - **name** *(string) --* 
        
                      The name of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                    - **version** *(string) --* 
        
                      The version of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                  - **tagList** *(list) --* 
        
                    The list of tags associated with this workflow execution. An execution can have up to 5 tags.
        
                    - *(string) --* 
                
                  - **continuedExecutionRunId** *(string) --* 
        
                    If this workflow execution was started due to a ``ContinueAsNewWorkflowExecution`` decision, then it contains the ``runId`` of the previous workflow execution that was closed and continued as this execution.
        
                  - **parentWorkflowExecution** *(dict) --* 
        
                    The source workflow execution that started this workflow execution. The member isn\'t set if the workflow execution was not started by a workflow.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **parentInitiatedEventId** *(integer) --* 
        
                    The ID of the ``StartChildWorkflowExecutionInitiated`` event corresponding to the ``StartChildWorkflowExecution``   Decision to start this workflow execution. The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **lambdaRole** *(string) --* 
        
                    The IAM role attached to the workflow execution.
        
                - **workflowExecutionCompletedEventAttributes** *(dict) --* 
        
                  If the event is of type ``WorkflowExecutionCompleted`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **result** *(string) --* 
        
                    The result produced by the workflow execution upon successful completion.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``CompleteWorkflowExecution`` decision to complete this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **completeWorkflowExecutionFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``CompleteWorkflowExecutionFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``CompleteWorkflowExecution`` decision to complete this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **workflowExecutionFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``WorkflowExecutionFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **reason** *(string) --* 
        
                    The descriptive reason provided for the failure.
        
                  - **details** *(string) --* 
        
                    The details of the failure.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``FailWorkflowExecution`` decision to fail this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **failWorkflowExecutionFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``FailWorkflowExecutionFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``FailWorkflowExecution`` decision to fail this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **workflowExecutionTimedOutEventAttributes** *(dict) --* 
        
                  If the event is of type ``WorkflowExecutionTimedOut`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **timeoutType** *(string) --* 
        
                    The type of timeout that caused this event.
        
                  - **childPolicy** *(string) --* 
        
                    The policy used for the child workflow executions of this workflow execution.
        
                    The supported child policies are:
        
                    * ``TERMINATE`` – The child executions are terminated. 
                     
                    * ``REQUEST_CANCEL`` – A request to cancel is attempted for each child execution by recording a ``WorkflowExecutionCancelRequested`` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event. 
                     
                    * ``ABANDON`` – No action is taken. The child executions continue to run. 
                     
                - **workflowExecutionCanceledEventAttributes** *(dict) --* 
        
                  If the event is of type ``WorkflowExecutionCanceled`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **details** *(string) --* 
        
                    The details of the cancellation.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``CancelWorkflowExecution`` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **cancelWorkflowExecutionFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``CancelWorkflowExecutionFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``CancelWorkflowExecution`` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **workflowExecutionContinuedAsNewEventAttributes** *(dict) --* 
        
                  If the event is of type ``WorkflowExecutionContinuedAsNew`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **input** *(string) --* 
        
                    The input provided to the new workflow execution.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``ContinueAsNewWorkflowExecution`` decision that started this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **newExecutionRunId** *(string) --* 
        
                    The ``runId`` of the new workflow execution.
        
                  - **executionStartToCloseTimeout** *(string) --* 
        
                    The total duration allowed for the new workflow execution.
        
                    The duration is specified in seconds, an integer greater than or equal to ``0`` . You can use ``NONE`` to specify unlimited duration.
        
                  - **taskList** *(dict) --* 
        
                    The task list to use for the decisions of the new (continued) workflow execution.
        
                    - **name** *(string) --* 
        
                      The name of the task list.
        
                  - **taskPriority** *(string) --* 
        
                    The priority of the task to use for the decisions of the new (continued) workflow execution.
        
                  - **taskStartToCloseTimeout** *(string) --* 
        
                    The maximum duration of decision tasks for the new workflow execution.
        
                    The duration is specified in seconds, an integer greater than or equal to ``0`` . You can use ``NONE`` to specify unlimited duration.
        
                  - **childPolicy** *(string) --* 
        
                    The policy to use for the child workflow executions of the new execution if it is terminated by calling the  TerminateWorkflowExecution action explicitly or due to an expired timeout.
        
                    The supported child policies are:
        
                    * ``TERMINATE`` – The child executions are terminated. 
                     
                    * ``REQUEST_CANCEL`` – A request to cancel is attempted for each child execution by recording a ``WorkflowExecutionCancelRequested`` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event. 
                     
                    * ``ABANDON`` – No action is taken. The child executions continue to run. 
                     
                  - **tagList** *(list) --* 
        
                    The list of tags associated with the new workflow execution.
        
                    - *(string) --* 
                
                  - **workflowType** *(dict) --* 
        
                    The workflow type of this execution.
        
                    - **name** *(string) --* 
        
                      The name of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                    - **version** *(string) --* 
        
                      The version of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                  - **lambdaRole** *(string) --* 
        
                    The IAM role to attach to the new (continued) workflow execution.
        
                - **continueAsNewWorkflowExecutionFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ContinueAsNewWorkflowExecutionFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``ContinueAsNewWorkflowExecution`` decision that started this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **workflowExecutionTerminatedEventAttributes** *(dict) --* 
        
                  If the event is of type ``WorkflowExecutionTerminated`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **reason** *(string) --* 
        
                    The reason provided for the termination.
        
                  - **details** *(string) --* 
        
                    The details provided for the termination.
        
                  - **childPolicy** *(string) --* 
        
                    The policy used for the child workflow executions of this workflow execution.
        
                    The supported child policies are:
        
                    * ``TERMINATE`` – The child executions are terminated. 
                     
                    * ``REQUEST_CANCEL`` – A request to cancel is attempted for each child execution by recording a ``WorkflowExecutionCancelRequested`` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event. 
                     
                    * ``ABANDON`` – No action is taken. The child executions continue to run. 
                     
                  - **cause** *(string) --* 
        
                    If set, indicates that the workflow execution was automatically terminated, and specifies the cause. This happens if the parent workflow execution times out or is terminated and the child policy is set to terminate child executions.
        
                - **workflowExecutionCancelRequestedEventAttributes** *(dict) --* 
        
                  If the event is of type ``WorkflowExecutionCancelRequested`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **externalWorkflowExecution** *(dict) --* 
        
                    The external workflow execution for which the cancellation was requested.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **externalInitiatedEventId** *(integer) --* 
        
                    The ID of the ``RequestCancelExternalWorkflowExecutionInitiated`` event corresponding to the ``RequestCancelExternalWorkflowExecution`` decision to cancel this workflow execution.The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **cause** *(string) --* 
        
                    If set, indicates that the request to cancel the workflow execution was automatically generated, and specifies the cause. This happens if the parent workflow execution times out or is terminated, and the child policy is set to cancel child executions.
        
                - **decisionTaskScheduledEventAttributes** *(dict) --* 
        
                  If the event is of type ``DecisionTaskScheduled`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **taskList** *(dict) --* 
        
                    The name of the task list in which the decision task was scheduled.
        
                    - **name** *(string) --* 
        
                      The name of the task list.
        
                  - **taskPriority** *(string) --* 
        
                    A task priority that, if set, specifies the priority for this decision task. Valid values are integers that range from Java\'s ``Integer.MIN_VALUE`` (-2147483648) to ``Integer.MAX_VALUE`` (2147483647). Higher numbers indicate higher priority.
        
                    For more information about setting task priority, see `Setting Task Priority <http://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **startToCloseTimeout** *(string) --* 
        
                    The maximum duration for this decision task. The task is considered timed out if it doesn\'t completed within this duration.
        
                    The duration is specified in seconds, an integer greater than or equal to ``0`` . You can use ``NONE`` to specify unlimited duration.
        
                - **decisionTaskStartedEventAttributes** *(dict) --* 
        
                  If the event is of type ``DecisionTaskStarted`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **identity** *(string) --* 
        
                    Identity of the decider making the request. This enables diagnostic tracing when problems arise. The form of this identity is user defined.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskScheduled`` event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **decisionTaskCompletedEventAttributes** *(dict) --* 
        
                  If the event is of type ``DecisionTaskCompleted`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **executionContext** *(string) --* 
        
                    User defined context for the workflow execution.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskScheduled`` event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskStarted`` event recorded when this decision task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **decisionTaskTimedOutEventAttributes** *(dict) --* 
        
                  If the event is of type ``DecisionTaskTimedOut`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **timeoutType** *(string) --* 
        
                    The type of timeout that expired before the decision task could be completed.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskScheduled`` event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskStarted`` event recorded when this decision task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **activityTaskScheduledEventAttributes** *(dict) --* 
        
                  If the event is of type ``ActivityTaskScheduled`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **activityType** *(dict) --* 
        
                    The type of the activity task.
        
                    - **name** *(string) --* 
        
                      The name of this activity.
        
                      .. note::
        
                        The combination of activity type name and version must be unique within a domain.
        
                    - **version** *(string) --* 
        
                      The version of this activity.
        
                      .. note::
        
                        The combination of activity type name and version must be unique with in a domain.
        
                  - **activityId** *(string) --* 
        
                    The unique ID of the activity task.
        
                  - **input** *(string) --* 
        
                    The input provided to the activity task.
        
                  - **control** *(string) --* 
        
                    Data attached to the event that can be used by the decider in subsequent workflow tasks. This data isn\'t sent to the activity.
        
                  - **scheduleToStartTimeout** *(string) --* 
        
                    The maximum amount of time the activity task can wait to be assigned to a worker.
        
                  - **scheduleToCloseTimeout** *(string) --* 
        
                    The maximum amount of time for this activity task.
        
                  - **startToCloseTimeout** *(string) --* 
        
                    The maximum amount of time a worker may take to process the activity task.
        
                  - **taskList** *(dict) --* 
        
                    The task list in which the activity task has been scheduled.
        
                    - **name** *(string) --* 
        
                      The name of the task list.
        
                  - **taskPriority** *(string) --* 
        
                    The priority to assign to the scheduled activity task. If set, this overrides any default priority value that was assigned when the activity type was registered.
        
                    Valid values are integers that range from Java\'s ``Integer.MIN_VALUE`` (-2147483648) to ``Integer.MAX_VALUE`` (2147483647). Higher numbers indicate higher priority.
        
                    For more information about setting task priority, see `Setting Task Priority <http://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision that resulted in the scheduling of this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **heartbeatTimeout** *(string) --* 
        
                    The maximum time before which the worker processing this task must report progress by calling  RecordActivityTaskHeartbeat . If the timeout is exceeded, the activity task is automatically timed out. If the worker subsequently attempts to record a heartbeat or return a result, it is ignored.
        
                - **activityTaskStartedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ActivityTaskStarted`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **identity** *(string) --* 
        
                    Identity of the worker that was assigned this task. This aids diagnostics when problems arise. The form of this identity is user defined.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskScheduled`` event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **activityTaskCompletedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ActivityTaskCompleted`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **result** *(string) --* 
        
                    The results of the activity task.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskScheduled`` event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskStarted`` event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **activityTaskFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ActivityTaskFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **reason** *(string) --* 
        
                    The reason provided for the failure.
        
                  - **details** *(string) --* 
        
                    The details of the failure.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskScheduled`` event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskStarted`` event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **activityTaskTimedOutEventAttributes** *(dict) --* 
        
                  If the event is of type ``ActivityTaskTimedOut`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **timeoutType** *(string) --* 
        
                    The type of the timeout that caused this event.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskScheduled`` event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskStarted`` event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **details** *(string) --* 
        
                    Contains the content of the ``details`` parameter for the last call made by the activity to ``RecordActivityTaskHeartbeat`` .
        
                - **activityTaskCanceledEventAttributes** *(dict) --* 
        
                  If the event is of type ``ActivityTaskCanceled`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **details** *(string) --* 
        
                    Details of the cancellation.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskScheduled`` event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskStarted`` event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **latestCancelRequestedEventId** *(integer) --* 
        
                    If set, contains the ID of the last ``ActivityTaskCancelRequested`` event recorded for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **activityTaskCancelRequestedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ActivityTaskcancelRequested`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``RequestCancelActivityTask`` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **activityId** *(string) --* 
        
                    The unique ID of the task.
        
                - **workflowExecutionSignaledEventAttributes** *(dict) --* 
        
                  If the event is of type ``WorkflowExecutionSignaled`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **signalName** *(string) --* 
        
                    The name of the signal received. The decider can use the signal name and inputs to determine how to the process the signal.
        
                  - **input** *(string) --* 
        
                    The inputs provided with the signal. The decider can use the signal name and inputs to determine how to process the signal.
        
                  - **externalWorkflowExecution** *(dict) --* 
        
                    The workflow execution that sent the signal. This is set only of the signal was sent by another workflow execution.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **externalInitiatedEventId** *(integer) --* 
        
                    The ID of the ``SignalExternalWorkflowExecutionInitiated`` event corresponding to the ``SignalExternalWorkflow`` decision to signal this workflow execution.The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event. This field is set only if the signal was initiated by another workflow execution.
        
                - **markerRecordedEventAttributes** *(dict) --* 
        
                  If the event is of type ``MarkerRecorded`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **markerName** *(string) --* 
        
                    The name of the marker.
        
                  - **details** *(string) --* 
        
                    The details of the marker.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``RecordMarker`` decision that requested this marker. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **recordMarkerFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``DecisionTaskFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **markerName** *(string) --* 
        
                    The marker\'s name.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``RecordMarkerFailed`` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **timerStartedEventAttributes** *(dict) --* 
        
                  If the event is of type ``TimerStarted`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **timerId** *(string) --* 
        
                    The unique ID of the timer that was started.
        
                  - **control** *(string) --* 
        
                    Data attached to the event that can be used by the decider in subsequent workflow tasks.
        
                  - **startToFireTimeout** *(string) --* 
        
                    The duration of time after which the timer fires.
        
                    The duration is specified in seconds, an integer greater than or equal to ``0`` .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``StartTimer`` decision for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **timerFiredEventAttributes** *(dict) --* 
        
                  If the event is of type ``TimerFired`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **timerId** *(string) --* 
        
                    The unique ID of the timer that fired.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``TimerStarted`` event that was recorded when this timer was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **timerCanceledEventAttributes** *(dict) --* 
        
                  If the event is of type ``TimerCanceled`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **timerId** *(string) --* 
        
                    The unique ID of the timer that was canceled.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``TimerStarted`` event that was recorded when this timer was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``CancelTimer`` decision to cancel this timer. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **startChildWorkflowExecutionInitiatedEventAttributes** *(dict) --* 
        
                  If the event is of type ``StartChildWorkflowExecutionInitiated`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowId** *(string) --* 
        
                    The ``workflowId`` of the child workflow execution.
        
                  - **workflowType** *(dict) --* 
        
                    The type of the child workflow execution.
        
                    - **name** *(string) --* 
        
                      The name of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                    - **version** *(string) --* 
        
                      The version of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                  - **control** *(string) --* 
        
                    Data attached to the event that can be used by the decider in subsequent decision tasks. This data isn\'t sent to the activity.
        
                  - **input** *(string) --* 
        
                    The inputs provided to the child workflow execution.
        
                  - **executionStartToCloseTimeout** *(string) --* 
        
                    The maximum duration for the child workflow execution. If the workflow execution isn\'t closed within this duration, it is timed out and force-terminated.
        
                    The duration is specified in seconds, an integer greater than or equal to ``0`` . You can use ``NONE`` to specify unlimited duration.
        
                  - **taskList** *(dict) --* 
        
                    The name of the task list used for the decision tasks of the child workflow execution.
        
                    - **name** *(string) --* 
        
                      The name of the task list.
        
                  - **taskPriority** *(string) --* 
        
                    The priority assigned for the decision tasks for this workflow execution. Valid values are integers that range from Java\'s ``Integer.MIN_VALUE`` (-2147483648) to ``Integer.MAX_VALUE`` (2147483647). Higher numbers indicate higher priority.
        
                    For more information about setting task priority, see `Setting Task Priority <http://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``StartChildWorkflowExecution``   Decision to request this child workflow execution. This information can be useful for diagnosing problems by tracing back the cause of events.
        
                  - **childPolicy** *(string) --* 
        
                    The policy to use for the child workflow executions if this execution gets terminated by explicitly calling the  TerminateWorkflowExecution action or due to an expired timeout.
        
                    The supported child policies are:
        
                    * ``TERMINATE`` – The child executions are terminated. 
                     
                    * ``REQUEST_CANCEL`` – A request to cancel is attempted for each child execution by recording a ``WorkflowExecutionCancelRequested`` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event. 
                     
                    * ``ABANDON`` – No action is taken. The child executions continue to run. 
                     
                  - **taskStartToCloseTimeout** *(string) --* 
        
                    The maximum duration allowed for the decision tasks for this workflow execution.
        
                    The duration is specified in seconds, an integer greater than or equal to ``0`` . You can use ``NONE`` to specify unlimited duration.
        
                  - **tagList** *(list) --* 
        
                    The list of tags to associated with the child workflow execution.
        
                    - *(string) --* 
                
                  - **lambdaRole** *(string) --* 
        
                    The IAM role to attach to the child workflow execution.
        
                - **childWorkflowExecutionStartedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ChildWorkflowExecutionStarted`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowExecution** *(dict) --* 
        
                    The child workflow execution that was started.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **workflowType** *(dict) --* 
        
                    The type of the child workflow execution.
        
                    - **name** *(string) --* 
        
                      The name of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                    - **version** *(string) --* 
        
                      The version of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                  - **initiatedEventId** *(integer) --* 
        
                    The ID of the ``StartChildWorkflowExecutionInitiated`` event corresponding to the ``StartChildWorkflowExecution``   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **childWorkflowExecutionCompletedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ChildWorkflowExecutionCompleted`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowExecution** *(dict) --* 
        
                    The child workflow execution that was completed.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **workflowType** *(dict) --* 
        
                    The type of the child workflow execution.
        
                    - **name** *(string) --* 
        
                      The name of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                    - **version** *(string) --* 
        
                      The version of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                  - **result** *(string) --* 
        
                    The result of the child workflow execution.
        
                  - **initiatedEventId** *(integer) --* 
        
                    The ID of the ``StartChildWorkflowExecutionInitiated`` event corresponding to the ``StartChildWorkflowExecution``   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``ChildWorkflowExecutionStarted`` event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **childWorkflowExecutionFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ChildWorkflowExecutionFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowExecution** *(dict) --* 
        
                    The child workflow execution that failed.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **workflowType** *(dict) --* 
        
                    The type of the child workflow execution.
        
                    - **name** *(string) --* 
        
                      The name of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                    - **version** *(string) --* 
        
                      The version of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                  - **reason** *(string) --* 
        
                    The reason for the failure (if provided).
        
                  - **details** *(string) --* 
        
                    The details of the failure (if provided).
        
                  - **initiatedEventId** *(integer) --* 
        
                    The ID of the ``StartChildWorkflowExecutionInitiated`` event corresponding to the ``StartChildWorkflowExecution``   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``ChildWorkflowExecutionStarted`` event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **childWorkflowExecutionTimedOutEventAttributes** *(dict) --* 
        
                  If the event is of type ``ChildWorkflowExecutionTimedOut`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowExecution** *(dict) --* 
        
                    The child workflow execution that timed out.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **workflowType** *(dict) --* 
        
                    The type of the child workflow execution.
        
                    - **name** *(string) --* 
        
                      The name of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                    - **version** *(string) --* 
        
                      The version of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                  - **timeoutType** *(string) --* 
        
                    The type of the timeout that caused the child workflow execution to time out.
        
                  - **initiatedEventId** *(integer) --* 
        
                    The ID of the ``StartChildWorkflowExecutionInitiated`` event corresponding to the ``StartChildWorkflowExecution``   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``ChildWorkflowExecutionStarted`` event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **childWorkflowExecutionCanceledEventAttributes** *(dict) --* 
        
                  If the event is of type ``ChildWorkflowExecutionCanceled`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowExecution** *(dict) --* 
        
                    The child workflow execution that was canceled.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **workflowType** *(dict) --* 
        
                    The type of the child workflow execution.
        
                    - **name** *(string) --* 
        
                      The name of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                    - **version** *(string) --* 
        
                      The version of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                  - **details** *(string) --* 
        
                    Details of the cancellation (if provided).
        
                  - **initiatedEventId** *(integer) --* 
        
                    The ID of the ``StartChildWorkflowExecutionInitiated`` event corresponding to the ``StartChildWorkflowExecution``   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``ChildWorkflowExecutionStarted`` event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **childWorkflowExecutionTerminatedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ChildWorkflowExecutionTerminated`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowExecution** *(dict) --* 
        
                    The child workflow execution that was terminated.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **workflowType** *(dict) --* 
        
                    The type of the child workflow execution.
        
                    - **name** *(string) --* 
        
                      The name of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                    - **version** *(string) --* 
        
                      The version of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                  - **initiatedEventId** *(integer) --* 
        
                    The ID of the ``StartChildWorkflowExecutionInitiated`` event corresponding to the ``StartChildWorkflowExecution``   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``ChildWorkflowExecutionStarted`` event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **signalExternalWorkflowExecutionInitiatedEventAttributes** *(dict) --* 
        
                  If the event is of type ``SignalExternalWorkflowExecutionInitiated`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowId** *(string) --* 
        
                    The ``workflowId`` of the external workflow execution.
        
                  - **runId** *(string) --* 
        
                    The ``runId`` of the external workflow execution to send the signal to.
        
                  - **signalName** *(string) --* 
        
                    The name of the signal.
        
                  - **input** *(string) --* 
        
                    The input provided to the signal.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``SignalExternalWorkflowExecution`` decision for this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **control** *(string) --* 
        
                    Data attached to the event that can be used by the decider in subsequent decision tasks.
        
                - **externalWorkflowExecutionSignaledEventAttributes** *(dict) --* 
        
                  If the event is of type ``ExternalWorkflowExecutionSignaled`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowExecution** *(dict) --* 
        
                    The external workflow execution that the signal was delivered to.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **initiatedEventId** *(integer) --* 
        
                    The ID of the ``SignalExternalWorkflowExecutionInitiated`` event corresponding to the ``SignalExternalWorkflowExecution`` decision to request this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **signalExternalWorkflowExecutionFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``SignalExternalWorkflowExecutionFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowId** *(string) --* 
        
                    The ``workflowId`` of the external workflow execution that the signal was being delivered to.
        
                  - **runId** *(string) --* 
        
                    The ``runId`` of the external workflow execution that the signal was being delivered to.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **initiatedEventId** *(integer) --* 
        
                    The ID of the ``SignalExternalWorkflowExecutionInitiated`` event corresponding to the ``SignalExternalWorkflowExecution`` decision to request this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``SignalExternalWorkflowExecution`` decision for this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **control** *(string) --* 
        
                    The data attached to the event that the decider can use in subsequent workflow tasks. This data isn\'t sent to the workflow execution.
        
                - **externalWorkflowExecutionCancelRequestedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ExternalWorkflowExecutionCancelRequested`` then this member is set and provides detailed information about the event. It isn\'t set for other event types. 
        
                  - **workflowExecution** *(dict) --* 
        
                    The external workflow execution to which the cancellation request was delivered.
        
                    - **workflowId** *(string) --* 
        
                      The user defined identifier associated with the workflow execution.
        
                    - **runId** *(string) --* 
        
                      A system-generated unique identifier for the workflow execution.
        
                  - **initiatedEventId** *(integer) --* 
        
                    The ID of the ``RequestCancelExternalWorkflowExecutionInitiated`` event corresponding to the ``RequestCancelExternalWorkflowExecution`` decision to cancel this external workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **requestCancelExternalWorkflowExecutionInitiatedEventAttributes** *(dict) --* 
        
                  If the event is of type ``RequestCancelExternalWorkflowExecutionInitiated`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowId** *(string) --* 
        
                    The ``workflowId`` of the external workflow execution to be canceled.
        
                  - **runId** *(string) --* 
        
                    The ``runId`` of the external workflow execution to be canceled.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``RequestCancelExternalWorkflowExecution`` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **control** *(string) --* 
        
                    Data attached to the event that can be used by the decider in subsequent workflow tasks.
        
                - **requestCancelExternalWorkflowExecutionFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``RequestCancelExternalWorkflowExecutionFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowId** *(string) --* 
        
                    The ``workflowId`` of the external workflow to which the cancel request was to be delivered.
        
                  - **runId** *(string) --* 
        
                    The ``runId`` of the external workflow execution.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **initiatedEventId** *(integer) --* 
        
                    The ID of the ``RequestCancelExternalWorkflowExecutionInitiated`` event corresponding to the ``RequestCancelExternalWorkflowExecution`` decision to cancel this external workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``RequestCancelExternalWorkflowExecution`` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                  - **control** *(string) --* 
        
                    The data attached to the event that the decider can use in subsequent workflow tasks. This data isn\'t sent to the workflow execution.
        
                - **scheduleActivityTaskFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``ScheduleActivityTaskFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **activityType** *(dict) --* 
        
                    The activity type provided in the ``ScheduleActivityTask`` decision that failed.
        
                    - **name** *(string) --* 
        
                      The name of this activity.
        
                      .. note::
        
                        The combination of activity type name and version must be unique within a domain.
        
                    - **version** *(string) --* 
        
                      The version of this activity.
        
                      .. note::
        
                        The combination of activity type name and version must be unique with in a domain.
        
                  - **activityId** *(string) --* 
        
                    The activityId provided in the ``ScheduleActivityTask`` decision that failed.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision that resulted in the scheduling of this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **requestCancelActivityTaskFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``RequestCancelActivityTaskFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **activityId** *(string) --* 
        
                    The activityId provided in the ``RequestCancelActivityTask`` decision that failed.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``RequestCancelActivityTask`` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **startTimerFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``StartTimerFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **timerId** *(string) --* 
        
                    The timerId provided in the ``StartTimer`` decision that failed.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``StartTimer`` decision for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **cancelTimerFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``CancelTimerFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **timerId** *(string) --* 
        
                    The timerId provided in the ``CancelTimer`` decision that failed.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``CancelTimer`` decision to cancel this timer. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
        
                - **startChildWorkflowExecutionFailedEventAttributes** *(dict) --* 
        
                  If the event is of type ``StartChildWorkflowExecutionFailed`` then this member is set and provides detailed information about the event. It isn\'t set for other event types.
        
                  - **workflowType** *(dict) --* 
        
                    The workflow type provided in the ``StartChildWorkflowExecution``   Decision that failed.
        
                    - **name** *(string) --* 
        
                      The name of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                    - **version** *(string) --* 
        
                      The version of the workflow type.
        
                      .. note::
        
                        The combination of workflow type name and version must be unique with in a domain.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
        
                    .. note::
        
                      When ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision fails because it lacks sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **workflowId** *(string) --* 
        
                    The ``workflowId`` of the child workflow execution.
        
                  - **initiatedEventId** *(integer) --* 
        
                    When the ``cause`` is ``WORKFLOW_ALREADY_RUNNING`` , ``initiatedEventId`` is the ID of the ``StartChildWorkflowExecutionInitiated`` event that corresponds to the ``StartChildWorkflowExecution``   Decision to start the workflow execution. You can use this information to diagnose problems by tracing back the chain of events leading up to this event.
        
                    When the ``cause`` isn\'t ``WORKFLOW_ALREADY_RUNNING`` , ``initiatedEventId`` is set to ``0`` because the ``StartChildWorkflowExecutionInitiated`` event doesn\'t exist.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``DecisionTaskCompleted`` event corresponding to the decision task that resulted in the ``StartChildWorkflowExecution``   Decision to request this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events.
        
                  - **control** *(string) --* 
        
                    The data attached to the event that the decider can use in subsequent workflow tasks. This data isn\'t sent to the child workflow execution.
        
                - **lambdaFunctionScheduledEventAttributes** *(dict) --* 
        
                  Provides the details of the ``LambdaFunctionScheduled`` event. It isn\'t set for other event types.
        
                  - **id** *(string) --* 
        
                    The unique ID of the Lambda task.
        
                  - **name** *(string) --* 
        
                    The name of the Lambda function.
        
                  - **control** *(string) --* 
        
                    Data attached to the event that the decider can use in subsequent workflow tasks. This data isn\'t sent to the Lambda task.
        
                  - **input** *(string) --* 
        
                    The input provided to the Lambda task.
        
                  - **startToCloseTimeout** *(string) --* 
        
                    The maximum amount of time a worker can take to process the Lambda task.
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``LambdaFunctionCompleted`` event corresponding to the decision that resulted in scheduling this activity task. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                - **lambdaFunctionStartedEventAttributes** *(dict) --* 
        
                  Provides the details of the ``LambdaFunctionStarted`` event. It isn\'t set for other event types.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``LambdaFunctionScheduled`` event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                - **lambdaFunctionCompletedEventAttributes** *(dict) --* 
        
                  Provides the details of the ``LambdaFunctionCompleted`` event. It isn\'t set for other event types.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``LambdaFunctionScheduled`` event that was recorded when this Lambda task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``LambdaFunctionStarted`` event recorded when this activity task started. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                  - **result** *(string) --* 
        
                    The results of the Lambda task.
        
                - **lambdaFunctionFailedEventAttributes** *(dict) --* 
        
                  Provides the details of the ``LambdaFunctionFailed`` event. It isn\'t set for other event types.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``LambdaFunctionScheduled`` event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``LambdaFunctionStarted`` event recorded when this activity task started. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                  - **reason** *(string) --* 
        
                    The reason provided for the failure.
        
                  - **details** *(string) --* 
        
                    The details of the failure.
        
                - **lambdaFunctionTimedOutEventAttributes** *(dict) --* 
        
                  Provides the details of the ``LambdaFunctionTimedOut`` event. It isn\'t set for other event types.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``LambdaFunctionScheduled`` event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                  - **startedEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskStarted`` event that was recorded when this activity task started. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                  - **timeoutType** *(string) --* 
        
                    The type of the timeout that caused this event.
        
                - **scheduleLambdaFunctionFailedEventAttributes** *(dict) --* 
        
                  Provides the details of the ``ScheduleLambdaFunctionFailed`` event. It isn\'t set for other event types.
        
                  - **id** *(string) --* 
        
                    The ID provided in the ``ScheduleLambdaFunction`` decision that failed. 
        
                  - **name** *(string) --* 
        
                    The name of the Lambda function.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see `Using IAM to Manage Access to Amazon SWF Workflows <http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **decisionTaskCompletedEventId** *(integer) --* 
        
                    The ID of the ``LambdaFunctionCompleted`` event corresponding to the decision that resulted in scheduling this Lambda task. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                - **startLambdaFunctionFailedEventAttributes** *(dict) --* 
        
                  Provides the details of the ``StartLambdaFunctionFailed`` event. It isn\'t set for other event types.
        
                  - **scheduledEventId** *(integer) --* 
        
                    The ID of the ``ActivityTaskScheduled`` event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                  - **cause** *(string) --* 
        
                    The cause of the failure. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
        
                    .. note::
        
                      If ``cause`` is set to ``OPERATION_NOT_PERMITTED`` , the decision failed because the IAM role attached to the execution lacked sufficient permissions. For details and example IAM policies, see `Lambda Tasks <http://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html>`__ in the *Amazon SWF Developer Guide* .
        
                  - **message** *(string) --* 
        
                    A description that can help diagnose the cause of the fault.
        
            - **previousStartedEventId** *(integer) --* 
        
              The ID of the DecisionTaskStarted event of the previous decision task of this workflow execution that was processed by the decider. This can be used to determine the events in the history new since the last decision task received by the decider.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
