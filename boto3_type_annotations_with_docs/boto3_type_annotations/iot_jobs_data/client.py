from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None) -> NoReturn:
        """
        
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

    def describe_job_execution(self, jobId: str, thingName: str, includeJobDocument: bool = None, executionNumber: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-jobs-data-2017-09-29/DescribeJobExecution>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_job_execution(
              jobId=\'string\',
              thingName=\'string\',
              includeJobDocument=True|False,
              executionNumber=123
          )
        :type jobId: string
        :param jobId: **[REQUIRED]** 
        
          The unique identifier assigned to this job when it was created.
        
        :type thingName: string
        :param thingName: **[REQUIRED]** 
        
          The thing name associated with the device the job execution is running on.
        
        :type includeJobDocument: boolean
        :param includeJobDocument: 
        
          Optional. When set to true, the response contains the job document. The default is false.
        
        :type executionNumber: integer
        :param executionNumber: 
        
          Optional. A number that identifies a particular job execution on a particular device. If not specified, the latest job execution is returned.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'execution\': {
                    \'jobId\': \'string\',
                    \'thingName\': \'string\',
                    \'status\': \'QUEUED\'|\'IN_PROGRESS\'|\'SUCCEEDED\'|\'FAILED\'|\'TIMED_OUT\'|\'REJECTED\'|\'REMOVED\'|\'CANCELED\',
                    \'statusDetails\': {
                        \'string\': \'string\'
                    },
                    \'queuedAt\': 123,
                    \'startedAt\': 123,
                    \'lastUpdatedAt\': 123,
                    \'approximateSecondsBeforeTimedOut\': 123,
                    \'versionNumber\': 123,
                    \'executionNumber\': 123,
                    \'jobDocument\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **execution** *(dict) --* 
        
              Contains data about a job execution.
        
              - **jobId** *(string) --* 
        
                The unique identifier you assigned to this job when it was created.
        
              - **thingName** *(string) --* 
        
                The name of the thing that is executing the job.
        
              - **status** *(string) --* 
        
                The status of the job execution. Can be one of: \"QUEUED\", \"IN_PROGRESS\", \"FAILED\", \"SUCCESS\", \"CANCELED\", \"REJECTED\", or \"REMOVED\".
        
              - **statusDetails** *(dict) --* 
        
                A collection of name/value pairs that describe the status of the job execution.
        
                - *(string) --* 
                  
                  - *(string) --* 
            
              - **queuedAt** *(integer) --* 
        
                The time, in milliseconds since the epoch, when the job execution was enqueued.
        
              - **startedAt** *(integer) --* 
        
                The time, in milliseconds since the epoch, when the job execution was started.
        
              - **lastUpdatedAt** *(integer) --* 
        
                The time, in milliseconds since the epoch, when the job execution was last updated. 
        
              - **approximateSecondsBeforeTimedOut** *(integer) --* 
        
                The estimated number of seconds that remain before the job execution status will be changed to ``TIMED_OUT`` .
        
              - **versionNumber** *(integer) --* 
        
                The version of the job execution. Job execution versions are incremented each time they are updated by a device.
        
              - **executionNumber** *(integer) --* 
        
                A number that identifies a particular job execution on a particular device. It can be used later in commands that return or update job execution information.
        
              - **jobDocument** *(string) --* 
        
                The content of the job document.
        
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        """
        
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

    def get_paginator(self, operation_name: str = None) -> Paginator:
        """
        
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

    def get_pending_job_executions(self, thingName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-jobs-data-2017-09-29/GetPendingJobExecutions>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_pending_job_executions(
              thingName=\'string\'
          )
        :type thingName: string
        :param thingName: **[REQUIRED]** 
        
          The name of the thing that is executing the job.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'inProgressJobs\': [
                    {
                        \'jobId\': \'string\',
                        \'queuedAt\': 123,
                        \'startedAt\': 123,
                        \'lastUpdatedAt\': 123,
                        \'versionNumber\': 123,
                        \'executionNumber\': 123
                    },
                ],
                \'queuedJobs\': [
                    {
                        \'jobId\': \'string\',
                        \'queuedAt\': 123,
                        \'startedAt\': 123,
                        \'lastUpdatedAt\': 123,
                        \'versionNumber\': 123,
                        \'executionNumber\': 123
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **inProgressJobs** *(list) --* 
        
              A list of JobExecutionSummary objects with status IN_PROGRESS.
        
              - *(dict) --* 
        
                Contains a subset of information about a job execution.
        
                - **jobId** *(string) --* 
        
                  The unique identifier you assigned to this job when it was created.
        
                - **queuedAt** *(integer) --* 
        
                  The time, in milliseconds since the epoch, when the job execution was enqueued.
        
                - **startedAt** *(integer) --* 
        
                  The time, in milliseconds since the epoch, when the job execution started.
        
                - **lastUpdatedAt** *(integer) --* 
        
                  The time, in milliseconds since the epoch, when the job execution was last updated.
        
                - **versionNumber** *(integer) --* 
        
                  The version of the job execution. Job execution versions are incremented each time AWS IoT Jobs receives an update from a device.
        
                - **executionNumber** *(integer) --* 
        
                  A number that identifies a particular job execution on a particular device.
        
            - **queuedJobs** *(list) --* 
        
              A list of JobExecutionSummary objects with status QUEUED.
        
              - *(dict) --* 
        
                Contains a subset of information about a job execution.
        
                - **jobId** *(string) --* 
        
                  The unique identifier you assigned to this job when it was created.
        
                - **queuedAt** *(integer) --* 
        
                  The time, in milliseconds since the epoch, when the job execution was enqueued.
        
                - **startedAt** *(integer) --* 
        
                  The time, in milliseconds since the epoch, when the job execution started.
        
                - **lastUpdatedAt** *(integer) --* 
        
                  The time, in milliseconds since the epoch, when the job execution was last updated.
        
                - **versionNumber** *(integer) --* 
        
                  The version of the job execution. Job execution versions are incremented each time AWS IoT Jobs receives an update from a device.
        
                - **executionNumber** *(integer) --* 
        
                  A number that identifies a particular job execution on a particular device.
        
        """
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def start_next_pending_job_execution(self, thingName: str, statusDetails: Dict = None, stepTimeoutInMinutes: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-jobs-data-2017-09-29/StartNextPendingJobExecution>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_next_pending_job_execution(
              thingName=\'string\',
              statusDetails={
                  \'string\': \'string\'
              },
              stepTimeoutInMinutes=123
          )
        :type thingName: string
        :param thingName: **[REQUIRED]** 
        
          The name of the thing associated with the device.
        
        :type statusDetails: dict
        :param statusDetails: 
        
          A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type stepTimeoutInMinutes: integer
        :param stepTimeoutInMinutes: 
        
          Specifies the amount of time this device has to finish execution of this job. If the job execution status is not set to a terminal state before this timer expires, or before the timer is reset (by calling ``UpdateJobExecution`` , setting the status to ``IN_PROGRESS`` and specifying a new timeout value in field ``stepTimeoutInMinutes`` ) the job execution status will be automatically set to ``TIMED_OUT`` . Note that setting this timeout has no effect on that job execution timeout which may have been specified when the job was created (``CreateJob`` using field ``timeoutConfig`` ).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'execution\': {
                    \'jobId\': \'string\',
                    \'thingName\': \'string\',
                    \'status\': \'QUEUED\'|\'IN_PROGRESS\'|\'SUCCEEDED\'|\'FAILED\'|\'TIMED_OUT\'|\'REJECTED\'|\'REMOVED\'|\'CANCELED\',
                    \'statusDetails\': {
                        \'string\': \'string\'
                    },
                    \'queuedAt\': 123,
                    \'startedAt\': 123,
                    \'lastUpdatedAt\': 123,
                    \'approximateSecondsBeforeTimedOut\': 123,
                    \'versionNumber\': 123,
                    \'executionNumber\': 123,
                    \'jobDocument\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **execution** *(dict) --* 
        
              A JobExecution object.
        
              - **jobId** *(string) --* 
        
                The unique identifier you assigned to this job when it was created.
        
              - **thingName** *(string) --* 
        
                The name of the thing that is executing the job.
        
              - **status** *(string) --* 
        
                The status of the job execution. Can be one of: \"QUEUED\", \"IN_PROGRESS\", \"FAILED\", \"SUCCESS\", \"CANCELED\", \"REJECTED\", or \"REMOVED\".
        
              - **statusDetails** *(dict) --* 
        
                A collection of name/value pairs that describe the status of the job execution.
        
                - *(string) --* 
                  
                  - *(string) --* 
            
              - **queuedAt** *(integer) --* 
        
                The time, in milliseconds since the epoch, when the job execution was enqueued.
        
              - **startedAt** *(integer) --* 
        
                The time, in milliseconds since the epoch, when the job execution was started.
        
              - **lastUpdatedAt** *(integer) --* 
        
                The time, in milliseconds since the epoch, when the job execution was last updated. 
        
              - **approximateSecondsBeforeTimedOut** *(integer) --* 
        
                The estimated number of seconds that remain before the job execution status will be changed to ``TIMED_OUT`` .
        
              - **versionNumber** *(integer) --* 
        
                The version of the job execution. Job execution versions are incremented each time they are updated by a device.
        
              - **executionNumber** *(integer) --* 
        
                A number that identifies a particular job execution on a particular device. It can be used later in commands that return or update job execution information.
        
              - **jobDocument** *(string) --* 
        
                The content of the job document.
        
        """
        pass

    def update_job_execution(self, jobId: str, thingName: str, status: str, statusDetails: Dict = None, stepTimeoutInMinutes: int = None, expectedVersion: int = None, includeJobExecutionState: bool = None, includeJobDocument: bool = None, executionNumber: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-jobs-data-2017-09-29/UpdateJobExecution>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_job_execution(
              jobId=\'string\',
              thingName=\'string\',
              status=\'QUEUED\'|\'IN_PROGRESS\'|\'SUCCEEDED\'|\'FAILED\'|\'TIMED_OUT\'|\'REJECTED\'|\'REMOVED\'|\'CANCELED\',
              statusDetails={
                  \'string\': \'string\'
              },
              stepTimeoutInMinutes=123,
              expectedVersion=123,
              includeJobExecutionState=True|False,
              includeJobDocument=True|False,
              executionNumber=123
          )
        :type jobId: string
        :param jobId: **[REQUIRED]** 
        
          The unique identifier assigned to this job when it was created.
        
        :type thingName: string
        :param thingName: **[REQUIRED]** 
        
          The name of the thing associated with the device.
        
        :type status: string
        :param status: **[REQUIRED]** 
        
          The new status for the job execution (IN_PROGRESS, FAILED, SUCCESS, or REJECTED). This must be specified on every update.
        
        :type statusDetails: dict
        :param statusDetails: 
        
          Optional. A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type stepTimeoutInMinutes: integer
        :param stepTimeoutInMinutes: 
        
          Specifies the amount of time this device has to finish execution of this job. If the job execution status is not set to a terminal state before this timer expires, or before the timer is reset (by again calling ``UpdateJobExecution`` , setting the status to ``IN_PROGRESS`` and specifying a new timeout value in this field) the job execution status will be automatically set to ``TIMED_OUT`` . Note that setting or resetting this timeout has no effect on that job execution timeout which may have been specified when the job was created (``CreateJob`` using field ``timeoutConfig`` ).
        
        :type expectedVersion: integer
        :param expectedVersion: 
        
          Optional. The expected current version of the job execution. Each time you update the job execution, its version is incremented. If the version of the job execution stored in Jobs does not match, the update is rejected with a VersionMismatch error, and an ErrorResponse that contains the current job execution status data is returned. (This makes it unnecessary to perform a separate DescribeJobExecution request in order to obtain the job execution status data.)
        
        :type includeJobExecutionState: boolean
        :param includeJobExecutionState: 
        
          Optional. When included and set to true, the response contains the JobExecutionState data. The default is false.
        
        :type includeJobDocument: boolean
        :param includeJobDocument: 
        
          Optional. When set to true, the response contains the job document. The default is false.
        
        :type executionNumber: integer
        :param executionNumber: 
        
          Optional. A number that identifies a particular job execution on a particular device.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'executionState\': {
                    \'status\': \'QUEUED\'|\'IN_PROGRESS\'|\'SUCCEEDED\'|\'FAILED\'|\'TIMED_OUT\'|\'REJECTED\'|\'REMOVED\'|\'CANCELED\',
                    \'statusDetails\': {
                        \'string\': \'string\'
                    },
                    \'versionNumber\': 123
                },
                \'jobDocument\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **executionState** *(dict) --* 
        
              A JobExecutionState object.
        
              - **status** *(string) --* 
        
                The status of the job execution. Can be one of: \"QUEUED\", \"IN_PROGRESS\", \"FAILED\", \"SUCCESS\", \"CANCELED\", \"REJECTED\", or \"REMOVED\".
        
              - **statusDetails** *(dict) --* 
        
                A collection of name/value pairs that describe the status of the job execution.
        
                - *(string) --* 
                  
                  - *(string) --* 
            
              - **versionNumber** *(integer) --* 
        
                The version of the job execution. Job execution versions are incremented each time they are updated by a device.
        
            - **jobDocument** *(string) --* 
        
              The contents of the Job Documents.
        
        """
        pass
