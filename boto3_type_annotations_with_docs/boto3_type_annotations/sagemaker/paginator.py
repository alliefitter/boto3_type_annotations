from datetime import datetime
from typing import Dict
from botocore.paginate import Paginator


class ListEndpointConfigs(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListEndpointConfigs>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              SortBy=\'Name\'|\'CreationTime\',
              SortOrder=\'Ascending\'|\'Descending\',
              NameContains=\'string\',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1),
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'EndpointConfigs\': [
                    {
                        \'EndpointConfigName\': \'string\',
                        \'EndpointConfigArn\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1)
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
        
        """
        pass


class ListEndpoints(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, StatusEquals: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListEndpoints>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              SortBy=\'Name\'|\'CreationTime\'|\'Status\',
              SortOrder=\'Ascending\'|\'Descending\',
              NameContains=\'string\',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              StatusEquals=\'OutOfService\'|\'Creating\'|\'Updating\'|\'SystemUpdating\'|\'RollingBack\'|\'InService\'|\'Deleting\'|\'Failed\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Endpoints\': [
                    {
                        \'EndpointName\': \'string\',
                        \'EndpointArn\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'LastModifiedTime\': datetime(2015, 1, 1),
                        \'EndpointStatus\': \'OutOfService\'|\'Creating\'|\'Updating\'|\'SystemUpdating\'|\'RollingBack\'|\'InService\'|\'Deleting\'|\'Failed\'
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
        
        """
        pass


class ListModels(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListModels>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              SortBy=\'Name\'|\'CreationTime\',
              SortOrder=\'Ascending\'|\'Descending\',
              NameContains=\'string\',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1),
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Models\': [
                    {
                        \'ModelName\': \'string\',
                        \'ModelArn\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1)
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
        
        """
        pass


class ListNotebookInstances(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, StatusEquals: str = None, NotebookInstanceLifecycleConfigNameContains: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListNotebookInstances>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              SortBy=\'Name\'|\'CreationTime\'|\'Status\',
              SortOrder=\'Ascending\'|\'Descending\',
              NameContains=\'string\',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              StatusEquals=\'Pending\'|\'InService\'|\'Stopping\'|\'Stopped\'|\'Failed\'|\'Deleting\'|\'Updating\',
              NotebookInstanceLifecycleConfigNameContains=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'NotebookInstances\': [
                    {
                        \'NotebookInstanceName\': \'string\',
                        \'NotebookInstanceArn\': \'string\',
                        \'NotebookInstanceStatus\': \'Pending\'|\'InService\'|\'Stopping\'|\'Stopped\'|\'Failed\'|\'Deleting\'|\'Updating\',
                        \'Url\': \'string\',
                        \'InstanceType\': \'ml.t2.medium\'|\'ml.t2.large\'|\'ml.t2.xlarge\'|\'ml.t2.2xlarge\'|\'ml.m4.xlarge\'|\'ml.m4.2xlarge\'|\'ml.m4.4xlarge\'|\'ml.m4.10xlarge\'|\'ml.m4.16xlarge\'|\'ml.p2.xlarge\'|\'ml.p2.8xlarge\'|\'ml.p2.16xlarge\'|\'ml.p3.2xlarge\'|\'ml.p3.8xlarge\'|\'ml.p3.16xlarge\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'LastModifiedTime\': datetime(2015, 1, 1),
                        \'NotebookInstanceLifecycleConfigName\': \'string\'
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
        
        """
        pass


class ListTags(Paginator):
    def paginate(self, ResourceArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTags>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ResourceArn=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Tags\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
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
        
        """
        pass


class ListTrainingJobs(Paginator):
    def paginate(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTrainingJobs>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              NameContains=\'string\',
              StatusEquals=\'InProgress\'|\'Completed\'|\'Failed\'|\'Stopping\'|\'Stopped\',
              SortBy=\'Name\'|\'CreationTime\'|\'Status\',
              SortOrder=\'Ascending\'|\'Descending\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'TrainingJobSummaries\': [
                    {
                        \'TrainingJobName\': \'string\',
                        \'TrainingJobArn\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'TrainingEndTime\': datetime(2015, 1, 1),
                        \'LastModifiedTime\': datetime(2015, 1, 1),
                        \'TrainingJobStatus\': \'InProgress\'|\'Completed\'|\'Failed\'|\'Stopping\'|\'Stopped\'
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
        
        """
        pass
