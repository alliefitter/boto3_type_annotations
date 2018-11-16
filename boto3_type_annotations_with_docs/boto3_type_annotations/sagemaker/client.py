from datetime import datetime
from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def add_tags(self, ResourceArn: str, Tags: List) -> Dict:
        """
        
        Each tag consists of a key and an optional value. Tag keys must be unique per resource. For more information about tags, see For more information, see `AWS Tagging Strategies <https://aws.amazon.com/answers/account-management/aws-tagging-strategies/>`__ .
        
        .. note::
        
          Tags that you add to a hyperparameter tuning job by calling this API are also added to any training jobs that the hyperparameter tuning job launches after you call this API, but not to training jobs that the hyperparameter tuning job launched before you called this API. To make sure that the tags associated with a hyperparameter tuning job are also added to all training jobs that the hyperparameter tuning job launches, add the tags when you first create the tuning job by specifying them in the ``Tags`` parameter of  CreateHyperParameterTuningJob  
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/AddTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.add_tags(
              ResourceArn=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the resource that you want to tag.
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          An array of ``Tag`` objects. Each tag is a key-value pair. Only the ``key`` parameter is required. If you don\'t specify a value, Amazon SageMaker sets the value to an empty string. 
        
          - *(dict) --* 
        
            Describes a tag. 
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The tag key.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The tag value.
        
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
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Tags** *(list) --* 
        
              A list of tags associated with the Amazon SageMaker resource.
        
              - *(dict) --* 
        
                Describes a tag. 
        
                - **Key** *(string) --* 
        
                  The tag key.
        
                - **Value** *(string) --* 
        
                  The tag value.
        
        """
        pass

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

    def create_endpoint(self, EndpointName: str, EndpointConfigName: str, Tags: List = None) -> Dict:
        """
        
        .. note::
        
          Use this API only for hosting models using Amazon SageMaker hosting services. 
        
        The endpoint name must be unique within an AWS Region in your AWS account. 
        
        When it receives the request, Amazon SageMaker creates the endpoint, launches the resources (ML compute instances), and deploys the model(s) on them. 
        
        When Amazon SageMaker receives the request, it sets the endpoint status to ``Creating`` . After it creates the endpoint, it sets the status to ``InService`` . Amazon SageMaker can then process incoming requests for inferences. To check the status of an endpoint, use the `DescribeEndpoint <http://docs.aws.amazon.com/sagemaker/latest/dg/API_DescribeEndpoint.html>`__ API.
        
        For an example, see `Exercise 1\: Using the K-Means Algorithm Provided by Amazon SageMaker <http://docs.aws.amazon.com/sagemaker/latest/dg/ex1.html>`__ . 
        
        If any of the models hosted at this endpoint get model data from an Amazon S3 location, Amazon SageMaker uses AWS Security Token Service to download model artifacts from the S3 path you provided. AWS STS is activated in your IAM user account by default. If you previously deactivated AWS STS for a region, you need to reactivate AWS STS for that region. For more information, see `Activating and Deactivating AWS STS i an AWS Region <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html>`__ in the *AWS Identity and Access Management User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateEndpoint>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_endpoint(
              EndpointName=\'string\',
              EndpointConfigName=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type EndpointName: string
        :param EndpointName: **[REQUIRED]** 
        
          The name of the endpoint. The name must be unique within an AWS Region in your AWS account.
        
        :type EndpointConfigName: string
        :param EndpointConfigName: **[REQUIRED]** 
        
          The name of an endpoint configuration. For more information, see `CreateEndpointConfig <http://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpointConfig.html>`__ . 
        
        :type Tags: list
        :param Tags: 
        
          An array of key-value pairs. For more information, see `Using Cost Allocation Tags <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what>`__ in the *AWS Billing and Cost Management User Guide* . 
        
          - *(dict) --* 
        
            Describes a tag. 
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The tag key.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The tag value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EndpointArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **EndpointArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the endpoint.
        
        """
        pass

    def create_endpoint_config(self, EndpointConfigName: str, ProductionVariants: List, Tags: List = None, KmsKeyId: str = None) -> Dict:
        """
        
        .. note::
        
          Use this API only if you want to use Amazon SageMaker hosting services to deploy models into production. 
        
        In the request, you define one or more ``ProductionVariant`` s, each of which identifies a model. Each ``ProductionVariant`` parameter also describes the resources that you want Amazon SageMaker to provision. This includes the number and type of ML compute instances to deploy. 
        
        If you are hosting multiple models, you also assign a ``VariantWeight`` to specify how much traffic you want to allocate to each model. For example, suppose that you want to host two models, A and B, and you assign traffic weight 2 for model A and 1 for model B. Amazon SageMaker distributes two-thirds of the traffic to Model A, and one-third to model B. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateEndpointConfig>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_endpoint_config(
              EndpointConfigName=\'string\',
              ProductionVariants=[
                  {
                      \'VariantName\': \'string\',
                      \'ModelName\': \'string\',
                      \'InitialInstanceCount\': 123,
                      \'InstanceType\': \'ml.t2.medium\'|\'ml.t2.large\'|\'ml.t2.xlarge\'|\'ml.t2.2xlarge\'|\'ml.m4.xlarge\'|\'ml.m4.2xlarge\'|\'ml.m4.4xlarge\'|\'ml.m4.10xlarge\'|\'ml.m4.16xlarge\'|\'ml.m5.large\'|\'ml.m5.xlarge\'|\'ml.m5.2xlarge\'|\'ml.m5.4xlarge\'|\'ml.m5.12xlarge\'|\'ml.m5.24xlarge\'|\'ml.c4.large\'|\'ml.c4.xlarge\'|\'ml.c4.2xlarge\'|\'ml.c4.4xlarge\'|\'ml.c4.8xlarge\'|\'ml.p2.xlarge\'|\'ml.p2.8xlarge\'|\'ml.p2.16xlarge\'|\'ml.p3.2xlarge\'|\'ml.p3.8xlarge\'|\'ml.p3.16xlarge\'|\'ml.c5.large\'|\'ml.c5.xlarge\'|\'ml.c5.2xlarge\'|\'ml.c5.4xlarge\'|\'ml.c5.9xlarge\'|\'ml.c5.18xlarge\',
                      \'InitialVariantWeight\': ...
                  },
              ],
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              KmsKeyId=\'string\'
          )
        :type EndpointConfigName: string
        :param EndpointConfigName: **[REQUIRED]** 
        
          The name of the endpoint configuration. You specify this name in a `CreateEndpoint <http://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html>`__ request. 
        
        :type ProductionVariants: list
        :param ProductionVariants: **[REQUIRED]** 
        
          An array of ``ProductionVariant`` objects, one for each model that you want to host at this endpoint.
        
          - *(dict) --* 
        
            Identifies a model that you want to host and the resources to deploy for hosting it. If you are deploying multiple models, tell Amazon SageMaker how to distribute traffic among the models by specifying variant weights. 
        
            - **VariantName** *(string) --* **[REQUIRED]** 
        
              The name of the production variant.
        
            - **ModelName** *(string) --* **[REQUIRED]** 
        
              The name of the model that you want to host. This is the name that you specified when creating the model.
        
            - **InitialInstanceCount** *(integer) --* **[REQUIRED]** 
        
              Number of instances to launch initially.
        
            - **InstanceType** *(string) --* **[REQUIRED]** 
        
              The ML compute instance type.
        
            - **InitialVariantWeight** *(float) --* 
        
              Determines initial traffic distribution among all of the models that you specify in the endpoint configuration. The traffic to a production variant is determined by the ratio of the ``VariantWeight`` to the sum of all ``VariantWeight`` values across all ProductionVariants. If unspecified, it defaults to 1.0. 
        
        :type Tags: list
        :param Tags: 
        
          An array of key-value pairs. For more information, see `Using Cost Allocation Tags <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what>`__ in the *AWS Billing and Cost Management User Guide* . 
        
          - *(dict) --* 
        
            Describes a tag. 
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The tag key.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The tag value.
        
        :type KmsKeyId: string
        :param KmsKeyId: 
        
          The Amazon Resource Name (ARN) of a AWS Key Management Service key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EndpointConfigArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **EndpointConfigArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the endpoint configuration. 
        
        """
        pass

    def create_hyper_parameter_tuning_job(self, HyperParameterTuningJobName: str, HyperParameterTuningJobConfig: Dict, TrainingJobDefinition: Dict, Tags: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateHyperParameterTuningJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_hyper_parameter_tuning_job(
              HyperParameterTuningJobName=\'string\',
              HyperParameterTuningJobConfig={
                  \'Strategy\': \'Bayesian\',
                  \'HyperParameterTuningJobObjective\': {
                      \'Type\': \'Maximize\'|\'Minimize\',
                      \'MetricName\': \'string\'
                  },
                  \'ResourceLimits\': {
                      \'MaxNumberOfTrainingJobs\': 123,
                      \'MaxParallelTrainingJobs\': 123
                  },
                  \'ParameterRanges\': {
                      \'IntegerParameterRanges\': [
                          {
                              \'Name\': \'string\',
                              \'MinValue\': \'string\',
                              \'MaxValue\': \'string\'
                          },
                      ],
                      \'ContinuousParameterRanges\': [
                          {
                              \'Name\': \'string\',
                              \'MinValue\': \'string\',
                              \'MaxValue\': \'string\'
                          },
                      ],
                      \'CategoricalParameterRanges\': [
                          {
                              \'Name\': \'string\',
                              \'Values\': [
                                  \'string\',
                              ]
                          },
                      ]
                  }
              },
              TrainingJobDefinition={
                  \'StaticHyperParameters\': {
                      \'string\': \'string\'
                  },
                  \'AlgorithmSpecification\': {
                      \'TrainingImage\': \'string\',
                      \'TrainingInputMode\': \'Pipe\'|\'File\',
                      \'MetricDefinitions\': [
                          {
                              \'Name\': \'string\',
                              \'Regex\': \'string\'
                          },
                      ]
                  },
                  \'RoleArn\': \'string\',
                  \'InputDataConfig\': [
                      {
                          \'ChannelName\': \'string\',
                          \'DataSource\': {
                              \'S3DataSource\': {
                                  \'S3DataType\': \'ManifestFile\'|\'S3Prefix\',
                                  \'S3Uri\': \'string\',
                                  \'S3DataDistributionType\': \'FullyReplicated\'|\'ShardedByS3Key\'
                              }
                          },
                          \'ContentType\': \'string\',
                          \'CompressionType\': \'None\'|\'Gzip\',
                          \'RecordWrapperType\': \'None\'|\'RecordIO\',
                          \'InputMode\': \'Pipe\'|\'File\'
                      },
                  ],
                  \'VpcConfig\': {
                      \'SecurityGroupIds\': [
                          \'string\',
                      ],
                      \'Subnets\': [
                          \'string\',
                      ]
                  },
                  \'OutputDataConfig\': {
                      \'KmsKeyId\': \'string\',
                      \'S3OutputPath\': \'string\'
                  },
                  \'ResourceConfig\': {
                      \'InstanceType\': \'ml.m4.xlarge\'|\'ml.m4.2xlarge\'|\'ml.m4.4xlarge\'|\'ml.m4.10xlarge\'|\'ml.m4.16xlarge\'|\'ml.m5.large\'|\'ml.m5.xlarge\'|\'ml.m5.2xlarge\'|\'ml.m5.4xlarge\'|\'ml.m5.12xlarge\'|\'ml.m5.24xlarge\'|\'ml.c4.xlarge\'|\'ml.c4.2xlarge\'|\'ml.c4.4xlarge\'|\'ml.c4.8xlarge\'|\'ml.p2.xlarge\'|\'ml.p2.8xlarge\'|\'ml.p2.16xlarge\'|\'ml.p3.2xlarge\'|\'ml.p3.8xlarge\'|\'ml.p3.16xlarge\'|\'ml.c5.xlarge\'|\'ml.c5.2xlarge\'|\'ml.c5.4xlarge\'|\'ml.c5.9xlarge\'|\'ml.c5.18xlarge\',
                      \'InstanceCount\': 123,
                      \'VolumeSizeInGB\': 123,
                      \'VolumeKmsKeyId\': \'string\'
                  },
                  \'StoppingCondition\': {
                      \'MaxRuntimeInSeconds\': 123
                  }
              },
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type HyperParameterTuningJobName: string
        :param HyperParameterTuningJobName: **[REQUIRED]** 
        
          The name of the tuning job. This name is the prefix for the names of all training jobs that this tuning job launches. The name must be unique within the same AWS account and AWS Region. Names are not case sensitive, and must be between 1-32 characters.
        
        :type HyperParameterTuningJobConfig: dict
        :param HyperParameterTuningJobConfig: **[REQUIRED]** 
        
          The  HyperParameterTuningJobConfig object that describes the tuning job, including the search strategy, metric used to evaluate training jobs, ranges of parameters to search, and resource limits for the tuning job.
        
          - **Strategy** *(string) --* **[REQUIRED]** 
        
            Specifies the search strategy for hyperparameters. Currently, the only valid value is ``Bayesian`` .
        
          - **HyperParameterTuningJobObjective** *(dict) --* **[REQUIRED]** 
        
            The  HyperParameterTuningJobObjective object that specifies the objective metric for this tuning job.
        
            - **Type** *(string) --* **[REQUIRED]** 
        
              Whether to minimize or maximize the objective metric.
        
            - **MetricName** *(string) --* **[REQUIRED]** 
        
              The name of the metric to use for the objective metric.
        
          - **ResourceLimits** *(dict) --* **[REQUIRED]** 
        
            The  ResourceLimits object that specifies the maximum number of training jobs and parallel training jobs for this tuning job.
        
            - **MaxNumberOfTrainingJobs** *(integer) --* **[REQUIRED]** 
        
              The maximum number of training jobs that a hyperparameter tuning job can launch.
        
            - **MaxParallelTrainingJobs** *(integer) --* **[REQUIRED]** 
        
              The maximum number of concurrent training jobs that a hyperparameter tuning job can launch.
        
          - **ParameterRanges** *(dict) --* **[REQUIRED]** 
        
            The  ParameterRanges object that specifies the ranges of hyperparameters that this tuning job searches.
        
            - **IntegerParameterRanges** *(list) --* 
        
              The array of  IntegerParameterRange objects that specify ranges of integer hyperparameters that a hyperparameter tuning job searches.
        
              - *(dict) --* 
        
                For a hyperparameter of the integer type, specifies the range that a hyperparameter tuning job searches.
        
                - **Name** *(string) --* **[REQUIRED]** 
        
                  The name of the hyperparameter to search.
        
                - **MinValue** *(string) --* **[REQUIRED]** 
        
                  The minimum value of the hyperparameter to search.
        
                - **MaxValue** *(string) --* **[REQUIRED]** 
        
                  The maximum value of the hyperparameter to search.
        
            - **ContinuousParameterRanges** *(list) --* 
        
              The array of  ContinuousParameterRange objects that specify ranges of continuous hyperparameters that a hyperparameter tuning job searches.
        
              - *(dict) --* 
        
                A list of continuous hyperparameters to tune.
        
                - **Name** *(string) --* **[REQUIRED]** 
        
                  The name of the continuous hyperparameter to tune.
        
                - **MinValue** *(string) --* **[REQUIRED]** 
        
                  The minimum value for the hyperparameter. The tuning job uses floating-point values between this value and ``MaxValue`` for tuning.
        
                - **MaxValue** *(string) --* **[REQUIRED]** 
        
                  The maximum value for the hyperparameter. The tuning job uses floating-point values between ``MinValue`` value and this value for tuning.
        
            - **CategoricalParameterRanges** *(list) --* 
        
              The array of  CategoricalParameterRange objects that specify ranges of categorical hyperparameters that a hyperparameter tuning job searches.
        
              - *(dict) --* 
        
                A list of categorical hyperparameters to tune.
        
                - **Name** *(string) --* **[REQUIRED]** 
        
                  The name of the categorical hyperparameter to tune.
        
                - **Values** *(list) --* **[REQUIRED]** 
        
                  A list of the categories for the hyperparameter.
        
                  - *(string) --* 
        
        :type TrainingJobDefinition: dict
        :param TrainingJobDefinition: **[REQUIRED]** 
        
          The  HyperParameterTrainingJobDefinition object that describes the training jobs that this tuning job launches, including static hyperparameters, input data configuration, output data configuration, resource configuration, and stopping condition.
        
          - **StaticHyperParameters** *(dict) --* 
        
            Specifies the values of hyperparameters that do not change for the tuning job.
        
            - *(string) --* 
        
              - *(string) --* 
        
          - **AlgorithmSpecification** *(dict) --* **[REQUIRED]** 
        
            The  HyperParameterAlgorithmSpecification object that specifies the algorithm to use for the training jobs that the tuning job launches.
        
            - **TrainingImage** *(string) --* **[REQUIRED]** 
        
              The registry path of the Docker image that contains the training algorithm. For information about Docker registry paths for built-in algorithms, see `Algorithms Provided by Amazon SageMaker\: Common Parameters <http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html>`__ .
        
            - **TrainingInputMode** *(string) --* **[REQUIRED]** 
        
              The input mode that the algorithm supports: File or Pipe. In File input mode, Amazon SageMaker downloads the training data from Amazon S3 to the storage volume that is attached to the training instance and mounts the directory to the Docker volume for the training container. In Pipe input mode, Amazon SageMaker streams data directly from Amazon S3 to the container. 
        
              If you specify File mode, make sure that you provision the storage volume that is attached to the training instance with enough capacity to accommodate the training data downloaded from Amazon S3, the model artifacts, and intermediate information.
        
              For more information about input modes, see `Algorithms <http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ . 
        
            - **MetricDefinitions** *(list) --* 
        
              An array of  MetricDefinition objects that specify the metrics that the algorithm emits.
        
              - *(dict) --* 
        
                Specifies a metric that the training algorithm writes to ``stderr`` or ``stdout`` . Amazon SageMakerhyperparameter tuning captures all defined metrics. You specify one metric that a hyperparameter tuning job uses as its objective metric to choose the best training job.
        
                - **Name** *(string) --* **[REQUIRED]** 
        
                  The name of the metric.
        
                - **Regex** *(string) --* **[REQUIRED]** 
        
                  A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see `Defining Objective Metrics <http://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics.html>`__ .
        
          - **RoleArn** *(string) --* **[REQUIRED]** 
        
            The Amazon Resource Name (ARN) of the IAM role associated with the training jobs that the tuning job launches.
        
          - **InputDataConfig** *(list) --* **[REQUIRED]** 
        
            An array of  Channel objects that specify the input for the training jobs that the tuning job launches.
        
            - *(dict) --* 
        
              A channel is a named input source that training algorithms can consume. 
        
              - **ChannelName** *(string) --* **[REQUIRED]** 
        
                The name of the channel. 
        
              - **DataSource** *(dict) --* **[REQUIRED]** 
        
                The location of the channel data.
        
                - **S3DataSource** *(dict) --* **[REQUIRED]** 
        
                  The S3 location of the data source that is associated with a channel.
        
                  - **S3DataType** *(string) --* **[REQUIRED]** 
        
                    If you choose ``S3Prefix`` , ``S3Uri`` identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for model training. 
        
                    If you choose ``ManifestFile`` , ``S3Uri`` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for model training. 
        
                  - **S3Uri** *(string) --* **[REQUIRED]** 
        
                    Depending on the value specified for the ``S3DataType`` , identifies either a key name prefix or a manifest. For example: 
        
                    * A key name prefix might look like this: ``s3://bucketname/exampleprefix`` .  
                     
                    * A manifest might look like this: ``s3://bucketname/example.manifest``   The manifest is an S3 object which is a JSON file with the following format:   ``[``    ``{\"prefix\": \"s3://customer_bucket/some/prefix/\"},``    ``\"relative/path/to/custdata-1\",``    ``\"relative/path/custdata-2\",``    ``...``    ``]``   The preceding JSON matches the following ``s3Uris`` :   ``s3://customer_bucket/some/prefix/relative/path/to/custdata-1``    ``s3://customer_bucket/some/prefix/relative/path/custdata-1``    ``...``   The complete set of ``s3uris`` in this manifest constitutes the input data for the channel for this datasource. The object that each ``s3uris`` points to must readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.  
                     
                  - **S3DataDistributionType** *(string) --* 
        
                    If you want Amazon SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify ``FullyReplicated`` . 
        
                    If you want Amazon SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify ``ShardedByS3Key`` . If there are *n* ML compute instances launched for a training job, each instance gets approximately 1/*n* of the number of S3 objects. In this case, model training on each machine uses only the subset of training data. 
        
                    Don\'t choose more ML compute instances for training than available S3 objects. If you do, some nodes won\'t get any data and you will pay for nodes that aren\'t getting any training data. This applies in both FILE and PIPE modes. Keep this in mind when developing algorithms. 
        
                    In distributed training, where you use multiple ML compute EC2 instances, you might choose ``ShardedByS3Key`` . If the algorithm requires copying training data to the ML storage volume (when ``TrainingInputMode`` is set to ``File`` ), this copies 1/*n* of the number of objects. 
        
              - **ContentType** *(string) --* 
        
                The MIME type of the data.
        
              - **CompressionType** *(string) --* 
        
                If training data is compressed, the compression type. The default value is ``None`` . ``CompressionType`` is used only in Pipe input mode. In File mode, leave this field unset or set it to None.
        
              - **RecordWrapperType** *(string) --* 
        
                Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format, in which case, Amazon SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you don\'t need to set this attribute. For more information, see `Create a Dataset Using RecordIO <https://mxnet.incubator.apache.org/architecture/note_data_loading.html#data-format>`__ . 
        
                In FILE mode, leave this field unset or set it to None.
        
              - **InputMode** *(string) --* 
        
          - **VpcConfig** *(dict) --* 
        
            The  VpcConfig object that specifies the VPC that you want the training jobs that this hyperparameter tuning job launches to connect to. Control access to and from your training container by configuring the VPC. For more information, see `Protect Training Jobs by Using an Amazon Virtual Private Cloud <http://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html>`__ .
        
            - **SecurityGroupIds** *(list) --* **[REQUIRED]** 
        
              The VPC security group IDs, in the form sg-xxxxxxxx. Specify the security groups for the VPC that is specified in the ``Subnets`` field.
        
              - *(string) --* 
        
            - **Subnets** *(list) --* **[REQUIRED]** 
        
              The ID of the subnets in the VPC to which you want to connect your training job or model. 
        
              - *(string) --* 
        
          - **OutputDataConfig** *(dict) --* **[REQUIRED]** 
        
            Specifies the path to the Amazon S3 bucket where you store model artifacts from the training jobs that the tuning job launches.
        
            - **KmsKeyId** *(string) --* 
        
              The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The ``KmsKeyId`` can be any of the following formats: 
        
              * // KMS Key ID  ``\"1234abcd-12ab-34cd-56ef-1234567890ab\"``   
               
              * // Amazon Resource Name (ARN) of a KMS Key  ``\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"``   
               
              * // KMS Key Alias  ``\"alias/ExampleAlias\"``   
               
              * // Amazon Resource Name (ARN) of a KMS Key Alias  ``\"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias\"``   
               
              If you don\'t provide the KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role\'s account. For more information, see `KMS-Managed Encryption Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ in *Amazon Simple Storage Service Developer Guide.*  
        
              .. note::
        
                The KMS key policy must grant permission to the IAM role that you specify in your ``CreateTrainingJob`` request. `Using Key Policies in AWS KMS <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the *AWS Key Management Service Developer Guide* . 
        
            - **S3OutputPath** *(string) --* **[REQUIRED]** 
        
              Identifies the S3 path where you want Amazon SageMaker to store the model artifacts. For example, ``s3://bucket-name/key-name-prefix`` . 
        
          - **ResourceConfig** *(dict) --* **[REQUIRED]** 
        
            The resources, including the compute instances and storage volumes, to use for the training jobs that the tuning job launches.
        
            Storage volumes store model artifacts and incremental states. Training algorithms might also use storage volumes for scratch space. If you want Amazon SageMaker to use the storage volume to store the training data, choose ``File`` as the ``TrainingInputMode`` in the algorithm specification. For distributed training algorithms, specify an instance count greater than 1.
        
            - **InstanceType** *(string) --* **[REQUIRED]** 
        
              The ML compute instance type. 
        
            - **InstanceCount** *(integer) --* **[REQUIRED]** 
        
              The number of ML compute instances to use. For distributed training, provide a value greater than 1. 
        
            - **VolumeSizeInGB** *(integer) --* **[REQUIRED]** 
        
              The size of the ML storage volume that you want to provision. 
        
              ML storage volumes store model artifacts and incremental states. Training algorithms might also use the ML storage volume for scratch space. If you want to store the training data in the ML storage volume, choose ``File`` as the ``TrainingInputMode`` in the algorithm specification. 
        
              You must specify sufficient ML storage for your scenario. 
        
              .. note::
        
                Amazon SageMaker supports only the General Purpose SSD (gp2) ML storage volume type. 
        
            - **VolumeKmsKeyId** *(string) --* 
        
              The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the training job. The ``VolumeKmsKeyId`` can be any of the following formats:
        
              * // KMS Key ID  ``\"1234abcd-12ab-34cd-56ef-1234567890ab\"``   
               
              * // Amazon Resource Name (ARN) of a KMS Key  ``\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"``   
               
          - **StoppingCondition** *(dict) --* **[REQUIRED]** 
        
            Sets a maximum duration for the training jobs that the tuning job launches. Use this parameter to limit model training costs. 
        
            To stop a job, Amazon SageMaker sends the algorithm the ``SIGTERM`` signal. This delays job termination for 120 seconds. Algorithms might use this 120-second window to save the model artifacts.
        
            When Amazon SageMaker terminates a job because the stopping condition has been met, training algorithms provided by Amazon SageMaker save the intermediate results of the job.
        
            - **MaxRuntimeInSeconds** *(integer) --* 
        
              The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 5 days.
        
        :type Tags: list
        :param Tags: 
        
          An array of key-value pairs. You can use tags to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. For more information, see `AWS Tagging Strategies <https://aws.amazon.com/answers/account-management/aws-tagging-strategies/>`__ .
        
          Tags that you specify for the tuning job are also added to all training jobs that the tuning job launches.
        
          - *(dict) --* 
        
            Describes a tag. 
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The tag key.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The tag value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'HyperParameterTuningJobArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **HyperParameterTuningJobArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the tuning job.
        
        """
        pass

    def create_model(self, ModelName: str, PrimaryContainer: Dict, ExecutionRoleArn: str, Tags: List = None, VpcConfig: Dict = None) -> Dict:
        """
        
        Use this API to create a model if you want to use Amazon SageMaker hosting services or run a batch transform job.
        
        To host your model, you create an endpoint configuration with the ``CreateEndpointConfig`` API, and then create an endpoint with the ``CreateEndpoint`` API. Amazon SageMaker then deploys all of the containers that you defined for the model in the hosting environment. 
        
        To run a batch transform using your model, you start a job with the ``CreateTransformJob`` API. Amazon SageMaker uses your model and your dataset to get inferences which are then saved to a specified S3 location.
        
        In the ``CreateModel`` request, you must define a container with the ``PrimaryContainer`` parameter.
        
        In the request, you also provide an IAM role that Amazon SageMaker can assume to access model artifacts and docker image for deployment on ML compute hosting instances or for batch transform jobs. In addition, you also use the IAM role to manage permissions the inference code needs. For example, if the inference code access any other AWS resources, you grant necessary permissions via this role.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateModel>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_model(
              ModelName=\'string\',
              PrimaryContainer={
                  \'ContainerHostname\': \'string\',
                  \'Image\': \'string\',
                  \'ModelDataUrl\': \'string\',
                  \'Environment\': {
                      \'string\': \'string\'
                  }
              },
              ExecutionRoleArn=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              VpcConfig={
                  \'SecurityGroupIds\': [
                      \'string\',
                  ],
                  \'Subnets\': [
                      \'string\',
                  ]
              }
          )
        :type ModelName: string
        :param ModelName: **[REQUIRED]** 
        
          The name of the new model.
        
        :type PrimaryContainer: dict
        :param PrimaryContainer: **[REQUIRED]** 
        
          The location of the primary docker image containing inference code, associated artifacts, and custom environment map that the inference code uses when the model is deployed for predictions. 
        
          - **ContainerHostname** *(string) --* 
        
            The DNS host name for the container after Amazon SageMaker deploys it.
        
          - **Image** *(string) --* **[REQUIRED]** 
        
            The Amazon EC2 Container Registry (Amazon ECR) path where inference code is stored. If you are using your own custom algorithm instead of an algorithm provided by Amazon SageMaker, the inference code must meet Amazon SageMaker requirements. Amazon SageMaker supports both ``registry/repository[:tag]`` and ``registry/repository[@digest]`` image path formats. For more information, see `Using Your Own Algorithms with Amazon SageMaker <http://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__  
        
          - **ModelDataUrl** *(string) --* 
        
            The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix). 
        
            If you provide a value for this parameter, Amazon SageMaker uses AWS Security Token Service to download model artifacts from the S3 path you provide. AWS STS is activated in your IAM user account by default. If you previously deactivated AWS STS for a region, you need to reactivate AWS STS for that region. For more information, see `Activating and Deactivating AWS STS i an AWS Region <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html>`__ in the *AWS Identity and Access Management User Guide* .
        
          - **Environment** *(dict) --* 
        
            The environment variables to set in the Docker container. Each key and value in the ``Environment`` string to string map can have length of up to 1024. We support up to 16 entries in the map. 
        
            - *(string) --* 
        
              - *(string) --* 
        
        :type ExecutionRoleArn: string
        :param ExecutionRoleArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker can assume to access model artifacts and docker image for deployment on ML compute instances or for batch transform jobs. Deploying on ML compute instances is part of model hosting. For more information, see `Amazon SageMaker Roles <http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html>`__ . 
        
          .. note::
        
            To be able to pass this role to Amazon SageMaker, the caller of this API must have the ``iam:PassRole`` permission.
        
        :type Tags: list
        :param Tags: 
        
          An array of key-value pairs. For more information, see `Using Cost Allocation Tags <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what>`__ in the *AWS Billing and Cost Management User Guide* . 
        
          - *(dict) --* 
        
            Describes a tag. 
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The tag key.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The tag value.
        
        :type VpcConfig: dict
        :param VpcConfig: 
        
          A  VpcConfig object that specifies the VPC that you want your model to connect to. Control access to and from your model container by configuring the VPC. ``VpcConfig`` is used in hosting services and in batch transform. For more information, see `Protect Endpoints by Using an Amazon Virtual Private Cloud <http://docs.aws.amazon.com/sagemaker/latest/dg/host-vpc.html>`__ and `Protect Data in Batch Transform Jobs by Using an Amazon Virtual Private Cloud <http://docs.aws.amazon.com/sagemaker/latest/dg/batch-vpc.html>`__ .
        
          - **SecurityGroupIds** *(list) --* **[REQUIRED]** 
        
            The VPC security group IDs, in the form sg-xxxxxxxx. Specify the security groups for the VPC that is specified in the ``Subnets`` field.
        
            - *(string) --* 
        
          - **Subnets** *(list) --* **[REQUIRED]** 
        
            The ID of the subnets in the VPC to which you want to connect your training job or model. 
        
            - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ModelArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ModelArn** *(string) --* 
        
              The ARN of the model created in Amazon SageMaker.
        
        """
        pass

    def create_notebook_instance(self, NotebookInstanceName: str, InstanceType: str, RoleArn: str, SubnetId: str = None, SecurityGroupIds: List = None, KmsKeyId: str = None, Tags: List = None, LifecycleConfigName: str = None, DirectInternetAccess: str = None, VolumeSizeInGB: int = None) -> Dict:
        """
        
        In a ``CreateNotebookInstance`` request, specify the type of ML compute instance that you want to run. Amazon SageMaker launches the instance, installs common libraries that you can use to explore datasets for model training, and attaches an ML storage volume to the notebook instance. 
        
        Amazon SageMaker also provides a set of example notebooks. Each notebook demonstrates how to use Amazon SageMaker with a specific algorithm or with a machine learning framework. 
        
        After receiving the request, Amazon SageMaker does the following:
        
        * Creates a network interface in the Amazon SageMaker VPC. 
         
        * (Option) If you specified ``SubnetId`` , Amazon SageMaker creates a network interface in your own VPC, which is inferred from the subnet ID that you provide in the input. When creating this network interface, Amazon SageMaker attaches the security group that you specified in the request to the network interface that it creates in your VPC. 
         
        * Launches an EC2 instance of the type specified in the request in the Amazon SageMaker VPC. If you specified ``SubnetId`` of your VPC, Amazon SageMaker specifies both network interfaces when launching this instance. This enables inbound traffic from your own VPC to the notebook instance, assuming that the security groups allow it. 
         
        After creating the notebook instance, Amazon SageMaker returns its Amazon Resource Name (ARN).
        
        After Amazon SageMaker creates the notebook instance, you can connect to the Jupyter server and work in Jupyter notebooks. For example, you can write code to explore a dataset that you can use for model training, train a model, host models by creating Amazon SageMaker endpoints, and validate hosted models. 
        
        For more information, see `How It Works <http://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html>`__ . 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateNotebookInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_notebook_instance(
              NotebookInstanceName=\'string\',
              InstanceType=\'ml.t2.medium\'|\'ml.t2.large\'|\'ml.t2.xlarge\'|\'ml.t2.2xlarge\'|\'ml.m4.xlarge\'|\'ml.m4.2xlarge\'|\'ml.m4.4xlarge\'|\'ml.m4.10xlarge\'|\'ml.m4.16xlarge\'|\'ml.p2.xlarge\'|\'ml.p2.8xlarge\'|\'ml.p2.16xlarge\'|\'ml.p3.2xlarge\'|\'ml.p3.8xlarge\'|\'ml.p3.16xlarge\',
              SubnetId=\'string\',
              SecurityGroupIds=[
                  \'string\',
              ],
              RoleArn=\'string\',
              KmsKeyId=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              LifecycleConfigName=\'string\',
              DirectInternetAccess=\'Enabled\'|\'Disabled\',
              VolumeSizeInGB=123
          )
        :type NotebookInstanceName: string
        :param NotebookInstanceName: **[REQUIRED]** 
        
          The name of the new notebook instance.
        
        :type InstanceType: string
        :param InstanceType: **[REQUIRED]** 
        
          The type of ML compute instance to launch for the notebook instance.
        
        :type SubnetId: string
        :param SubnetId: 
        
          The ID of the subnet in a VPC to which you would like to have a connectivity from your ML compute instance. 
        
        :type SecurityGroupIds: list
        :param SecurityGroupIds: 
        
          The VPC security group IDs, in the form sg-xxxxxxxx. The security groups must be for the same VPC as specified in the subnet. 
        
          - *(string) --* 
        
        :type RoleArn: string
        :param RoleArn: **[REQUIRED]** 
        
          When you send any requests to AWS resources from the notebook instance, Amazon SageMaker assumes this role to perform tasks on your behalf. You must grant this role necessary permissions so Amazon SageMaker can perform these tasks. The policy must allow the Amazon SageMaker service principal (sagemaker.amazonaws.com) permissions to assume this role. For more information, see `Amazon SageMaker Roles <http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html>`__ . 
        
          .. note::
        
            To be able to pass this role to Amazon SageMaker, the caller of this API must have the ``iam:PassRole`` permission.
        
        :type KmsKeyId: string
        :param KmsKeyId: 
        
          If you provide a AWS KMS key ID, Amazon SageMaker uses it to encrypt data at rest on the ML storage volume that is attached to your notebook instance. 
        
        :type Tags: list
        :param Tags: 
        
          A list of tags to associate with the notebook instance. You can add tags later by using the ``CreateTags`` API.
        
          - *(dict) --* 
        
            Describes a tag. 
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The tag key.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The tag value.
        
        :type LifecycleConfigName: string
        :param LifecycleConfigName: 
        
          The name of a lifecycle configuration to associate with the notebook instance. For information about lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <http://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
        
        :type DirectInternetAccess: string
        :param DirectInternetAccess: 
        
          Sets whether Amazon SageMaker provides internet access to the notebook instance. If you set this to ``Disabled`` this notebook instance will be able to access resources only in your VPC, and will not be able to connect to Amazon SageMaker training and endpoint services unless your configure a NAT Gateway in your VPC.
        
          For more information, see `Notebook Instances Are Internet-Enabled by Default <http://docs.aws.amazon.com/sagemaker/latest/dg/appendix-additional-considerations.html#appendix-notebook-and-internet-access>`__ . You can set the value of this parameter to ``Disabled`` only if you set a value for the ``SubnetId`` parameter.
        
        :type VolumeSizeInGB: integer
        :param VolumeSizeInGB: 
        
          The size, in GB, of the ML storage volume to attach to the notebook instance.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NotebookInstanceArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NotebookInstanceArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the notebook instance. 
        
        """
        pass

    def create_notebook_instance_lifecycle_config(self, NotebookInstanceLifecycleConfigName: str, OnCreate: List = None, OnStart: List = None) -> Dict:
        """
        
        Each lifecycle configuration script has a limit of 16384 characters.
        
        The value of the ``$PATH`` environment variable that is available to both scripts is ``/sbin:bin:/usr/sbin:/usr/bin`` .
        
        View CloudWatch Logs for notebook instance lifecycle configurations in log group ``/aws/sagemaker/NotebookInstances`` in log stream ``[notebook-instance-name]/[LifecycleConfigHook]`` .
        
        Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for longer than 5 minutes, it fails and the notebook instance is not created or started.
        
        For information about notebook instance lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <http://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateNotebookInstanceLifecycleConfig>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_notebook_instance_lifecycle_config(
              NotebookInstanceLifecycleConfigName=\'string\',
              OnCreate=[
                  {
                      \'Content\': \'string\'
                  },
              ],
              OnStart=[
                  {
                      \'Content\': \'string\'
                  },
              ]
          )
        :type NotebookInstanceLifecycleConfigName: string
        :param NotebookInstanceLifecycleConfigName: **[REQUIRED]** 
        
          The name of the lifecycle configuration.
        
        :type OnCreate: list
        :param OnCreate: 
        
          A shell script that runs only once, when you create a notebook instance. The shell script must be a base64-encoded string.
        
          - *(dict) --* 
        
            Contains the notebook instance lifecycle configuration script.
        
            Each lifecycle configuration script has a limit of 16384 characters.
        
            The value of the ``$PATH`` environment variable that is available to both scripts is ``/sbin:bin:/usr/sbin:/usr/bin`` .
        
            View CloudWatch Logs for notebook instance lifecycle configurations in log group ``/aws/sagemaker/NotebookInstances`` in log stream ``[notebook-instance-name]/[LifecycleConfigHook]`` .
        
            Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for longer than 5 minutes, it fails and the notebook instance is not created or started.
        
            For information about notebook instance lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <http://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
        
            - **Content** *(string) --* 
        
              A base64-encoded string that contains a shell script for a notebook instance lifecycle configuration.
        
        :type OnStart: list
        :param OnStart: 
        
          A shell script that runs every time you start a notebook instance, including when you create the notebook instance. The shell script must be a base64-encoded string.
        
          - *(dict) --* 
        
            Contains the notebook instance lifecycle configuration script.
        
            Each lifecycle configuration script has a limit of 16384 characters.
        
            The value of the ``$PATH`` environment variable that is available to both scripts is ``/sbin:bin:/usr/sbin:/usr/bin`` .
        
            View CloudWatch Logs for notebook instance lifecycle configurations in log group ``/aws/sagemaker/NotebookInstances`` in log stream ``[notebook-instance-name]/[LifecycleConfigHook]`` .
        
            Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for longer than 5 minutes, it fails and the notebook instance is not created or started.
        
            For information about notebook instance lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <http://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
        
            - **Content** *(string) --* 
        
              A base64-encoded string that contains a shell script for a notebook instance lifecycle configuration.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NotebookInstanceLifecycleConfigArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NotebookInstanceLifecycleConfigArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the lifecycle configuration.
        
        """
        pass

    def create_presigned_notebook_instance_url(self, NotebookInstanceName: str, SessionExpirationDurationInSeconds: int = None) -> Dict:
        """
        
        You can restrict access to this API and to the URL that it returns to a list of IP addresses that you specify. To restrict access, attach an IAM policy that denies access to this API unless the call comes from an IP address in the specified list to every AWS Identity and Access Management user, group, or role used to access the notebook instance. Use the ``NotIpAddress`` condition operator and the ``aws:SourceIP`` condition context key to specify the list of IP addresses that you want to have access to the notebook instance. For more information, see `Limit Access to a Notebook Instance by IP Address <http://docs.aws.amazon.com/https:/docs.aws.amazon.com/sagemaker/latest/dg/howitworks-access-ws.html#nbi-ip-filter>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreatePresignedNotebookInstanceUrl>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_presigned_notebook_instance_url(
              NotebookInstanceName=\'string\',
              SessionExpirationDurationInSeconds=123
          )
        :type NotebookInstanceName: string
        :param NotebookInstanceName: **[REQUIRED]** 
        
          The name of the notebook instance.
        
        :type SessionExpirationDurationInSeconds: integer
        :param SessionExpirationDurationInSeconds: 
        
          The duration of the session, in seconds. The default is 12 hours.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AuthorizedUrl\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AuthorizedUrl** *(string) --* 
        
              A JSON object that contains the URL string. 
        
        """
        pass

    def create_training_job(self, TrainingJobName: str, AlgorithmSpecification: Dict, RoleArn: str, OutputDataConfig: Dict, ResourceConfig: Dict, StoppingCondition: Dict, HyperParameters: Dict = None, InputDataConfig: List = None, VpcConfig: Dict = None, Tags: List = None) -> Dict:
        """
        
        If you choose to host your model using Amazon SageMaker hosting services, you can use the resulting model artifacts as part of the model. You can also use the artifacts in a deep learning service other than Amazon SageMaker, provided that you know how to use them for inferences. 
        
        In the request body, you provide the following: 
        
        * ``AlgorithmSpecification`` - Identifies the training algorithm to use.  
         
        * ``HyperParameters`` - Specify these algorithm-specific parameters to influence the quality of the final model. For a list of hyperparameters for each training algorithm provided by Amazon SageMaker, see `Algorithms <http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ .  
         
        * ``InputDataConfig`` - Describes the training dataset and the Amazon S3 location where it is stored. 
         
        * ``OutputDataConfig`` - Identifies the Amazon S3 location where you want Amazon SageMaker to save the results of model training.   
         
        * ``ResourceConfig`` - Identifies the resources, ML compute instances, and ML storage volumes to deploy for model training. In distributed training, you specify more than one instance.  
         
        * ``RoleARN`` - The Amazon Resource Number (ARN) that Amazon SageMaker assumes to perform tasks on your behalf during model training. You must grant this role the necessary permissions so that Amazon SageMaker can successfully complete model training.  
         
        * ``StoppingCondition`` - Sets a duration for training. Use this parameter to cap model training costs.  
         
        For more information about Amazon SageMaker, see `How It Works <http://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html>`__ . 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateTrainingJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_training_job(
              TrainingJobName=\'string\',
              HyperParameters={
                  \'string\': \'string\'
              },
              AlgorithmSpecification={
                  \'TrainingImage\': \'string\',
                  \'TrainingInputMode\': \'Pipe\'|\'File\'
              },
              RoleArn=\'string\',
              InputDataConfig=[
                  {
                      \'ChannelName\': \'string\',
                      \'DataSource\': {
                          \'S3DataSource\': {
                              \'S3DataType\': \'ManifestFile\'|\'S3Prefix\',
                              \'S3Uri\': \'string\',
                              \'S3DataDistributionType\': \'FullyReplicated\'|\'ShardedByS3Key\'
                          }
                      },
                      \'ContentType\': \'string\',
                      \'CompressionType\': \'None\'|\'Gzip\',
                      \'RecordWrapperType\': \'None\'|\'RecordIO\',
                      \'InputMode\': \'Pipe\'|\'File\'
                  },
              ],
              OutputDataConfig={
                  \'KmsKeyId\': \'string\',
                  \'S3OutputPath\': \'string\'
              },
              ResourceConfig={
                  \'InstanceType\': \'ml.m4.xlarge\'|\'ml.m4.2xlarge\'|\'ml.m4.4xlarge\'|\'ml.m4.10xlarge\'|\'ml.m4.16xlarge\'|\'ml.m5.large\'|\'ml.m5.xlarge\'|\'ml.m5.2xlarge\'|\'ml.m5.4xlarge\'|\'ml.m5.12xlarge\'|\'ml.m5.24xlarge\'|\'ml.c4.xlarge\'|\'ml.c4.2xlarge\'|\'ml.c4.4xlarge\'|\'ml.c4.8xlarge\'|\'ml.p2.xlarge\'|\'ml.p2.8xlarge\'|\'ml.p2.16xlarge\'|\'ml.p3.2xlarge\'|\'ml.p3.8xlarge\'|\'ml.p3.16xlarge\'|\'ml.c5.xlarge\'|\'ml.c5.2xlarge\'|\'ml.c5.4xlarge\'|\'ml.c5.9xlarge\'|\'ml.c5.18xlarge\',
                  \'InstanceCount\': 123,
                  \'VolumeSizeInGB\': 123,
                  \'VolumeKmsKeyId\': \'string\'
              },
              VpcConfig={
                  \'SecurityGroupIds\': [
                      \'string\',
                  ],
                  \'Subnets\': [
                      \'string\',
                  ]
              },
              StoppingCondition={
                  \'MaxRuntimeInSeconds\': 123
              },
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type TrainingJobName: string
        :param TrainingJobName: **[REQUIRED]** 
        
          The name of the training job. The name must be unique within an AWS Region in an AWS account. 
        
        :type HyperParameters: dict
        :param HyperParameters: 
        
          Algorithm-specific parameters that influence the quality of the model. You set hyperparameters before you start the learning process. For a list of hyperparameters for each training algorithm provided by Amazon SageMaker, see `Algorithms <http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ . 
        
          You can specify a maximum of 100 hyperparameters. Each hyperparameter is a key-value pair. Each key and value is limited to 256 characters, as specified by the ``Length Constraint`` . 
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type AlgorithmSpecification: dict
        :param AlgorithmSpecification: **[REQUIRED]** 
        
          The registry path of the Docker image that contains the training algorithm and algorithm-specific metadata, including the input mode. For more information about algorithms provided by Amazon SageMaker, see `Algorithms <http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ . For information about providing your own algorithms, see `Using Your Own Algorithms with Amazon SageMaker <http://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__ . 
        
          - **TrainingImage** *(string) --* **[REQUIRED]** 
        
            The registry path of the Docker image that contains the training algorithm. For information about docker registry paths for built-in algorithms, see `Algorithms Provided by Amazon SageMaker\: Common Parameters <http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html>`__ .
        
          - **TrainingInputMode** *(string) --* **[REQUIRED]** 
        
            The input mode that the algorithm supports. For the input modes that Amazon SageMaker algorithms support, see `Algorithms <http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ . If an algorithm supports the ``File`` input mode, Amazon SageMaker downloads the training data from S3 to the provisioned ML storage Volume, and mounts the directory to docker volume for training container. If an algorithm supports the ``Pipe`` input mode, Amazon SageMaker streams data directly from S3 to the container. 
        
            In File mode, make sure you provision ML storage volume with sufficient capacity to accommodate the data download from S3. In addition to the training data, the ML storage volume also stores the output model. The algorithm container use ML storage volume to also store intermediate information, if any. 
        
            For distributed algorithms using File mode, training data is distributed uniformly, and your training duration is predictable if the input data objects size is approximately same. Amazon SageMaker does not split the files any further for model training. If the object sizes are skewed, training won\'t be optimal as the data distribution is also skewed where one host in a training cluster is overloaded, thus becoming bottleneck in training. 
        
        :type RoleArn: string
        :param RoleArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf. 
        
          During model training, Amazon SageMaker needs your permission to read input data from an S3 bucket, download a Docker image that contains training code, write model artifacts to an S3 bucket, write logs to Amazon CloudWatch Logs, and publish metrics to Amazon CloudWatch. You grant permissions for all of these tasks to an IAM role. For more information, see `Amazon SageMaker Roles <http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html>`__ . 
        
          .. note::
        
            To be able to pass this role to Amazon SageMaker, the caller of this API must have the ``iam:PassRole`` permission.
        
        :type InputDataConfig: list
        :param InputDataConfig: 
        
          An array of ``Channel`` objects. Each channel is a named input source. ``InputDataConfig`` describes the input data and its location. 
        
          Algorithms can accept input data from one or more channels. For example, an algorithm might have two channels of input data, ``training_data`` and ``validation_data`` . The configuration for each channel provides the S3 location where the input data is stored. It also provides information about the stored data: the MIME type, compression method, and whether the data is wrapped in RecordIO format. 
        
          Depending on the input mode that the algorithm supports, Amazon SageMaker either copies input data files from an S3 bucket to a local directory in the Docker container, or makes it available as input streams. 
        
          - *(dict) --* 
        
            A channel is a named input source that training algorithms can consume. 
        
            - **ChannelName** *(string) --* **[REQUIRED]** 
        
              The name of the channel. 
        
            - **DataSource** *(dict) --* **[REQUIRED]** 
        
              The location of the channel data.
        
              - **S3DataSource** *(dict) --* **[REQUIRED]** 
        
                The S3 location of the data source that is associated with a channel.
        
                - **S3DataType** *(string) --* **[REQUIRED]** 
        
                  If you choose ``S3Prefix`` , ``S3Uri`` identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for model training. 
        
                  If you choose ``ManifestFile`` , ``S3Uri`` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for model training. 
        
                - **S3Uri** *(string) --* **[REQUIRED]** 
        
                  Depending on the value specified for the ``S3DataType`` , identifies either a key name prefix or a manifest. For example: 
        
                  * A key name prefix might look like this: ``s3://bucketname/exampleprefix`` .  
                   
                  * A manifest might look like this: ``s3://bucketname/example.manifest``   The manifest is an S3 object which is a JSON file with the following format:   ``[``    ``{\"prefix\": \"s3://customer_bucket/some/prefix/\"},``    ``\"relative/path/to/custdata-1\",``    ``\"relative/path/custdata-2\",``    ``...``    ``]``   The preceding JSON matches the following ``s3Uris`` :   ``s3://customer_bucket/some/prefix/relative/path/to/custdata-1``    ``s3://customer_bucket/some/prefix/relative/path/custdata-1``    ``...``   The complete set of ``s3uris`` in this manifest constitutes the input data for the channel for this datasource. The object that each ``s3uris`` points to must readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.  
                   
                - **S3DataDistributionType** *(string) --* 
        
                  If you want Amazon SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify ``FullyReplicated`` . 
        
                  If you want Amazon SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify ``ShardedByS3Key`` . If there are *n* ML compute instances launched for a training job, each instance gets approximately 1/*n* of the number of S3 objects. In this case, model training on each machine uses only the subset of training data. 
        
                  Don\'t choose more ML compute instances for training than available S3 objects. If you do, some nodes won\'t get any data and you will pay for nodes that aren\'t getting any training data. This applies in both FILE and PIPE modes. Keep this in mind when developing algorithms. 
        
                  In distributed training, where you use multiple ML compute EC2 instances, you might choose ``ShardedByS3Key`` . If the algorithm requires copying training data to the ML storage volume (when ``TrainingInputMode`` is set to ``File`` ), this copies 1/*n* of the number of objects. 
        
            - **ContentType** *(string) --* 
        
              The MIME type of the data.
        
            - **CompressionType** *(string) --* 
        
              If training data is compressed, the compression type. The default value is ``None`` . ``CompressionType`` is used only in Pipe input mode. In File mode, leave this field unset or set it to None.
        
            - **RecordWrapperType** *(string) --* 
        
              Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format, in which case, Amazon SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you don\'t need to set this attribute. For more information, see `Create a Dataset Using RecordIO <https://mxnet.incubator.apache.org/architecture/note_data_loading.html#data-format>`__ . 
        
              In FILE mode, leave this field unset or set it to None.
        
            - **InputMode** *(string) --* 
        
        :type OutputDataConfig: dict
        :param OutputDataConfig: **[REQUIRED]** 
        
          Specifies the path to the S3 bucket where you want to store model artifacts. Amazon SageMaker creates subfolders for the artifacts. 
        
          - **KmsKeyId** *(string) --* 
        
            The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The ``KmsKeyId`` can be any of the following formats: 
        
            * // KMS Key ID  ``\"1234abcd-12ab-34cd-56ef-1234567890ab\"``   
             
            * // Amazon Resource Name (ARN) of a KMS Key  ``\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"``   
             
            * // KMS Key Alias  ``\"alias/ExampleAlias\"``   
             
            * // Amazon Resource Name (ARN) of a KMS Key Alias  ``\"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias\"``   
             
            If you don\'t provide the KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role\'s account. For more information, see `KMS-Managed Encryption Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ in *Amazon Simple Storage Service Developer Guide.*  
        
            .. note::
        
              The KMS key policy must grant permission to the IAM role that you specify in your ``CreateTrainingJob`` request. `Using Key Policies in AWS KMS <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the *AWS Key Management Service Developer Guide* . 
        
          - **S3OutputPath** *(string) --* **[REQUIRED]** 
        
            Identifies the S3 path where you want Amazon SageMaker to store the model artifacts. For example, ``s3://bucket-name/key-name-prefix`` . 
        
        :type ResourceConfig: dict
        :param ResourceConfig: **[REQUIRED]** 
        
          The resources, including the ML compute instances and ML storage volumes, to use for model training. 
        
          ML storage volumes store model artifacts and incremental states. Training algorithms might also use ML storage volumes for scratch space. If you want Amazon SageMaker to use the ML storage volume to store the training data, choose ``File`` as the ``TrainingInputMode`` in the algorithm specification. For distributed training algorithms, specify an instance count greater than 1.
        
          - **InstanceType** *(string) --* **[REQUIRED]** 
        
            The ML compute instance type. 
        
          - **InstanceCount** *(integer) --* **[REQUIRED]** 
        
            The number of ML compute instances to use. For distributed training, provide a value greater than 1. 
        
          - **VolumeSizeInGB** *(integer) --* **[REQUIRED]** 
        
            The size of the ML storage volume that you want to provision. 
        
            ML storage volumes store model artifacts and incremental states. Training algorithms might also use the ML storage volume for scratch space. If you want to store the training data in the ML storage volume, choose ``File`` as the ``TrainingInputMode`` in the algorithm specification. 
        
            You must specify sufficient ML storage for your scenario. 
        
            .. note::
        
              Amazon SageMaker supports only the General Purpose SSD (gp2) ML storage volume type. 
        
          - **VolumeKmsKeyId** *(string) --* 
        
            The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the training job. The ``VolumeKmsKeyId`` can be any of the following formats:
        
            * // KMS Key ID  ``\"1234abcd-12ab-34cd-56ef-1234567890ab\"``   
             
            * // Amazon Resource Name (ARN) of a KMS Key  ``\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"``   
             
        :type VpcConfig: dict
        :param VpcConfig: 
        
          A  VpcConfig object that specifies the VPC that you want your training job to connect to. Control access to and from your training container by configuring the VPC. For more information, see `Protect Training Jobs by Using an Amazon Virtual Private Cloud <http://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html>`__ .
        
          - **SecurityGroupIds** *(list) --* **[REQUIRED]** 
        
            The VPC security group IDs, in the form sg-xxxxxxxx. Specify the security groups for the VPC that is specified in the ``Subnets`` field.
        
            - *(string) --* 
        
          - **Subnets** *(list) --* **[REQUIRED]** 
        
            The ID of the subnets in the VPC to which you want to connect your training job or model. 
        
            - *(string) --* 
        
        :type StoppingCondition: dict
        :param StoppingCondition: **[REQUIRED]** 
        
          Sets a duration for training. Use this parameter to cap model training costs. To stop a job, Amazon SageMaker sends the algorithm the ``SIGTERM`` signal, which delays job termination for 120 seconds. Algorithms might use this 120-second window to save the model artifacts. 
        
          When Amazon SageMaker terminates a job because the stopping condition has been met, training algorithms provided by Amazon SageMaker save the intermediate results of the job. This intermediate data is a valid model artifact. You can use it to create a model using the ``CreateModel`` API. 
        
          - **MaxRuntimeInSeconds** *(integer) --* 
        
            The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 5 days.
        
        :type Tags: list
        :param Tags: 
        
          An array of key-value pairs. For more information, see `Using Cost Allocation Tags <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what>`__ in the *AWS Billing and Cost Management User Guide* . 
        
          - *(dict) --* 
        
            Describes a tag. 
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The tag key.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The tag value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TrainingJobArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TrainingJobArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the training job.
        
        """
        pass

    def create_transform_job(self, TransformJobName: str, ModelName: str, TransformInput: Dict, TransformOutput: Dict, TransformResources: Dict, MaxConcurrentTransforms: int = None, MaxPayloadInMB: int = None, BatchStrategy: str = None, Environment: Dict = None, Tags: List = None) -> Dict:
        """
        
        To perform batch transformations, you create a transform job and use the data that you have readily available.
        
        In the request body, you provide the following:
        
        * ``TransformJobName`` - Identifies the transform job. The name must be unique within an AWS Region in an AWS account. 
         
        * ``ModelName`` - Identifies the model to use. ``ModelName`` must be the name of an existing Amazon SageMaker model in the same AWS Region and AWS account. For information on creating a model, see  CreateModel . 
         
        * ``TransformInput`` - Describes the dataset to be transformed and the Amazon S3 location where it is stored. 
         
        * ``TransformOutput`` - Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job. 
         
        * ``TransformResources`` - Identifies the ML compute instances for the transform job. 
         
        For more information about how batch transformation works Amazon SageMaker, see `How It Works <http://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html>`__ . 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateTransformJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_transform_job(
              TransformJobName=\'string\',
              ModelName=\'string\',
              MaxConcurrentTransforms=123,
              MaxPayloadInMB=123,
              BatchStrategy=\'MultiRecord\'|\'SingleRecord\',
              Environment={
                  \'string\': \'string\'
              },
              TransformInput={
                  \'DataSource\': {
                      \'S3DataSource\': {
                          \'S3DataType\': \'ManifestFile\'|\'S3Prefix\',
                          \'S3Uri\': \'string\'
                      }
                  },
                  \'ContentType\': \'string\',
                  \'CompressionType\': \'None\'|\'Gzip\',
                  \'SplitType\': \'None\'|\'Line\'|\'RecordIO\'
              },
              TransformOutput={
                  \'S3OutputPath\': \'string\',
                  \'Accept\': \'string\',
                  \'AssembleWith\': \'None\'|\'Line\',
                  \'KmsKeyId\': \'string\'
              },
              TransformResources={
                  \'InstanceType\': \'ml.m4.xlarge\'|\'ml.m4.2xlarge\'|\'ml.m4.4xlarge\'|\'ml.m4.10xlarge\'|\'ml.m4.16xlarge\'|\'ml.c4.xlarge\'|\'ml.c4.2xlarge\'|\'ml.c4.4xlarge\'|\'ml.c4.8xlarge\'|\'ml.p2.xlarge\'|\'ml.p2.8xlarge\'|\'ml.p2.16xlarge\'|\'ml.p3.2xlarge\'|\'ml.p3.8xlarge\'|\'ml.p3.16xlarge\'|\'ml.c5.xlarge\'|\'ml.c5.2xlarge\'|\'ml.c5.4xlarge\'|\'ml.c5.9xlarge\'|\'ml.c5.18xlarge\'|\'ml.m5.large\'|\'ml.m5.xlarge\'|\'ml.m5.2xlarge\'|\'ml.m5.4xlarge\'|\'ml.m5.12xlarge\'|\'ml.m5.24xlarge\',
                  \'InstanceCount\': 123,
                  \'VolumeKmsKeyId\': \'string\'
              },
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type TransformJobName: string
        :param TransformJobName: **[REQUIRED]** 
        
          The name of the transform job. The name must be unique within an AWS Region in an AWS account. 
        
        :type ModelName: string
        :param ModelName: **[REQUIRED]** 
        
          The name of the model that you want to use for the transform job. ``ModelName`` must be the name of an existing Amazon SageMaker model within an AWS Region in an AWS account.
        
        :type MaxConcurrentTransforms: integer
        :param MaxConcurrentTransforms: 
        
          The maximum number of parallel requests that can be sent to each instance in a transform job. This is good for algorithms that implement multiple workers on larger instances . The default value is ``1`` . To allow Amazon SageMaker to determine the appropriate number for ``MaxConcurrentTransforms`` , set the value to ``0`` .
        
        :type MaxPayloadInMB: integer
        :param MaxPayloadInMB: 
        
          The maximum payload size allowed, in MB. A payload is the data portion of a record (without metadata). The value in ``MaxPayloadInMB`` must be greater or equal to the size of a single record. You can approximate the size of a record by dividing the size of your dataset by the number of records. Then multiply this value by the number of records you want in a mini-batch. It is recommended to enter a value slightly larger than this to ensure the records fit within the maximum payload size. The default value is ``6`` MB. For an unlimited payload size, set the value to ``0`` .
        
        :type BatchStrategy: string
        :param BatchStrategy: 
        
          Determines the number of records included in a single mini-batch. ``SingleRecord`` means only one record is used per mini-batch. ``MultiRecord`` means a mini-batch is set to contain as many records that can fit within the ``MaxPayloadInMB`` limit.
        
          Batch transform will automatically split your input data into whatever payload size is specified if you set ``SplitType`` to ``Line`` and ``BatchStrategy`` to ``MultiRecord`` . There\'s no need to split the dataset into smaller files or to use larger payload sizes unless the records in your dataset are very large.
        
        :type Environment: dict
        :param Environment: 
        
          The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type TransformInput: dict
        :param TransformInput: **[REQUIRED]** 
        
          Describes the input source and the way the transform job consumes it.
        
          - **DataSource** *(dict) --* **[REQUIRED]** 
        
            Describes the location of the channel data, meaning the S3 location of the input data that the model can consume.
        
            - **S3DataSource** *(dict) --* **[REQUIRED]** 
        
              The S3 location of the data source that is associated with a channel.
        
              - **S3DataType** *(string) --* **[REQUIRED]** 
        
                If you choose ``S3Prefix`` , ``S3Uri`` identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for batch transform. 
        
                If you choose ``ManifestFile`` , ``S3Uri`` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for batch transform. 
        
              - **S3Uri** *(string) --* **[REQUIRED]** 
        
                Depending on the value specified for the ``S3DataType`` , identifies either a key name prefix or a manifest. For example:
        
                * A key name prefix might look like this: ``s3://bucketname/exampleprefix`` .  
                 
                * A manifest might look like this: ``s3://bucketname/example.manifest``   The manifest is an S3 object which is a JSON file with the following format:   ``[``    ``{\"prefix\": \"s3://customer_bucket/some/prefix/\"},``    ``\"relative/path/to/custdata-1\",``    ``\"relative/path/custdata-2\",``    ``...``    ``]``   The preceding JSON matches the following ``S3Uris`` :   ``s3://customer_bucket/some/prefix/relative/path/to/custdata-1``    ``s3://customer_bucket/some/prefix/relative/path/custdata-1``    ``...``   The complete set of ``S3Uris`` in this manifest constitutes the input data for the channel for this datasource. The object that each ``S3Uris`` points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf. 
                 
          - **ContentType** *(string) --* 
        
            The multipurpose internet mail extension (MIME) type of the data. Amazon SageMaker uses the MIME type with each http call to transfer data to the transform job.
        
          - **CompressionType** *(string) --* 
        
            Compressing data helps save on storage space. If your transform data is compressed, specify the compression type. Amazon SageMaker automatically decompresses the data for the transform job accordingly. The default value is ``None`` .
        
          - **SplitType** *(string) --* 
        
            The method to use to split the transform job\'s data into smaller batches. The default value is ``None`` . If you don\'t want to split the data, specify ``None`` . If you want to split records on a newline character boundary, specify ``Line`` . To split records according to the RecordIO format, specify ``RecordIO`` .
        
            Amazon SageMaker will send maximum number of records per batch in each request up to the MaxPayloadInMB limit. For more information, see `RecordIO data format <http://mxnet.io/architecture/note_data_loading.html#data-format>`__ .
        
            .. note::
        
              For information about the ``RecordIO`` format, see `Data Format <http://mxnet.io/architecture/note_data_loading.html#data-format>`__ .
        
        :type TransformOutput: dict
        :param TransformOutput: **[REQUIRED]** 
        
          Describes the results of the transform job.
        
          - **S3OutputPath** *(string) --* **[REQUIRED]** 
        
            The Amazon S3 path where you want Amazon SageMaker to store the results of the transform job. For example, ``s3://bucket-name/key-name-prefix`` .
        
            For every S3 object used as input for the transform job, the transformed data is stored in a corresponding subfolder in the location under the output prefix. For example, the input data ``s3://bucket-name/input-name-prefix/dataset01/data.csv`` will have the transformed data stored at ``s3://bucket-name/key-name-prefix/dataset01/`` , based on the original name, as a series of .part files (.part0001, part0002, etc).
        
          - **Accept** *(string) --* 
        
            The MIME type used to specify the output data. Amazon SageMaker uses the MIME type with each http call to transfer data from the transform job.
        
          - **AssembleWith** *(string) --* 
        
            Defines how to assemble the results of the transform job as a single S3 object. You should select a format that is most convenient to you. To concatenate the results in binary format, specify ``None`` . To add a newline character at the end of every transformed record, specify ``Line`` .
        
          - **KmsKeyId** *(string) --* 
        
            The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The ``KmsKeyId`` can be any of the following formats: 
        
            * // KMS Key ID  ``\"1234abcd-12ab-34cd-56ef-1234567890ab\"``   
             
            * // Amazon Resource Name (ARN) of a KMS Key  ``\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"``   
             
            * // KMS Key Alias  ``\"alias/ExampleAlias\"``   
             
            * // Amazon Resource Name (ARN) of a KMS Key Alias  ``\"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias\"``   
             
            If you don\'t provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role\'s account. For more information, see `KMS-Managed Encryption Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ in the *Amazon Simple Storage Service Developer Guide.*  
        
            The KMS key policy must grant permission to the IAM role that you specify in your ``CreateTramsformJob`` request. For more information, see `Using Key Policies in AWS KMS <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        :type TransformResources: dict
        :param TransformResources: **[REQUIRED]** 
        
          Describes the resources, including ML instance types and ML instance count, to use for the transform job.
        
          - **InstanceType** *(string) --* **[REQUIRED]** 
        
            The ML compute instance type for the transform job. For using built-in algorithms to transform moderately sized datasets, ml.m4.xlarge or ``ml.m5.large`` should suffice. There is no default value for ``InstanceType`` .
        
          - **InstanceCount** *(integer) --* **[REQUIRED]** 
        
            The number of ML compute instances to use in the transform job. For distributed transform, provide a value greater than 1. The default value is ``1`` .
        
          - **VolumeKmsKeyId** *(string) --* 
        
            The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the batch transform job. The ``VolumeKmsKeyId`` can be any of the following formats:
        
            * // KMS Key ID  ``\"1234abcd-12ab-34cd-56ef-1234567890ab\"``   
             
            * // Amazon Resource Name (ARN) of a KMS Key  ``\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"``   
             
        :type Tags: list
        :param Tags: 
        
          An array of key-value pairs. Adding tags is optional. For more information, see `Using Cost Allocation Tags <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what>`__ in the *AWS Billing and Cost Management User Guide* .
        
          - *(dict) --* 
        
            Describes a tag. 
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The tag key.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The tag value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TransformJobArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TransformJobArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the transform job.
        
        """
        pass

    def delete_endpoint(self, EndpointName: str) -> NoReturn:
        """
        
        Amazon SageMaker retires any custom KMS key grants associated with the endpoint, meaning you don\'t need to use the `RevokeGrant <http://docs.aws.amazon.com/kms/latest/APIReference/API_RevokeGrant.html>`__ API call.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DeleteEndpoint>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_endpoint(
              EndpointName=\'string\'
          )
        :type EndpointName: string
        :param EndpointName: **[REQUIRED]** 
        
          The name of the endpoint that you want to delete.
        
        :returns: None
        """
        pass

    def delete_endpoint_config(self, EndpointConfigName: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DeleteEndpointConfig>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_endpoint_config(
              EndpointConfigName=\'string\'
          )
        :type EndpointConfigName: string
        :param EndpointConfigName: **[REQUIRED]** 
        
          The name of the endpoint configuration that you want to delete.
        
        :returns: None
        """
        pass

    def delete_model(self, ModelName: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DeleteModel>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_model(
              ModelName=\'string\'
          )
        :type ModelName: string
        :param ModelName: **[REQUIRED]** 
        
          The name of the model to delete.
        
        :returns: None
        """
        pass

    def delete_notebook_instance(self, NotebookInstanceName: str) -> NoReturn:
        """
        
        .. warning::
        
          When you delete a notebook instance, you lose all of your data. Amazon SageMaker removes the ML compute instance, and deletes the ML storage volume and the network interface associated with the notebook instance. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DeleteNotebookInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_notebook_instance(
              NotebookInstanceName=\'string\'
          )
        :type NotebookInstanceName: string
        :param NotebookInstanceName: **[REQUIRED]** 
        
          The name of the Amazon SageMaker notebook instance to delete.
        
        :returns: None
        """
        pass

    def delete_notebook_instance_lifecycle_config(self, NotebookInstanceLifecycleConfigName: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DeleteNotebookInstanceLifecycleConfig>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_notebook_instance_lifecycle_config(
              NotebookInstanceLifecycleConfigName=\'string\'
          )
        :type NotebookInstanceLifecycleConfigName: string
        :param NotebookInstanceLifecycleConfigName: **[REQUIRED]** 
        
          The name of the lifecycle configuration to delete.
        
        :returns: None
        """
        pass

    def delete_tags(self, ResourceArn: str, TagKeys: List) -> Dict:
        """
        
        To list a resource\'s tags, use the ``ListTags`` API. 
        
        .. note::
        
          When you call this API to delete tags from a hyperparameter tuning job, the deleted tags are not removed from training jobs that the hyperparameter tuning job launched before you called this API.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DeleteTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_tags(
              ResourceArn=\'string\',
              TagKeys=[
                  \'string\',
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the resource whose tags you want to delete.
        
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]** 
        
          An array or one or more tag keys to delete.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def describe_endpoint(self, EndpointName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeEndpoint>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_endpoint(
              EndpointName=\'string\'
          )
        :type EndpointName: string
        :param EndpointName: **[REQUIRED]** 
        
          The name of the endpoint.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EndpointName\': \'string\',
                \'EndpointArn\': \'string\',
                \'EndpointConfigName\': \'string\',
                \'ProductionVariants\': [
                    {
                        \'VariantName\': \'string\',
                        \'DeployedImages\': [
                            {
                                \'SpecifiedImage\': \'string\',
                                \'ResolvedImage\': \'string\',
                                \'ResolutionTime\': datetime(2015, 1, 1)
                            },
                        ],
                        \'CurrentWeight\': ...,
                        \'DesiredWeight\': ...,
                        \'CurrentInstanceCount\': 123,
                        \'DesiredInstanceCount\': 123
                    },
                ],
                \'EndpointStatus\': \'OutOfService\'|\'Creating\'|\'Updating\'|\'SystemUpdating\'|\'RollingBack\'|\'InService\'|\'Deleting\'|\'Failed\',
                \'FailureReason\': \'string\',
                \'CreationTime\': datetime(2015, 1, 1),
                \'LastModifiedTime\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **EndpointName** *(string) --* 
        
              Name of the endpoint.
        
            - **EndpointArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the endpoint.
        
            - **EndpointConfigName** *(string) --* 
        
              The name of the endpoint configuration associated with this endpoint.
        
            - **ProductionVariants** *(list) --* 
        
              An array of  ProductionVariantSummary objects, one for each model hosted behind this endpoint. 
        
              - *(dict) --* 
        
                Describes weight and capacities for a production variant associated with an endpoint. If you sent a request to the ``UpdateEndpointWeightsAndCapacities`` API and the endpoint status is ``Updating`` , you get different desired and current values. 
        
                - **VariantName** *(string) --* 
        
                  The name of the variant.
        
                - **DeployedImages** *(list) --* 
        
                  An array of ``DeployedImage`` objects that specify the Amazon EC2 Container Registry paths of the inference images deployed on instances of this ``ProductionVariant`` .
        
                  - *(dict) --* 
        
                    Gets the Amazon EC2 Container Registry path of the docker image of the model that is hosted in this  ProductionVariant .
        
                    If you used the ``registry/repository[:tag]`` form to specify the image path of the primary container when you created the model hosted in this ``ProductionVariant`` , the path resolves to a path of the form ``registry/repository[@digest]`` . A digest is a hash value that identifies a specific version of an image. For information about Amazon ECR paths, see `Pulling an Image <http://docs.aws.amazon.com//AmazonECR/latest/userguide/docker-pull-ecr-image.html>`__ in the *Amazon ECR User Guide* .
        
                    - **SpecifiedImage** *(string) --* 
        
                      The image path you specified when you created the model.
        
                    - **ResolvedImage** *(string) --* 
        
                      The specific digest path of the image hosted in this ``ProductionVariant`` .
        
                    - **ResolutionTime** *(datetime) --* 
        
                      The date and time when the image path for the model resolved to the ``ResolvedImage``  
        
                - **CurrentWeight** *(float) --* 
        
                  The weight associated with the variant.
        
                - **DesiredWeight** *(float) --* 
        
                  The requested weight, as specified in the ``UpdateEndpointWeightsAndCapacities`` request. 
        
                - **CurrentInstanceCount** *(integer) --* 
        
                  The number of instances associated with the variant.
        
                - **DesiredInstanceCount** *(integer) --* 
        
                  The number of instances requested in the ``UpdateEndpointWeightsAndCapacities`` request. 
        
            - **EndpointStatus** *(string) --* 
        
              The status of the endpoint.
        
              * ``OutOfService`` : Endpoint is not available to take incoming requests. 
               
              * ``Creating`` :  CreateEndpoint is executing. 
               
              * ``Updating`` :  UpdateEndpoint or  UpdateEndpointWeightsAndCapacities is executing. 
               
              * ``SystemUpdating`` : Endpoint is undergoing maintenance and cannot be updated or deleted or re-scaled until it has completed. This maintenance operation does not change any customer-specified values such as VPC config, KMS encryption, model, instance type, or instance count. 
               
              * ``RollingBack`` : Endpoint fails to scale up or down or change its variant weight and is in the process of rolling back to its previous configuration. Once the rollback completes, endpoint returns to an ``InService`` status. This transitional status only applies to an endpoint that has autoscaling enabled and is undergoing variant weight or capacity changes as part of an  UpdateEndpointWeightsAndCapacities call or when the  UpdateEndpointWeightsAndCapacities operation is called explicitly. 
               
              * ``InService`` : Endpoint is available to process incoming requests. 
               
              * ``Deleting`` :  DeleteEndpoint is executing. 
               
              * ``Failed`` : Endpoint could not be created, updated, or re-scaled. Use  DescribeEndpointOutput$FailureReason for information about the failure.  DeleteEndpoint is the only operation that can be performed on a failed endpoint. 
               
            - **FailureReason** *(string) --* 
        
              If the status of the endpoint is ``Failed`` , the reason why it failed. 
        
            - **CreationTime** *(datetime) --* 
        
              A timestamp that shows when the endpoint was created.
        
            - **LastModifiedTime** *(datetime) --* 
        
              A timestamp that shows when the endpoint was last modified.
        
        """
        pass

    def describe_endpoint_config(self, EndpointConfigName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeEndpointConfig>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_endpoint_config(
              EndpointConfigName=\'string\'
          )
        :type EndpointConfigName: string
        :param EndpointConfigName: **[REQUIRED]** 
        
          The name of the endpoint configuration.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EndpointConfigName\': \'string\',
                \'EndpointConfigArn\': \'string\',
                \'ProductionVariants\': [
                    {
                        \'VariantName\': \'string\',
                        \'ModelName\': \'string\',
                        \'InitialInstanceCount\': 123,
                        \'InstanceType\': \'ml.t2.medium\'|\'ml.t2.large\'|\'ml.t2.xlarge\'|\'ml.t2.2xlarge\'|\'ml.m4.xlarge\'|\'ml.m4.2xlarge\'|\'ml.m4.4xlarge\'|\'ml.m4.10xlarge\'|\'ml.m4.16xlarge\'|\'ml.m5.large\'|\'ml.m5.xlarge\'|\'ml.m5.2xlarge\'|\'ml.m5.4xlarge\'|\'ml.m5.12xlarge\'|\'ml.m5.24xlarge\'|\'ml.c4.large\'|\'ml.c4.xlarge\'|\'ml.c4.2xlarge\'|\'ml.c4.4xlarge\'|\'ml.c4.8xlarge\'|\'ml.p2.xlarge\'|\'ml.p2.8xlarge\'|\'ml.p2.16xlarge\'|\'ml.p3.2xlarge\'|\'ml.p3.8xlarge\'|\'ml.p3.16xlarge\'|\'ml.c5.large\'|\'ml.c5.xlarge\'|\'ml.c5.2xlarge\'|\'ml.c5.4xlarge\'|\'ml.c5.9xlarge\'|\'ml.c5.18xlarge\',
                        \'InitialVariantWeight\': ...
                    },
                ],
                \'KmsKeyId\': \'string\',
                \'CreationTime\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **EndpointConfigName** *(string) --* 
        
              Name of the Amazon SageMaker endpoint configuration.
        
            - **EndpointConfigArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the endpoint configuration.
        
            - **ProductionVariants** *(list) --* 
        
              An array of ``ProductionVariant`` objects, one for each model that you want to host at this endpoint.
        
              - *(dict) --* 
        
                Identifies a model that you want to host and the resources to deploy for hosting it. If you are deploying multiple models, tell Amazon SageMaker how to distribute traffic among the models by specifying variant weights. 
        
                - **VariantName** *(string) --* 
        
                  The name of the production variant.
        
                - **ModelName** *(string) --* 
        
                  The name of the model that you want to host. This is the name that you specified when creating the model.
        
                - **InitialInstanceCount** *(integer) --* 
        
                  Number of instances to launch initially.
        
                - **InstanceType** *(string) --* 
        
                  The ML compute instance type.
        
                - **InitialVariantWeight** *(float) --* 
        
                  Determines initial traffic distribution among all of the models that you specify in the endpoint configuration. The traffic to a production variant is determined by the ratio of the ``VariantWeight`` to the sum of all ``VariantWeight`` values across all ProductionVariants. If unspecified, it defaults to 1.0. 
        
            - **KmsKeyId** *(string) --* 
        
              AWS KMS key ID Amazon SageMaker uses to encrypt data when storing it on the ML storage volume attached to the instance.
        
            - **CreationTime** *(datetime) --* 
        
              A timestamp that shows when the endpoint configuration was created.
        
        """
        pass

    def describe_hyper_parameter_tuning_job(self, HyperParameterTuningJobName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeHyperParameterTuningJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_hyper_parameter_tuning_job(
              HyperParameterTuningJobName=\'string\'
          )
        :type HyperParameterTuningJobName: string
        :param HyperParameterTuningJobName: **[REQUIRED]** 
        
          The name of the tuning job to describe.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'HyperParameterTuningJobName\': \'string\',
                \'HyperParameterTuningJobArn\': \'string\',
                \'HyperParameterTuningJobConfig\': {
                    \'Strategy\': \'Bayesian\',
                    \'HyperParameterTuningJobObjective\': {
                        \'Type\': \'Maximize\'|\'Minimize\',
                        \'MetricName\': \'string\'
                    },
                    \'ResourceLimits\': {
                        \'MaxNumberOfTrainingJobs\': 123,
                        \'MaxParallelTrainingJobs\': 123
                    },
                    \'ParameterRanges\': {
                        \'IntegerParameterRanges\': [
                            {
                                \'Name\': \'string\',
                                \'MinValue\': \'string\',
                                \'MaxValue\': \'string\'
                            },
                        ],
                        \'ContinuousParameterRanges\': [
                            {
                                \'Name\': \'string\',
                                \'MinValue\': \'string\',
                                \'MaxValue\': \'string\'
                            },
                        ],
                        \'CategoricalParameterRanges\': [
                            {
                                \'Name\': \'string\',
                                \'Values\': [
                                    \'string\',
                                ]
                            },
                        ]
                    }
                },
                \'TrainingJobDefinition\': {
                    \'StaticHyperParameters\': {
                        \'string\': \'string\'
                    },
                    \'AlgorithmSpecification\': {
                        \'TrainingImage\': \'string\',
                        \'TrainingInputMode\': \'Pipe\'|\'File\',
                        \'MetricDefinitions\': [
                            {
                                \'Name\': \'string\',
                                \'Regex\': \'string\'
                            },
                        ]
                    },
                    \'RoleArn\': \'string\',
                    \'InputDataConfig\': [
                        {
                            \'ChannelName\': \'string\',
                            \'DataSource\': {
                                \'S3DataSource\': {
                                    \'S3DataType\': \'ManifestFile\'|\'S3Prefix\',
                                    \'S3Uri\': \'string\',
                                    \'S3DataDistributionType\': \'FullyReplicated\'|\'ShardedByS3Key\'
                                }
                            },
                            \'ContentType\': \'string\',
                            \'CompressionType\': \'None\'|\'Gzip\',
                            \'RecordWrapperType\': \'None\'|\'RecordIO\',
                            \'InputMode\': \'Pipe\'|\'File\'
                        },
                    ],
                    \'VpcConfig\': {
                        \'SecurityGroupIds\': [
                            \'string\',
                        ],
                        \'Subnets\': [
                            \'string\',
                        ]
                    },
                    \'OutputDataConfig\': {
                        \'KmsKeyId\': \'string\',
                        \'S3OutputPath\': \'string\'
                    },
                    \'ResourceConfig\': {
                        \'InstanceType\': \'ml.m4.xlarge\'|\'ml.m4.2xlarge\'|\'ml.m4.4xlarge\'|\'ml.m4.10xlarge\'|\'ml.m4.16xlarge\'|\'ml.m5.large\'|\'ml.m5.xlarge\'|\'ml.m5.2xlarge\'|\'ml.m5.4xlarge\'|\'ml.m5.12xlarge\'|\'ml.m5.24xlarge\'|\'ml.c4.xlarge\'|\'ml.c4.2xlarge\'|\'ml.c4.4xlarge\'|\'ml.c4.8xlarge\'|\'ml.p2.xlarge\'|\'ml.p2.8xlarge\'|\'ml.p2.16xlarge\'|\'ml.p3.2xlarge\'|\'ml.p3.8xlarge\'|\'ml.p3.16xlarge\'|\'ml.c5.xlarge\'|\'ml.c5.2xlarge\'|\'ml.c5.4xlarge\'|\'ml.c5.9xlarge\'|\'ml.c5.18xlarge\',
                        \'InstanceCount\': 123,
                        \'VolumeSizeInGB\': 123,
                        \'VolumeKmsKeyId\': \'string\'
                    },
                    \'StoppingCondition\': {
                        \'MaxRuntimeInSeconds\': 123
                    }
                },
                \'HyperParameterTuningJobStatus\': \'Completed\'|\'InProgress\'|\'Failed\'|\'Stopped\'|\'Stopping\',
                \'CreationTime\': datetime(2015, 1, 1),
                \'HyperParameterTuningEndTime\': datetime(2015, 1, 1),
                \'LastModifiedTime\': datetime(2015, 1, 1),
                \'TrainingJobStatusCounters\': {
                    \'Completed\': 123,
                    \'InProgress\': 123,
                    \'RetryableError\': 123,
                    \'NonRetryableError\': 123,
                    \'Stopped\': 123
                },
                \'ObjectiveStatusCounters\': {
                    \'Succeeded\': 123,
                    \'Pending\': 123,
                    \'Failed\': 123
                },
                \'BestTrainingJob\': {
                    \'TrainingJobName\': \'string\',
                    \'TrainingJobArn\': \'string\',
                    \'CreationTime\': datetime(2015, 1, 1),
                    \'TrainingStartTime\': datetime(2015, 1, 1),
                    \'TrainingEndTime\': datetime(2015, 1, 1),
                    \'TrainingJobStatus\': \'InProgress\'|\'Completed\'|\'Failed\'|\'Stopping\'|\'Stopped\',
                    \'TunedHyperParameters\': {
                        \'string\': \'string\'
                    },
                    \'FailureReason\': \'string\',
                    \'FinalHyperParameterTuningJobObjectiveMetric\': {
                        \'Type\': \'Maximize\'|\'Minimize\',
                        \'MetricName\': \'string\',
                        \'Value\': ...
                    },
                    \'ObjectiveStatus\': \'Succeeded\'|\'Pending\'|\'Failed\'
                },
                \'FailureReason\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **HyperParameterTuningJobName** *(string) --* 
        
              The name of the tuning job.
        
            - **HyperParameterTuningJobArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the tuning job.
        
            - **HyperParameterTuningJobConfig** *(dict) --* 
        
              The  HyperParameterTuningJobConfig object that specifies the configuration of the tuning job.
        
              - **Strategy** *(string) --* 
        
                Specifies the search strategy for hyperparameters. Currently, the only valid value is ``Bayesian`` .
        
              - **HyperParameterTuningJobObjective** *(dict) --* 
        
                The  HyperParameterTuningJobObjective object that specifies the objective metric for this tuning job.
        
                - **Type** *(string) --* 
        
                  Whether to minimize or maximize the objective metric.
        
                - **MetricName** *(string) --* 
        
                  The name of the metric to use for the objective metric.
        
              - **ResourceLimits** *(dict) --* 
        
                The  ResourceLimits object that specifies the maximum number of training jobs and parallel training jobs for this tuning job.
        
                - **MaxNumberOfTrainingJobs** *(integer) --* 
        
                  The maximum number of training jobs that a hyperparameter tuning job can launch.
        
                - **MaxParallelTrainingJobs** *(integer) --* 
        
                  The maximum number of concurrent training jobs that a hyperparameter tuning job can launch.
        
              - **ParameterRanges** *(dict) --* 
        
                The  ParameterRanges object that specifies the ranges of hyperparameters that this tuning job searches.
        
                - **IntegerParameterRanges** *(list) --* 
        
                  The array of  IntegerParameterRange objects that specify ranges of integer hyperparameters that a hyperparameter tuning job searches.
        
                  - *(dict) --* 
        
                    For a hyperparameter of the integer type, specifies the range that a hyperparameter tuning job searches.
        
                    - **Name** *(string) --* 
        
                      The name of the hyperparameter to search.
        
                    - **MinValue** *(string) --* 
        
                      The minimum value of the hyperparameter to search.
        
                    - **MaxValue** *(string) --* 
        
                      The maximum value of the hyperparameter to search.
        
                - **ContinuousParameterRanges** *(list) --* 
        
                  The array of  ContinuousParameterRange objects that specify ranges of continuous hyperparameters that a hyperparameter tuning job searches.
        
                  - *(dict) --* 
        
                    A list of continuous hyperparameters to tune.
        
                    - **Name** *(string) --* 
        
                      The name of the continuous hyperparameter to tune.
        
                    - **MinValue** *(string) --* 
        
                      The minimum value for the hyperparameter. The tuning job uses floating-point values between this value and ``MaxValue`` for tuning.
        
                    - **MaxValue** *(string) --* 
        
                      The maximum value for the hyperparameter. The tuning job uses floating-point values between ``MinValue`` value and this value for tuning.
        
                - **CategoricalParameterRanges** *(list) --* 
        
                  The array of  CategoricalParameterRange objects that specify ranges of categorical hyperparameters that a hyperparameter tuning job searches.
        
                  - *(dict) --* 
        
                    A list of categorical hyperparameters to tune.
        
                    - **Name** *(string) --* 
        
                      The name of the categorical hyperparameter to tune.
        
                    - **Values** *(list) --* 
        
                      A list of the categories for the hyperparameter.
        
                      - *(string) --* 
                  
            - **TrainingJobDefinition** *(dict) --* 
        
              The  HyperParameterTrainingJobDefinition object that specifies the definition of the training jobs that this tuning job launches.
        
              - **StaticHyperParameters** *(dict) --* 
        
                Specifies the values of hyperparameters that do not change for the tuning job.
        
                - *(string) --* 
                  
                  - *(string) --* 
            
              - **AlgorithmSpecification** *(dict) --* 
        
                The  HyperParameterAlgorithmSpecification object that specifies the algorithm to use for the training jobs that the tuning job launches.
        
                - **TrainingImage** *(string) --* 
        
                  The registry path of the Docker image that contains the training algorithm. For information about Docker registry paths for built-in algorithms, see `Algorithms Provided by Amazon SageMaker\: Common Parameters <http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html>`__ .
        
                - **TrainingInputMode** *(string) --* 
        
                  The input mode that the algorithm supports: File or Pipe. In File input mode, Amazon SageMaker downloads the training data from Amazon S3 to the storage volume that is attached to the training instance and mounts the directory to the Docker volume for the training container. In Pipe input mode, Amazon SageMaker streams data directly from Amazon S3 to the container. 
        
                  If you specify File mode, make sure that you provision the storage volume that is attached to the training instance with enough capacity to accommodate the training data downloaded from Amazon S3, the model artifacts, and intermediate information.
        
                  For more information about input modes, see `Algorithms <http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ . 
        
                - **MetricDefinitions** *(list) --* 
        
                  An array of  MetricDefinition objects that specify the metrics that the algorithm emits.
        
                  - *(dict) --* 
        
                    Specifies a metric that the training algorithm writes to ``stderr`` or ``stdout`` . Amazon SageMakerhyperparameter tuning captures all defined metrics. You specify one metric that a hyperparameter tuning job uses as its objective metric to choose the best training job.
        
                    - **Name** *(string) --* 
        
                      The name of the metric.
        
                    - **Regex** *(string) --* 
        
                      A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see `Defining Objective Metrics <http://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics.html>`__ .
        
              - **RoleArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the IAM role associated with the training jobs that the tuning job launches.
        
              - **InputDataConfig** *(list) --* 
        
                An array of  Channel objects that specify the input for the training jobs that the tuning job launches.
        
                - *(dict) --* 
        
                  A channel is a named input source that training algorithms can consume. 
        
                  - **ChannelName** *(string) --* 
        
                    The name of the channel. 
        
                  - **DataSource** *(dict) --* 
        
                    The location of the channel data.
        
                    - **S3DataSource** *(dict) --* 
        
                      The S3 location of the data source that is associated with a channel.
        
                      - **S3DataType** *(string) --* 
        
                        If you choose ``S3Prefix`` , ``S3Uri`` identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for model training. 
        
                        If you choose ``ManifestFile`` , ``S3Uri`` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for model training. 
        
                      - **S3Uri** *(string) --* 
        
                        Depending on the value specified for the ``S3DataType`` , identifies either a key name prefix or a manifest. For example: 
        
                        * A key name prefix might look like this: ``s3://bucketname/exampleprefix`` .  
                         
                        * A manifest might look like this: ``s3://bucketname/example.manifest``   The manifest is an S3 object which is a JSON file with the following format:   ``[``    ``{\"prefix\": \"s3://customer_bucket/some/prefix/\"},``    ``\"relative/path/to/custdata-1\",``    ``\"relative/path/custdata-2\",``    ``...``    ``]``   The preceding JSON matches the following ``s3Uris`` :   ``s3://customer_bucket/some/prefix/relative/path/to/custdata-1``    ``s3://customer_bucket/some/prefix/relative/path/custdata-1``    ``...``   The complete set of ``s3uris`` in this manifest constitutes the input data for the channel for this datasource. The object that each ``s3uris`` points to must readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.  
                         
                      - **S3DataDistributionType** *(string) --* 
        
                        If you want Amazon SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify ``FullyReplicated`` . 
        
                        If you want Amazon SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify ``ShardedByS3Key`` . If there are *n* ML compute instances launched for a training job, each instance gets approximately 1/*n* of the number of S3 objects. In this case, model training on each machine uses only the subset of training data. 
        
                        Don\'t choose more ML compute instances for training than available S3 objects. If you do, some nodes won\'t get any data and you will pay for nodes that aren\'t getting any training data. This applies in both FILE and PIPE modes. Keep this in mind when developing algorithms. 
        
                        In distributed training, where you use multiple ML compute EC2 instances, you might choose ``ShardedByS3Key`` . If the algorithm requires copying training data to the ML storage volume (when ``TrainingInputMode`` is set to ``File`` ), this copies 1/*n* of the number of objects. 
        
                  - **ContentType** *(string) --* 
        
                    The MIME type of the data.
        
                  - **CompressionType** *(string) --* 
        
                    If training data is compressed, the compression type. The default value is ``None`` . ``CompressionType`` is used only in Pipe input mode. In File mode, leave this field unset or set it to None.
        
                  - **RecordWrapperType** *(string) --* 
        
                    Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format, in which case, Amazon SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you don\'t need to set this attribute. For more information, see `Create a Dataset Using RecordIO <https://mxnet.incubator.apache.org/architecture/note_data_loading.html#data-format>`__ . 
        
                    In FILE mode, leave this field unset or set it to None.
        
                  - **InputMode** *(string) --* 
              
              - **VpcConfig** *(dict) --* 
        
                The  VpcConfig object that specifies the VPC that you want the training jobs that this hyperparameter tuning job launches to connect to. Control access to and from your training container by configuring the VPC. For more information, see `Protect Training Jobs by Using an Amazon Virtual Private Cloud <http://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html>`__ .
        
                - **SecurityGroupIds** *(list) --* 
        
                  The VPC security group IDs, in the form sg-xxxxxxxx. Specify the security groups for the VPC that is specified in the ``Subnets`` field.
        
                  - *(string) --* 
              
                - **Subnets** *(list) --* 
        
                  The ID of the subnets in the VPC to which you want to connect your training job or model. 
        
                  - *(string) --* 
              
              - **OutputDataConfig** *(dict) --* 
        
                Specifies the path to the Amazon S3 bucket where you store model artifacts from the training jobs that the tuning job launches.
        
                - **KmsKeyId** *(string) --* 
        
                  The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The ``KmsKeyId`` can be any of the following formats: 
        
                  * // KMS Key ID  ``\"1234abcd-12ab-34cd-56ef-1234567890ab\"``   
                   
                  * // Amazon Resource Name (ARN) of a KMS Key  ``\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"``   
                   
                  * // KMS Key Alias  ``\"alias/ExampleAlias\"``   
                   
                  * // Amazon Resource Name (ARN) of a KMS Key Alias  ``\"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias\"``   
                   
                  If you don\'t provide the KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role\'s account. For more information, see `KMS-Managed Encryption Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ in *Amazon Simple Storage Service Developer Guide.*  
        
                  .. note::
        
                    The KMS key policy must grant permission to the IAM role that you specify in your ``CreateTrainingJob`` request. `Using Key Policies in AWS KMS <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the *AWS Key Management Service Developer Guide* . 
        
                - **S3OutputPath** *(string) --* 
        
                  Identifies the S3 path where you want Amazon SageMaker to store the model artifacts. For example, ``s3://bucket-name/key-name-prefix`` . 
        
              - **ResourceConfig** *(dict) --* 
        
                The resources, including the compute instances and storage volumes, to use for the training jobs that the tuning job launches.
        
                Storage volumes store model artifacts and incremental states. Training algorithms might also use storage volumes for scratch space. If you want Amazon SageMaker to use the storage volume to store the training data, choose ``File`` as the ``TrainingInputMode`` in the algorithm specification. For distributed training algorithms, specify an instance count greater than 1.
        
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
        
                  * // KMS Key ID  ``\"1234abcd-12ab-34cd-56ef-1234567890ab\"``   
                   
                  * // Amazon Resource Name (ARN) of a KMS Key  ``\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"``   
                   
              - **StoppingCondition** *(dict) --* 
        
                Sets a maximum duration for the training jobs that the tuning job launches. Use this parameter to limit model training costs. 
        
                To stop a job, Amazon SageMaker sends the algorithm the ``SIGTERM`` signal. This delays job termination for 120 seconds. Algorithms might use this 120-second window to save the model artifacts.
        
                When Amazon SageMaker terminates a job because the stopping condition has been met, training algorithms provided by Amazon SageMaker save the intermediate results of the job.
        
                - **MaxRuntimeInSeconds** *(integer) --* 
        
                  The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 5 days.
        
            - **HyperParameterTuningJobStatus** *(string) --* 
        
              The status of the tuning job: InProgress, Completed, Failed, Stopping, or Stopped.
        
            - **CreationTime** *(datetime) --* 
        
              The date and time that the tuning job started.
        
            - **HyperParameterTuningEndTime** *(datetime) --* 
        
              The date and time that the tuning job ended.
        
            - **LastModifiedTime** *(datetime) --* 
        
              The date and time that the status of the tuning job was modified. 
        
            - **TrainingJobStatusCounters** *(dict) --* 
        
              The  TrainingJobStatusCounters object that specifies the number of training jobs, categorized by status, that this tuning job launched.
        
              - **Completed** *(integer) --* 
        
                The number of completed training jobs launched by a hyperparameter tuning job.
        
              - **InProgress** *(integer) --* 
        
                The number of in-progress training jobs launched by a hyperparameter tuning job.
        
              - **RetryableError** *(integer) --* 
        
                The number of training jobs that failed, but can be retried. A failed training job can be retried only if it failed because an internal service error occurred.
        
              - **NonRetryableError** *(integer) --* 
        
                The number of training jobs that failed and can\'t be retried. A failed training job can\'t be retried if it failed because a client error occurred.
        
              - **Stopped** *(integer) --* 
        
                The number of training jobs launched by a hyperparameter tuning job that were manually stopped.
        
            - **ObjectiveStatusCounters** *(dict) --* 
        
              The  ObjectiveStatusCounters object that specifies the number of training jobs, categorized by the status of their final objective metric, that this tuning job launched.
        
              - **Succeeded** *(integer) --* 
        
                The number of training jobs whose final objective metric was evaluated by the hyperparameter tuning job and used in the hyperparameter tuning process.
        
              - **Pending** *(integer) --* 
        
                The number of training jobs that are in progress and pending evaluation of their final objective metric.
        
              - **Failed** *(integer) --* 
        
                The number of training jobs whose final objective metric was not evaluated and used in the hyperparameter tuning process. This typically occurs when the training job failed or did not emit an objective metric.
        
            - **BestTrainingJob** *(dict) --* 
        
              A  TrainingJobSummary object that describes the training job that completed with the best current  HyperParameterTuningJobObjective .
        
              - **TrainingJobName** *(string) --* 
        
                The name of the training job.
        
              - **TrainingJobArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the training job.
        
              - **CreationTime** *(datetime) --* 
        
                The date and time that the training job was created.
        
              - **TrainingStartTime** *(datetime) --* 
        
                The date and time that the training job started.
        
              - **TrainingEndTime** *(datetime) --* 
        
                The date and time that the training job ended.
        
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
                 
            - **FailureReason** *(string) --* 
        
              If the tuning job failed, the reason it failed.
        
        """
        pass

    def describe_model(self, ModelName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeModel>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_model(
              ModelName=\'string\'
          )
        :type ModelName: string
        :param ModelName: **[REQUIRED]** 
        
          The name of the model.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ModelName\': \'string\',
                \'PrimaryContainer\': {
                    \'ContainerHostname\': \'string\',
                    \'Image\': \'string\',
                    \'ModelDataUrl\': \'string\',
                    \'Environment\': {
                        \'string\': \'string\'
                    }
                },
                \'ExecutionRoleArn\': \'string\',
                \'VpcConfig\': {
                    \'SecurityGroupIds\': [
                        \'string\',
                    ],
                    \'Subnets\': [
                        \'string\',
                    ]
                },
                \'CreationTime\': datetime(2015, 1, 1),
                \'ModelArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ModelName** *(string) --* 
        
              Name of the Amazon SageMaker model.
        
            - **PrimaryContainer** *(dict) --* 
        
              The location of the primary inference code, associated artifacts, and custom environment map that the inference code uses when it is deployed in production. 
        
              - **ContainerHostname** *(string) --* 
        
                The DNS host name for the container after Amazon SageMaker deploys it.
        
              - **Image** *(string) --* 
        
                The Amazon EC2 Container Registry (Amazon ECR) path where inference code is stored. If you are using your own custom algorithm instead of an algorithm provided by Amazon SageMaker, the inference code must meet Amazon SageMaker requirements. Amazon SageMaker supports both ``registry/repository[:tag]`` and ``registry/repository[@digest]`` image path formats. For more information, see `Using Your Own Algorithms with Amazon SageMaker <http://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__  
        
              - **ModelDataUrl** *(string) --* 
        
                The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix). 
        
                If you provide a value for this parameter, Amazon SageMaker uses AWS Security Token Service to download model artifacts from the S3 path you provide. AWS STS is activated in your IAM user account by default. If you previously deactivated AWS STS for a region, you need to reactivate AWS STS for that region. For more information, see `Activating and Deactivating AWS STS i an AWS Region <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html>`__ in the *AWS Identity and Access Management User Guide* .
        
              - **Environment** *(dict) --* 
        
                The environment variables to set in the Docker container. Each key and value in the ``Environment`` string to string map can have length of up to 1024. We support up to 16 entries in the map. 
        
                - *(string) --* 
                  
                  - *(string) --* 
            
            - **ExecutionRoleArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the IAM role that you specified for the model.
        
            - **VpcConfig** *(dict) --* 
        
              A  VpcConfig object that specifies the VPC that this model has access to. For more information, see `Protect Endpoints by Using an Amazon Virtual Private Cloud <http://docs.aws.amazon.com/sagemaker/latest/dg/host-vpc.html>`__  
        
              - **SecurityGroupIds** *(list) --* 
        
                The VPC security group IDs, in the form sg-xxxxxxxx. Specify the security groups for the VPC that is specified in the ``Subnets`` field.
        
                - *(string) --* 
            
              - **Subnets** *(list) --* 
        
                The ID of the subnets in the VPC to which you want to connect your training job or model. 
        
                - *(string) --* 
            
            - **CreationTime** *(datetime) --* 
        
              A timestamp that shows when the model was created.
        
            - **ModelArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the model.
        
        """
        pass

    def describe_notebook_instance(self, NotebookInstanceName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeNotebookInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_notebook_instance(
              NotebookInstanceName=\'string\'
          )
        :type NotebookInstanceName: string
        :param NotebookInstanceName: **[REQUIRED]** 
        
          The name of the notebook instance that you want information about.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NotebookInstanceArn\': \'string\',
                \'NotebookInstanceName\': \'string\',
                \'NotebookInstanceStatus\': \'Pending\'|\'InService\'|\'Stopping\'|\'Stopped\'|\'Failed\'|\'Deleting\'|\'Updating\',
                \'FailureReason\': \'string\',
                \'Url\': \'string\',
                \'InstanceType\': \'ml.t2.medium\'|\'ml.t2.large\'|\'ml.t2.xlarge\'|\'ml.t2.2xlarge\'|\'ml.m4.xlarge\'|\'ml.m4.2xlarge\'|\'ml.m4.4xlarge\'|\'ml.m4.10xlarge\'|\'ml.m4.16xlarge\'|\'ml.p2.xlarge\'|\'ml.p2.8xlarge\'|\'ml.p2.16xlarge\'|\'ml.p3.2xlarge\'|\'ml.p3.8xlarge\'|\'ml.p3.16xlarge\',
                \'SubnetId\': \'string\',
                \'SecurityGroups\': [
                    \'string\',
                ],
                \'RoleArn\': \'string\',
                \'KmsKeyId\': \'string\',
                \'NetworkInterfaceId\': \'string\',
                \'LastModifiedTime\': datetime(2015, 1, 1),
                \'CreationTime\': datetime(2015, 1, 1),
                \'NotebookInstanceLifecycleConfigName\': \'string\',
                \'DirectInternetAccess\': \'Enabled\'|\'Disabled\',
                \'VolumeSizeInGB\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NotebookInstanceArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the notebook instance.
        
            - **NotebookInstanceName** *(string) --* 
        
              Name of the Amazon SageMaker notebook instance. 
        
            - **NotebookInstanceStatus** *(string) --* 
        
              The status of the notebook instance.
        
            - **FailureReason** *(string) --* 
        
              If status is failed, the reason it failed.
        
            - **Url** *(string) --* 
        
              The URL that you use to connect to the Jupyter notebook that is running in your notebook instance. 
        
            - **InstanceType** *(string) --* 
        
              The type of ML compute instance running on the notebook instance.
        
            - **SubnetId** *(string) --* 
        
              The ID of the VPC subnet.
        
            - **SecurityGroups** *(list) --* 
        
              The IDs of the VPC security groups.
        
              - *(string) --* 
          
            - **RoleArn** *(string) --* 
        
              Amazon Resource Name (ARN) of the IAM role associated with the instance. 
        
            - **KmsKeyId** *(string) --* 
        
              AWS KMS key ID Amazon SageMaker uses to encrypt data when storing it on the ML storage volume attached to the instance. 
        
            - **NetworkInterfaceId** *(string) --* 
        
              Network interface IDs that Amazon SageMaker created at the time of creating the instance. 
        
            - **LastModifiedTime** *(datetime) --* 
        
              A timestamp. Use this parameter to retrieve the time when the notebook instance was last modified. 
        
            - **CreationTime** *(datetime) --* 
        
              A timestamp. Use this parameter to return the time when the notebook instance was created
        
            - **NotebookInstanceLifecycleConfigName** *(string) --* 
        
              Returns the name of a notebook instance lifecycle configuration.
        
              For information about notebook instance lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <http://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__  
        
            - **DirectInternetAccess** *(string) --* 
        
              Describes whether Amazon SageMaker provides internet access to the notebook instance. If this value is set to *Disabled, he notebook instance does not have internet access, and cannot connect to Amazon SageMaker training and endpoint services* .
        
              For more information, see `Notebook Instances Are Internet-Enabled by Default <http://docs.aws.amazon.com/sagemaker/latest/dg/appendix-additional-considerations.html#appendix-notebook-and-internet-access>`__ .
        
            - **VolumeSizeInGB** *(integer) --* 
        
              The size, in GB, of the ML storage volume attached to the notebook instance.
        
        """
        pass

    def describe_notebook_instance_lifecycle_config(self, NotebookInstanceLifecycleConfigName: str) -> Dict:
        """
        
        For information about notebook instance lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <http://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeNotebookInstanceLifecycleConfig>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_notebook_instance_lifecycle_config(
              NotebookInstanceLifecycleConfigName=\'string\'
          )
        :type NotebookInstanceLifecycleConfigName: string
        :param NotebookInstanceLifecycleConfigName: **[REQUIRED]** 
        
          The name of the lifecycle configuration to describe.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NotebookInstanceLifecycleConfigArn\': \'string\',
                \'NotebookInstanceLifecycleConfigName\': \'string\',
                \'OnCreate\': [
                    {
                        \'Content\': \'string\'
                    },
                ],
                \'OnStart\': [
                    {
                        \'Content\': \'string\'
                    },
                ],
                \'LastModifiedTime\': datetime(2015, 1, 1),
                \'CreationTime\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NotebookInstanceLifecycleConfigArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the lifecycle configuration.
        
            - **NotebookInstanceLifecycleConfigName** *(string) --* 
        
              The name of the lifecycle configuration.
        
            - **OnCreate** *(list) --* 
        
              The shell script that runs only once, when you create a notebook instance.
        
              - *(dict) --* 
        
                Contains the notebook instance lifecycle configuration script.
        
                Each lifecycle configuration script has a limit of 16384 characters.
        
                The value of the ``$PATH`` environment variable that is available to both scripts is ``/sbin:bin:/usr/sbin:/usr/bin`` .
        
                View CloudWatch Logs for notebook instance lifecycle configurations in log group ``/aws/sagemaker/NotebookInstances`` in log stream ``[notebook-instance-name]/[LifecycleConfigHook]`` .
        
                Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for longer than 5 minutes, it fails and the notebook instance is not created or started.
        
                For information about notebook instance lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <http://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
        
                - **Content** *(string) --* 
        
                  A base64-encoded string that contains a shell script for a notebook instance lifecycle configuration.
        
            - **OnStart** *(list) --* 
        
              The shell script that runs every time you start a notebook instance, including when you create the notebook instance.
        
              - *(dict) --* 
        
                Contains the notebook instance lifecycle configuration script.
        
                Each lifecycle configuration script has a limit of 16384 characters.
        
                The value of the ``$PATH`` environment variable that is available to both scripts is ``/sbin:bin:/usr/sbin:/usr/bin`` .
        
                View CloudWatch Logs for notebook instance lifecycle configurations in log group ``/aws/sagemaker/NotebookInstances`` in log stream ``[notebook-instance-name]/[LifecycleConfigHook]`` .
        
                Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for longer than 5 minutes, it fails and the notebook instance is not created or started.
        
                For information about notebook instance lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <http://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
        
                - **Content** *(string) --* 
        
                  A base64-encoded string that contains a shell script for a notebook instance lifecycle configuration.
        
            - **LastModifiedTime** *(datetime) --* 
        
              A timestamp that tells when the lifecycle configuration was last modified.
        
            - **CreationTime** *(datetime) --* 
        
              A timestamp that tells when the lifecycle configuration was created.
        
        """
        pass

    def describe_training_job(self, TrainingJobName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeTrainingJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_training_job(
              TrainingJobName=\'string\'
          )
        :type TrainingJobName: string
        :param TrainingJobName: **[REQUIRED]** 
        
          The name of the training job.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TrainingJobName\': \'string\',
                \'TrainingJobArn\': \'string\',
                \'TuningJobArn\': \'string\',
                \'ModelArtifacts\': {
                    \'S3ModelArtifacts\': \'string\'
                },
                \'TrainingJobStatus\': \'InProgress\'|\'Completed\'|\'Failed\'|\'Stopping\'|\'Stopped\',
                \'SecondaryStatus\': \'Starting\'|\'LaunchingMLInstances\'|\'PreparingTrainingStack\'|\'Downloading\'|\'DownloadingTrainingImage\'|\'Training\'|\'Uploading\'|\'Stopping\'|\'Stopped\'|\'MaxRuntimeExceeded\'|\'Completed\'|\'Failed\',
                \'FailureReason\': \'string\',
                \'HyperParameters\': {
                    \'string\': \'string\'
                },
                \'AlgorithmSpecification\': {
                    \'TrainingImage\': \'string\',
                    \'TrainingInputMode\': \'Pipe\'|\'File\'
                },
                \'RoleArn\': \'string\',
                \'InputDataConfig\': [
                    {
                        \'ChannelName\': \'string\',
                        \'DataSource\': {
                            \'S3DataSource\': {
                                \'S3DataType\': \'ManifestFile\'|\'S3Prefix\',
                                \'S3Uri\': \'string\',
                                \'S3DataDistributionType\': \'FullyReplicated\'|\'ShardedByS3Key\'
                            }
                        },
                        \'ContentType\': \'string\',
                        \'CompressionType\': \'None\'|\'Gzip\',
                        \'RecordWrapperType\': \'None\'|\'RecordIO\',
                        \'InputMode\': \'Pipe\'|\'File\'
                    },
                ],
                \'OutputDataConfig\': {
                    \'KmsKeyId\': \'string\',
                    \'S3OutputPath\': \'string\'
                },
                \'ResourceConfig\': {
                    \'InstanceType\': \'ml.m4.xlarge\'|\'ml.m4.2xlarge\'|\'ml.m4.4xlarge\'|\'ml.m4.10xlarge\'|\'ml.m4.16xlarge\'|\'ml.m5.large\'|\'ml.m5.xlarge\'|\'ml.m5.2xlarge\'|\'ml.m5.4xlarge\'|\'ml.m5.12xlarge\'|\'ml.m5.24xlarge\'|\'ml.c4.xlarge\'|\'ml.c4.2xlarge\'|\'ml.c4.4xlarge\'|\'ml.c4.8xlarge\'|\'ml.p2.xlarge\'|\'ml.p2.8xlarge\'|\'ml.p2.16xlarge\'|\'ml.p3.2xlarge\'|\'ml.p3.8xlarge\'|\'ml.p3.16xlarge\'|\'ml.c5.xlarge\'|\'ml.c5.2xlarge\'|\'ml.c5.4xlarge\'|\'ml.c5.9xlarge\'|\'ml.c5.18xlarge\',
                    \'InstanceCount\': 123,
                    \'VolumeSizeInGB\': 123,
                    \'VolumeKmsKeyId\': \'string\'
                },
                \'VpcConfig\': {
                    \'SecurityGroupIds\': [
                        \'string\',
                    ],
                    \'Subnets\': [
                        \'string\',
                    ]
                },
                \'StoppingCondition\': {
                    \'MaxRuntimeInSeconds\': 123
                },
                \'CreationTime\': datetime(2015, 1, 1),
                \'TrainingStartTime\': datetime(2015, 1, 1),
                \'TrainingEndTime\': datetime(2015, 1, 1),
                \'LastModifiedTime\': datetime(2015, 1, 1),
                \'SecondaryStatusTransitions\': [
                    {
                        \'Status\': \'Starting\'|\'LaunchingMLInstances\'|\'PreparingTrainingStack\'|\'Downloading\'|\'DownloadingTrainingImage\'|\'Training\'|\'Uploading\'|\'Stopping\'|\'Stopped\'|\'MaxRuntimeExceeded\'|\'Completed\'|\'Failed\',
                        \'StartTime\': datetime(2015, 1, 1),
                        \'EndTime\': datetime(2015, 1, 1),
                        \'StatusMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TrainingJobName** *(string) --* 
        
              Name of the model training job. 
        
            - **TrainingJobArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the training job.
        
            - **TuningJobArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the associated hyperparameter tuning job if the training job was launched by a hyperparameter tuning job.
        
            - **ModelArtifacts** *(dict) --* 
        
              Information about the Amazon S3 location that is configured for storing model artifacts. 
        
              - **S3ModelArtifacts** *(string) --* 
        
                The path of the S3 object that contains the model artifacts. For example, ``s3://bucket-name/keynameprefix/model.tar.gz`` .
        
            - **TrainingJobStatus** *(string) --* 
        
              The status of the training job.
        
              Amazon SageMaker provides the following training job statuses:
        
              * ``InProgress`` - The training is in progress. 
               
              * ``Completed`` - The training job has completed. 
               
              * ``Failed`` - The training job has failed. To see the reason for the failure, see the ``FailureReason`` field in the response to a ``DescribeTrainingJobResponse`` call. 
               
              * ``Stopping`` - The training job is stopping. 
               
              * ``Stopped`` - The training job has stopped. 
               
              For more detailed information, see ``SecondaryStatus`` . 
        
            - **SecondaryStatus** *(string) --* 
        
              Provides detailed information about the state of the training job. For detailed information on the secondary status of the training job, see ``StatusMessage`` under  SecondaryStatusTransition .
        
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
        
              - **TrainingInputMode** *(string) --* 
        
                The input mode that the algorithm supports. For the input modes that Amazon SageMaker algorithms support, see `Algorithms <http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ . If an algorithm supports the ``File`` input mode, Amazon SageMaker downloads the training data from S3 to the provisioned ML storage Volume, and mounts the directory to docker volume for training container. If an algorithm supports the ``Pipe`` input mode, Amazon SageMaker streams data directly from S3 to the container. 
        
                In File mode, make sure you provision ML storage volume with sufficient capacity to accommodate the data download from S3. In addition to the training data, the ML storage volume also stores the output model. The algorithm container use ML storage volume to also store intermediate information, if any. 
        
                For distributed algorithms using File mode, training data is distributed uniformly, and your training duration is predictable if the input data objects size is approximately same. Amazon SageMaker does not split the files any further for model training. If the object sizes are skewed, training won\'t be optimal as the data distribution is also skewed where one host in a training cluster is overloaded, thus becoming bottleneck in training. 
        
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
        
                      If you choose ``S3Prefix`` , ``S3Uri`` identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for model training. 
        
                      If you choose ``ManifestFile`` , ``S3Uri`` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for model training. 
        
                    - **S3Uri** *(string) --* 
        
                      Depending on the value specified for the ``S3DataType`` , identifies either a key name prefix or a manifest. For example: 
        
                      * A key name prefix might look like this: ``s3://bucketname/exampleprefix`` .  
                       
                      * A manifest might look like this: ``s3://bucketname/example.manifest``   The manifest is an S3 object which is a JSON file with the following format:   ``[``    ``{\"prefix\": \"s3://customer_bucket/some/prefix/\"},``    ``\"relative/path/to/custdata-1\",``    ``\"relative/path/custdata-2\",``    ``...``    ``]``   The preceding JSON matches the following ``s3Uris`` :   ``s3://customer_bucket/some/prefix/relative/path/to/custdata-1``    ``s3://customer_bucket/some/prefix/relative/path/custdata-1``    ``...``   The complete set of ``s3uris`` in this manifest constitutes the input data for the channel for this datasource. The object that each ``s3uris`` points to must readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.  
                       
                    - **S3DataDistributionType** *(string) --* 
        
                      If you want Amazon SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify ``FullyReplicated`` . 
        
                      If you want Amazon SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify ``ShardedByS3Key`` . If there are *n* ML compute instances launched for a training job, each instance gets approximately 1/*n* of the number of S3 objects. In this case, model training on each machine uses only the subset of training data. 
        
                      Don\'t choose more ML compute instances for training than available S3 objects. If you do, some nodes won\'t get any data and you will pay for nodes that aren\'t getting any training data. This applies in both FILE and PIPE modes. Keep this in mind when developing algorithms. 
        
                      In distributed training, where you use multiple ML compute EC2 instances, you might choose ``ShardedByS3Key`` . If the algorithm requires copying training data to the ML storage volume (when ``TrainingInputMode`` is set to ``File`` ), this copies 1/*n* of the number of objects. 
        
                - **ContentType** *(string) --* 
        
                  The MIME type of the data.
        
                - **CompressionType** *(string) --* 
        
                  If training data is compressed, the compression type. The default value is ``None`` . ``CompressionType`` is used only in Pipe input mode. In File mode, leave this field unset or set it to None.
        
                - **RecordWrapperType** *(string) --* 
        
                  Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format, in which case, Amazon SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you don\'t need to set this attribute. For more information, see `Create a Dataset Using RecordIO <https://mxnet.incubator.apache.org/architecture/note_data_loading.html#data-format>`__ . 
        
                  In FILE mode, leave this field unset or set it to None.
        
                - **InputMode** *(string) --* 
            
            - **OutputDataConfig** *(dict) --* 
        
              The S3 path where model artifacts that you configured when creating the job are stored. Amazon SageMaker creates subfolders for model artifacts. 
        
              - **KmsKeyId** *(string) --* 
        
                The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The ``KmsKeyId`` can be any of the following formats: 
        
                * // KMS Key ID  ``\"1234abcd-12ab-34cd-56ef-1234567890ab\"``   
                 
                * // Amazon Resource Name (ARN) of a KMS Key  ``\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"``   
                 
                * // KMS Key Alias  ``\"alias/ExampleAlias\"``   
                 
                * // Amazon Resource Name (ARN) of a KMS Key Alias  ``\"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias\"``   
                 
                If you don\'t provide the KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role\'s account. For more information, see `KMS-Managed Encryption Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ in *Amazon Simple Storage Service Developer Guide.*  
        
                .. note::
        
                  The KMS key policy must grant permission to the IAM role that you specify in your ``CreateTrainingJob`` request. `Using Key Policies in AWS KMS <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the *AWS Key Management Service Developer Guide* . 
        
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
        
                * // KMS Key ID  ``\"1234abcd-12ab-34cd-56ef-1234567890ab\"``   
                 
                * // Amazon Resource Name (ARN) of a KMS Key  ``\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"``   
                 
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
        
                The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 5 days.
        
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
        
                An array element of  DescribeTrainingJobResponse$SecondaryStatusTransitions . It provides additional details about a status that the training job has transitioned through. A training job can be in one of several states, for example, starting, downloading, training, or uploading. Within each state, there are a number of intermediate states. For example, within the starting state, Amazon SageMaker could be starting the training job or launching the ML instances. These transitional states are referred to as the job\'s secondary status. 
        
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
        
                    Status messages are subject to change. Therefore, we recommend not including them in code that programmatically initiates actions. For examples, don\'t use status messages in if statements.
        
                  To have an overview of your training job\'s progress, view ``TrainingJobStatus`` and ``SecondaryStatus`` in  DescribeTrainingJobResponse , and ``StatusMessage`` together. For example, at the start of a training job, you might see the following:
        
                  * ``TrainingJobStatus`` - InProgress 
                   
                  * ``SecondaryStatus`` - Training 
                   
                  * ``StatusMessage`` - Downloading the training image 
                   
        """
        pass

    def describe_transform_job(self, TransformJobName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeTransformJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_transform_job(
              TransformJobName=\'string\'
          )
        :type TransformJobName: string
        :param TransformJobName: **[REQUIRED]** 
        
          The name of the transform job that you want to view details of.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TransformJobName\': \'string\',
                \'TransformJobArn\': \'string\',
                \'TransformJobStatus\': \'InProgress\'|\'Completed\'|\'Failed\'|\'Stopping\'|\'Stopped\',
                \'FailureReason\': \'string\',
                \'ModelName\': \'string\',
                \'MaxConcurrentTransforms\': 123,
                \'MaxPayloadInMB\': 123,
                \'BatchStrategy\': \'MultiRecord\'|\'SingleRecord\',
                \'Environment\': {
                    \'string\': \'string\'
                },
                \'TransformInput\': {
                    \'DataSource\': {
                        \'S3DataSource\': {
                            \'S3DataType\': \'ManifestFile\'|\'S3Prefix\',
                            \'S3Uri\': \'string\'
                        }
                    },
                    \'ContentType\': \'string\',
                    \'CompressionType\': \'None\'|\'Gzip\',
                    \'SplitType\': \'None\'|\'Line\'|\'RecordIO\'
                },
                \'TransformOutput\': {
                    \'S3OutputPath\': \'string\',
                    \'Accept\': \'string\',
                    \'AssembleWith\': \'None\'|\'Line\',
                    \'KmsKeyId\': \'string\'
                },
                \'TransformResources\': {
                    \'InstanceType\': \'ml.m4.xlarge\'|\'ml.m4.2xlarge\'|\'ml.m4.4xlarge\'|\'ml.m4.10xlarge\'|\'ml.m4.16xlarge\'|\'ml.c4.xlarge\'|\'ml.c4.2xlarge\'|\'ml.c4.4xlarge\'|\'ml.c4.8xlarge\'|\'ml.p2.xlarge\'|\'ml.p2.8xlarge\'|\'ml.p2.16xlarge\'|\'ml.p3.2xlarge\'|\'ml.p3.8xlarge\'|\'ml.p3.16xlarge\'|\'ml.c5.xlarge\'|\'ml.c5.2xlarge\'|\'ml.c5.4xlarge\'|\'ml.c5.9xlarge\'|\'ml.c5.18xlarge\'|\'ml.m5.large\'|\'ml.m5.xlarge\'|\'ml.m5.2xlarge\'|\'ml.m5.4xlarge\'|\'ml.m5.12xlarge\'|\'ml.m5.24xlarge\',
                    \'InstanceCount\': 123,
                    \'VolumeKmsKeyId\': \'string\'
                },
                \'CreationTime\': datetime(2015, 1, 1),
                \'TransformStartTime\': datetime(2015, 1, 1),
                \'TransformEndTime\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TransformJobName** *(string) --* 
        
              The name of the transform job.
        
            - **TransformJobArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the transform job.
        
            - **TransformJobStatus** *(string) --* 
        
              The status of the transform job. If the transform job failed, the reason is returned in the ``FailureReason`` field.
        
            - **FailureReason** *(string) --* 
        
              If the transform job failed, the reason that it failed.
        
            - **ModelName** *(string) --* 
        
              The name of the model used in the transform job.
        
            - **MaxConcurrentTransforms** *(integer) --* 
        
              The maximum number of parallel requests on each instance node that can be launched in a transform job. The default value is 1.
        
            - **MaxPayloadInMB** *(integer) --* 
        
              The maximum payload size , in MB used in the transform job.
        
            - **BatchStrategy** *(string) --* 
        
              SingleRecord means only one record was used per a batch. ``MultiRecord`` means batches contained as many records that could possibly fit within the ``MaxPayloadInMB`` limit.
        
            - **Environment** *(dict) --* 
        
              - *(string) --* 
                
                - *(string) --* 
          
            - **TransformInput** *(dict) --* 
        
              Describes the dataset to be transformed and the Amazon S3 location where it is stored.
        
              - **DataSource** *(dict) --* 
        
                Describes the location of the channel data, meaning the S3 location of the input data that the model can consume.
        
                - **S3DataSource** *(dict) --* 
        
                  The S3 location of the data source that is associated with a channel.
        
                  - **S3DataType** *(string) --* 
        
                    If you choose ``S3Prefix`` , ``S3Uri`` identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for batch transform. 
        
                    If you choose ``ManifestFile`` , ``S3Uri`` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for batch transform. 
        
                  - **S3Uri** *(string) --* 
        
                    Depending on the value specified for the ``S3DataType`` , identifies either a key name prefix or a manifest. For example:
        
                    * A key name prefix might look like this: ``s3://bucketname/exampleprefix`` .  
                     
                    * A manifest might look like this: ``s3://bucketname/example.manifest``   The manifest is an S3 object which is a JSON file with the following format:   ``[``    ``{\"prefix\": \"s3://customer_bucket/some/prefix/\"},``    ``\"relative/path/to/custdata-1\",``    ``\"relative/path/custdata-2\",``    ``...``    ``]``   The preceding JSON matches the following ``S3Uris`` :   ``s3://customer_bucket/some/prefix/relative/path/to/custdata-1``    ``s3://customer_bucket/some/prefix/relative/path/custdata-1``    ``...``   The complete set of ``S3Uris`` in this manifest constitutes the input data for the channel for this datasource. The object that each ``S3Uris`` points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf. 
                     
              - **ContentType** *(string) --* 
        
                The multipurpose internet mail extension (MIME) type of the data. Amazon SageMaker uses the MIME type with each http call to transfer data to the transform job.
        
              - **CompressionType** *(string) --* 
        
                Compressing data helps save on storage space. If your transform data is compressed, specify the compression type. Amazon SageMaker automatically decompresses the data for the transform job accordingly. The default value is ``None`` .
        
              - **SplitType** *(string) --* 
        
                The method to use to split the transform job\'s data into smaller batches. The default value is ``None`` . If you don\'t want to split the data, specify ``None`` . If you want to split records on a newline character boundary, specify ``Line`` . To split records according to the RecordIO format, specify ``RecordIO`` .
        
                Amazon SageMaker will send maximum number of records per batch in each request up to the MaxPayloadInMB limit. For more information, see `RecordIO data format <http://mxnet.io/architecture/note_data_loading.html#data-format>`__ .
        
                .. note::
        
                  For information about the ``RecordIO`` format, see `Data Format <http://mxnet.io/architecture/note_data_loading.html#data-format>`__ .
        
            - **TransformOutput** *(dict) --* 
        
              Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job.
        
              - **S3OutputPath** *(string) --* 
        
                The Amazon S3 path where you want Amazon SageMaker to store the results of the transform job. For example, ``s3://bucket-name/key-name-prefix`` .
        
                For every S3 object used as input for the transform job, the transformed data is stored in a corresponding subfolder in the location under the output prefix. For example, the input data ``s3://bucket-name/input-name-prefix/dataset01/data.csv`` will have the transformed data stored at ``s3://bucket-name/key-name-prefix/dataset01/`` , based on the original name, as a series of .part files (.part0001, part0002, etc).
        
              - **Accept** *(string) --* 
        
                The MIME type used to specify the output data. Amazon SageMaker uses the MIME type with each http call to transfer data from the transform job.
        
              - **AssembleWith** *(string) --* 
        
                Defines how to assemble the results of the transform job as a single S3 object. You should select a format that is most convenient to you. To concatenate the results in binary format, specify ``None`` . To add a newline character at the end of every transformed record, specify ``Line`` .
        
              - **KmsKeyId** *(string) --* 
        
                The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The ``KmsKeyId`` can be any of the following formats: 
        
                * // KMS Key ID  ``\"1234abcd-12ab-34cd-56ef-1234567890ab\"``   
                 
                * // Amazon Resource Name (ARN) of a KMS Key  ``\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"``   
                 
                * // KMS Key Alias  ``\"alias/ExampleAlias\"``   
                 
                * // Amazon Resource Name (ARN) of a KMS Key Alias  ``\"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias\"``   
                 
                If you don\'t provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role\'s account. For more information, see `KMS-Managed Encryption Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ in the *Amazon Simple Storage Service Developer Guide.*  
        
                The KMS key policy must grant permission to the IAM role that you specify in your ``CreateTramsformJob`` request. For more information, see `Using Key Policies in AWS KMS <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the *AWS Key Management Service Developer Guide* .
        
            - **TransformResources** *(dict) --* 
        
              Describes the resources, including ML instance types and ML instance count, to use for the transform job.
        
              - **InstanceType** *(string) --* 
        
                The ML compute instance type for the transform job. For using built-in algorithms to transform moderately sized datasets, ml.m4.xlarge or ``ml.m5.large`` should suffice. There is no default value for ``InstanceType`` .
        
              - **InstanceCount** *(integer) --* 
        
                The number of ML compute instances to use in the transform job. For distributed transform, provide a value greater than 1. The default value is ``1`` .
        
              - **VolumeKmsKeyId** *(string) --* 
        
                The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the batch transform job. The ``VolumeKmsKeyId`` can be any of the following formats:
        
                * // KMS Key ID  ``\"1234abcd-12ab-34cd-56ef-1234567890ab\"``   
                 
                * // Amazon Resource Name (ARN) of a KMS Key  ``\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"``   
                 
            - **CreationTime** *(datetime) --* 
        
              A timestamp that shows when the transform Job was created.
        
            - **TransformStartTime** *(datetime) --* 
        
              Indicates when the transform job starts on ML instances. You are billed for the time interval between this time and the value of ``TransformEndTime`` .
        
            - **TransformEndTime** *(datetime) --* 
        
              Indicates when the transform job is ``Completed`` , ``Stopped`` , or ``Failed`` . You are billed for the time interval between this time and the value of ``TransformStartTime`` .
        
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

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def list_endpoint_configs(self, SortBy: str = None, SortOrder: str = None, NextToken: str = None, MaxResults: int = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListEndpointConfigs>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_endpoint_configs(
              SortBy=\'Name\'|\'CreationTime\',
              SortOrder=\'Ascending\'|\'Descending\',
              NextToken=\'string\',
              MaxResults=123,
              NameContains=\'string\',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1)
          )
        :type SortBy: string
        :param SortBy: 
        
          The field to sort results by. The default is ``CreationTime`` .
        
        :type SortOrder: string
        :param SortOrder: 
        
          The sort order for results. The default is ``Ascending`` .
        
        :type NextToken: string
        :param NextToken: 
        
          If the result of the previous ``ListEndpointConfig`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of endpoint configurations, use the token in the next request. 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of training jobs to return in the response.
        
        :type NameContains: string
        :param NameContains: 
        
          A string in the endpoint configuration name. This filter returns only endpoint configurations whose name contains the specified string. 
        
        :type CreationTimeBefore: datetime
        :param CreationTimeBefore: 
        
          A filter that returns only endpoint configurations created before the specified time (timestamp).
        
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter: 
        
          A filter that returns only endpoint configurations created after the specified time (timestamp).
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of endpoint configurations, use it in the subsequent request 
        
        """
        pass

    def list_endpoints(self, SortBy: str = None, SortOrder: str = None, NextToken: str = None, MaxResults: int = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, StatusEquals: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListEndpoints>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_endpoints(
              SortBy=\'Name\'|\'CreationTime\'|\'Status\',
              SortOrder=\'Ascending\'|\'Descending\',
              NextToken=\'string\',
              MaxResults=123,
              NameContains=\'string\',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              StatusEquals=\'OutOfService\'|\'Creating\'|\'Updating\'|\'SystemUpdating\'|\'RollingBack\'|\'InService\'|\'Deleting\'|\'Failed\'
          )
        :type SortBy: string
        :param SortBy: 
        
          Sorts the list of results. The default is ``CreationTime`` .
        
        :type SortOrder: string
        :param SortOrder: 
        
          The sort order for results. The default is ``Ascending`` .
        
        :type NextToken: string
        :param NextToken: 
        
          If the result of a ``ListEndpoints`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of endpoints, use the token in the next request.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of endpoints to return in the response.
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of training jobs, use it in the subsequent request. 
        
        """
        pass

    def list_hyper_parameter_tuning_jobs(self, NextToken: str = None, MaxResults: int = None, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, StatusEquals: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListHyperParameterTuningJobs>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_hyper_parameter_tuning_jobs(
              NextToken=\'string\',
              MaxResults=123,
              SortBy=\'Name\'|\'Status\'|\'CreationTime\',
              SortOrder=\'Ascending\'|\'Descending\',
              NameContains=\'string\',
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              StatusEquals=\'Completed\'|\'InProgress\'|\'Failed\'|\'Stopped\'|\'Stopping\'
          )
        :type NextToken: string
        :param NextToken: 
        
          If the result of the previous ``ListHyperParameterTuningJobs`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of tuning jobs, use the token in the next request.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of tuning jobs to return. The default value is 10.
        
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
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'HyperParameterTuningJobSummaries\': [
                    {
                        \'HyperParameterTuningJobName\': \'string\',
                        \'HyperParameterTuningJobArn\': \'string\',
                        \'HyperParameterTuningJobStatus\': \'Completed\'|\'InProgress\'|\'Failed\'|\'Stopped\'|\'Stopping\',
                        \'Strategy\': \'Bayesian\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'HyperParameterTuningEndTime\': datetime(2015, 1, 1),
                        \'LastModifiedTime\': datetime(2015, 1, 1),
                        \'TrainingJobStatusCounters\': {
                            \'Completed\': 123,
                            \'InProgress\': 123,
                            \'RetryableError\': 123,
                            \'NonRetryableError\': 123,
                            \'Stopped\': 123
                        },
                        \'ObjectiveStatusCounters\': {
                            \'Succeeded\': 123,
                            \'Pending\': 123,
                            \'Failed\': 123
                        },
                        \'ResourceLimits\': {
                            \'MaxNumberOfTrainingJobs\': 123,
                            \'MaxParallelTrainingJobs\': 123
                        }
                    },
                ],
                \'NextToken\': \'string\'
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
        
                    The number of completed training jobs launched by a hyperparameter tuning job.
        
                  - **InProgress** *(integer) --* 
        
                    The number of in-progress training jobs launched by a hyperparameter tuning job.
        
                  - **RetryableError** *(integer) --* 
        
                    The number of training jobs that failed, but can be retried. A failed training job can be retried only if it failed because an internal service error occurred.
        
                  - **NonRetryableError** *(integer) --* 
        
                    The number of training jobs that failed and can\'t be retried. A failed training job can\'t be retried if it failed because a client error occurred.
        
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
        
            - **NextToken** *(string) --* 
        
              If the result of this ``ListHyperParameterTuningJobs`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of tuning jobs, use the token in the next request.
        
        """
        pass

    def list_models(self, SortBy: str = None, SortOrder: str = None, NextToken: str = None, MaxResults: int = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListModels>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_models(
              SortBy=\'Name\'|\'CreationTime\',
              SortOrder=\'Ascending\'|\'Descending\',
              NextToken=\'string\',
              MaxResults=123,
              NameContains=\'string\',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1)
          )
        :type SortBy: string
        :param SortBy: 
        
          Sorts the list of results. The default is ``CreationTime`` .
        
        :type SortOrder: string
        :param SortOrder: 
        
          The sort order for results. The default is ``Ascending`` .
        
        :type NextToken: string
        :param NextToken: 
        
          If the response to a previous ``ListModels`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of models, use the token in the next request.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of models to return in the response.
        
        :type NameContains: string
        :param NameContains: 
        
          A string in the training job name. This filter returns only models in the training job whose name contains the specified string.
        
        :type CreationTimeBefore: datetime
        :param CreationTimeBefore: 
        
          A filter that returns only models created before the specified time (timestamp).
        
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter: 
        
          A filter that returns only models created after the specified time (timestamp).
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of models, use it in the subsequent request. 
        
        """
        pass

    def list_notebook_instance_lifecycle_configs(self, NextToken: str = None, MaxResults: int = None, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListNotebookInstanceLifecycleConfigs>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_notebook_instance_lifecycle_configs(
              NextToken=\'string\',
              MaxResults=123,
              SortBy=\'Name\'|\'CreationTime\'|\'LastModifiedTime\',
              SortOrder=\'Ascending\'|\'Descending\',
              NameContains=\'string\',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1)
          )
        :type NextToken: string
        :param NextToken: 
        
          If the result of a ``ListNotebookInstanceLifecycleConfigs`` request was truncated, the response includes a ``NextToken`` . To get the next set of lifecycle configurations, use the token in the next request.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of lifecycle configurations to return in the response.
        
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
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'NotebookInstanceLifecycleConfigs\': [
                    {
                        \'NotebookInstanceLifecycleConfigName\': \'string\',
                        \'NotebookInstanceLifecycleConfigArn\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'LastModifiedTime\': datetime(2015, 1, 1)
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NextToken** *(string) --* 
        
              If the response is truncated, Amazon SageMaker returns this token. To get the next set of lifecycle configurations, use it in the next request. 
        
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
        
        """
        pass

    def list_notebook_instances(self, NextToken: str = None, MaxResults: int = None, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, StatusEquals: str = None, NotebookInstanceLifecycleConfigNameContains: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListNotebookInstances>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_notebook_instances(
              NextToken=\'string\',
              MaxResults=123,
              SortBy=\'Name\'|\'CreationTime\'|\'Status\',
              SortOrder=\'Ascending\'|\'Descending\',
              NameContains=\'string\',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              StatusEquals=\'Pending\'|\'InService\'|\'Stopping\'|\'Stopped\'|\'Failed\'|\'Deleting\'|\'Updating\',
              NotebookInstanceLifecycleConfigNameContains=\'string\'
          )
        :type NextToken: string
        :param NextToken: 
        
          If the previous call to the ``ListNotebookInstances`` is truncated, the response includes a ``NextToken`` . You can use this token in your subsequent ``ListNotebookInstances`` request to fetch the next set of notebook instances. 
        
          .. note::
        
            You might specify a filter or a sort order in your request. When response is truncated, you must use the same values for the filer and sort order in the next request. 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of notebook instances to return.
        
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
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
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
            
            - **NextToken** *(string) --* 
        
              If the response to the previous ``ListNotebookInstances`` request was truncated, Amazon SageMaker returns this token. To retrieve the next set of notebook instances, use the token in the next request.
        
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

    def list_tags(self, ResourceArn: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_tags(
              ResourceArn=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the resource whose tags you want to retrieve.
        
        :type NextToken: string
        :param NextToken: 
        
          If the response to the previous ``ListTags`` request is truncated, Amazon SageMaker returns this token. To retrieve the next set of tags, use it in the subsequent request. 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          Maximum number of tags to return.
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              If response is truncated, Amazon SageMaker includes a token in the response. You can use this token in your subsequent request to fetch next set of tokens. 
        
        """
        pass

    def list_training_jobs(self, NextToken: str = None, MaxResults: int = None, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTrainingJobs>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_training_jobs(
              NextToken=\'string\',
              MaxResults=123,
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              NameContains=\'string\',
              StatusEquals=\'InProgress\'|\'Completed\'|\'Failed\'|\'Stopping\'|\'Stopped\',
              SortBy=\'Name\'|\'CreationTime\'|\'Status\',
              SortOrder=\'Ascending\'|\'Descending\'
          )
        :type NextToken: string
        :param NextToken: 
        
          If the result of the previous ``ListTrainingJobs`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of training jobs, use the token in the next request. 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of training jobs to return in the response.
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of training jobs, use it in the subsequent request.
        
        """
        pass

    def list_training_jobs_for_hyper_parameter_tuning_job(self, HyperParameterTuningJobName: str, NextToken: str = None, MaxResults: int = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTrainingJobsForHyperParameterTuningJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_training_jobs_for_hyper_parameter_tuning_job(
              HyperParameterTuningJobName=\'string\',
              NextToken=\'string\',
              MaxResults=123,
              StatusEquals=\'InProgress\'|\'Completed\'|\'Failed\'|\'Stopping\'|\'Stopped\',
              SortBy=\'Name\'|\'CreationTime\'|\'Status\'|\'FinalObjectiveMetricValue\',
              SortOrder=\'Ascending\'|\'Descending\'
          )
        :type HyperParameterTuningJobName: string
        :param HyperParameterTuningJobName: **[REQUIRED]** 
        
          The name of the tuning job whose training jobs you want to list.
        
        :type NextToken: string
        :param NextToken: 
        
          If the result of the previous ``ListTrainingJobsForHyperParameterTuningJob`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of training jobs, use the token in the next request.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of training jobs to return. The default value is 10.
        
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
                        \'TrainingStartTime\': datetime(2015, 1, 1),
                        \'TrainingEndTime\': datetime(2015, 1, 1),
                        \'TrainingJobStatus\': \'InProgress\'|\'Completed\'|\'Failed\'|\'Stopping\'|\'Stopped\',
                        \'TunedHyperParameters\': {
                            \'string\': \'string\'
                        },
                        \'FailureReason\': \'string\',
                        \'FinalHyperParameterTuningJobObjectiveMetric\': {
                            \'Type\': \'Maximize\'|\'Minimize\',
                            \'MetricName\': \'string\',
                            \'Value\': ...
                        },
                        \'ObjectiveStatus\': \'Succeeded\'|\'Pending\'|\'Failed\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
                - **CreationTime** *(datetime) --* 
        
                  The date and time that the training job was created.
        
                - **TrainingStartTime** *(datetime) --* 
        
                  The date and time that the training job started.
        
                - **TrainingEndTime** *(datetime) --* 
        
                  The date and time that the training job ended.
        
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
                   
            - **NextToken** *(string) --* 
        
              If the result of this ``ListTrainingJobsForHyperParameterTuningJob`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of training jobs, use the token in the next request.
        
        """
        pass

    def list_transform_jobs(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTransformJobs>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_transform_jobs(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              NameContains=\'string\',
              StatusEquals=\'InProgress\'|\'Completed\'|\'Failed\'|\'Stopping\'|\'Stopped\',
              SortBy=\'Name\'|\'CreationTime\'|\'Status\',
              SortOrder=\'Ascending\'|\'Descending\',
              NextToken=\'string\',
              MaxResults=123
          )
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
        
        :type NextToken: string
        :param NextToken: 
        
          If the result of the previous ``ListTransformJobs`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of transform jobs, use the token in the next request.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of transform jobs to return in the response. The default value is ``10`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TransformJobSummaries\': [
                    {
                        \'TransformJobName\': \'string\',
                        \'TransformJobArn\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'TransformEndTime\': datetime(2015, 1, 1),
                        \'LastModifiedTime\': datetime(2015, 1, 1),
                        \'TransformJobStatus\': \'InProgress\'|\'Completed\'|\'Failed\'|\'Stopping\'|\'Stopped\',
                        \'FailureReason\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TransformJobSummaries** *(list) --* 
        
              An array of ``TransformJobSummary`` objects.
        
              - *(dict) --* 
        
                Provides a summary of a transform job. Multiple TransformJobSummary objects are returned as a list after calling  ListTransformJobs .
        
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
        
            - **NextToken** *(string) --* 
        
              If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of transform jobs, use it in the next request.
        
        """
        pass

    def start_notebook_instance(self, NotebookInstanceName: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/StartNotebookInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_notebook_instance(
              NotebookInstanceName=\'string\'
          )
        :type NotebookInstanceName: string
        :param NotebookInstanceName: **[REQUIRED]** 
        
          The name of the notebook instance to start.
        
        :returns: None
        """
        pass

    def stop_hyper_parameter_tuning_job(self, HyperParameterTuningJobName: str) -> NoReturn:
        """
        
        All model artifacts output from the training jobs are stored in Amazon Simple Storage Service (Amazon S3). All data that the training jobs write to Amazon CloudWatch Logs are still available in CloudWatch. After the tuning job moves to the ``Stopped`` state, it releases all reserved resources for the tuning job.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/StopHyperParameterTuningJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_hyper_parameter_tuning_job(
              HyperParameterTuningJobName=\'string\'
          )
        :type HyperParameterTuningJobName: string
        :param HyperParameterTuningJobName: **[REQUIRED]** 
        
          The name of the tuning job to stop.
        
        :returns: None
        """
        pass

    def stop_notebook_instance(self, NotebookInstanceName: str) -> NoReturn:
        """
        
        To access data on the ML storage volume for a notebook instance that has been terminated, call the ``StartNotebookInstance`` API. ``StartNotebookInstance`` launches another ML compute instance, configures it, and attaches the preserved ML storage volume so you can continue your work. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/StopNotebookInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_notebook_instance(
              NotebookInstanceName=\'string\'
          )
        :type NotebookInstanceName: string
        :param NotebookInstanceName: **[REQUIRED]** 
        
          The name of the notebook instance to terminate.
        
        :returns: None
        """
        pass

    def stop_training_job(self, TrainingJobName: str) -> NoReturn:
        """
        
        Training algorithms provided by Amazon SageMaker save the intermediate results of a model training job. This intermediate data is a valid model artifact. You can use the model artifacts that are saved when Amazon SageMaker stops a training job to create a model. 
        
        When it receives a ``StopTrainingJob`` request, Amazon SageMaker changes the status of the job to ``Stopping`` . After Amazon SageMaker stops the job, it sets the status to ``Stopped`` .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/StopTrainingJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_training_job(
              TrainingJobName=\'string\'
          )
        :type TrainingJobName: string
        :param TrainingJobName: **[REQUIRED]** 
        
          The name of the training job to stop.
        
        :returns: None
        """
        pass

    def stop_transform_job(self, TransformJobName: str) -> NoReturn:
        """
        
        When Amazon SageMaker receives a ``StopTransformJob`` request, the status of the job changes to ``Stopping`` . After Amazon SageMaker stops the job, the status is set to ``Stopped`` . When you stop a transform job before it is completed, Amazon SageMaker doesn\'t store the job\'s output in Amazon S3.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/StopTransformJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_transform_job(
              TransformJobName=\'string\'
          )
        :type TransformJobName: string
        :param TransformJobName: **[REQUIRED]** 
        
          The name of the transform job to stop.
        
        :returns: None
        """
        pass

    def update_endpoint(self, EndpointName: str, EndpointConfigName: str) -> Dict:
        """
        
        When Amazon SageMaker receives the request, it sets the endpoint status to ``Updating`` . After updating the endpoint, it sets the status to ``InService`` . To check the status of an endpoint, use the `DescribeEndpoint <http://docs.aws.amazon.com/sagemaker/latest/dg/API_DescribeEndpoint.html>`__ API. 
        
        .. note::
        
          You cannot update an endpoint with the current ``EndpointConfig`` . To update an endpoint, you must create a new ``EndpointConfig`` .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/UpdateEndpoint>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_endpoint(
              EndpointName=\'string\',
              EndpointConfigName=\'string\'
          )
        :type EndpointName: string
        :param EndpointName: **[REQUIRED]** 
        
          The name of the endpoint whose configuration you want to update.
        
        :type EndpointConfigName: string
        :param EndpointConfigName: **[REQUIRED]** 
        
          The name of the new endpoint configuration.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EndpointArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **EndpointArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the endpoint.
        
        """
        pass

    def update_endpoint_weights_and_capacities(self, EndpointName: str, DesiredWeightsAndCapacities: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/UpdateEndpointWeightsAndCapacities>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_endpoint_weights_and_capacities(
              EndpointName=\'string\',
              DesiredWeightsAndCapacities=[
                  {
                      \'VariantName\': \'string\',
                      \'DesiredWeight\': ...,
                      \'DesiredInstanceCount\': 123
                  },
              ]
          )
        :type EndpointName: string
        :param EndpointName: **[REQUIRED]** 
        
          The name of an existing Amazon SageMaker endpoint.
        
        :type DesiredWeightsAndCapacities: list
        :param DesiredWeightsAndCapacities: **[REQUIRED]** 
        
          An object that provides new capacity and weight values for a variant.
        
          - *(dict) --* 
        
            Specifies weight and capacity values for a production variant.
        
            - **VariantName** *(string) --* **[REQUIRED]** 
        
              The name of the variant to update.
        
            - **DesiredWeight** *(float) --* 
        
              The variant\'s weight.
        
            - **DesiredInstanceCount** *(integer) --* 
        
              The variant\'s capacity.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EndpointArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **EndpointArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the updated endpoint.
        
        """
        pass

    def update_notebook_instance(self, NotebookInstanceName: str, InstanceType: str = None, RoleArn: str = None, LifecycleConfigName: str = None, DisassociateLifecycleConfig: bool = None, VolumeSizeInGB: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/UpdateNotebookInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_notebook_instance(
              NotebookInstanceName=\'string\',
              InstanceType=\'ml.t2.medium\'|\'ml.t2.large\'|\'ml.t2.xlarge\'|\'ml.t2.2xlarge\'|\'ml.m4.xlarge\'|\'ml.m4.2xlarge\'|\'ml.m4.4xlarge\'|\'ml.m4.10xlarge\'|\'ml.m4.16xlarge\'|\'ml.p2.xlarge\'|\'ml.p2.8xlarge\'|\'ml.p2.16xlarge\'|\'ml.p3.2xlarge\'|\'ml.p3.8xlarge\'|\'ml.p3.16xlarge\',
              RoleArn=\'string\',
              LifecycleConfigName=\'string\',
              DisassociateLifecycleConfig=True|False,
              VolumeSizeInGB=123
          )
        :type NotebookInstanceName: string
        :param NotebookInstanceName: **[REQUIRED]** 
        
          The name of the notebook instance to update.
        
        :type InstanceType: string
        :param InstanceType: 
        
          The Amazon ML compute instance type.
        
        :type RoleArn: string
        :param RoleArn: 
        
          The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker can assume to access the notebook instance. For more information, see `Amazon SageMaker Roles <http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html>`__ . 
        
          .. note::
        
            To be able to pass this role to Amazon SageMaker, the caller of this API must have the ``iam:PassRole`` permission.
        
        :type LifecycleConfigName: string
        :param LifecycleConfigName: 
        
          The name of a lifecycle configuration to associate with the notebook instance. For information about lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <http://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
        
        :type DisassociateLifecycleConfig: boolean
        :param DisassociateLifecycleConfig: 
        
          Set to ``true`` to remove the notebook instance lifecycle configuration currently associated with the notebook instance.
        
        :type VolumeSizeInGB: integer
        :param VolumeSizeInGB: 
        
          The size, in GB, of the ML storage volume to attach to the notebook instance.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_notebook_instance_lifecycle_config(self, NotebookInstanceLifecycleConfigName: str, OnCreate: List = None, OnStart: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/UpdateNotebookInstanceLifecycleConfig>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_notebook_instance_lifecycle_config(
              NotebookInstanceLifecycleConfigName=\'string\',
              OnCreate=[
                  {
                      \'Content\': \'string\'
                  },
              ],
              OnStart=[
                  {
                      \'Content\': \'string\'
                  },
              ]
          )
        :type NotebookInstanceLifecycleConfigName: string
        :param NotebookInstanceLifecycleConfigName: **[REQUIRED]** 
        
          The name of the lifecycle configuration.
        
        :type OnCreate: list
        :param OnCreate: 
        
          The shell script that runs only once, when you create a notebook instance
        
          - *(dict) --* 
        
            Contains the notebook instance lifecycle configuration script.
        
            Each lifecycle configuration script has a limit of 16384 characters.
        
            The value of the ``$PATH`` environment variable that is available to both scripts is ``/sbin:bin:/usr/sbin:/usr/bin`` .
        
            View CloudWatch Logs for notebook instance lifecycle configurations in log group ``/aws/sagemaker/NotebookInstances`` in log stream ``[notebook-instance-name]/[LifecycleConfigHook]`` .
        
            Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for longer than 5 minutes, it fails and the notebook instance is not created or started.
        
            For information about notebook instance lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <http://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
        
            - **Content** *(string) --* 
        
              A base64-encoded string that contains a shell script for a notebook instance lifecycle configuration.
        
        :type OnStart: list
        :param OnStart: 
        
          The shell script that runs every time you start a notebook instance, including when you create the notebook instance.
        
          - *(dict) --* 
        
            Contains the notebook instance lifecycle configuration script.
        
            Each lifecycle configuration script has a limit of 16384 characters.
        
            The value of the ``$PATH`` environment variable that is available to both scripts is ``/sbin:bin:/usr/sbin:/usr/bin`` .
        
            View CloudWatch Logs for notebook instance lifecycle configurations in log group ``/aws/sagemaker/NotebookInstances`` in log stream ``[notebook-instance-name]/[LifecycleConfigHook]`` .
        
            Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for longer than 5 minutes, it fails and the notebook instance is not created or started.
        
            For information about notebook instance lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <http://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
        
            - **Content** *(string) --* 
        
              A base64-encoded string that contains a shell script for a notebook instance lifecycle configuration.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass
