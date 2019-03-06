from datetime import datetime
from typing import Dict
from botocore.paginate import Paginator


class ListAlgorithms(Paginator):
    def paginate(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, NameContains: str = None, SortBy: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SageMaker.Client.list_algorithms`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListAlgorithms>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              NameContains='string',
              SortBy='Name'|'CreationTime',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'AlgorithmSummaryList': [
                    {
                        'AlgorithmName': 'string',
                        'AlgorithmArn': 'string',
                        'AlgorithmDescription': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'AlgorithmStatus': 'Pending'|'InProgress'|'Completed'|'Failed'|'Deleting'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AlgorithmSummaryList** *(list) --* 
              >An array of ``AlgorithmSummary`` objects, each of which lists an algorithm.
              - *(dict) --* 
                Provides summary information about an algorithm.
                - **AlgorithmName** *(string) --* 
                  The name of the algorithm that is described by the summary.
                - **AlgorithmArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the algorithm.
                - **AlgorithmDescription** *(string) --* 
                  A brief description of the algorithm.
                - **CreationTime** *(datetime) --* 
                  A timestamp that shows when the algorithm was created.
                - **AlgorithmStatus** *(string) --* 
                  The overall status of the algorithm.
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:
          A filter that returns only algorithms created after the specified time (timestamp).
        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:
          A filter that returns only algorithms created before the specified time (timestamp).
        :type NameContains: string
        :param NameContains:
          A string in the algorithm name. This filter returns only algorithms whose name contains the specified string.
        :type SortBy: string
        :param SortBy:
          The parameter by which to sort the results. The default is ``CreationTime`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for the results. The default is ``Ascending`` .
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
        """
        pass


class ListCodeRepositories(Paginator):
    def paginate(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, SortBy: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SageMaker.Client.list_code_repositories`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListCodeRepositories>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              NameContains='string',
              SortBy='Name'|'CreationTime'|'LastModifiedTime',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'CodeRepositorySummaryList': [
                    {
                        'CodeRepositoryName': 'string',
                        'CodeRepositoryArn': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'GitConfig': {
                            'RepositoryUrl': 'string',
                            'Branch': 'string',
                            'SecretArn': 'string'
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CodeRepositorySummaryList** *(list) --* 
              Gets a list of summaries of the Git repositories. Each summary specifies the following values for the repository: 
              * Name 
              * Amazon Resource Name (ARN) 
              * Creation time 
              * Last modified time 
              * Configuration information, including the URL location of the repository and the ARN of the AWS Secrets Manager secret that contains the credentials used to access the repository. 
              - *(dict) --* 
                Specifies summary information about a Git repository.
                - **CodeRepositoryName** *(string) --* 
                  The name of the Git repository.
                - **CodeRepositoryArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the Git repository.
                - **CreationTime** *(datetime) --* 
                  The date and time that the Git repository was created.
                - **LastModifiedTime** *(datetime) --* 
                  The date and time that the Git repository was last modified.
                - **GitConfig** *(dict) --* 
                  Configuration details for the Git repository, including the URL where it is located and the ARN of the AWS Secrets Manager secret that contains the credentials used to access the repository.
                  - **RepositoryUrl** *(string) --* 
                    The URL where the Git repository is located.
                  - **Branch** *(string) --* 
                    The default branch for the Git repository.
                  - **SecretArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the credentials used to access the git repository. The secret must have a staging label of ``AWSCURRENT`` and must be in the following format:
                     ``{"username": *UserName* , "password": *Password* }``  
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:
          A filter that returns only Git repositories that were created after the specified time.
        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:
          A filter that returns only Git repositories that were created before the specified time.
        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:
          A filter that returns only Git repositories that were last modified after the specified time.
        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:
          A filter that returns only Git repositories that were last modified before the specified time.
        :type NameContains: string
        :param NameContains:
          A string in the Git repositories name. This filter returns only repositories whose name contains the specified string.
        :type SortBy: string
        :param SortBy:
          The field to sort results by. The default is ``Name`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for results. The default is ``Ascending`` .
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
        """
        pass


class ListCompilationJobs(Paginator):
    def paginate(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SageMaker.Client.list_compilation_jobs`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListCompilationJobs>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              NameContains='string',
              StatusEquals='INPROGRESS'|'COMPLETED'|'FAILED'|'STARTING'|'STOPPING'|'STOPPED',
              SortBy='Name'|'CreationTime'|'Status',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'CompilationJobSummaries': [
                    {
                        'CompilationJobName': 'string',
                        'CompilationJobArn': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'CompilationStartTime': datetime(2015, 1, 1),
                        'CompilationEndTime': datetime(2015, 1, 1),
                        'CompilationTargetDevice': 'ml_m4'|'ml_m5'|'ml_c4'|'ml_c5'|'ml_p2'|'ml_p3'|'jetson_tx1'|'jetson_tx2'|'rasp3b'|'deeplens',
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'CompilationJobStatus': 'INPROGRESS'|'COMPLETED'|'FAILED'|'STARTING'|'STOPPING'|'STOPPED'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CompilationJobSummaries** *(list) --* 
              An array of  CompilationJobSummary objects, each describing a model compilation job. 
              - *(dict) --* 
                A summary of a model compilation job.
                - **CompilationJobName** *(string) --* 
                  The name of the model compilation job that you want a summary for.
                - **CompilationJobArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the model compilation job.
                - **CreationTime** *(datetime) --* 
                  The time when the model compilation job was created.
                - **CompilationStartTime** *(datetime) --* 
                  The time when the model compilation job started.
                - **CompilationEndTime** *(datetime) --* 
                  The time when the model compilation job completed.
                - **CompilationTargetDevice** *(string) --* 
                  The type of device that the model will run on after compilation has completed.
                - **LastModifiedTime** *(datetime) --* 
                  The time when the model compilation job was last modified.
                - **CompilationJobStatus** *(string) --* 
                  The status of the model compilation job.
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:
          A filter that returns the model compilation jobs that were created after a specified time.
        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:
          A filter that returns the model compilation jobs that were created before a specified time.
        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:
          A filter that returns the model compilation jobs that were modified after a specified time.
        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:
          A filter that returns the model compilation jobs that were modified before a specified time.
        :type NameContains: string
        :param NameContains:
          A filter that returns the model compilation jobs whose name contains a specified string.
        :type StatusEquals: string
        :param StatusEquals:
          A filter that retrieves model compilation jobs with a specific  DescribeCompilationJobResponse$CompilationJobStatus status.
        :type SortBy: string
        :param SortBy:
          The field by which to sort results. The default is ``CreationTime`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for results. The default is ``Ascending`` .
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
        """
        pass


class ListEndpointConfigs(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SageMaker.Client.list_endpoint_configs`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListEndpointConfigs>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              SortBy='Name'|'CreationTime',
              SortOrder='Ascending'|'Descending',
              NameContains='string',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1),
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'EndpointConfigs': [
                    {
                        'EndpointConfigName': 'string',
                        'EndpointConfigArn': 'string',
                        'CreationTime': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **EndpointConfigs** *(list) --* 
              An array of endpoint configurations.
              - *(dict) --* 
                Provides summary information for an endpoint configuration.
                - **EndpointConfigName** *(string) --* 
                  The name of the endpoint configuration.
                - **EndpointConfigArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the endpoint configuration.
                - **CreationTime** *(datetime) --* 
                  A timestamp that shows when the endpoint configuration was created.
        :type SortBy: string
        :param SortBy:
          The field to sort results by. The default is ``CreationTime`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for results. The default is ``Ascending`` .
        :type NameContains: string
        :param NameContains:
          A string in the endpoint configuration name. This filter returns only endpoint configurations whose name contains the specified string.
        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:
          A filter that returns only endpoint configurations created before the specified time (timestamp).
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:
          A filter that returns only endpoint configurations created after the specified time (timestamp).
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
        """
        pass


class ListEndpoints(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, StatusEquals: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SageMaker.Client.list_endpoints`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListEndpoints>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              SortBy='Name'|'CreationTime'|'Status',
              SortOrder='Ascending'|'Descending',
              NameContains='string',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              StatusEquals='OutOfService'|'Creating'|'Updating'|'SystemUpdating'|'RollingBack'|'InService'|'Deleting'|'Failed',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Endpoints': [
                    {
                        'EndpointName': 'string',
                        'EndpointArn': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'EndpointStatus': 'OutOfService'|'Creating'|'Updating'|'SystemUpdating'|'RollingBack'|'InService'|'Deleting'|'Failed'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Endpoints** *(list) --* 
              An array or endpoint objects. 
              - *(dict) --* 
                Provides summary information for an endpoint.
                - **EndpointName** *(string) --* 
                  The name of the endpoint.
                - **EndpointArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the endpoint.
                - **CreationTime** *(datetime) --* 
                  A timestamp that shows when the endpoint was created.
                - **LastModifiedTime** *(datetime) --* 
                  A timestamp that shows when the endpoint was last modified.
                - **EndpointStatus** *(string) --* 
                  The status of the endpoint.
                  * ``OutOfService`` : Endpoint is not available to take incoming requests. 
                  * ``Creating`` :  CreateEndpoint is executing. 
                  * ``Updating`` :  UpdateEndpoint or  UpdateEndpointWeightsAndCapacities is executing. 
                  * ``SystemUpdating`` : Endpoint is undergoing maintenance and cannot be updated or deleted or re-scaled until it has completed. This mainenance operation does not change any customer-specified values such as VPC config, KMS encryption, model, instance type, or instance count. 
                  * ``RollingBack`` : Endpoint fails to scale up or down or change its variant weight and is in the process of rolling back to its previous configuration. Once the rollback completes, endpoint returns to an ``InService`` status. This transitional status only applies to an endpoint that has autoscaling enabled and is undergoing variant weight or capacity changes as part of an  UpdateEndpointWeightsAndCapacities call or when the  UpdateEndpointWeightsAndCapacities operation is called explicitly. 
                  * ``InService`` : Endpoint is available to process incoming requests. 
                  * ``Deleting`` :  DeleteEndpoint is executing. 
                  * ``Failed`` : Endpoint could not be created, updated, or re-scaled. Use  DescribeEndpointOutput$FailureReason for information about the failure.  DeleteEndpoint is the only operation that can be performed on a failed endpoint. 
                  To get a list of endpoints with a specified status, use the  ListEndpointsInput$StatusEquals filter.
        :type SortBy: string
        :param SortBy:
          Sorts the list of results. The default is ``CreationTime`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for results. The default is ``Ascending`` .
        :type NameContains: string
        :param NameContains:
          A string in endpoint names. This filter returns only endpoints whose name contains the specified string.
        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:
          A filter that returns only endpoints that were created before the specified time (timestamp).
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:
          A filter that returns only endpoints that were created after the specified time (timestamp).
        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:
          A filter that returns only endpoints that were modified before the specified timestamp.
        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:
          A filter that returns only endpoints that were modified after the specified timestamp.
        :type StatusEquals: string
        :param StatusEquals:
          A filter that returns only endpoints with the specified status.
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
        """
        pass


class ListHyperParameterTuningJobs(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, StatusEquals: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SageMaker.Client.list_hyper_parameter_tuning_jobs`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListHyperParameterTuningJobs>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              SortBy='Name'|'Status'|'CreationTime',
              SortOrder='Ascending'|'Descending',
              NameContains='string',
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              StatusEquals='Completed'|'InProgress'|'Failed'|'Stopped'|'Stopping',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'HyperParameterTuningJobSummaries': [
                    {
                        'HyperParameterTuningJobName': 'string',
                        'HyperParameterTuningJobArn': 'string',
                        'HyperParameterTuningJobStatus': 'Completed'|'InProgress'|'Failed'|'Stopped'|'Stopping',
                        'Strategy': 'Bayesian',
                        'CreationTime': datetime(2015, 1, 1),
                        'HyperParameterTuningEndTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'TrainingJobStatusCounters': {
                            'Completed': 123,
                            'InProgress': 123,
                            'RetryableError': 123,
                            'NonRetryableError': 123,
                            'Stopped': 123
                        },
                        'ObjectiveStatusCounters': {
                            'Succeeded': 123,
                            'Pending': 123,
                            'Failed': 123
                        },
                        'ResourceLimits': {
                            'MaxNumberOfTrainingJobs': 123,
                            'MaxParallelTrainingJobs': 123
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **HyperParameterTuningJobSummaries** *(list) --* 
              A list of  HyperParameterTuningJobSummary objects that describe the tuning jobs that the ``ListHyperParameterTuningJobs`` request returned.
              - *(dict) --* 
                Provides summary information about a hyperparameter tuning job.
                - **HyperParameterTuningJobName** *(string) --* 
                  The name of the tuning job.
                - **HyperParameterTuningJobArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the tuning job.
                - **HyperParameterTuningJobStatus** *(string) --* 
                  The status of the tuning job.
                - **Strategy** *(string) --* 
                  Specifies the search strategy hyperparameter tuning uses to choose which hyperparameters to use for each iteration. Currently, the only valid value is Bayesian.
                - **CreationTime** *(datetime) --* 
                  The date and time that the tuning job was created.
                - **HyperParameterTuningEndTime** *(datetime) --* 
                  The date and time that the tuning job ended.
                - **LastModifiedTime** *(datetime) --* 
                  The date and time that the tuning job was modified.
                - **TrainingJobStatusCounters** *(dict) --* 
                  The  TrainingJobStatusCounters object that specifies the numbers of training jobs, categorized by status, that this tuning job launched.
                  - **Completed** *(integer) --* 
                    The number of completed training jobs launched by the hyperparameter tuning job.
                  - **InProgress** *(integer) --* 
                    The number of in-progress training jobs launched by a hyperparameter tuning job.
                  - **RetryableError** *(integer) --* 
                    The number of training jobs that failed, but can be retried. A failed training job can be retried only if it failed because an internal service error occurred.
                  - **NonRetryableError** *(integer) --* 
                    The number of training jobs that failed and can't be retried. A failed training job can't be retried if it failed because a client error occurred.
                  - **Stopped** *(integer) --* 
                    The number of training jobs launched by a hyperparameter tuning job that were manually stopped.
                - **ObjectiveStatusCounters** *(dict) --* 
                  The  ObjectiveStatusCounters object that specifies the numbers of training jobs, categorized by objective metric status, that this tuning job launched.
                  - **Succeeded** *(integer) --* 
                    The number of training jobs whose final objective metric was evaluated by the hyperparameter tuning job and used in the hyperparameter tuning process.
                  - **Pending** *(integer) --* 
                    The number of training jobs that are in progress and pending evaluation of their final objective metric.
                  - **Failed** *(integer) --* 
                    The number of training jobs whose final objective metric was not evaluated and used in the hyperparameter tuning process. This typically occurs when the training job failed or did not emit an objective metric.
                - **ResourceLimits** *(dict) --* 
                  The  ResourceLimits object that specifies the maximum number of training jobs and parallel training jobs allowed for this tuning job.
                  - **MaxNumberOfTrainingJobs** *(integer) --* 
                    The maximum number of training jobs that a hyperparameter tuning job can launch.
                  - **MaxParallelTrainingJobs** *(integer) --* 
                    The maximum number of concurrent training jobs that a hyperparameter tuning job can launch.
        :type SortBy: string
        :param SortBy:
          The field to sort results by. The default is ``Name`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for results. The default is ``Ascending`` .
        :type NameContains: string
        :param NameContains:
          A string in the tuning job name. This filter returns only tuning jobs whose name contains the specified string.
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:
          A filter that returns only tuning jobs that were created after the specified time.
        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:
          A filter that returns only tuning jobs that were created before the specified time.
        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:
          A filter that returns only tuning jobs that were modified after the specified time.
        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:
          A filter that returns only tuning jobs that were modified before the specified time.
        :type StatusEquals: string
        :param StatusEquals:
          A filter that returns only tuning jobs with the specified status.
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
        """
        pass


class ListLabelingJobs(Paginator):
    def paginate(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, SortBy: str = None, SortOrder: str = None, StatusEquals: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SageMaker.Client.list_labeling_jobs`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListLabelingJobs>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              NameContains='string',
              SortBy='Name'|'CreationTime'|'Status',
              SortOrder='Ascending'|'Descending',
              StatusEquals='InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'LabelingJobSummaryList': [
                    {
                        'LabelingJobName': 'string',
                        'LabelingJobArn': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'LabelingJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
                        'LabelCounters': {
                            'TotalLabeled': 123,
                            'HumanLabeled': 123,
                            'MachineLabeled': 123,
                            'FailedNonRetryableError': 123,
                            'Unlabeled': 123
                        },
                        'WorkteamArn': 'string',
                        'PreHumanTaskLambdaArn': 'string',
                        'AnnotationConsolidationLambdaArn': 'string',
                        'FailureReason': 'string',
                        'LabelingJobOutput': {
                            'OutputDatasetS3Uri': 'string',
                            'FinalActiveLearningModelArn': 'string'
                        },
                        'InputConfig': {
                            'DataSource': {
                                'S3DataSource': {
                                    'ManifestS3Uri': 'string'
                                }
                            },
                            'DataAttributes': {
                                'ContentClassifiers': [
                                    'FreeOfPersonallyIdentifiableInformation'|'FreeOfAdultContent',
                                ]
                            }
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LabelingJobSummaryList** *(list) --* 
              An array of ``LabelingJobSummary`` objects, each describing a labeling job.
              - *(dict) --* 
                Provides summary information about a labeling job.
                - **LabelingJobName** *(string) --* 
                  The name of the labeling job.
                - **LabelingJobArn** *(string) --* 
                  The Amazon Resource Name (ARN) assigned to the labeling job when it was created.
                - **CreationTime** *(datetime) --* 
                  The date and time that the job was created (timestamp).
                - **LastModifiedTime** *(datetime) --* 
                  The date and time that the job was last modified (timestamp).
                - **LabelingJobStatus** *(string) --* 
                  The current status of the labeling job. 
                - **LabelCounters** *(dict) --* 
                  Counts showing the progress of the labeling job.
                  - **TotalLabeled** *(integer) --* 
                    The total number of objects labeled.
                  - **HumanLabeled** *(integer) --* 
                    The total number of objects labeled by a human worker.
                  - **MachineLabeled** *(integer) --* 
                    The total number of objects labeled by automated data labeling.
                  - **FailedNonRetryableError** *(integer) --* 
                    The total number of objects that could not be labeled due to an error.
                  - **Unlabeled** *(integer) --* 
                    The total number of objects not yet labeled.
                - **WorkteamArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the work team assigned to the job.
                - **PreHumanTaskLambdaArn** *(string) --* 
                  The Amazon Resource Name (ARN) of a Lambda function. The function is run before each data object is sent to a worker.
                - **AnnotationConsolidationLambdaArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the Lambda function used to consolidate the annotations from individual workers into a label for a data object. For more information, see `Annotation Consolidation <http://docs.aws.amazon.com/sagemaker/latest/dg/sms-annotation-consolidation.html>`__ .
                - **FailureReason** *(string) --* 
                  If the ``LabelingJobStatus`` field is ``Failed`` , this field contains a description of the error.
                - **LabelingJobOutput** *(dict) --* 
                  The location of the output produced by the labeling job.
                  - **OutputDatasetS3Uri** *(string) --* 
                    The Amazon S3 bucket location of the manifest file for labeled data. 
                  - **FinalActiveLearningModelArn** *(string) --* 
                    The Amazon Resource Name (ARN) for the most recent Amazon SageMaker model trained as part of automated data labeling. 
                - **InputConfig** *(dict) --* 
                  Input configuration for the labeling job.
                  - **DataSource** *(dict) --* 
                    The location of the input data.
                    - **S3DataSource** *(dict) --* 
                      The Amazon S3 location of the input data objects.
                      - **ManifestS3Uri** *(string) --* 
                        The Amazon S3 location of the manifest file that describes the input data objects.
                  - **DataAttributes** *(dict) --* 
                    Attributes of the data specified by the customer.
                    - **ContentClassifiers** *(list) --* 
                      Declares that your content is free of personally identifiable information or adult content. Amazon SageMaker may restrict the Amazon Mechanical Turk workers that can view your task based on this information.
                      - *(string) --* 
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:
          A filter that returns only labeling jobs created after the specified time (timestamp).
        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:
          A filter that returns only labeling jobs created before the specified time (timestamp).
        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:
          A filter that returns only labeling jobs modified after the specified time (timestamp).
        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:
          A filter that returns only labeling jobs modified before the specified time (timestamp).
        :type NameContains: string
        :param NameContains:
          A string in the labeling job name. This filter returns only labeling jobs whose name contains the specified string.
        :type SortBy: string
        :param SortBy:
          The field to sort results by. The default is ``CreationTime`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for results. The default is ``Ascending`` .
        :type StatusEquals: string
        :param StatusEquals:
          A filter that retrieves only labeling jobs with a specific status.
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
        """
        pass


class ListLabelingJobsForWorkteam(Paginator):
    def paginate(self, WorkteamArn: str, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, JobReferenceCodeContains: str = None, SortBy: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SageMaker.Client.list_labeling_jobs_for_workteam`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListLabelingJobsForWorkteam>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              WorkteamArn='string',
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              JobReferenceCodeContains='string',
              SortBy='CreationTime',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'LabelingJobSummaryList': [
                    {
                        'LabelingJobName': 'string',
                        'JobReferenceCode': 'string',
                        'WorkRequesterAccountId': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'LabelCounters': {
                            'HumanLabeled': 123,
                            'PendingHuman': 123,
                            'Total': 123
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LabelingJobSummaryList** *(list) --* 
              An array of ``LabelingJobSummary`` objects, each describing a labeling job.
              - *(dict) --* 
                Provides summary information for a work team.
                - **LabelingJobName** *(string) --* 
                  The name of the labeling job that the work team is assigned to.
                - **JobReferenceCode** *(string) --* 
                  A unique identifier for a labeling job. You can use this to refer to a specific labeling job.
                - **WorkRequesterAccountId** *(string) --* 
                - **CreationTime** *(datetime) --* 
                  The date and time that the labeling job was created.
                - **LabelCounters** *(dict) --* 
                  Provides information about the progress of a labeling job.
                  - **HumanLabeled** *(integer) --* 
                    The total number of data objects labeled by a human worker.
                  - **PendingHuman** *(integer) --* 
                    The total number of data objects that need to be labeled by a human worker.
                  - **Total** *(integer) --* 
                    The total number of tasks in the labeling job.
        :type WorkteamArn: string
        :param WorkteamArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the work team for which you want to see labeling jobs for.
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:
          A filter that returns only labeling jobs created after the specified time (timestamp).
        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:
          A filter that returns only labeling jobs created before the specified time (timestamp).
        :type JobReferenceCodeContains: string
        :param JobReferenceCodeContains:
          A filter the limits jobs to only the ones whose job reference code contains the specified string.
        :type SortBy: string
        :param SortBy:
          The field to sort results by. The default is ``CreationTime`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for results. The default is ``Ascending`` .
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
        """
        pass


class ListModelPackages(Paginator):
    def paginate(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, NameContains: str = None, SortBy: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SageMaker.Client.list_model_packages`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListModelPackages>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              NameContains='string',
              SortBy='Name'|'CreationTime',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ModelPackageSummaryList': [
                    {
                        'ModelPackageName': 'string',
                        'ModelPackageArn': 'string',
                        'ModelPackageDescription': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'ModelPackageStatus': 'Pending'|'InProgress'|'Completed'|'Failed'|'Deleting'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ModelPackageSummaryList** *(list) --* 
              An array of ``ModelPackageSummary`` objects, each of which lists a model package.
              - *(dict) --* 
                Provides summary information about a model package.
                - **ModelPackageName** *(string) --* 
                  The name of the model package.
                - **ModelPackageArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the model package.
                - **ModelPackageDescription** *(string) --* 
                  A brief description of the model package.
                - **CreationTime** *(datetime) --* 
                  A timestamp that shows when the model package was created.
                - **ModelPackageStatus** *(string) --* 
                  The overall status of the model package.
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:
          A filter that returns only model packages created after the specified time (timestamp).
        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:
          A filter that returns only model packages created before the specified time (timestamp).
        :type NameContains: string
        :param NameContains:
          A string in the model package name. This filter returns only model packages whose name contains the specified string.
        :type SortBy: string
        :param SortBy:
          The parameter by which to sort the results. The default is ``CreationTime`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for the results. The default is ``Ascending`` .
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
        """
        pass


class ListModels(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SageMaker.Client.list_models`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListModels>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              SortBy='Name'|'CreationTime',
              SortOrder='Ascending'|'Descending',
              NameContains='string',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1),
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Models': [
                    {
                        'ModelName': 'string',
                        'ModelArn': 'string',
                        'CreationTime': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Models** *(list) --* 
              An array of ``ModelSummary`` objects, each of which lists a model.
              - *(dict) --* 
                Provides summary information about a model.
                - **ModelName** *(string) --* 
                  The name of the model that you want a summary for.
                - **ModelArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the model.
                - **CreationTime** *(datetime) --* 
                  A timestamp that indicates when the model was created.
        :type SortBy: string
        :param SortBy:
          Sorts the list of results. The default is ``CreationTime`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for results. The default is ``Ascending`` .
        :type NameContains: string
        :param NameContains:
          A string in the training job name. This filter returns only models in the training job whose name contains the specified string.
        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:
          A filter that returns only models created before the specified time (timestamp).
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:
          A filter that returns only models created after the specified time (timestamp).
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
        """
        pass


class ListNotebookInstanceLifecycleConfigs(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SageMaker.Client.list_notebook_instance_lifecycle_configs`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListNotebookInstanceLifecycleConfigs>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              SortBy='Name'|'CreationTime'|'LastModifiedTime',
              SortOrder='Ascending'|'Descending',
              NameContains='string',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'NotebookInstanceLifecycleConfigs': [
                    {
                        'NotebookInstanceLifecycleConfigName': 'string',
                        'NotebookInstanceLifecycleConfigArn': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1)
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **NotebookInstanceLifecycleConfigs** *(list) --* 
              An array of ``NotebookInstanceLifecycleConfiguration`` objects, each listing a lifecycle configuration.
              - *(dict) --* 
                Provides a summary of a notebook instance lifecycle configuration.
                - **NotebookInstanceLifecycleConfigName** *(string) --* 
                  The name of the lifecycle configuration.
                - **NotebookInstanceLifecycleConfigArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the lifecycle configuration.
                - **CreationTime** *(datetime) --* 
                  A timestamp that tells when the lifecycle configuration was created.
                - **LastModifiedTime** *(datetime) --* 
                  A timestamp that tells when the lifecycle configuration was last modified.
        :type SortBy: string
        :param SortBy:
          Sorts the list of results. The default is ``CreationTime`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for results.
        :type NameContains: string
        :param NameContains:
          A string in the lifecycle configuration name. This filter returns only lifecycle configurations whose name contains the specified string.
        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:
          A filter that returns only lifecycle configurations that were created before the specified time (timestamp).
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:
          A filter that returns only lifecycle configurations that were created after the specified time (timestamp).
        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:
          A filter that returns only lifecycle configurations that were modified before the specified time (timestamp).
        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:
          A filter that returns only lifecycle configurations that were modified after the specified time (timestamp).
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
        """
        pass


class ListNotebookInstances(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, StatusEquals: str = None, NotebookInstanceLifecycleConfigNameContains: str = None, DefaultCodeRepositoryContains: str = None, AdditionalCodeRepositoryEquals: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SageMaker.Client.list_notebook_instances`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListNotebookInstances>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              SortBy='Name'|'CreationTime'|'Status',
              SortOrder='Ascending'|'Descending',
              NameContains='string',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              StatusEquals='Pending'|'InService'|'Stopping'|'Stopped'|'Failed'|'Deleting'|'Updating',
              NotebookInstanceLifecycleConfigNameContains='string',
              DefaultCodeRepositoryContains='string',
              AdditionalCodeRepositoryEquals='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'NotebookInstances': [
                    {
                        'NotebookInstanceName': 'string',
                        'NotebookInstanceArn': 'string',
                        'NotebookInstanceStatus': 'Pending'|'InService'|'Stopping'|'Stopped'|'Failed'|'Deleting'|'Updating',
                        'Url': 'string',
                        'InstanceType': 'ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.t3.medium'|'ml.t3.large'|'ml.t3.xlarge'|'ml.t3.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.c5d.xlarge'|'ml.c5d.2xlarge'|'ml.c5d.4xlarge'|'ml.c5d.9xlarge'|'ml.c5d.18xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'NotebookInstanceLifecycleConfigName': 'string',
                        'DefaultCodeRepository': 'string',
                        'AdditionalCodeRepositories': [
                            'string',
                        ]
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **NotebookInstances** *(list) --* 
              An array of ``NotebookInstanceSummary`` objects, one for each notebook instance.
              - *(dict) --* 
                Provides summary information for an Amazon SageMaker notebook instance.
                - **NotebookInstanceName** *(string) --* 
                  The name of the notebook instance that you want a summary for.
                - **NotebookInstanceArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the notebook instance.
                - **NotebookInstanceStatus** *(string) --* 
                  The status of the notebook instance.
                - **Url** *(string) --* 
                  The URL that you use to connect to the Jupyter instance running in your notebook instance. 
                - **InstanceType** *(string) --* 
                  The type of ML compute instance that the notebook instance is running on.
                - **CreationTime** *(datetime) --* 
                  A timestamp that shows when the notebook instance was created.
                - **LastModifiedTime** *(datetime) --* 
                  A timestamp that shows when the notebook instance was last modified.
                - **NotebookInstanceLifecycleConfigName** *(string) --* 
                  The name of a notebook instance lifecycle configuration associated with this notebook instance.
                  For information about notebook instance lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <http://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
                - **DefaultCodeRepository** *(string) --* 
                  The Git repository associated with the notebook instance as its default code repository. This can be either the name of a Git repository stored as a resource in your account, or the URL of a Git repository in `AWS CodeCommit <http://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html>`__ or in any other Git repository. When you open a notebook instance, it opens in the directory that contains this repository. For more information, see `Associating Git Repositories with Amazon SageMaker Notebook Instances <http://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html>`__ .
                - **AdditionalCodeRepositories** *(list) --* 
                  An array of up to three Git repositories associated with the notebook instance. These can be either the names of Git repositories stored as resources in your account, or the URL of Git repositories in `AWS CodeCommit <http://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html>`__ or in any other Git repository. These repositories are cloned at the same level as the default repository of your notebook instance. For more information, see `Associating Git Repositories with Amazon SageMaker Notebook Instances <http://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html>`__ .
                  - *(string) --* 
        :type SortBy: string
        :param SortBy:
          The field to sort results by. The default is ``Name`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for results.
        :type NameContains: string
        :param NameContains:
          A string in the notebook instances\' name. This filter returns only notebook instances whose name contains the specified string.
        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:
          A filter that returns only notebook instances that were created before the specified time (timestamp).
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:
          A filter that returns only notebook instances that were created after the specified time (timestamp).
        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:
          A filter that returns only notebook instances that were modified before the specified time (timestamp).
        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:
          A filter that returns only notebook instances that were modified after the specified time (timestamp).
        :type StatusEquals: string
        :param StatusEquals:
          A filter that returns only notebook instances with the specified status.
        :type NotebookInstanceLifecycleConfigNameContains: string
        :param NotebookInstanceLifecycleConfigNameContains:
          A string in the name of a notebook instances lifecycle configuration associated with this notebook instance. This filter returns only notebook instances associated with a lifecycle configuration with a name that contains the specified string.
        :type DefaultCodeRepositoryContains: string
        :param DefaultCodeRepositoryContains:
          A string in the name or URL of a Git repository associated with this notebook instance. This filter returns only notebook instances associated with a git repository with a name that contains the specified string.
        :type AdditionalCodeRepositoryEquals: string
        :param AdditionalCodeRepositoryEquals:
          A filter that returns only notebook instances with associated with the specified git repository.
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
        """
        pass


class ListSubscribedWorkteams(Paginator):
    def paginate(self, NameContains: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SageMaker.Client.list_subscribed_workteams`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListSubscribedWorkteams>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              NameContains='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'SubscribedWorkteams': [
                    {
                        'WorkteamArn': 'string',
                        'MarketplaceTitle': 'string',
                        'SellerName': 'string',
                        'MarketplaceDescription': 'string',
                        'ListingId': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **SubscribedWorkteams** *(list) --* 
              An array of ``Workteam`` objects, each describing a work team.
              - *(dict) --* 
                Describes a work team of a vendor that does the a labelling job.
                - **WorkteamArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the vendor that you have subscribed.
                - **MarketplaceTitle** *(string) --* 
                  The title of the service provided by the vendor in the Amazon Marketplace.
                - **SellerName** *(string) --* 
                  The name of the vendor in the Amazon Marketplace.
                - **MarketplaceDescription** *(string) --* 
                  The description of the vendor from the Amazon Marketplace.
                - **ListingId** *(string) --* 
        :type NameContains: string
        :param NameContains:
          A string in the work team name. This filter returns only work teams whose name contains the specified string.
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
        """
        pass


class ListTags(Paginator):
    def paginate(self, ResourceArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SageMaker.Client.list_tags`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTags>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ResourceArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Tags** *(list) --* 
              An array of ``Tag`` objects, each with a tag key and a value.
              - *(dict) --* 
                Describes a tag. 
                - **Key** *(string) --* 
                  The tag key.
                - **Value** *(string) --* 
                  The tag value.
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the resource whose tags you want to retrieve.
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
        """
        pass


class ListTrainingJobs(Paginator):
    def paginate(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SageMaker.Client.list_training_jobs`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTrainingJobs>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              NameContains='string',
              StatusEquals='InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
              SortBy='Name'|'CreationTime'|'Status',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'TrainingJobSummaries': [
                    {
                        'TrainingJobName': 'string',
                        'TrainingJobArn': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'TrainingEndTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'TrainingJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TrainingJobSummaries** *(list) --* 
              An array of ``TrainingJobSummary`` objects, each listing a training job.
              - *(dict) --* 
                Provides summary information about a training job.
                - **TrainingJobName** *(string) --* 
                  The name of the training job that you want a summary for.
                - **TrainingJobArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the training job.
                - **CreationTime** *(datetime) --* 
                  A timestamp that shows when the training job was created.
                - **TrainingEndTime** *(datetime) --* 
                  A timestamp that shows when the training job ended. This field is set only if the training job has one of the terminal statuses (``Completed`` , ``Failed`` , or ``Stopped`` ). 
                - **LastModifiedTime** *(datetime) --* 
                  Timestamp when the training job was last modified. 
                - **TrainingJobStatus** *(string) --* 
                  The status of the training job.
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:
          A filter that returns only training jobs created after the specified time (timestamp).
        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:
          A filter that returns only training jobs created before the specified time (timestamp).
        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:
          A filter that returns only training jobs modified after the specified time (timestamp).
        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:
          A filter that returns only training jobs modified before the specified time (timestamp).
        :type NameContains: string
        :param NameContains:
          A string in the training job name. This filter returns only training jobs whose name contains the specified string.
        :type StatusEquals: string
        :param StatusEquals:
          A filter that retrieves only training jobs with a specific status.
        :type SortBy: string
        :param SortBy:
          The field to sort results by. The default is ``CreationTime`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for results. The default is ``Ascending`` .
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
        """
        pass


class ListTrainingJobsForHyperParameterTuningJob(Paginator):
    def paginate(self, HyperParameterTuningJobName: str, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SageMaker.Client.list_training_jobs_for_hyper_parameter_tuning_job`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTrainingJobsForHyperParameterTuningJob>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              HyperParameterTuningJobName='string',
              StatusEquals='InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
              SortBy='Name'|'CreationTime'|'Status'|'FinalObjectiveMetricValue',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'TrainingJobSummaries': [
                    {
                        'TrainingJobName': 'string',
                        'TrainingJobArn': 'string',
                        'TuningJobName': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'TrainingStartTime': datetime(2015, 1, 1),
                        'TrainingEndTime': datetime(2015, 1, 1),
                        'TrainingJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
                        'TunedHyperParameters': {
                            'string': 'string'
                        },
                        'FailureReason': 'string',
                        'FinalHyperParameterTuningJobObjectiveMetric': {
                            'Type': 'Maximize'|'Minimize',
                            'MetricName': 'string',
                            'Value': ...
                        },
                        'ObjectiveStatus': 'Succeeded'|'Pending'|'Failed'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TrainingJobSummaries** *(list) --* 
              A list of  TrainingJobSummary objects that describe the training jobs that the ``ListTrainingJobsForHyperParameterTuningJob`` request returned.
              - *(dict) --* 
                Specifies summary information about a training job.
                - **TrainingJobName** *(string) --* 
                  The name of the training job.
                - **TrainingJobArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the training job.
                - **TuningJobName** *(string) --* 
                  The HyperParameter tuning job that launched the training job.
                - **CreationTime** *(datetime) --* 
                  The date and time that the training job was created.
                - **TrainingStartTime** *(datetime) --* 
                  The date and time that the training job started.
                - **TrainingEndTime** *(datetime) --* 
                  Specifies the time when the training job ends on training instances. You are billed for the time interval between the value of ``TrainingStartTime`` and this time. For successful jobs and stopped jobs, this is the time after model artifacts are uploaded. For failed jobs, this is the time when Amazon SageMaker detects a job failure.
                - **TrainingJobStatus** *(string) --* 
                  The status of the training job.
                - **TunedHyperParameters** *(dict) --* 
                  A list of the hyperparameters for which you specified ranges to search.
                  - *(string) --* 
                    - *(string) --* 
                - **FailureReason** *(string) --* 
                  The reason that the training job failed. 
                - **FinalHyperParameterTuningJobObjectiveMetric** *(dict) --* 
                  The  FinalHyperParameterTuningJobObjectiveMetric object that specifies the value of the objective metric of the tuning job that launched this training job.
                  - **Type** *(string) --* 
                    Whether to minimize or maximize the objective metric. Valid values are Minimize and Maximize.
                  - **MetricName** *(string) --* 
                    The name of the objective metric.
                  - **Value** *(float) --* 
                    The value of the objective metric.
                - **ObjectiveStatus** *(string) --* 
                  The status of the objective metric for the training job:
                  * Succeeded: The final objective metric for the training job was evaluated by the hyperparameter tuning job and used in the hyperparameter tuning process. 
                  * Pending: The training job is in progress and evaluation of its final objective metric is pending. 
                  * Failed: The final objective metric for the training job was not evaluated, and was not used in the hyperparameter tuning process. This typically occurs when the training job failed or did not emit an objective metric. 
        :type HyperParameterTuningJobName: string
        :param HyperParameterTuningJobName: **[REQUIRED]**
          The name of the tuning job whose training jobs you want to list.
        :type StatusEquals: string
        :param StatusEquals:
          A filter that returns only training jobs with the specified status.
        :type SortBy: string
        :param SortBy:
          The field to sort results by. The default is ``Name`` .
          If the value of this field is ``FinalObjectiveMetricValue`` , any training jobs that did not return an objective metric are not listed.
        :type SortOrder: string
        :param SortOrder:
          The sort order for results. The default is ``Ascending`` .
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
        """
        pass


class ListTransformJobs(Paginator):
    def paginate(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SageMaker.Client.list_transform_jobs`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTransformJobs>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              NameContains='string',
              StatusEquals='InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
              SortBy='Name'|'CreationTime'|'Status',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'TransformJobSummaries': [
                    {
                        'TransformJobName': 'string',
                        'TransformJobArn': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'TransformEndTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'TransformJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
                        'FailureReason': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TransformJobSummaries** *(list) --* 
              An array of ``TransformJobSummary`` objects.
              - *(dict) --* 
                Provides a summary of a transform job. Multiple ``TransformJobSummary`` objects are returned as a list after in response to a  ListTransformJobs call.
                - **TransformJobName** *(string) --* 
                  The name of the transform job.
                - **TransformJobArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the transform job.
                - **CreationTime** *(datetime) --* 
                  A timestamp that shows when the transform Job was created.
                - **TransformEndTime** *(datetime) --* 
                  Indicates when the transform job ends on compute instances. For successful jobs and stopped jobs, this is the exact time recorded after the results are uploaded. For failed jobs, this is when Amazon SageMaker detected that the job failed.
                - **LastModifiedTime** *(datetime) --* 
                  Indicates when the transform job was last modified.
                - **TransformJobStatus** *(string) --* 
                  The status of the transform job.
                - **FailureReason** *(string) --* 
                  If the transform job failed, the reason it failed.
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:
          A filter that returns only transform jobs created after the specified time.
        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:
          A filter that returns only transform jobs created before the specified time.
        :type LastModifiedTimeAfter: datetime
        :param LastModifiedTimeAfter:
          A filter that returns only transform jobs modified after the specified time.
        :type LastModifiedTimeBefore: datetime
        :param LastModifiedTimeBefore:
          A filter that returns only transform jobs modified before the specified time.
        :type NameContains: string
        :param NameContains:
          A string in the transform job name. This filter returns only transform jobs whose name contains the specified string.
        :type StatusEquals: string
        :param StatusEquals:
          A filter that retrieves only transform jobs with a specific status.
        :type SortBy: string
        :param SortBy:
          The field to sort results by. The default is ``CreationTime`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for results. The default is ``Descending`` .
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
        """
        pass


class ListWorkteams(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SageMaker.Client.list_workteams`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListWorkteams>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              SortBy='Name'|'CreateDate',
              SortOrder='Ascending'|'Descending',
              NameContains='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Workteams': [
                    {
                        'WorkteamName': 'string',
                        'MemberDefinitions': [
                            {
                                'CognitoMemberDefinition': {
                                    'UserPool': 'string',
                                    'UserGroup': 'string',
                                    'ClientId': 'string'
                                }
                            },
                        ],
                        'WorkteamArn': 'string',
                        'ProductListingIds': [
                            'string',
                        ],
                        'Description': 'string',
                        'SubDomain': 'string',
                        'CreateDate': datetime(2015, 1, 1),
                        'LastUpdatedDate': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Workteams** *(list) --* 
              An array of ``Workteam`` objects, each describing a work team.
              - *(dict) --* 
                Provides details about a labeling work team.
                - **WorkteamName** *(string) --* 
                  The name of the work team.
                - **MemberDefinitions** *(list) --* 
                  The Amazon Cognito user groups that make up the work team.
                  - *(dict) --* 
                    Defines the Amazon Cognito user group that is part of a work team.
                    - **CognitoMemberDefinition** *(dict) --* 
                      The Amazon Cognito user group that is part of the work team.
                      - **UserPool** *(string) --* 
                        An identifier for a user pool. The user pool must be in the same region as the service that you are calling.
                      - **UserGroup** *(string) --* 
                        An identifier for a user group.
                      - **ClientId** *(string) --* 
                        An identifier for an application client. You must create the app client ID using Amazon Cognito.
                - **WorkteamArn** *(string) --* 
                  The Amazon Resource Name (ARN) that identifies the work team.
                - **ProductListingIds** *(list) --* 
                  The Amazon Marketplace identifier for a vendor's work team.
                  - *(string) --* 
                - **Description** *(string) --* 
                  A description of the work team.
                - **SubDomain** *(string) --* 
                  The URI of the labeling job's user interface. Workers open this URI to start labeling your data objects.
                - **CreateDate** *(datetime) --* 
                  The date and time that the work team was created (timestamp).
                - **LastUpdatedDate** *(datetime) --* 
                  The date and time that the work team was last updated (timestamp).
        :type SortBy: string
        :param SortBy:
          The field to sort results by. The default is ``CreationTime`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for results. The default is ``Ascending`` .
        :type NameContains: string
        :param NameContains:
          A string in the work team\'s name. This filter returns only work teams whose name contains the specified string.
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
        """
        pass


class Search(Paginator):
    def paginate(self, Resource: str, SearchExpression: Dict = None, SortBy: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SageMaker.Client.search`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/Search>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Resource='TrainingJob',
              SearchExpression={
                  'Filters': [
                      {
                          'Name': 'string',
                          'Operator': 'Equals'|'NotEquals'|'GreaterThan'|'GreaterThanOrEqualTo'|'LessThan'|'LessThanOrEqualTo'|'Contains',
                          'Value': 'string'
                      },
                  ],
                  'NestedFilters': [
                      {
                          'NestedPropertyName': 'string',
                          'Filters': [
                              {
                                  'Name': 'string',
                                  'Operator': 'Equals'|'NotEquals'|'GreaterThan'|'GreaterThanOrEqualTo'|'LessThan'|'LessThanOrEqualTo'|'Contains',
                                  'Value': 'string'
                              },
                          ]
                      },
                  ],
                  'SubExpressions': [
                      {'... recursive ...'},
                  ],
                  'Operator': 'And'|'Or'
              },
              SortBy='string',
              SortOrder='Ascending'|'Descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Results': [
                    {
                        'TrainingJob': {
                            'TrainingJobName': 'string',
                            'TrainingJobArn': 'string',
                            'TuningJobArn': 'string',
                            'LabelingJobArn': 'string',
                            'ModelArtifacts': {
                                'S3ModelArtifacts': 'string'
                            },
                            'TrainingJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
                            'SecondaryStatus': 'Starting'|'LaunchingMLInstances'|'PreparingTrainingStack'|'Downloading'|'DownloadingTrainingImage'|'Training'|'Uploading'|'Stopping'|'Stopped'|'MaxRuntimeExceeded'|'Completed'|'Failed',
                            'FailureReason': 'string',
                            'HyperParameters': {
                                'string': 'string'
                            },
                            'AlgorithmSpecification': {
                                'TrainingImage': 'string',
                                'AlgorithmName': 'string',
                                'TrainingInputMode': 'Pipe'|'File',
                                'MetricDefinitions': [
                                    {
                                        'Name': 'string',
                                        'Regex': 'string'
                                    },
                                ]
                            },
                            'RoleArn': 'string',
                            'InputDataConfig': [
                                {
                                    'ChannelName': 'string',
                                    'DataSource': {
                                        'S3DataSource': {
                                            'S3DataType': 'ManifestFile'|'S3Prefix'|'AugmentedManifestFile',
                                            'S3Uri': 'string',
                                            'S3DataDistributionType': 'FullyReplicated'|'ShardedByS3Key',
                                            'AttributeNames': [
                                                'string',
                                            ]
                                        }
                                    },
                                    'ContentType': 'string',
                                    'CompressionType': 'None'|'Gzip',
                                    'RecordWrapperType': 'None'|'RecordIO',
                                    'InputMode': 'Pipe'|'File',
                                    'ShuffleConfig': {
                                        'Seed': 123
                                    }
                                },
                            ],
                            'OutputDataConfig': {
                                'KmsKeyId': 'string',
                                'S3OutputPath': 'string'
                            },
                            'ResourceConfig': {
                                'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
                                'InstanceCount': 123,
                                'VolumeSizeInGB': 123,
                                'VolumeKmsKeyId': 'string'
                            },
                            'VpcConfig': {
                                'SecurityGroupIds': [
                                    'string',
                                ],
                                'Subnets': [
                                    'string',
                                ]
                            },
                            'StoppingCondition': {
                                'MaxRuntimeInSeconds': 123
                            },
                            'CreationTime': datetime(2015, 1, 1),
                            'TrainingStartTime': datetime(2015, 1, 1),
                            'TrainingEndTime': datetime(2015, 1, 1),
                            'LastModifiedTime': datetime(2015, 1, 1),
                            'SecondaryStatusTransitions': [
                                {
                                    'Status': 'Starting'|'LaunchingMLInstances'|'PreparingTrainingStack'|'Downloading'|'DownloadingTrainingImage'|'Training'|'Uploading'|'Stopping'|'Stopped'|'MaxRuntimeExceeded'|'Completed'|'Failed',
                                    'StartTime': datetime(2015, 1, 1),
                                    'EndTime': datetime(2015, 1, 1),
                                    'StatusMessage': 'string'
                                },
                            ],
                            'FinalMetricDataList': [
                                {
                                    'MetricName': 'string',
                                    'Value': ...,
                                    'Timestamp': datetime(2015, 1, 1)
                                },
                            ],
                            'EnableNetworkIsolation': True|False,
                            'Tags': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ]
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Results** *(list) --* 
              A list of ``SearchResult`` objects.
              - *(dict) --* 
                An individual search result record that contains a single resource object.
                - **TrainingJob** *(dict) --* 
                  A ``TrainingJob`` object that is returned as part of a ``Search`` request.
                  - **TrainingJobName** *(string) --* 
                    The name of the training job.
                  - **TrainingJobArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the training job.
                  - **TuningJobArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the associated hyperparameter tuning job if the training job was launched by a hyperparameter tuning job.
                  - **LabelingJobArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the labeling job.
                  - **ModelArtifacts** *(dict) --* 
                    Information about the Amazon S3 location that is configured for storing model artifacts.
                    - **S3ModelArtifacts** *(string) --* 
                      The path of the S3 object that contains the model artifacts. For example, ``s3://bucket-name/keynameprefix/model.tar.gz`` .
                  - **TrainingJobStatus** *(string) --* 
                    The status of the training job.
                    Training job statuses are:
                    * ``InProgress`` - The training is in progress. 
                    * ``Completed`` - The training job has completed. 
                    * ``Failed`` - The training job has failed. To see the reason for the failure, see the ``FailureReason`` field in the response to a ``DescribeTrainingJobResponse`` call. 
                    * ``Stopping`` - The training job is stopping. 
                    * ``Stopped`` - The training job has stopped. 
                    For more detailed information, see ``SecondaryStatus`` . 
                  - **SecondaryStatus** *(string) --* 
                    Provides detailed information about the state of the training job. For detailed information about the secondary status of the training job, see ``StatusMessage`` under  SecondaryStatusTransition .
                    Amazon SageMaker provides primary statuses and secondary statuses that apply to each of them:
                      InProgress  
                    * ``Starting`` - Starting the training job. 
                    * ``Downloading`` - An optional stage for algorithms that support ``File`` training input mode. It indicates that data is being downloaded to the ML storage volumes. 
                    * ``Training`` - Training is in progress. 
                    * ``Uploading`` - Training is complete and the model artifacts are being uploaded to the S3 location. 
                      Completed  
                    * ``Completed`` - The training job has completed. 
                      Failed  
                    * ``Failed`` - The training job has failed. The reason for the failure is returned in the ``FailureReason`` field of ``DescribeTrainingJobResponse`` . 
                      Stopped  
                    * ``MaxRuntimeExceeded`` - The job stopped because it exceeded the maximum allowed runtime. 
                    * ``Stopped`` - The training job has stopped. 
                      Stopping  
                    * ``Stopping`` - Stopping the training job. 
                    .. warning::
                      Valid values for ``SecondaryStatus`` are subject to change. 
                    We no longer support the following secondary statuses:
                    * ``LaunchingMLInstances``   
                    * ``PreparingTrainingStack``   
                    * ``DownloadingTrainingImage``   
                  - **FailureReason** *(string) --* 
                    If the training job failed, the reason it failed.
                  - **HyperParameters** *(dict) --* 
                    Algorithm-specific parameters.
                    - *(string) --* 
                      - *(string) --* 
                  - **AlgorithmSpecification** *(dict) --* 
                    Information about the algorithm used for training, and algorithm metadata.
                    - **TrainingImage** *(string) --* 
                      The registry path of the Docker image that contains the training algorithm. For information about docker registry paths for built-in algorithms, see `Algorithms Provided by Amazon SageMaker\: Common Parameters <http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html>`__ .
                    - **AlgorithmName** *(string) --* 
                      The name of the algorithm resource to use for the training job. This must be an algorithm resource that you created or subscribe to on AWS Marketplace. If you specify a value for this parameter, you can't specify a value for ``TrainingImage`` .
                    - **TrainingInputMode** *(string) --* 
                      The input mode that the algorithm supports. For the input modes that Amazon SageMaker algorithms support, see `Algorithms <http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ . If an algorithm supports the ``File`` input mode, Amazon SageMaker downloads the training data from S3 to the provisioned ML storage Volume, and mounts the directory to docker volume for training container. If an algorithm supports the ``Pipe`` input mode, Amazon SageMaker streams data directly from S3 to the container. 
                      In File mode, make sure you provision ML storage volume with sufficient capacity to accommodate the data download from S3. In addition to the training data, the ML storage volume also stores the output model. The algorithm container use ML storage volume to also store intermediate information, if any. 
                      For distributed algorithms using File mode, training data is distributed uniformly, and your training duration is predictable if the input data objects size is approximately same. Amazon SageMaker does not split the files any further for model training. If the object sizes are skewed, training won't be optimal as the data distribution is also skewed where one host in a training cluster is overloaded, thus becoming bottleneck in training. 
                    - **MetricDefinitions** *(list) --* 
                      A list of metric definition objects. Each object specifies the metric name and regular expressions used to parse algorithm logs. Amazon SageMaker publishes each metric to Amazon CloudWatch.
                      - *(dict) --* 
                        Specifies a metric that the training algorithm writes to ``stderr`` or ``stdout`` . Amazon SageMakerhyperparameter tuning captures all defined metrics. You specify one metric that a hyperparameter tuning job uses as its objective metric to choose the best training job.
                        - **Name** *(string) --* 
                          The name of the metric.
                        - **Regex** *(string) --* 
                          A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see `Defining Objective Metrics <http://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics.html>`__ .
                  - **RoleArn** *(string) --* 
                    The AWS Identity and Access Management (IAM) role configured for the training job.
                  - **InputDataConfig** *(list) --* 
                    An array of ``Channel`` objects that describes each data input channel.
                    - *(dict) --* 
                      A channel is a named input source that training algorithms can consume. 
                      - **ChannelName** *(string) --* 
                        The name of the channel. 
                      - **DataSource** *(dict) --* 
                        The location of the channel data.
                        - **S3DataSource** *(dict) --* 
                          The S3 location of the data source that is associated with a channel.
                          - **S3DataType** *(string) --* 
                            If you choose ``S3Prefix`` , ``S3Uri`` identifies a key name prefix. Amazon SageMaker uses all objects that match the specified key name prefix for model training. 
                            If you choose ``ManifestFile`` , ``S3Uri`` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for model training. 
                            If you choose ``AugmentedManifestFile`` , S3Uri identifies an object that is an augmented manifest file in JSON lines format. This file contains the data you want to use for model training. ``AugmentedManifestFile`` can only be used if the Channel's input mode is ``Pipe`` .
                          - **S3Uri** *(string) --* 
                            Depending on the value specified for the ``S3DataType`` , identifies either a key name prefix or a manifest. For example: 
                            * A key name prefix might look like this: ``s3://bucketname/exampleprefix`` .  
                            * A manifest might look like this: ``s3://bucketname/example.manifest``   The manifest is an S3 object which is a JSON file with the following format:   ``[``    ``{"prefix": "s3://customer_bucket/some/prefix/"},``    ``"relative/path/to/custdata-1",``    ``"relative/path/custdata-2",``    ``...``    ``]``   The preceding JSON matches the following ``s3Uris`` :   ``s3://customer_bucket/some/prefix/relative/path/to/custdata-1``    ``s3://customer_bucket/some/prefix/relative/path/custdata-2``    ``...``   The complete set of ``s3uris`` in this manifest is the input data for the channel for this datasource. The object that each ``s3uris`` points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.  
                          - **S3DataDistributionType** *(string) --* 
                            If you want Amazon SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify ``FullyReplicated`` . 
                            If you want Amazon SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify ``ShardedByS3Key`` . If there are *n* ML compute instances launched for a training job, each instance gets approximately 1/*n* of the number of S3 objects. In this case, model training on each machine uses only the subset of training data. 
                            Don't choose more ML compute instances for training than available S3 objects. If you do, some nodes won't get any data and you will pay for nodes that aren't getting any training data. This applies in both File and Pipe modes. Keep this in mind when developing algorithms. 
                            In distributed training, where you use multiple ML compute EC2 instances, you might choose ``ShardedByS3Key`` . If the algorithm requires copying training data to the ML storage volume (when ``TrainingInputMode`` is set to ``File`` ), this copies 1/*n* of the number of objects. 
                          - **AttributeNames** *(list) --* 
                            A list of one or more attribute names to use that are found in a specified augmented manifest file.
                            - *(string) --* 
                      - **ContentType** *(string) --* 
                        The MIME type of the data.
                      - **CompressionType** *(string) --* 
                        If training data is compressed, the compression type. The default value is ``None`` . ``CompressionType`` is used only in Pipe input mode. In File mode, leave this field unset or set it to None.
                      - **RecordWrapperType** *(string) --* 
                        Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format. In this case, Amazon SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you don't need to set this attribute. For more information, see `Create a Dataset Using RecordIO <https://mxnet.incubator.apache.org/architecture/note_data_loading.html#data-format>`__ . 
                        In File mode, leave this field unset or set it to None.
                      - **InputMode** *(string) --* 
                        (Optional) The input mode to use for the data channel in a training job. If you don't set a value for ``InputMode`` , Amazon SageMaker uses the value set for ``TrainingInputMode`` . Use this parameter to override the ``TrainingInputMode`` setting in a  AlgorithmSpecification request when you have a channel that needs a different input mode from the training job's general setting. To download the data from Amazon Simple Storage Service (Amazon S3) to the provisioned ML storage volume, and mount the directory to a Docker volume, use ``File`` input mode. To stream data directly from Amazon S3 to the container, choose ``Pipe`` input mode.
                        To use a model for incremental training, choose ``File`` input model.
                      - **ShuffleConfig** *(dict) --* 
                        A configuration for a shuffle option for input data in a channel. If you use ``S3Prefix`` for ``S3DataType`` , this shuffles the results of the S3 key prefix matches. If you use ``ManifestFile`` , the order of the S3 object references in the ``ManifestFile`` is shuffled. If you use ``AugmentedManifestFile`` , the order of the JSON lines in the ``AugmentedManifestFile`` is shuffled. The shuffling order is determined using the ``Seed`` value.
                        For Pipe input mode, shuffling is done at the start of every epoch. With large datasets this ensures that the order of the training data is different for each epoch, it helps reduce bias and possible overfitting. In a multi-node training job when ShuffleConfig is combined with ``S3DataDistributionType`` of ``ShardedByS3Key`` , the data is shuffled across nodes so that the content sent to a particular node on the first epoch might be sent to a different node on the second epoch.
                        - **Seed** *(integer) --* 
                          Determines the shuffling order in ``ShuffleConfig`` value.
                  - **OutputDataConfig** *(dict) --* 
                    The S3 path where model artifacts that you configured when creating the job are stored. Amazon SageMaker creates subfolders for model artifacts.
                    - **KmsKeyId** *(string) --* 
                      The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The ``KmsKeyId`` can be any of the following formats: 
                      * // KMS Key ID  ``"1234abcd-12ab-34cd-56ef-1234567890ab"``   
                      * // Amazon Resource Name (ARN) of a KMS Key  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``   
                      * // KMS Key Alias  ``"alias/ExampleAlias"``   
                      * // Amazon Resource Name (ARN) of a KMS Key Alias  ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``   
                      If you don't provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role's account. For more information, see `KMS-Managed Encryption Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ in the *Amazon Simple Storage Service Developer Guide.*  
                      The KMS key policy must grant permission to the IAM role that you specify in your ``CreateTramsformJob`` request. For more information, see `Using Key Policies in AWS KMS <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the *AWS Key Management Service Developer Guide* .
                    - **S3OutputPath** *(string) --* 
                      Identifies the S3 path where you want Amazon SageMaker to store the model artifacts. For example, ``s3://bucket-name/key-name-prefix`` . 
                  - **ResourceConfig** *(dict) --* 
                    Resources, including ML compute instances and ML storage volumes, that are configured for model training.
                    - **InstanceType** *(string) --* 
                      The ML compute instance type. 
                    - **InstanceCount** *(integer) --* 
                      The number of ML compute instances to use. For distributed training, provide a value greater than 1. 
                    - **VolumeSizeInGB** *(integer) --* 
                      The size of the ML storage volume that you want to provision. 
                      ML storage volumes store model artifacts and incremental states. Training algorithms might also use the ML storage volume for scratch space. If you want to store the training data in the ML storage volume, choose ``File`` as the ``TrainingInputMode`` in the algorithm specification. 
                      You must specify sufficient ML storage for your scenario. 
                      .. note::
                        Amazon SageMaker supports only the General Purpose SSD (gp2) ML storage volume type. 
                    - **VolumeKmsKeyId** *(string) --* 
                      The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the training job. The ``VolumeKmsKeyId`` can be any of the following formats:
                      * // KMS Key ID  ``"1234abcd-12ab-34cd-56ef-1234567890ab"``   
                      * // Amazon Resource Name (ARN) of a KMS Key  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``   
                  - **VpcConfig** *(dict) --* 
                    A  VpcConfig object that specifies the VPC that this training job has access to. For more information, see `Protect Training Jobs by Using an Amazon Virtual Private Cloud <http://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html>`__ .
                    - **SecurityGroupIds** *(list) --* 
                      The VPC security group IDs, in the form sg-xxxxxxxx. Specify the security groups for the VPC that is specified in the ``Subnets`` field.
                      - *(string) --* 
                    - **Subnets** *(list) --* 
                      The ID of the subnets in the VPC to which you want to connect your training job or model. 
                      - *(string) --* 
                  - **StoppingCondition** *(dict) --* 
                    The condition under which to stop the training job.
                    - **MaxRuntimeInSeconds** *(integer) --* 
                      The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 28 days.
                  - **CreationTime** *(datetime) --* 
                    A timestamp that indicates when the training job was created.
                  - **TrainingStartTime** *(datetime) --* 
                    Indicates the time when the training job starts on training instances. You are billed for the time interval between this time and the value of ``TrainingEndTime`` . The start time in CloudWatch Logs might be later than this time. The difference is due to the time it takes to download the training data and to the size of the training container.
                  - **TrainingEndTime** *(datetime) --* 
                    Indicates the time when the training job ends on training instances. You are billed for the time interval between the value of ``TrainingStartTime`` and this time. For successful jobs and stopped jobs, this is the time after model artifacts are uploaded. For failed jobs, this is the time when Amazon SageMaker detects a job failure.
                  - **LastModifiedTime** *(datetime) --* 
                    A timestamp that indicates when the status of the training job was last modified.
                  - **SecondaryStatusTransitions** *(list) --* 
                    A history of all of the secondary statuses that the training job has transitioned through.
                    - *(dict) --* 
                      An array element of  DescribeTrainingJobResponse$SecondaryStatusTransitions . It provides additional details about a status that the training job has transitioned through. A training job can be in one of several states, for example, starting, downloading, training, or uploading. Within each state, there are a number of intermediate states. For example, within the starting state, Amazon SageMaker could be starting the training job or launching the ML instances. These transitional states are referred to as the job's secondary status. 
                      - **Status** *(string) --* 
                        Contains a secondary status information from a training job.
                        Status might be one of the following secondary statuses:
                          InProgress  
                        * ``Starting`` - Starting the training job. 
                        * ``Downloading`` - An optional stage for algorithms that support ``File`` training input mode. It indicates that data is being downloaded to the ML storage volumes. 
                        * ``Training`` - Training is in progress. 
                        * ``Uploading`` - Training is complete and the model artifacts are being uploaded to the S3 location. 
                          Completed  
                        * ``Completed`` - The training job has completed. 
                          Failed  
                        * ``Failed`` - The training job has failed. The reason for the failure is returned in the ``FailureReason`` field of ``DescribeTrainingJobResponse`` . 
                          Stopped  
                        * ``MaxRuntimeExceeded`` - The job stopped because it exceeded the maximum allowed runtime. 
                        * ``Stopped`` - The training job has stopped. 
                          Stopping  
                        * ``Stopping`` - Stopping the training job. 
                        We no longer support the following secondary statuses:
                        * ``LaunchingMLInstances``   
                        * ``PreparingTrainingStack``   
                        * ``DownloadingTrainingImage``   
                      - **StartTime** *(datetime) --* 
                        A timestamp that shows when the training job transitioned to the current secondary status state.
                      - **EndTime** *(datetime) --* 
                        A timestamp that shows when the training job transitioned out of this secondary status state into another secondary status state or when the training job has ended.
                      - **StatusMessage** *(string) --* 
                        A detailed description of the progress within a secondary status. 
                        Amazon SageMaker provides secondary statuses and status messages that apply to each of them:
                          Starting  
                        * Starting the training job. 
                        * Launching requested ML instances. 
                        * Insufficient capacity error from EC2 while launching instances, retrying! 
                        * Launched instance was unhealthy, replacing it! 
                        * Preparing the instances for training. 
                          Training  
                        * Downloading the training image. 
                        * Training image download completed. Training in progress. 
                        .. warning::
                          Status messages are subject to change. Therefore, we recommend not including them in code that programmatically initiates actions. For examples, don't use status messages in if statements.
                        To have an overview of your training job's progress, view ``TrainingJobStatus`` and ``SecondaryStatus`` in  DescribeTrainingJobResponse , and ``StatusMessage`` together. For example, at the start of a training job, you might see the following:
                        * ``TrainingJobStatus`` - InProgress 
                        * ``SecondaryStatus`` - Training 
                        * ``StatusMessage`` - Downloading the training image 
                  - **FinalMetricDataList** *(list) --* 
                    A list of final metric values that are set when the training job completes. Used only if the training job was configured to use metrics.
                    - *(dict) --* 
                      The name, value, and date and time of a metric that was emitted to Amazon CloudWatch.
                      - **MetricName** *(string) --* 
                        The name of the metric.
                      - **Value** *(float) --* 
                        The value of the metric.
                      - **Timestamp** *(datetime) --* 
                        The date and time that the algorithm emitted the metric.
                  - **EnableNetworkIsolation** *(boolean) --* 
                    If the ``TrainingJob`` was created with network isolation, the value is set to ``true`` . If network isolation is enabled, nodes can't communicate beyond the VPC they run in.
                  - **Tags** *(list) --* 
                    An array of key-value pairs. For more information, see `Using Cost Allocation Tags <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what>`__ in the *AWS Billing and Cost Management User Guide* .
                    - *(dict) --* 
                      Describes a tag. 
                      - **Key** *(string) --* 
                        The tag key.
                      - **Value** *(string) --* 
                        The tag value.
        :type Resource: string
        :param Resource: **[REQUIRED]**
          The name of the Amazon SageMaker resource to search for. Currently, the only valid ``Resource`` value is ``TrainingJob`` .
        :type SearchExpression: dict
        :param SearchExpression:
          A Boolean conditional statement. Resource objects must satisfy this condition to be included in search results. You must provide at least one subexpression, filter, or nested filter. The maximum number of recursive ``SubExpressions`` , ``NestedFilters`` , and ``Filters`` that can be included in a ``SearchExpression`` object is 50.
          - **Filters** *(list) --*
            A list of filter objects.
            - *(dict) --*
              A conditional statement for a search expression that includes a Boolean operator, a resource property, and a value.
              If you don\'t specify an ``Operator`` and a ``Value`` , the filter searches for only the specified property. For example, defining a ``Filter`` for the ``FailureReason`` for the ``TrainingJob``  ``Resource`` searches for training job objects that have a value in the ``FailureReason`` field.
              If you specify a ``Value`` , but not an ``Operator`` , Amazon SageMaker uses the equals operator as the default.
              In search, there are several property types:
                Metrics
              To define a metric filter, enter a value using the form ``\"Metrics.<name>\"`` , where ``<name>`` is a metric name. For example, the following filter searches for training jobs with an ``\"accuracy\"`` metric greater than ``\"0.9\"`` :
               ``{``
               ``\"Name\": \"Metrics.accuracy\",``
               ``\"Operator\": \"GREATER_THAN\",``
               ``\"Value\": \"0.9\"``
               ``}``
                HyperParameters
              To define a hyperparameter filter, enter a value with the form ``\"HyperParameters.<name>\"`` . Decimal hyperparameter values are treated as a decimal in a comparison if the specified ``Value`` is also a decimal value. If the specified ``Value`` is an integer, the decimal hyperparameter values are treated as integers. For example, the following filter is satisfied by training jobs with a ``\"learning_rate\"`` hyperparameter that is less than ``\"0.5\"`` :
               ``{``
               ``\"Name\": \"HyperParameters.learning_rate\",``
               ``\"Operator\": \"LESS_THAN\",``
               ``\"Value\": \"0.5\"``
               ``}``
                Tags
              To define a tag filter, enter a value with the form ``\"Tags.<key>\"`` .
              - **Name** *(string) --* **[REQUIRED]**
                A property name. For example, ``TrainingJobName`` . For the list of valid property names returned in a search result for each supported resource, see  TrainingJob properties. You must specify a valid property name for the resource.
              - **Operator** *(string) --*
                A Boolean binary operator that is used to evaluate the filter. The operator field contains one of the following values:
                  Equals
                The specified resource in ``Name`` equals the specified ``Value`` .
                  NotEquals
                The specified resource in ``Name`` does not equal the specified ``Value`` .
                  GreaterThan
                The specified resource in ``Name`` is greater than the specified ``Value`` . Not supported for text-based properties.
                  GreaterThanOrEqualTo
                The specified resource in ``Name`` is greater than or equal to the specified ``Value`` . Not supported for text-based properties.
                  LessThan
                The specified resource in ``Name`` is less than the specified ``Value`` . Not supported for text-based properties.
                  LessThanOrEqualTo
                The specified resource in ``Name`` is less than or equal to the specified ``Value`` . Not supported for text-based properties.
                  Contains
                Only supported for text-based properties. The word-list of the property contains the specified ``Value`` .
                If you have specified a filter ``Value`` , the default is ``Equals`` .
              - **Value** *(string) --*
                A value used with ``Resource`` and ``Operator`` to determine if objects satisfy the filter\'s condition. For numerical properties, ``Value`` must be an integer or floating-point decimal. For timestamp properties, ``Value`` must be an ISO 8601 date-time string of the following format: ``YYYY-mm-dd\'T\'HH:MM:SS`` .
          - **NestedFilters** *(list) --*
            A list of nested filter objects.
            - *(dict) --*
              Defines a list of ``NestedFilters`` objects. To satisfy the conditions specified in the ``NestedFilters`` call, a resource must satisfy the conditions of all of the filters.
              For example, you could define a ``NestedFilters`` using the training job\'s ``InputDataConfig`` property to filter on ``Channel`` objects.
              A ``NestedFilters`` object contains multiple filters. For example, to find all training jobs whose name contains ``train`` and that have ``cat/data`` in their ``S3Uri`` (specified in ``InputDataConfig`` ), you need to create a ``NestedFilters`` object that specifies the ``InputDataConfig`` property with the following ``Filter`` objects:
              * ``\'{Name:\"InputDataConfig.ChannelName\", \"Operator\":\"EQUALS\", \"Value\":\"train\"}\',``
              * ``\'{Name:\"InputDataConfig.DataSource.S3DataSource.S3Uri\", \"Operator\":\"CONTAINS\", \"Value\":\"cat/data\"}\'``
              - **NestedPropertyName** *(string) --* **[REQUIRED]**
                The name of the property to use in the nested filters. The value must match a listed property name, such as ``InputDataConfig`` .
              - **Filters** *(list) --* **[REQUIRED]**
                A list of filters. Each filter acts on a property. Filters must contain at least one ``Filters`` value. For example, a ``NestedFilters`` call might include a filter on the ``PropertyName`` parameter of the ``InputDataConfig`` property: ``InputDataConfig.DataSource.S3DataSource.S3Uri`` .
                - *(dict) --*
                  A conditional statement for a search expression that includes a Boolean operator, a resource property, and a value.
                  If you don\'t specify an ``Operator`` and a ``Value`` , the filter searches for only the specified property. For example, defining a ``Filter`` for the ``FailureReason`` for the ``TrainingJob``  ``Resource`` searches for training job objects that have a value in the ``FailureReason`` field.
                  If you specify a ``Value`` , but not an ``Operator`` , Amazon SageMaker uses the equals operator as the default.
                  In search, there are several property types:
                    Metrics
                  To define a metric filter, enter a value using the form ``\"Metrics.<name>\"`` , where ``<name>`` is a metric name. For example, the following filter searches for training jobs with an ``\"accuracy\"`` metric greater than ``\"0.9\"`` :
                   ``{``
                   ``\"Name\": \"Metrics.accuracy\",``
                   ``\"Operator\": \"GREATER_THAN\",``
                   ``\"Value\": \"0.9\"``
                   ``}``
                    HyperParameters
                  To define a hyperparameter filter, enter a value with the form ``\"HyperParameters.<name>\"`` . Decimal hyperparameter values are treated as a decimal in a comparison if the specified ``Value`` is also a decimal value. If the specified ``Value`` is an integer, the decimal hyperparameter values are treated as integers. For example, the following filter is satisfied by training jobs with a ``\"learning_rate\"`` hyperparameter that is less than ``\"0.5\"`` :
                   ``{``
                   ``\"Name\": \"HyperParameters.learning_rate\",``
                   ``\"Operator\": \"LESS_THAN\",``
                   ``\"Value\": \"0.5\"``
                   ``}``
                    Tags
                  To define a tag filter, enter a value with the form ``\"Tags.<key>\"`` .
                  - **Name** *(string) --* **[REQUIRED]**
                    A property name. For example, ``TrainingJobName`` . For the list of valid property names returned in a search result for each supported resource, see  TrainingJob properties. You must specify a valid property name for the resource.
                  - **Operator** *(string) --*
                    A Boolean binary operator that is used to evaluate the filter. The operator field contains one of the following values:
                      Equals
                    The specified resource in ``Name`` equals the specified ``Value`` .
                      NotEquals
                    The specified resource in ``Name`` does not equal the specified ``Value`` .
                      GreaterThan
                    The specified resource in ``Name`` is greater than the specified ``Value`` . Not supported for text-based properties.
                      GreaterThanOrEqualTo
                    The specified resource in ``Name`` is greater than or equal to the specified ``Value`` . Not supported for text-based properties.
                      LessThan
                    The specified resource in ``Name`` is less than the specified ``Value`` . Not supported for text-based properties.
                      LessThanOrEqualTo
                    The specified resource in ``Name`` is less than or equal to the specified ``Value`` . Not supported for text-based properties.
                      Contains
                    Only supported for text-based properties. The word-list of the property contains the specified ``Value`` .
                    If you have specified a filter ``Value`` , the default is ``Equals`` .
                  - **Value** *(string) --*
                    A value used with ``Resource`` and ``Operator`` to determine if objects satisfy the filter\'s condition. For numerical properties, ``Value`` must be an integer or floating-point decimal. For timestamp properties, ``Value`` must be an ISO 8601 date-time string of the following format: ``YYYY-mm-dd\'T\'HH:MM:SS`` .
          - **SubExpressions** *(list) --*
            A list of search expression objects.
            - *(dict) --*
              A multi-expression that searches for the specified resource or resources in a search. All resource objects that satisfy the expression\'s condition are included in the search results. You must specify at least one subexpression, filter, or nested filter. A ``SearchExpression`` can contain up to twenty elements.
              A ``SearchExpression`` contains the following components:
              * A list of ``Filter`` objects. Each filter defines a simple Boolean expression comprised of a resource property name, Boolean operator, and value.
              * A list of ``NestedFilter`` objects. Each nested filter defines a list of Boolean expressions using a list of resource properties. A nested filter is satisfied if a single object in the list satisfies all Boolean expressions.
              * A list of ``SearchExpression`` objects. A search expression object can be nested in a list of search expression objects.
              * A Boolean operator: ``And`` or ``Or`` .
          - **Operator** *(string) --*
            A Boolean operator used to evaluate the search expression. If you want every conditional statement in all lists to be satisfied for the entire search expression to be true, specify ``And`` . If only a single conditional statement needs to be true for the entire search expression to be true, specify ``Or`` . The default value is ``And`` .
        :type SortBy: string
        :param SortBy:
          The name of the resource property used to sort the ``SearchResults`` . The default is ``LastModifiedTime`` .
        :type SortOrder: string
        :param SortOrder:
          How ``SearchResults`` are ordered. Valid values are ``Ascending`` or ``Descending`` . The default is ``Descending`` .
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
        """
        pass
