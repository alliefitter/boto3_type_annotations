from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from botocore.paginate import Paginator
from datetime import datetime
from botocore.waiter import Waiter
from typing import Union
from typing import List


class Client(BaseClient):
    def add_tags(self, ResourceArn: str, Tags: List) -> Dict:
        """
        Adds or overwrites one or more tags for the specified Amazon SageMaker resource. You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, models, endpoint configurations, and endpoints.
        Each tag consists of a key and an optional value. Tag keys must be unique per resource. For more information about tags, see For more information, see `AWS Tagging Strategies <https://aws.amazon.com/answers/account-management/aws-tagging-strategies/>`__ .
        .. note::
          Tags that you add to a hyperparameter tuning job by calling this API are also added to any training jobs that the hyperparameter tuning job launches after you call this API, but not to training jobs that the hyperparameter tuning job launched before you called this API. To make sure that the tags associated with a hyperparameter tuning job are also added to all training jobs that the hyperparameter tuning job launches, add the tags when you first create the tuning job by specifying them in the ``Tags`` parameter of  CreateHyperParameterTuningJob  
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/AddTags>`_
        
        **Request Syntax**
        ::
          response = client.add_tags(
              ResourceArn='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
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
        """
        pass

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

    def create_algorithm(self, AlgorithmName: str, TrainingSpecification: Dict, AlgorithmDescription: str = None, InferenceSpecification: Dict = None, ValidationSpecification: Dict = None, CertifyForMarketplace: bool = None) -> Dict:
        """
        Create a machine learning algorithm that you can use in Amazon SageMaker and list in the AWS Marketplace.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateAlgorithm>`_
        
        **Request Syntax**
        ::
          response = client.create_algorithm(
              AlgorithmName='string',
              AlgorithmDescription='string',
              TrainingSpecification={
                  'TrainingImage': 'string',
                  'TrainingImageDigest': 'string',
                  'SupportedHyperParameters': [
                      {
                          'Name': 'string',
                          'Description': 'string',
                          'Type': 'Integer'|'Continuous'|'Categorical'|'FreeText',
                          'Range': {
                              'IntegerParameterRangeSpecification': {
                                  'MinValue': 'string',
                                  'MaxValue': 'string'
                              },
                              'ContinuousParameterRangeSpecification': {
                                  'MinValue': 'string',
                                  'MaxValue': 'string'
                              },
                              'CategoricalParameterRangeSpecification': {
                                  'Values': [
                                      'string',
                                  ]
                              }
                          },
                          'IsTunable': True|False,
                          'IsRequired': True|False,
                          'DefaultValue': 'string'
                      },
                  ],
                  'SupportedTrainingInstanceTypes': [
                      'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
                  ],
                  'SupportsDistributedTraining': True|False,
                  'MetricDefinitions': [
                      {
                          'Name': 'string',
                          'Regex': 'string'
                      },
                  ],
                  'TrainingChannels': [
                      {
                          'Name': 'string',
                          'Description': 'string',
                          'IsRequired': True|False,
                          'SupportedContentTypes': [
                              'string',
                          ],
                          'SupportedCompressionTypes': [
                              'None'|'Gzip',
                          ],
                          'SupportedInputModes': [
                              'Pipe'|'File',
                          ]
                      },
                  ],
                  'SupportedTuningJobObjectiveMetrics': [
                      {
                          'Type': 'Maximize'|'Minimize',
                          'MetricName': 'string'
                      },
                  ]
              },
              InferenceSpecification={
                  'Containers': [
                      {
                          'ContainerHostname': 'string',
                          'Image': 'string',
                          'ImageDigest': 'string',
                          'ModelDataUrl': 'string',
                          'ProductId': 'string'
                      },
                  ],
                  'SupportedTransformInstanceTypes': [
                      'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge',
                  ],
                  'SupportedRealtimeInferenceInstanceTypes': [
                      'ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.large'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.large'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
                  ],
                  'SupportedContentTypes': [
                      'string',
                  ],
                  'SupportedResponseMIMETypes': [
                      'string',
                  ]
              },
              ValidationSpecification={
                  'ValidationRole': 'string',
                  'ValidationProfiles': [
                      {
                          'ProfileName': 'string',
                          'TrainingJobDefinition': {
                              'TrainingInputMode': 'Pipe'|'File',
                              'HyperParameters': {
                                  'string': 'string'
                              },
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
                              'StoppingCondition': {
                                  'MaxRuntimeInSeconds': 123
                              }
                          },
                          'TransformJobDefinition': {
                              'MaxConcurrentTransforms': 123,
                              'MaxPayloadInMB': 123,
                              'BatchStrategy': 'MultiRecord'|'SingleRecord',
                              'Environment': {
                                  'string': 'string'
                              },
                              'TransformInput': {
                                  'DataSource': {
                                      'S3DataSource': {
                                          'S3DataType': 'ManifestFile'|'S3Prefix'|'AugmentedManifestFile',
                                          'S3Uri': 'string'
                                      }
                                  },
                                  'ContentType': 'string',
                                  'CompressionType': 'None'|'Gzip',
                                  'SplitType': 'None'|'Line'|'RecordIO'|'TFRecord'
                              },
                              'TransformOutput': {
                                  'S3OutputPath': 'string',
                                  'Accept': 'string',
                                  'AssembleWith': 'None'|'Line',
                                  'KmsKeyId': 'string'
                              },
                              'TransformResources': {
                                  'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge',
                                  'InstanceCount': 123,
                                  'VolumeKmsKeyId': 'string'
                              }
                          }
                      },
                  ]
              },
              CertifyForMarketplace=True|False
          )
        
        **Response Syntax**
        ::
            {
                'AlgorithmArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AlgorithmArn** *(string) --* 
              The Amazon Resource Name (ARN) of the new algorithm.
        :type AlgorithmName: string
        :param AlgorithmName: **[REQUIRED]**
          The name of the algorithm.
        :type AlgorithmDescription: string
        :param AlgorithmDescription:
          A description of the algorithm.
        :type TrainingSpecification: dict
        :param TrainingSpecification: **[REQUIRED]**
          Specifies details about training jobs run by this algorithm, including the following:
          * The Amazon ECR path of the container and the version digest of the algorithm.
          * The hyperparameters that the algorithm supports.
          * The instance types that the algorithm supports for training.
          * Whether the algorithm supports distributed training.
          * The metrics that the algorithm emits to Amazon CloudWatch.
          * Which metrics that the algorithm emits can be used as the objective metric for hyperparameter tuning jobs.
          * The input channels that the algorithm supports for training data. For example, an algorithm might support ``train`` , ``validation`` , and ``test`` channels.
          - **TrainingImage** *(string) --* **[REQUIRED]**
            The Amazon ECR registry path of the Docker image that contains the training algorithm.
          - **TrainingImageDigest** *(string) --*
            An MD5 hash of the training algorithm that identifies the Docker image used for training.
          - **SupportedHyperParameters** *(list) --*
            A list of the ``HyperParameterSpecification`` objects, that define the supported hyperparameters. This is required if the algorithm supports automatic model tuning.>
            - *(dict) --*
              Defines a hyperparameter to be used by an algorithm.
              - **Name** *(string) --* **[REQUIRED]**
                The name of this hyperparameter. The name must be unique.
              - **Description** *(string) --*
                A brief description of the hyperparameter.
              - **Type** *(string) --* **[REQUIRED]**
                The type of this hyperparameter. The valid types are ``Integer`` , ``Continuous`` , ``Categorical`` , and ``FreeText`` .
              - **Range** *(dict) --*
                The allowed range for this hyperparameter.
                - **IntegerParameterRangeSpecification** *(dict) --*
                  A ``IntegerParameterRangeSpecification`` object that defines the possible values for an integer hyperparameter.
                  - **MinValue** *(string) --* **[REQUIRED]**
                    The minimum integer value allowed.
                  - **MaxValue** *(string) --* **[REQUIRED]**
                    The maximum integer value allowed.
                - **ContinuousParameterRangeSpecification** *(dict) --*
                  A ``ContinuousParameterRangeSpecification`` object that defines the possible values for a continuous hyperparameter.
                  - **MinValue** *(string) --* **[REQUIRED]**
                    The minimum floating-point value allowed.
                  - **MaxValue** *(string) --* **[REQUIRED]**
                    The maximum floating-point value allowed.
                - **CategoricalParameterRangeSpecification** *(dict) --*
                  A ``CategoricalParameterRangeSpecification`` object that defines the possible values for a categorical hyperparameter.
                  - **Values** *(list) --* **[REQUIRED]**
                    The allowed categories for the hyperparameter.
                    - *(string) --*
              - **IsTunable** *(boolean) --*
                Indicates whether this hyperparameter is tunable in a hyperparameter tuning job.
              - **IsRequired** *(boolean) --*
                Indicates whether this hyperparameter is required.
              - **DefaultValue** *(string) --*
                The default value for this hyperparameter. If a default value is specified, a hyperparameter cannot be required.
          - **SupportedTrainingInstanceTypes** *(list) --* **[REQUIRED]**
            A list of the instance types that this algorithm can use for training.
            - *(string) --*
          - **SupportsDistributedTraining** *(boolean) --*
            Indicates whether the algorithm supports distributed training. If set to false, buyers can’t request more than one instance during training.
          - **MetricDefinitions** *(list) --*
            A list of ``MetricDefinition`` objects, which are used for parsing metrics generated by the algorithm.
            - *(dict) --*
              Specifies a metric that the training algorithm writes to ``stderr`` or ``stdout`` . Amazon SageMakerhyperparameter tuning captures all defined metrics. You specify one metric that a hyperparameter tuning job uses as its objective metric to choose the best training job.
              - **Name** *(string) --* **[REQUIRED]**
                The name of the metric.
              - **Regex** *(string) --* **[REQUIRED]**
                A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see `Defining Objective Metrics <https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics.html>`__ .
          - **TrainingChannels** *(list) --* **[REQUIRED]**
            A list of ``ChannelSpecification`` objects, which specify the input sources to be used by the algorithm.
            - *(dict) --*
              Defines a named input source, called a channel, to be used by an algorithm.
              - **Name** *(string) --* **[REQUIRED]**
                The name of the channel.
              - **Description** *(string) --*
                A brief description of the channel.
              - **IsRequired** *(boolean) --*
                Indicates whether the channel is required by the algorithm.
              - **SupportedContentTypes** *(list) --* **[REQUIRED]**
                The supported MIME types for the data.
                - *(string) --*
              - **SupportedCompressionTypes** *(list) --*
                The allowed compression types, if data compression is used.
                - *(string) --*
              - **SupportedInputModes** *(list) --* **[REQUIRED]**
                The allowed input mode, either FILE or PIPE.
                In FILE mode, Amazon SageMaker copies the data from the input source onto the local Amazon Elastic Block Store (Amazon EBS) volumes before starting your training algorithm. This is the most commonly used input mode.
                In PIPE mode, Amazon SageMaker streams input data from the source directly to your algorithm without using the EBS volume.
                - *(string) --*
          - **SupportedTuningJobObjectiveMetrics** *(list) --*
            A list of the metrics that the algorithm emits that can be used as the objective metric in a hyperparameter tuning job.
            - *(dict) --*
              Defines the objective metric for a hyperparameter tuning job. Hyperparameter tuning uses the value of this metric to evaluate the training jobs it launches, and returns the training job that results in either the highest or lowest value for this metric, depending on the value you specify for the ``Type`` parameter.
              - **Type** *(string) --* **[REQUIRED]**
                Whether to minimize or maximize the objective metric.
              - **MetricName** *(string) --* **[REQUIRED]**
                The name of the metric to use for the objective metric.
        :type InferenceSpecification: dict
        :param InferenceSpecification:
          Specifies details about inference jobs that the algorithm runs, including the following:
          * The Amazon ECR paths of containers that contain the inference code and model artifacts.
          * The instance types that the algorithm supports for transform jobs and real-time endpoints used for inference.
          * The input and output content formats that the algorithm supports for inference.
          - **Containers** *(list) --* **[REQUIRED]**
            The Amazon ECR registry path of the Docker image that contains the inference code.
            - *(dict) --*
              Describes the Docker container for the model package.
              - **ContainerHostname** *(string) --*
                The DNS host name for the Docker container.
              - **Image** *(string) --* **[REQUIRED]**
                The Amazon EC2 Container Registry (Amazon ECR) path where inference code is stored.
                If you are using your own custom algorithm instead of an algorithm provided by Amazon SageMaker, the inference code must meet Amazon SageMaker requirements. Amazon SageMaker supports both ``registry/repository[:tag]`` and ``registry/repository[@digest]`` image path formats. For more information, see `Using Your Own Algorithms with Amazon SageMaker <https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__ .
              - **ImageDigest** *(string) --*
                An MD5 hash of the training algorithm that identifies the Docker image used for training.
              - **ModelDataUrl** *(string) --*
                The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single ``gzip`` compressed tar archive (``.tar.gz`` suffix).
              - **ProductId** *(string) --*
                The AWS Marketplace product ID of the model package.
          - **SupportedTransformInstanceTypes** *(list) --* **[REQUIRED]**
            A list of the instance types on which a transformation job can be run or on which an endpoint can be deployed.
            - *(string) --*
          - **SupportedRealtimeInferenceInstanceTypes** *(list) --* **[REQUIRED]**
            A list of the instance types that are used to generate inferences in real-time.
            - *(string) --*
          - **SupportedContentTypes** *(list) --* **[REQUIRED]**
            The supported MIME types for the input data.
            - *(string) --*
          - **SupportedResponseMIMETypes** *(list) --* **[REQUIRED]**
            The supported MIME types for the output data.
            - *(string) --*
        :type ValidationSpecification: dict
        :param ValidationSpecification:
          Specifies configurations for one or more training jobs and that Amazon SageMaker runs to test the algorithm\'s training code and, optionally, one or more batch transform jobs that Amazon SageMaker runs to test the algorithm\'s inference code.
          - **ValidationRole** *(string) --* **[REQUIRED]**
            The IAM roles that Amazon SageMaker uses to run the training jobs.
          - **ValidationProfiles** *(list) --* **[REQUIRED]**
            An array of ``AlgorithmValidationProfile`` objects, each of which specifies a training job and batch transform job that Amazon SageMaker runs to validate your algorithm.
            - *(dict) --*
              Defines a training job and a batch transform job that Amazon SageMaker runs to validate your algorithm.
              The data provided in the validation profile is made available to your buyers on AWS Marketplace.
              - **ProfileName** *(string) --* **[REQUIRED]**
                The name of the profile for the algorithm. The name must have 1 to 63 characters. Valid characters are a-z, A-Z, 0-9, and - (hyphen).
              - **TrainingJobDefinition** *(dict) --* **[REQUIRED]**
                The ``TrainingJobDefinition`` object that describes the training job that Amazon SageMaker runs to validate your algorithm.
                - **TrainingInputMode** *(string) --* **[REQUIRED]**
                  The input mode used by the algorithm for the training job. For the input modes that Amazon SageMaker algorithms support, see `Algorithms <https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ .
                  If an algorithm supports the ``File`` input mode, Amazon SageMaker downloads the training data from S3 to the provisioned ML storage Volume, and mounts the directory to docker volume for training container. If an algorithm supports the ``Pipe`` input mode, Amazon SageMaker streams data directly from S3 to the container.
                - **HyperParameters** *(dict) --*
                  The hyperparameters used for the training job.
                  - *(string) --*
                    - *(string) --*
                - **InputDataConfig** *(list) --* **[REQUIRED]**
                  An array of ``Channel`` objects, each of which specifies an input source.
                  - *(dict) --*
                    A channel is a named input source that training algorithms can consume.
                    - **ChannelName** *(string) --* **[REQUIRED]**
                      The name of the channel.
                    - **DataSource** *(dict) --* **[REQUIRED]**
                      The location of the channel data.
                      - **S3DataSource** *(dict) --* **[REQUIRED]**
                        The S3 location of the data source that is associated with a channel.
                        - **S3DataType** *(string) --* **[REQUIRED]**
                          If you choose ``S3Prefix`` , ``S3Uri`` identifies a key name prefix. Amazon SageMaker uses all objects that match the specified key name prefix for model training.
                          If you choose ``ManifestFile`` , ``S3Uri`` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for model training.
                          If you choose ``AugmentedManifestFile`` , S3Uri identifies an object that is an augmented manifest file in JSON lines format. This file contains the data you want to use for model training. ``AugmentedManifestFile`` can only be used if the Channel\'s input mode is ``Pipe`` .
                        - **S3Uri** *(string) --* **[REQUIRED]**
                          Depending on the value specified for the ``S3DataType`` , identifies either a key name prefix or a manifest. For example:
                          * A key name prefix might look like this: ``s3://bucketname/exampleprefix`` .
                          * A manifest might look like this: ``s3://bucketname/example.manifest``   The manifest is an S3 object which is a JSON file with the following format:   ``[``    ``{\"prefix\": \"s3://customer_bucket/some/prefix/\"},``    ``\"relative/path/to/custdata-1\",``    ``\"relative/path/custdata-2\",``    ``...``    ``]``   The preceding JSON matches the following ``s3Uris`` :   ``s3://customer_bucket/some/prefix/relative/path/to/custdata-1``    ``s3://customer_bucket/some/prefix/relative/path/custdata-2``    ``...``   The complete set of ``s3uris`` in this manifest is the input data for the channel for this datasource. The object that each ``s3uris`` points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.
                        - **S3DataDistributionType** *(string) --*
                          If you want Amazon SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify ``FullyReplicated`` .
                          If you want Amazon SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify ``ShardedByS3Key`` . If there are *n* ML compute instances launched for a training job, each instance gets approximately 1/*n* of the number of S3 objects. In this case, model training on each machine uses only the subset of training data.
                          Don\'t choose more ML compute instances for training than available S3 objects. If you do, some nodes won\'t get any data and you will pay for nodes that aren\'t getting any training data. This applies in both File and Pipe modes. Keep this in mind when developing algorithms.
                          In distributed training, where you use multiple ML compute EC2 instances, you might choose ``ShardedByS3Key`` . If the algorithm requires copying training data to the ML storage volume (when ``TrainingInputMode`` is set to ``File`` ), this copies 1/*n* of the number of objects.
                        - **AttributeNames** *(list) --*
                          A list of one or more attribute names to use that are found in a specified augmented manifest file.
                          - *(string) --*
                    - **ContentType** *(string) --*
                      The MIME type of the data.
                    - **CompressionType** *(string) --*
                      If training data is compressed, the compression type. The default value is ``None`` . ``CompressionType`` is used only in Pipe input mode. In File mode, leave this field unset or set it to None.
                    - **RecordWrapperType** *(string) --*
                      Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format. In this case, Amazon SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you don\'t need to set this attribute. For more information, see `Create a Dataset Using RecordIO <https://mxnet.incubator.apache.org/architecture/note_data_loading.html#data-format>`__ .
                      In File mode, leave this field unset or set it to None.
                    - **InputMode** *(string) --*
                      (Optional) The input mode to use for the data channel in a training job. If you don\'t set a value for ``InputMode`` , Amazon SageMaker uses the value set for ``TrainingInputMode`` . Use this parameter to override the ``TrainingInputMode`` setting in a  AlgorithmSpecification request when you have a channel that needs a different input mode from the training job\'s general setting. To download the data from Amazon Simple Storage Service (Amazon S3) to the provisioned ML storage volume, and mount the directory to a Docker volume, use ``File`` input mode. To stream data directly from Amazon S3 to the container, choose ``Pipe`` input mode.
                      To use a model for incremental training, choose ``File`` input model.
                    - **ShuffleConfig** *(dict) --*
                      A configuration for a shuffle option for input data in a channel. If you use ``S3Prefix`` for ``S3DataType`` , this shuffles the results of the S3 key prefix matches. If you use ``ManifestFile`` , the order of the S3 object references in the ``ManifestFile`` is shuffled. If you use ``AugmentedManifestFile`` , the order of the JSON lines in the ``AugmentedManifestFile`` is shuffled. The shuffling order is determined using the ``Seed`` value.
                      For Pipe input mode, shuffling is done at the start of every epoch. With large datasets this ensures that the order of the training data is different for each epoch, it helps reduce bias and possible overfitting. In a multi-node training job when ShuffleConfig is combined with ``S3DataDistributionType`` of ``ShardedByS3Key`` , the data is shuffled across nodes so that the content sent to a particular node on the first epoch might be sent to a different node on the second epoch.
                      - **Seed** *(integer) --* **[REQUIRED]**
                        Determines the shuffling order in ``ShuffleConfig`` value.
                - **OutputDataConfig** *(dict) --* **[REQUIRED]**
                  the path to the S3 bucket where you want to store model artifacts. Amazon SageMaker creates subfolders for the artifacts.
                  - **KmsKeyId** *(string) --*
                    The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The ``KmsKeyId`` can be any of the following formats:
                    * // KMS Key ID  ``\"1234abcd-12ab-34cd-56ef-1234567890ab\"``
                    * // Amazon Resource Name (ARN) of a KMS Key  ``\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"``
                    * // KMS Key Alias  ``\"alias/ExampleAlias\"``
                    * // Amazon Resource Name (ARN) of a KMS Key Alias  ``\"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias\"``
                    If you don\'t provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role\'s account. For more information, see `KMS-Managed Encryption Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ in the *Amazon Simple Storage Service Developer Guide.*
                    The KMS key policy must grant permission to the IAM role that you specify in your ``CreateTramsformJob`` request. For more information, see `Using Key Policies in AWS KMS <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the *AWS Key Management Service Developer Guide* .
                  - **S3OutputPath** *(string) --* **[REQUIRED]**
                    Identifies the S3 path where you want Amazon SageMaker to store the model artifacts. For example, ``s3://bucket-name/key-name-prefix`` .
                - **ResourceConfig** *(dict) --* **[REQUIRED]**
                  The resources, including the ML compute instances and ML storage volumes, to use for model training.
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
                  Sets a duration for training. Use this parameter to cap model training costs.
                  To stop a job, Amazon SageMaker sends the algorithm the SIGTERM signal, which delays job termination for 120 seconds. Algorithms might use this 120-second window to save the model artifacts.
                  - **MaxRuntimeInSeconds** *(integer) --*
                    The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 28 days.
              - **TransformJobDefinition** *(dict) --*
                The ``TransformJobDefinition`` object that describes the transform job that Amazon SageMaker runs to validate your algorithm.
                - **MaxConcurrentTransforms** *(integer) --*
                  The maximum number of parallel requests that can be sent to each instance in a transform job. The default value is 1.
                - **MaxPayloadInMB** *(integer) --*
                  The maximum payload size allowed, in MB. A payload is the data portion of a record (without metadata).
                - **BatchStrategy** *(string) --*
                  A string that determines the number of records included in a single mini-batch.
                   ``SingleRecord`` means only one record is used per mini-batch. ``MultiRecord`` means a mini-batch is set to contain as many records that can fit within the ``MaxPayloadInMB`` limit.
                - **Environment** *(dict) --*
                  The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.
                  - *(string) --*
                    - *(string) --*
                - **TransformInput** *(dict) --* **[REQUIRED]**
                  A description of the input source and the way the transform job consumes it.
                  - **DataSource** *(dict) --* **[REQUIRED]**
                    Describes the location of the channel data, which is, the S3 location of the input data that the model can consume.
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
                    If your transform data is compressed, specify the compression type. Amazon SageMaker automatically decompresses the data for the transform job accordingly. The default value is ``None`` .
                  - **SplitType** *(string) --*
                    The method to use to split the transform job\'s data files into smaller batches. Splitting is necessary when the total size of each object is too large to fit in a single request. You can also use data splitting to improve performance by processing multiple concurrent mini-batches. The default value for ``SplitType`` is ``None`` , which indicates that input data files are not split, and request payloads contain the entire contents of an input object. Set the value of this parameter to ``Line`` to split records on a newline character boundary. ``SplitType`` also supports a number of record-oriented binary data formats.
                    When splitting is enabled, the size of a mini-batch depends on the values of the ``BatchStrategy`` and ``MaxPayloadInMB`` parameters. When the value of ``BatchStrategy`` is ``MultiRecord`` , Amazon SageMaker sends the maximum number of records in each request, up to the ``MaxPayloadInMB`` limit. If the value of ``BatchStrategy`` is ``SingleRecord`` , Amazon SageMaker sends individual records in each request.
                    .. note::
                      Some data formats represent a record as a binary payload wrapped with extra padding bytes. When splitting is applied to a binary data format, padding is removed if the value of ``BatchStrategy`` is set to ``SingleRecord`` . Padding is not removed if the value of ``BatchStrategy`` is set to ``MultiRecord`` .
                      For more information about the RecordIO, see `Data Format <http://mxnet.io/architecture/note_data_loading.html#data-format>`__ in the MXNet documentation. For more information about the TFRecord, see `Consuming TFRecord data <https://www.tensorflow.org/guide/datasets#consuming_tfrecord_data>`__ in the TensorFlow documentation.
                - **TransformOutput** *(dict) --* **[REQUIRED]**
                  Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job.
                  - **S3OutputPath** *(string) --* **[REQUIRED]**
                    The Amazon S3 path where you want Amazon SageMaker to store the results of the transform job. For example, ``s3://bucket-name/key-name-prefix`` .
                    For every S3 object used as input for the transform job, batch transform stores the transformed data with an .``out`` suffix in a corresponding subfolder in the location in the output prefix. For example, for the input data stored at ``s3://bucket-name/input-name-prefix/dataset01/data.csv`` , batch transform stores the transformed data at ``s3://bucket-name/output-name-prefix/input-name-prefix/data.csv.out`` . Batch transform doesn\'t upload partially processed objects. For an input S3 object that contains multiple records, it creates an .``out`` file only if the transform job succeeds on the entire file. When the input contains multiple S3 objects, the batch transform job processes the listed S3 objects and uploads only the output for successfully processed objects. If any object fails in the transform job batch transform marks the job as failed to prompt investigation.
                  - **Accept** *(string) --*
                    The MIME type used to specify the output data. Amazon SageMaker uses the MIME type with each http call to transfer data from the transform job.
                  - **AssembleWith** *(string) --*
                    Defines how to assemble the results of the transform job as a single S3 object. Choose a format that is most convenient to you. To concatenate the results in binary format, specify ``None`` . To add a newline character at the end of every transformed record, specify ``Line`` .
                  - **KmsKeyId** *(string) --*
                    The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The ``KmsKeyId`` can be any of the following formats:
                    * // KMS Key ID  ``\"1234abcd-12ab-34cd-56ef-1234567890ab\"``
                    * // Amazon Resource Name (ARN) of a KMS Key  ``\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"``
                    * // KMS Key Alias  ``\"alias/ExampleAlias\"``
                    * // Amazon Resource Name (ARN) of a KMS Key Alias  ``\"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias\"``
                    If you don\'t provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role\'s account. For more information, see `KMS-Managed Encryption Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ in the *Amazon Simple Storage Service Developer Guide.*
                    The KMS key policy must grant permission to the IAM role that you specify in your ``CreateTramsformJob`` request. For more information, see `Using Key Policies in AWS KMS <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the *AWS Key Management Service Developer Guide* .
                - **TransformResources** *(dict) --* **[REQUIRED]**
                  Identifies the ML compute instances for the transform job.
                  - **InstanceType** *(string) --* **[REQUIRED]**
                    The ML compute instance type for the transform job. For using built-in algorithms to transform moderately sized datasets, ml.m4.xlarge or ``ml.m5.large`` should suffice. There is no default value for ``InstanceType`` .
                  - **InstanceCount** *(integer) --* **[REQUIRED]**
                    The number of ML compute instances to use in the transform job. For distributed transform, provide a value greater than 1. The default value is ``1`` .
                  - **VolumeKmsKeyId** *(string) --*
                    The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the batch transform job. The ``VolumeKmsKeyId`` can be any of the following formats:
                    * // KMS Key ID  ``\"1234abcd-12ab-34cd-56ef-1234567890ab\"``
                    * // Amazon Resource Name (ARN) of a KMS Key  ``\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"``
        :type CertifyForMarketplace: boolean
        :param CertifyForMarketplace:
          Whether to certify the algorithm so that it can be listed in AWS Marketplace.
        :rtype: dict
        :returns:
        """
        pass

    def create_code_repository(self, CodeRepositoryName: str, GitConfig: Dict) -> Dict:
        """
        Creates a Git repository as a resource in your Amazon SageMaker account. You can associate the repository with notebook instances so that you can use Git source control for the notebooks you create. The Git repository is a resource in your Amazon SageMaker account, so it can be associated with more than one notebook instance, and it persists independently from the lifecycle of any notebook instances it is associated with.
        The repository can be hosted either in `AWS CodeCommit <http://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html>`__ or in any other Git repository.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateCodeRepository>`_
        
        **Request Syntax**
        ::
          response = client.create_code_repository(
              CodeRepositoryName='string',
              GitConfig={
                  'RepositoryUrl': 'string',
                  'Branch': 'string',
                  'SecretArn': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'CodeRepositoryArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CodeRepositoryArn** *(string) --* 
              The Amazon Resource Name (ARN) of the new repository.
        :type CodeRepositoryName: string
        :param CodeRepositoryName: **[REQUIRED]**
          The name of the Git repository. The name must have 1 to 63 characters. Valid characters are a-z, A-Z, 0-9, and - (hyphen).
        :type GitConfig: dict
        :param GitConfig: **[REQUIRED]**
          Specifies details about the repository, including the URL where the repository is located, the default branch, and credentials to use to access the repository.
          - **RepositoryUrl** *(string) --* **[REQUIRED]**
            The URL where the Git repository is located.
          - **Branch** *(string) --*
            The default branch for the Git repository.
          - **SecretArn** *(string) --*
            The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the credentials used to access the git repository. The secret must have a staging label of ``AWSCURRENT`` and must be in the following format:
             ``{\"username\": *UserName* , \"password\": *Password* }``
        :rtype: dict
        :returns:
        """
        pass

    def create_compilation_job(self, CompilationJobName: str, RoleArn: str, InputConfig: Dict, OutputConfig: Dict, StoppingCondition: Dict) -> Dict:
        """
        Starts a model compilation job. After the model has been compiled, Amazon SageMaker saves the resulting model artifacts to an Amazon Simple Storage Service (Amazon S3) bucket that you specify. 
        If you choose to host your model using Amazon SageMaker hosting services, you can use the resulting model artifacts as part of the model. You can also use the artifacts with AWS IoT Greengrass. In that case, deploy them as an ML resource.
        In the request body, you provide the following:
        * A name for the compilation job 
        * Information about the input model artifacts  
        * The output location for the compiled model and the device (target) that the model runs on  
        * ``The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker assumes to perform the model compilation job``   
        You can also provide a ``Tag`` to track the model compilation job's resource use and costs. The response body contains the ``CompilationJobArn`` for the compiled job.
        To stop a model compilation job, use  StopCompilationJob . To get information about a particular model compilation job, use  DescribeCompilationJob . To get information about multiple model compilation jobs, use  ListCompilationJobs .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateCompilationJob>`_
        
        **Request Syntax**
        ::
          response = client.create_compilation_job(
              CompilationJobName='string',
              RoleArn='string',
              InputConfig={
                  'S3Uri': 'string',
                  'DataInputConfig': 'string',
                  'Framework': 'TENSORFLOW'|'MXNET'|'ONNX'|'PYTORCH'|'XGBOOST'
              },
              OutputConfig={
                  'S3OutputLocation': 'string',
                  'TargetDevice': 'ml_m4'|'ml_m5'|'ml_c4'|'ml_c5'|'ml_p2'|'ml_p3'|'jetson_tx1'|'jetson_tx2'|'rasp3b'|'deeplens'|'rk3399'|'rk3288'
              },
              StoppingCondition={
                  'MaxRuntimeInSeconds': 123
              }
          )
        
        **Response Syntax**
        ::
            {
                'CompilationJobArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CompilationJobArn** *(string) --* 
              If the action is successful, the service sends back an HTTP 200 response. Amazon SageMaker returns the following data in JSON format:
              * ``CompilationJobArn`` : The Amazon Resource Name (ARN) of the compiled job. 
        :type CompilationJobName: string
        :param CompilationJobName: **[REQUIRED]**
          A name for the model compilation job. The name must be unique within the AWS Region and within your AWS account.
        :type RoleArn: string
        :param RoleArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of an IIAMAM role that enables Amazon SageMaker to perform tasks on your behalf.
          During model compilation, Amazon SageMaker needs your permission to:
          * Read input data from an S3 bucket
          * Write model artifacts to an S3 bucket
          * Write logs to Amazon CloudWatch Logs
          * Publish metrics to Amazon CloudWatch
          You grant permissions for all of these tasks to an IAM role. To pass this role to Amazon SageMaker, the caller of this API must have the ``iam:PassRole`` permission. For more information, see `Amazon SageMaker Roles. <https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html>`__
        :type InputConfig: dict
        :param InputConfig: **[REQUIRED]**
          Provides information about the location of input model artifacts, the name and shape of the expected data inputs, and the framework in which the model was trained.
          - **S3Uri** *(string) --* **[REQUIRED]**
            The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).
          - **DataInputConfig** *(string) --* **[REQUIRED]**
            Specifies the name and shape of the expected data inputs for your trained model with a JSON dictionary form. The data inputs are  InputConfig$Framework specific.
            * ``TensorFlow`` : You must specify the name and shape (NHWC format) of the expected data inputs using a dictionary format for your trained model. The dictionary formats required for the console and CLI are different.
              * Examples for one input:
                * If using the console, ``{\"input\":[1,1024,1024,3]}``
                * If using the CLI, ``{\\"input\\":[1,1024,1024,3]}``
              * Examples for two inputs:
                * If using the console, ``{\"data1\": [1,28,28,1], \"data2\":[1,28,28,1]}``
                * If using the CLI, ``{\\"data1\\": [1,28,28,1], \\"data2\\":[1,28,28,1]}``
            * ``MXNET/ONNX`` : You must specify the name and shape (NCHW format) of the expected data inputs in order using a dictionary format for your trained model. The dictionary formats required for the console and CLI are different.
              * Examples for one input:
                * If using the console, ``{\"data\":[1,3,1024,1024]}``
                * If using the CLI, ``{\\"data\\":[1,3,1024,1024]}``
              * Examples for two inputs:
                * If using the console, ``{\"var1\": [1,1,28,28], \"var2\":[1,1,28,28]}``
                * If using the CLI, ``{\\"var1\\": [1,1,28,28], \\"var2\\":[1,1,28,28]}``
            * ``PyTorch`` : You can either specify the name and shape (NCHW format) of expected data inputs in order using a dictionary format for your trained model or you can specify the shape only using a list format. The dictionary formats required for the console and CLI are different. The list formats for the console and CLI are the same.
              * Examples for one input in dictionary format:
                * If using the console, ``{\"input0\":[1,3,224,224]}``
                * If using the CLI, ``{\\"input0\\":[1,3,224,224]}``
              * Example for one input in list format: ``[[1,3,224,224]]``
              * Examples for two inputs in dictionary format:
                * If using the console, ``{\"input0\":[1,3,224,224], \"input1\":[1,3,224,224]}``
                * If using the CLI, ``{\\"input0\\":[1,3,224,224], \\"input1\\":[1,3,224,224]}``
              * Example for two inputs in list format: ``[[1,3,224,224], [1,3,224,224]]``
            * ``XGBOOST`` : input data name and shape are not needed.
          - **Framework** *(string) --* **[REQUIRED]**
            Identifies the framework in which the model was trained. For example: TENSORFLOW.
        :type OutputConfig: dict
        :param OutputConfig: **[REQUIRED]**
          Provides information about the output location for the compiled model and the target device the model runs on.
          - **S3OutputLocation** *(string) --* **[REQUIRED]**
            Identifies the S3 path where you want Amazon SageMaker to store the model artifacts. For example, s3://bucket-name/key-name-prefix.
          - **TargetDevice** *(string) --* **[REQUIRED]**
            Identifies the device that you want to run your model on after it has been compiled. For example: ml_c5.
        :type StoppingCondition: dict
        :param StoppingCondition: **[REQUIRED]**
          The duration allowed for model compilation.
          - **MaxRuntimeInSeconds** *(integer) --*
            The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 28 days.
        :rtype: dict
        :returns:
        """
        pass

    def create_endpoint(self, EndpointName: str, EndpointConfigName: str, Tags: List = None) -> Dict:
        """
        Creates an endpoint using the endpoint configuration specified in the request. Amazon SageMaker uses the endpoint to provision resources and deploy models. You create the endpoint configuration with the `CreateEndpointConfig <https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpointConfig.html>`__ API. 
        .. note::
          Use this API only for hosting models using Amazon SageMaker hosting services. 
        The endpoint name must be unique within an AWS Region in your AWS account. 
        When it receives the request, Amazon SageMaker creates the endpoint, launches the resources (ML compute instances), and deploys the model(s) on them. 
        When Amazon SageMaker receives the request, it sets the endpoint status to ``Creating`` . After it creates the endpoint, it sets the status to ``InService`` . Amazon SageMaker can then process incoming requests for inferences. To check the status of an endpoint, use the `DescribeEndpoint <https://docs.aws.amazon.com/sagemaker/latest/dg/API_DescribeEndpoint.html>`__ API.
        For an example, see `Exercise 1\: Using the K-Means Algorithm Provided by Amazon SageMaker <https://docs.aws.amazon.com/sagemaker/latest/dg/ex1.html>`__ . 
        If any of the models hosted at this endpoint get model data from an Amazon S3 location, Amazon SageMaker uses AWS Security Token Service to download model artifacts from the S3 path you provided. AWS STS is activated in your IAM user account by default. If you previously deactivated AWS STS for a region, you need to reactivate AWS STS for that region. For more information, see `Activating and Deactivating AWS STS i an AWS Region <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html>`__ in the *AWS Identity and Access Management User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateEndpoint>`_
        
        **Request Syntax**
        ::
          response = client.create_endpoint(
              EndpointName='string',
              EndpointConfigName='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'EndpointArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **EndpointArn** *(string) --* 
              The Amazon Resource Name (ARN) of the endpoint.
        :type EndpointName: string
        :param EndpointName: **[REQUIRED]**
          The name of the endpoint. The name must be unique within an AWS Region in your AWS account.
        :type EndpointConfigName: string
        :param EndpointConfigName: **[REQUIRED]**
          The name of an endpoint configuration. For more information, see `CreateEndpointConfig <https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpointConfig.html>`__ .
        :type Tags: list
        :param Tags:
          An array of key-value pairs. For more information, see `Using Cost Allocation Tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what>`__ in the *AWS Billing and Cost Management User Guide* .
          - *(dict) --*
            Describes a tag.
            - **Key** *(string) --* **[REQUIRED]**
              The tag key.
            - **Value** *(string) --* **[REQUIRED]**
              The tag value.
        :rtype: dict
        :returns:
        """
        pass

    def create_endpoint_config(self, EndpointConfigName: str, ProductionVariants: List, Tags: List = None, KmsKeyId: str = None) -> Dict:
        """
        Creates an endpoint configuration that Amazon SageMaker hosting services uses to deploy models. In the configuration, you identify one or more models, created using the ``CreateModel`` API, to deploy and the resources that you want Amazon SageMaker to provision. Then you call the `CreateEndpoint <https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html>`__ API.
        .. note::
          Use this API only if you want to use Amazon SageMaker hosting services to deploy models into production. 
        In the request, you define one or more ``ProductionVariant`` s, each of which identifies a model. Each ``ProductionVariant`` parameter also describes the resources that you want Amazon SageMaker to provision. This includes the number and type of ML compute instances to deploy. 
        If you are hosting multiple models, you also assign a ``VariantWeight`` to specify how much traffic you want to allocate to each model. For example, suppose that you want to host two models, A and B, and you assign traffic weight 2 for model A and 1 for model B. Amazon SageMaker distributes two-thirds of the traffic to Model A, and one-third to model B. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateEndpointConfig>`_
        
        **Request Syntax**
        ::
          response = client.create_endpoint_config(
              EndpointConfigName='string',
              ProductionVariants=[
                  {
                      'VariantName': 'string',
                      'ModelName': 'string',
                      'InitialInstanceCount': 123,
                      'InstanceType': 'ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.large'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.large'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
                      'InitialVariantWeight': ...,
                      'AcceleratorType': 'ml.eia1.medium'|'ml.eia1.large'|'ml.eia1.xlarge'
                  },
              ],
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              KmsKeyId='string'
          )
        
        **Response Syntax**
        ::
            {
                'EndpointConfigArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **EndpointConfigArn** *(string) --* 
              The Amazon Resource Name (ARN) of the endpoint configuration. 
        :type EndpointConfigName: string
        :param EndpointConfigName: **[REQUIRED]**
          The name of the endpoint configuration. You specify this name in a `CreateEndpoint <https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html>`__ request.
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
            - **AcceleratorType** *(string) --*
              The size of the Elastic Inference (EI) instance to use for the production variant. EI instances provide on-demand GPU computing for inference. For more information, see `Using Elastic Inference in Amazon SageMaker <http://docs.aws.amazon.com/sagemaker/latest/dg/ei.html>`__ . For more information, see `Using Elastic Inference in Amazon SageMaker <http://docs.aws.amazon.com/sagemaker/latest/dg/ei.html>`__ .
        :type Tags: list
        :param Tags:
          An array of key-value pairs. For more information, see `Using Cost Allocation Tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what>`__ in the *AWS Billing and Cost Management User Guide* .
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
        """
        pass

    def create_hyper_parameter_tuning_job(self, HyperParameterTuningJobName: str, HyperParameterTuningJobConfig: Dict, TrainingJobDefinition: Dict, WarmStartConfig: Dict = None, Tags: List = None) -> Dict:
        """
        Starts a hyperparameter tuning job. A hyperparameter tuning job finds the best version of a model by running many training jobs on your dataset using the algorithm you choose and values for hyperparameters within ranges that you specify. It then chooses the hyperparameter values that result in a model that performs the best, as measured by an objective metric that you choose.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateHyperParameterTuningJob>`_
        
        **Request Syntax**
        ::
          response = client.create_hyper_parameter_tuning_job(
              HyperParameterTuningJobName='string',
              HyperParameterTuningJobConfig={
                  'Strategy': 'Bayesian'|'Random',
                  'HyperParameterTuningJobObjective': {
                      'Type': 'Maximize'|'Minimize',
                      'MetricName': 'string'
                  },
                  'ResourceLimits': {
                      'MaxNumberOfTrainingJobs': 123,
                      'MaxParallelTrainingJobs': 123
                  },
                  'ParameterRanges': {
                      'IntegerParameterRanges': [
                          {
                              'Name': 'string',
                              'MinValue': 'string',
                              'MaxValue': 'string',
                              'ScalingType': 'Auto'|'Linear'|'Logarithmic'|'ReverseLogarithmic'
                          },
                      ],
                      'ContinuousParameterRanges': [
                          {
                              'Name': 'string',
                              'MinValue': 'string',
                              'MaxValue': 'string',
                              'ScalingType': 'Auto'|'Linear'|'Logarithmic'|'ReverseLogarithmic'
                          },
                      ],
                      'CategoricalParameterRanges': [
                          {
                              'Name': 'string',
                              'Values': [
                                  'string',
                              ]
                          },
                      ]
                  },
                  'TrainingJobEarlyStoppingType': 'Off'|'Auto'
              },
              TrainingJobDefinition={
                  'StaticHyperParameters': {
                      'string': 'string'
                  },
                  'AlgorithmSpecification': {
                      'TrainingImage': 'string',
                      'TrainingInputMode': 'Pipe'|'File',
                      'AlgorithmName': 'string',
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
                  'VpcConfig': {
                      'SecurityGroupIds': [
                          'string',
                      ],
                      'Subnets': [
                          'string',
                      ]
                  },
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
                  'StoppingCondition': {
                      'MaxRuntimeInSeconds': 123
                  },
                  'EnableNetworkIsolation': True|False,
                  'EnableInterContainerTrafficEncryption': True|False
              },
              WarmStartConfig={
                  'ParentHyperParameterTuningJobs': [
                      {
                          'HyperParameterTuningJobName': 'string'
                      },
                  ],
                  'WarmStartType': 'IdenticalDataAndAlgorithm'|'TransferLearning'
              },
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'HyperParameterTuningJobArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **HyperParameterTuningJobArn** *(string) --* 
              The Amazon Resource Name (ARN) of the tuning job. Amazon SageMaker assigns an ARN to a hyperparameter tuning job when you create it.
        :type HyperParameterTuningJobName: string
        :param HyperParameterTuningJobName: **[REQUIRED]**
          The name of the tuning job. This name is the prefix for the names of all training jobs that this tuning job launches. The name must be unique within the same AWS account and AWS Region. The name must have { } to { } characters. Valid characters are a-z, A-Z, 0-9, and : + = @ _ % - (hyphen). The name is not case sensitive.
        :type HyperParameterTuningJobConfig: dict
        :param HyperParameterTuningJobConfig: **[REQUIRED]**
          The  HyperParameterTuningJobConfig object that describes the tuning job, including the search strategy, the objective metric used to evaluate training jobs, ranges of parameters to search, and resource limits for the tuning job. For more information, see  automatic-model-tuning
          - **Strategy** *(string) --* **[REQUIRED]**
            Specifies how hyperparameter tuning chooses the combinations of hyperparameter values to use for the training job it launches. To use the Bayesian search stategy, set this to ``Bayesian`` . To randomly search, set it to ``Random`` . For information about search strategies, see `How Hyperparameter Tuning Works <http://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html>`__ .
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
                - **ScalingType** *(string) --*
                  The scale that hyperparameter tuning uses to search the hyperparameter range. For information about choosing a hyperparameter scale, see `Hyperparameter Range Scaling <http://docs.aws.amazon.com//sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type>`__ . One of the following values:
                    Auto
                  Amazon SageMaker hyperparameter tuning chooses the best scale for the hyperparameter.
                    Linear
                  Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.
                    Logarithmic
                  Hyperparemeter tuning searches the values in the hyperparameter range by using a logarithmic scale.
                  Logarithmic scaling works only for ranges that have only values greater than 0.
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
                - **ScalingType** *(string) --*
                  The scale that hyperparameter tuning uses to search the hyperparameter range. For information about choosing a hyperparameter scale, see `Hyperparameter Range Scaling <http://docs.aws.amazon.com//sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type>`__ . One of the following values:
                    Auto
                  Amazon SageMaker hyperparameter tuning chooses the best scale for the hyperparameter.
                    Linear
                  Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.
                    Logarithmic
                  Hyperparemeter tuning searches the values in the hyperparameter range by using a logarithmic scale.
                  Logarithmic scaling works only for ranges that have only values greater than 0.
                    ReverseLogarithmic
                  Hyperparemeter tuning searches the values in the hyperparameter range by using a reverse logarithmic scale.
                  Reverse logarithmic scaling works only for ranges that are entirely within the range 0<=x<1.0.
            - **CategoricalParameterRanges** *(list) --*
              The array of  CategoricalParameterRange objects that specify ranges of categorical hyperparameters that a hyperparameter tuning job searches.
              - *(dict) --*
                A list of categorical hyperparameters to tune.
                - **Name** *(string) --* **[REQUIRED]**
                  The name of the categorical hyperparameter to tune.
                - **Values** *(list) --* **[REQUIRED]**
                  A list of the categories for the hyperparameter.
                  - *(string) --*
          - **TrainingJobEarlyStoppingType** *(string) --*
            Specifies whether to use early stopping for training jobs launched by the hyperparameter tuning job. This can be one of the following values (the default value is ``OFF`` ):
              OFF
            Training jobs launched by the hyperparameter tuning job do not use early stopping.
              AUTO
            Amazon SageMaker stops training jobs launched by the hyperparameter tuning job when they are unlikely to perform better than previously completed training jobs. For more information, see `Stop Training Jobs Early <http://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-early-stopping.html>`__ .
        :type TrainingJobDefinition: dict
        :param TrainingJobDefinition: **[REQUIRED]**
          The  HyperParameterTrainingJobDefinition object that describes the training jobs that this tuning job launches, including static hyperparameters, input data configuration, output data configuration, resource configuration, and stopping condition.
          - **StaticHyperParameters** *(dict) --*
            Specifies the values of hyperparameters that do not change for the tuning job.
            - *(string) --*
              - *(string) --*
          - **AlgorithmSpecification** *(dict) --* **[REQUIRED]**
            The  HyperParameterAlgorithmSpecification object that specifies the resource algorithm to use for the training jobs that the tuning job launches.
            - **TrainingImage** *(string) --*
              The registry path of the Docker image that contains the training algorithm. For information about Docker registry paths for built-in algorithms, see `Algorithms Provided by Amazon SageMaker\: Common Parameters <https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html>`__ . Amazon SageMaker supports both ``registry/repository[:tag]`` and ``registry/repository[@digest]`` image path formats. For more information, see `Using Your Own Algorithms with Amazon SageMaker <https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__ .
            - **TrainingInputMode** *(string) --* **[REQUIRED]**
              The input mode that the algorithm supports: File or Pipe. In File input mode, Amazon SageMaker downloads the training data from Amazon S3 to the storage volume that is attached to the training instance and mounts the directory to the Docker volume for the training container. In Pipe input mode, Amazon SageMaker streams data directly from Amazon S3 to the container.
              If you specify File mode, make sure that you provision the storage volume that is attached to the training instance with enough capacity to accommodate the training data downloaded from Amazon S3, the model artifacts, and intermediate information.
              For more information about input modes, see `Algorithms <https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ .
            - **AlgorithmName** *(string) --*
              The name of the resource algorithm to use for the hyperparameter tuning job. If you specify a value for this parameter, do not specify a value for ``TrainingImage`` .
            - **MetricDefinitions** *(list) --*
              An array of  MetricDefinition objects that specify the metrics that the algorithm emits.
              - *(dict) --*
                Specifies a metric that the training algorithm writes to ``stderr`` or ``stdout`` . Amazon SageMakerhyperparameter tuning captures all defined metrics. You specify one metric that a hyperparameter tuning job uses as its objective metric to choose the best training job.
                - **Name** *(string) --* **[REQUIRED]**
                  The name of the metric.
                - **Regex** *(string) --* **[REQUIRED]**
                  A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see `Defining Objective Metrics <https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics.html>`__ .
          - **RoleArn** *(string) --* **[REQUIRED]**
            The Amazon Resource Name (ARN) of the IAM role associated with the training jobs that the tuning job launches.
          - **InputDataConfig** *(list) --*
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
                    If you choose ``S3Prefix`` , ``S3Uri`` identifies a key name prefix. Amazon SageMaker uses all objects that match the specified key name prefix for model training.
                    If you choose ``ManifestFile`` , ``S3Uri`` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for model training.
                    If you choose ``AugmentedManifestFile`` , S3Uri identifies an object that is an augmented manifest file in JSON lines format. This file contains the data you want to use for model training. ``AugmentedManifestFile`` can only be used if the Channel\'s input mode is ``Pipe`` .
                  - **S3Uri** *(string) --* **[REQUIRED]**
                    Depending on the value specified for the ``S3DataType`` , identifies either a key name prefix or a manifest. For example:
                    * A key name prefix might look like this: ``s3://bucketname/exampleprefix`` .
                    * A manifest might look like this: ``s3://bucketname/example.manifest``   The manifest is an S3 object which is a JSON file with the following format:   ``[``    ``{\"prefix\": \"s3://customer_bucket/some/prefix/\"},``    ``\"relative/path/to/custdata-1\",``    ``\"relative/path/custdata-2\",``    ``...``    ``]``   The preceding JSON matches the following ``s3Uris`` :   ``s3://customer_bucket/some/prefix/relative/path/to/custdata-1``    ``s3://customer_bucket/some/prefix/relative/path/custdata-2``    ``...``   The complete set of ``s3uris`` in this manifest is the input data for the channel for this datasource. The object that each ``s3uris`` points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.
                  - **S3DataDistributionType** *(string) --*
                    If you want Amazon SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify ``FullyReplicated`` .
                    If you want Amazon SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify ``ShardedByS3Key`` . If there are *n* ML compute instances launched for a training job, each instance gets approximately 1/*n* of the number of S3 objects. In this case, model training on each machine uses only the subset of training data.
                    Don\'t choose more ML compute instances for training than available S3 objects. If you do, some nodes won\'t get any data and you will pay for nodes that aren\'t getting any training data. This applies in both File and Pipe modes. Keep this in mind when developing algorithms.
                    In distributed training, where you use multiple ML compute EC2 instances, you might choose ``ShardedByS3Key`` . If the algorithm requires copying training data to the ML storage volume (when ``TrainingInputMode`` is set to ``File`` ), this copies 1/*n* of the number of objects.
                  - **AttributeNames** *(list) --*
                    A list of one or more attribute names to use that are found in a specified augmented manifest file.
                    - *(string) --*
              - **ContentType** *(string) --*
                The MIME type of the data.
              - **CompressionType** *(string) --*
                If training data is compressed, the compression type. The default value is ``None`` . ``CompressionType`` is used only in Pipe input mode. In File mode, leave this field unset or set it to None.
              - **RecordWrapperType** *(string) --*
                Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format. In this case, Amazon SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you don\'t need to set this attribute. For more information, see `Create a Dataset Using RecordIO <https://mxnet.incubator.apache.org/architecture/note_data_loading.html#data-format>`__ .
                In File mode, leave this field unset or set it to None.
              - **InputMode** *(string) --*
                (Optional) The input mode to use for the data channel in a training job. If you don\'t set a value for ``InputMode`` , Amazon SageMaker uses the value set for ``TrainingInputMode`` . Use this parameter to override the ``TrainingInputMode`` setting in a  AlgorithmSpecification request when you have a channel that needs a different input mode from the training job\'s general setting. To download the data from Amazon Simple Storage Service (Amazon S3) to the provisioned ML storage volume, and mount the directory to a Docker volume, use ``File`` input mode. To stream data directly from Amazon S3 to the container, choose ``Pipe`` input mode.
                To use a model for incremental training, choose ``File`` input model.
              - **ShuffleConfig** *(dict) --*
                A configuration for a shuffle option for input data in a channel. If you use ``S3Prefix`` for ``S3DataType`` , this shuffles the results of the S3 key prefix matches. If you use ``ManifestFile`` , the order of the S3 object references in the ``ManifestFile`` is shuffled. If you use ``AugmentedManifestFile`` , the order of the JSON lines in the ``AugmentedManifestFile`` is shuffled. The shuffling order is determined using the ``Seed`` value.
                For Pipe input mode, shuffling is done at the start of every epoch. With large datasets this ensures that the order of the training data is different for each epoch, it helps reduce bias and possible overfitting. In a multi-node training job when ShuffleConfig is combined with ``S3DataDistributionType`` of ``ShardedByS3Key`` , the data is shuffled across nodes so that the content sent to a particular node on the first epoch might be sent to a different node on the second epoch.
                - **Seed** *(integer) --* **[REQUIRED]**
                  Determines the shuffling order in ``ShuffleConfig`` value.
          - **VpcConfig** *(dict) --*
            The  VpcConfig object that specifies the VPC that you want the training jobs that this hyperparameter tuning job launches to connect to. Control access to and from your training container by configuring the VPC. For more information, see `Protect Training Jobs by Using an Amazon Virtual Private Cloud <https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html>`__ .
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
              If you don\'t provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role\'s account. For more information, see `KMS-Managed Encryption Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ in the *Amazon Simple Storage Service Developer Guide.*
              The KMS key policy must grant permission to the IAM role that you specify in your ``CreateTramsformJob`` request. For more information, see `Using Key Policies in AWS KMS <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the *AWS Key Management Service Developer Guide* .
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
              The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 28 days.
          - **EnableNetworkIsolation** *(boolean) --*
            Isolates the training container. No inbound or outbound network calls can be made, except for calls between peers within a training cluster for distributed training. If network isolation is used for training jobs that are configured to use a VPC, Amazon SageMaker downloads and uploads customer data and model artifacts through the specified VPC, but the training container does not have network access.
            .. note::
              The Semantic Segmentation built-in algorithm does not support network isolation.
          - **EnableInterContainerTrafficEncryption** *(boolean) --*
            To encrypt all communications between ML compute instances in distributed training, choose ``True`` . Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithm in distributed training.
        :type WarmStartConfig: dict
        :param WarmStartConfig:
          Specifies the configuration for starting the hyperparameter tuning job using one or more previous tuning jobs as a starting point. The results of previous tuning jobs are used to inform which combinations of hyperparameters to search over in the new tuning job.
          All training jobs launched by the new hyperparameter tuning job are evaluated by using the objective metric. If you specify ``IDENTICAL_DATA_AND_ALGORITHM`` as the ``WarmStartType`` value for the warm start configuration, the training job that performs the best in the new tuning job is compared to the best training jobs from the parent tuning jobs. From these, the training job that performs the best as measured by the objective metric is returned as the overall best training job.
          .. note::
            All training jobs launched by parent hyperparameter tuning jobs and the new hyperparameter tuning jobs count against the limit of training jobs for the tuning job.
          - **ParentHyperParameterTuningJobs** *(list) --* **[REQUIRED]**
            An array of hyperparameter tuning jobs that are used as the starting point for the new hyperparameter tuning job. For more information about warm starting a hyperparameter tuning job, see `Using a Previous Hyperparameter Tuning Job as a Starting Point <http://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-warm-start.html>`__ .
            Hyperparameter tuning jobs created before October 1, 2018 cannot be used as parent jobs for warm start tuning jobs.
            - *(dict) --*
              A previously completed or stopped hyperparameter tuning job to be used as a starting point for a new hyperparameter tuning job.
              - **HyperParameterTuningJobName** *(string) --*
                The name of the hyperparameter tuning job to be used as a starting point for a new hyperparameter tuning job.
          - **WarmStartType** *(string) --* **[REQUIRED]**
            Specifies one of the following:
              IDENTICAL_DATA_AND_ALGORITHM
            The new hyperparameter tuning job uses the same input data and training image as the parent tuning jobs. You can change the hyperparameter ranges to search and the maximum number of training jobs that the hyperparameter tuning job launches. You cannot use a new version of the training algorithm, unless the changes in the new version do not affect the algorithm itself. For example, changes that improve logging or adding support for a different data format are allowed. You can also change hyperparameters from tunable to static, and from static to tunable, but the total number of static plus tunable hyperparameters must remain the same as it is in all parent jobs. The objective metric for the new tuning job must be the same as for all parent jobs.
              TRANSFER_LEARNING
            The new hyperparameter tuning job can include input data, hyperparameter ranges, maximum number of concurrent training jobs, and maximum number of training jobs that are different than those of its parent hyperparameter tuning jobs. The training image can also be a different version from the version used in the parent hyperparameter tuning job. You can also change hyperparameters from tunable to static, and from static to tunable, but the total number of static plus tunable hyperparameters must remain the same as it is in all parent jobs. The objective metric for the new tuning job must be the same as for all parent jobs.
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
        """
        pass

    def create_labeling_job(self, LabelingJobName: str, LabelAttributeName: str, InputConfig: Dict, OutputConfig: Dict, RoleArn: str, HumanTaskConfig: Dict, LabelCategoryConfigS3Uri: str = None, StoppingConditions: Dict = None, LabelingJobAlgorithmsConfig: Dict = None, Tags: List = None) -> Dict:
        """
        Creates a job that uses workers to label the data objects in your input dataset. You can use the labeled data to train machine learning models.
        You can select your workforce from one of three providers:
        * A private workforce that you create. It can include employees, contractors, and outside experts. Use a private workforce when want the data to stay within your organization or when a specific set of skills is required. 
        * One or more vendors that you select from the AWS Marketplace. Vendors provide expertise in specific areas.  
        * The Amazon Mechanical Turk workforce. This is the largest workforce, but it should only be used for public data or data that has been stripped of any personally identifiable information. 
        You can also use *automated data labeling* to reduce the number of data objects that need to be labeled by a human. Automated data labeling uses *active learning* to determine if a data object can be labeled by machine or if it needs to be sent to a human worker. For more information, see `Using Automated Data Labeling <http://docs.aws.amazon.com/sagemaker/latest/dg/sms-automated-labeling.html>`__ .
        The data objects to be labeled are contained in an Amazon S3 bucket. You create a *manifest file* that describes the location of each object. For more information, see `Using Input and Output Data <http://docs.aws.amazon.com/sagemaker/latest/dg/sms-data.html>`__ .
        The output can be used as the manifest file for another labeling job or as training data for your machine learning models.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateLabelingJob>`_
        
        **Request Syntax**
        ::
          response = client.create_labeling_job(
              LabelingJobName='string',
              LabelAttributeName='string',
              InputConfig={
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
              },
              OutputConfig={
                  'S3OutputPath': 'string',
                  'KmsKeyId': 'string'
              },
              RoleArn='string',
              LabelCategoryConfigS3Uri='string',
              StoppingConditions={
                  'MaxHumanLabeledObjectCount': 123,
                  'MaxPercentageOfInputDatasetLabeled': 123
              },
              LabelingJobAlgorithmsConfig={
                  'LabelingJobAlgorithmSpecificationArn': 'string',
                  'InitialActiveLearningModelArn': 'string',
                  'LabelingJobResourceConfig': {
                      'VolumeKmsKeyId': 'string'
                  }
              },
              HumanTaskConfig={
                  'WorkteamArn': 'string',
                  'UiConfig': {
                      'UiTemplateS3Uri': 'string'
                  },
                  'PreHumanTaskLambdaArn': 'string',
                  'TaskKeywords': [
                      'string',
                  ],
                  'TaskTitle': 'string',
                  'TaskDescription': 'string',
                  'NumberOfHumanWorkersPerDataObject': 123,
                  'TaskTimeLimitInSeconds': 123,
                  'TaskAvailabilityLifetimeInSeconds': 123,
                  'MaxConcurrentTaskCount': 123,
                  'AnnotationConsolidationConfig': {
                      'AnnotationConsolidationLambdaArn': 'string'
                  },
                  'PublicWorkforceTaskPrice': {
                      'AmountInUsd': {
                          'Dollars': 123,
                          'Cents': 123,
                          'TenthFractionsOfACent': 123
                      }
                  }
              },
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'LabelingJobArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LabelingJobArn** *(string) --* 
              The Amazon Resource Name (ARN) of the labeling job. You use this ARN to identify the labeling job.
        :type LabelingJobName: string
        :param LabelingJobName: **[REQUIRED]**
          The name of the labeling job. This name is used to identify the job in a list of labeling jobs.
        :type LabelAttributeName: string
        :param LabelAttributeName: **[REQUIRED]**
          The attribute name to use for the label in the output manifest file. This is the key for the key/value pair formed with the label that a worker assigns to the object. The name can\'t end with \"-metadata\". If you are running a semantic segmentation labeling job, the attribute name must end with \"-ref\". If you are running any other kind of labeling job, the attribute name must not end with \"-ref\".
        :type InputConfig: dict
        :param InputConfig: **[REQUIRED]**
          Input data for the labeling job, such as the Amazon S3 location of the data objects and the location of the manifest file that describes the data objects.
          - **DataSource** *(dict) --* **[REQUIRED]**
            The location of the input data.
            - **S3DataSource** *(dict) --* **[REQUIRED]**
              The Amazon S3 location of the input data objects.
              - **ManifestS3Uri** *(string) --* **[REQUIRED]**
                The Amazon S3 location of the manifest file that describes the input data objects.
          - **DataAttributes** *(dict) --*
            Attributes of the data specified by the customer.
            - **ContentClassifiers** *(list) --*
              Declares that your content is free of personally identifiable information or adult content. Amazon SageMaker may restrict the Amazon Mechanical Turk workers that can view your task based on this information.
              - *(string) --*
        :type OutputConfig: dict
        :param OutputConfig: **[REQUIRED]**
          The location of the output data and the AWS Key Management Service key ID for the key used to encrypt the output data, if any.
          - **S3OutputPath** *(string) --* **[REQUIRED]**
            The Amazon S3 location to write output data.
          - **KmsKeyId** *(string) --*
            The AWS Key Management Service ID of the key used to encrypt the output data, if any.
        :type RoleArn: string
        :param RoleArn: **[REQUIRED]**
          The Amazon Resource Number (ARN) that Amazon SageMaker assumes to perform tasks on your behalf during data labeling. You must grant this role the necessary permissions so that Amazon SageMaker can successfully complete data labeling.
        :type LabelCategoryConfigS3Uri: string
        :param LabelCategoryConfigS3Uri:
          The S3 URL of the file that defines the categories used to label the data objects.
          The file is a JSON structure in the following format:
           ``{``
           ``\"document-version\": \"2018-11-28\"``
           ``\"labels\": [``
           ``{``
           ``\"label\": \"*label 1* \"``
           ``},``
           ``{``
           ``\"label\": \"*label 2* \"``
           ``},``
           ``...``
           ``{``
           ``\"label\": \"*label n* \"``
           ``}``
           ``]``
           ``}``
        :type StoppingConditions: dict
        :param StoppingConditions:
          A set of conditions for stopping the labeling job. If any of the conditions are met, the job is automatically stopped. You can use these conditions to control the cost of data labeling.
          - **MaxHumanLabeledObjectCount** *(integer) --*
            The maximum number of objects that can be labeled by human workers.
          - **MaxPercentageOfInputDatasetLabeled** *(integer) --*
            The maximum number of input data objects that should be labeled.
        :type LabelingJobAlgorithmsConfig: dict
        :param LabelingJobAlgorithmsConfig:
          Configures the information required to perform automated data labeling.
          - **LabelingJobAlgorithmSpecificationArn** *(string) --* **[REQUIRED]**
            Specifies the Amazon Resource Name (ARN) of the algorithm used for auto-labeling. You must select one of the following ARNs:
            * *Image classification*    ``arn:aws:sagemaker:*region* :027400017018:labeling-job-algorithm-specification/image-classification``
            * *Text classification*    ``arn:aws:sagemaker:*region* :027400017018:labeling-job-algorithm-specification/text-classification``
            * *Object detection*    ``arn:aws:sagemaker:*region* :027400017018:labeling-job-algorithm-specification/object-detection``
          - **InitialActiveLearningModelArn** *(string) --*
            At the end of an auto-label job Amazon SageMaker Ground Truth sends the Amazon Resource Nam (ARN) of the final model used for auto-labeling. You can use this model as the starting point for subsequent similar jobs by providing the ARN of the model here.
          - **LabelingJobResourceConfig** *(dict) --*
            Provides configuration information for a labeling job.
            - **VolumeKmsKeyId** *(string) --*
              The AWS Key Management Service key ID for the key used to encrypt the output data, if any.
        :type HumanTaskConfig: dict
        :param HumanTaskConfig: **[REQUIRED]**
          Configures the information required for human workers to complete a labeling task.
          - **WorkteamArn** *(string) --* **[REQUIRED]**
            The Amazon Resource Name (ARN) of the work team assigned to complete the tasks.
          - **UiConfig** *(dict) --* **[REQUIRED]**
            Information about the user interface that workers use to complete the labeling task.
            - **UiTemplateS3Uri** *(string) --* **[REQUIRED]**
              The Amazon S3 bucket location of the UI template. For more information about the contents of a UI template, see `Creating Your Custom Labeling Task Template <http://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates-step2.html>`__ .
          - **PreHumanTaskLambdaArn** *(string) --* **[REQUIRED]**
            The Amazon Resource Name (ARN) of a Lambda function that is run before a data object is sent to a human worker. Use this function to provide input to a custom labeling job.
            For the built-in bounding box, image classification, semantic segmentation, and text classification task types, Amazon SageMaker Ground Truth provides the following Lambda functions:
             **US East (Northern Virginia) (us-east-1):**
            * ``arn:aws:lambda:us-east-1:432418664414:function:PRE-BoundingBox``
            * ``arn:aws:lambda:us-east-1:432418664414:function:PRE-ImageMultiClass``
            * ``arn:aws:lambda:us-east-1:432418664414:function:PRE-SemanticSegmentation``
            * ``arn:aws:lambda:us-east-1:432418664414:function:PRE-TextMultiClass``
             **US East (Ohio) (us-east-2):**
            * ``arn:aws:lambda:us-east-2:266458841044:function:PRE-BoundingBox``
            * ``arn:aws:lambda:us-east-2:266458841044:function:PRE-ImageMultiClass``
            * ``arn:aws:lambda:us-east-2:266458841044:function:PRE-SemanticSegmentation``
            * ``arn:aws:lambda:us-east-2:266458841044:function:PRE-TextMultiClass``
             **US West (Oregon) (us-west-2):**
            * ``arn:aws:lambda:us-west-2:081040173940:function:PRE-BoundingBox``
            * ``arn:aws:lambda:us-west-2:081040173940:function:PRE-ImageMultiClass``
            * ``arn:aws:lambda:us-west-2:081040173940:function:PRE-SemanticSegmentation``
            * ``arn:aws:lambda:us-west-2:081040173940:function:PRE-TextMultiClass``
             **EU (Ireland) (eu-west-1):**
            * ``arn:aws:lambda:eu-west-1:568282634449:function:PRE-BoundingBox``
            * ``arn:aws:lambda:eu-west-1:568282634449:function:PRE-ImageMultiClass``
            * ``arn:aws:lambda:eu-west-1:568282634449:function:PRE-SemanticSegmentation``
            * ``arn:aws:lambda:eu-west-1:568282634449:function:PRE-TextMultiClass``
             **Asia Pacific (Tokyo (ap-northeast-1):**
            * ``arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-BoundingBox``
            * ``arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-ImageMultiClass``
            * ``arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-SemanticSegmentation``
            * ``arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-TextMultiClass``
          - **TaskKeywords** *(list) --*
            Keywords used to describe the task so that workers on Amazon Mechanical Turk can discover the task.
            - *(string) --*
          - **TaskTitle** *(string) --* **[REQUIRED]**
            A title for the task for your human workers.
          - **TaskDescription** *(string) --* **[REQUIRED]**
            A description of the task for your human workers.
          - **NumberOfHumanWorkersPerDataObject** *(integer) --* **[REQUIRED]**
            The number of human workers that will label an object.
          - **TaskTimeLimitInSeconds** *(integer) --* **[REQUIRED]**
            The amount of time that a worker has to complete a task.
          - **TaskAvailabilityLifetimeInSeconds** *(integer) --*
            The length of time that a task remains available for labelling by human workers.
          - **MaxConcurrentTaskCount** *(integer) --*
            Defines the maximum number of data objects that can be labeled by human workers at the same time. Each object may have more than one worker at one time.
          - **AnnotationConsolidationConfig** *(dict) --* **[REQUIRED]**
            Configures how labels are consolidated across human workers.
            - **AnnotationConsolidationLambdaArn** *(string) --* **[REQUIRED]**
              The Amazon Resource Name (ARN) of a Lambda function implements the logic for annotation consolidation.
              For the built-in bounding box, image classification, semantic segmentation, and text classification task types, Amazon SageMaker Ground Truth provides the following Lambda functions:
              * *Bounding box* - Finds the most similar boxes from different workers based on the Jaccard index of the boxes.  ``arn:aws:lambda:us-east-1:432418664414:function:ACS-BoundingBox``    ``arn:aws:lambda:us-east-2:266458841044:function:ACS-BoundingBox``    ``arn:aws:lambda:us-west-2:081040173940:function:ACS-BoundingBox``    ``arn:aws:lambda:eu-west-1:568282634449:function:ACS-BoundingBox``    ``arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-BoundingBox``
              * *Image classification* - Uses a variant of the Expectation Maximization approach to estimate the true class of an image based on annotations from individual workers.  ``arn:aws:lambda:us-east-1:432418664414:function:ACS-ImageMultiClass``    ``arn:aws:lambda:us-east-2:266458841044:function:ACS-ImageMultiClass``    ``arn:aws:lambda:us-west-2:081040173940:function:ACS-ImageMultiClass``    ``arn:aws:lambda:eu-west-1:568282634449:function:ACS-ImageMultiClass``    ``arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-ImageMultiClass``
              * *Semantic segmentation* - Treats each pixel in an image as a multi-class classification and treats pixel annotations from workers as \"votes\" for the correct label.  ``arn:aws:lambda:us-east-1:432418664414:function:ACS-SemanticSegmentation``    ``arn:aws:lambda:us-east-2:266458841044:function:ACS-SemanticSegmentation``    ``arn:aws:lambda:us-west-2:081040173940:function:ACS-SemanticSegmentation``    ``arn:aws:lambda:eu-west-1:568282634449:function:ACS-SemanticSegmentation``    ``arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-SemanticSegmentation``
              * *Text classification* - Uses a variant of the Expectation Maximization approach to estimate the true class of text based on annotations from individual workers.  ``arn:aws:lambda:us-east-1:432418664414:function:ACS-TextMultiClass``    ``arn:aws:lambda:us-east-2:266458841044:function:ACS-TextMultiClass``    ``arn:aws:lambda:us-west-2:081040173940:function:ACS-TextMultiClass``    ``arn:aws:lambda:eu-west-1:568282634449:function:ACS-TextMultiClass``    ``arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-TextMultiClass``
              For more information, see `Annotation Consolidation <http://docs.aws.amazon.com/sagemaker/latest/dg/sms-annotation-consolidation.html>`__ .
          - **PublicWorkforceTaskPrice** *(dict) --*
            The price that you pay for each task performed by a public worker.
            - **AmountInUsd** *(dict) --*
              Defines the amount of money paid to a worker in United States dollars.
              - **Dollars** *(integer) --*
                The whole number of dollars in the amount.
              - **Cents** *(integer) --*
                The fractional portion, in cents, of the amount.
              - **TenthFractionsOfACent** *(integer) --*
                Fractions of a cent, in tenths.
        :type Tags: list
        :param Tags:
          An array of key/value pairs. For more information, see `Using Cost Allocation Tags <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what>`__ in the *AWS Billing and Cost Management User Guide* .
          - *(dict) --*
            Describes a tag.
            - **Key** *(string) --* **[REQUIRED]**
              The tag key.
            - **Value** *(string) --* **[REQUIRED]**
              The tag value.
        :rtype: dict
        :returns:
        """
        pass

    def create_model(self, ModelName: str, ExecutionRoleArn: str, PrimaryContainer: Dict = None, Containers: List = None, Tags: List = None, VpcConfig: Dict = None, EnableNetworkIsolation: bool = None) -> Dict:
        """
        Creates a model in Amazon SageMaker. In the request, you name the model and describe a primary container. For the primary container, you specify the docker image containing inference code, artifacts (from prior training), and custom environment map that the inference code uses when you deploy the model for predictions.
        Use this API to create a model if you want to use Amazon SageMaker hosting services or run a batch transform job.
        To host your model, you create an endpoint configuration with the ``CreateEndpointConfig`` API, and then create an endpoint with the ``CreateEndpoint`` API. Amazon SageMaker then deploys all of the containers that you defined for the model in the hosting environment. 
        To run a batch transform using your model, you start a job with the ``CreateTransformJob`` API. Amazon SageMaker uses your model and your dataset to get inferences which are then saved to a specified S3 location.
        In the ``CreateModel`` request, you must define a container with the ``PrimaryContainer`` parameter.
        In the request, you also provide an IAM role that Amazon SageMaker can assume to access model artifacts and docker image for deployment on ML compute hosting instances or for batch transform jobs. In addition, you also use the IAM role to manage permissions the inference code needs. For example, if the inference code access any other AWS resources, you grant necessary permissions via this role.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateModel>`_
        
        **Request Syntax**
        ::
          response = client.create_model(
              ModelName='string',
              PrimaryContainer={
                  'ContainerHostname': 'string',
                  'Image': 'string',
                  'ModelDataUrl': 'string',
                  'Environment': {
                      'string': 'string'
                  },
                  'ModelPackageName': 'string'
              },
              Containers=[
                  {
                      'ContainerHostname': 'string',
                      'Image': 'string',
                      'ModelDataUrl': 'string',
                      'Environment': {
                          'string': 'string'
                      },
                      'ModelPackageName': 'string'
                  },
              ],
              ExecutionRoleArn='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              VpcConfig={
                  'SecurityGroupIds': [
                      'string',
                  ],
                  'Subnets': [
                      'string',
                  ]
              },
              EnableNetworkIsolation=True|False
          )
        
        **Response Syntax**
        ::
            {
                'ModelArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ModelArn** *(string) --* 
              The ARN of the model created in Amazon SageMaker.
        :type ModelName: string
        :param ModelName: **[REQUIRED]**
          The name of the new model.
        :type PrimaryContainer: dict
        :param PrimaryContainer:
          The location of the primary docker image containing inference code, associated artifacts, and custom environment map that the inference code uses when the model is deployed for predictions.
          - **ContainerHostname** *(string) --*
            This parameter is ignored.
          - **Image** *(string) --*
            The Amazon EC2 Container Registry (Amazon ECR) path where inference code is stored. If you are using your own custom algorithm instead of an algorithm provided by Amazon SageMaker, the inference code must meet Amazon SageMaker requirements. Amazon SageMaker supports both ``registry/repository[:tag]`` and ``registry/repository[@digest]`` image path formats. For more information, see `Using Your Own Algorithms with Amazon SageMaker <https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__
          - **ModelDataUrl** *(string) --*
            The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).
            If you provide a value for this parameter, Amazon SageMaker uses AWS Security Token Service to download model artifacts from the S3 path you provide. AWS STS is activated in your IAM user account by default. If you previously deactivated AWS STS for a region, you need to reactivate AWS STS for that region. For more information, see `Activating and Deactivating AWS STS in an AWS Region <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html>`__ in the *AWS Identity and Access Management User Guide* .
          - **Environment** *(dict) --*
            The environment variables to set in the Docker container. Each key and value in the ``Environment`` string to string map can have length of up to 1024. We support up to 16 entries in the map.
            - *(string) --*
              - *(string) --*
          - **ModelPackageName** *(string) --*
            The name of the model package to use to create the model.
        :type Containers: list
        :param Containers:
          Specifies the containers in the inference pipeline.
          - *(dict) --*
            Describes the container, as part of model definition.
            - **ContainerHostname** *(string) --*
              This parameter is ignored.
            - **Image** *(string) --*
              The Amazon EC2 Container Registry (Amazon ECR) path where inference code is stored. If you are using your own custom algorithm instead of an algorithm provided by Amazon SageMaker, the inference code must meet Amazon SageMaker requirements. Amazon SageMaker supports both ``registry/repository[:tag]`` and ``registry/repository[@digest]`` image path formats. For more information, see `Using Your Own Algorithms with Amazon SageMaker <https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__
            - **ModelDataUrl** *(string) --*
              The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).
              If you provide a value for this parameter, Amazon SageMaker uses AWS Security Token Service to download model artifacts from the S3 path you provide. AWS STS is activated in your IAM user account by default. If you previously deactivated AWS STS for a region, you need to reactivate AWS STS for that region. For more information, see `Activating and Deactivating AWS STS in an AWS Region <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html>`__ in the *AWS Identity and Access Management User Guide* .
            - **Environment** *(dict) --*
              The environment variables to set in the Docker container. Each key and value in the ``Environment`` string to string map can have length of up to 1024. We support up to 16 entries in the map.
              - *(string) --*
                - *(string) --*
            - **ModelPackageName** *(string) --*
              The name of the model package to use to create the model.
        :type ExecutionRoleArn: string
        :param ExecutionRoleArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker can assume to access model artifacts and docker image for deployment on ML compute instances or for batch transform jobs. Deploying on ML compute instances is part of model hosting. For more information, see `Amazon SageMaker Roles <https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html>`__ .
          .. note::
            To be able to pass this role to Amazon SageMaker, the caller of this API must have the ``iam:PassRole`` permission.
        :type Tags: list
        :param Tags:
          An array of key-value pairs. For more information, see `Using Cost Allocation Tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what>`__ in the *AWS Billing and Cost Management User Guide* .
          - *(dict) --*
            Describes a tag.
            - **Key** *(string) --* **[REQUIRED]**
              The tag key.
            - **Value** *(string) --* **[REQUIRED]**
              The tag value.
        :type VpcConfig: dict
        :param VpcConfig:
          A  VpcConfig object that specifies the VPC that you want your model to connect to. Control access to and from your model container by configuring the VPC. ``VpcConfig`` is used in hosting services and in batch transform. For more information, see `Protect Endpoints by Using an Amazon Virtual Private Cloud <https://docs.aws.amazon.com/sagemaker/latest/dg/host-vpc.html>`__ and `Protect Data in Batch Transform Jobs by Using an Amazon Virtual Private Cloud <https://docs.aws.amazon.com/sagemaker/latest/dg/batch-vpc.html>`__ .
          - **SecurityGroupIds** *(list) --* **[REQUIRED]**
            The VPC security group IDs, in the form sg-xxxxxxxx. Specify the security groups for the VPC that is specified in the ``Subnets`` field.
            - *(string) --*
          - **Subnets** *(list) --* **[REQUIRED]**
            The ID of the subnets in the VPC to which you want to connect your training job or model.
            - *(string) --*
        :type EnableNetworkIsolation: boolean
        :param EnableNetworkIsolation:
          Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
          .. note::
            The Semantic Segmentation built-in algorithm does not support network isolation.
        :rtype: dict
        :returns:
        """
        pass

    def create_model_package(self, ModelPackageName: str, ModelPackageDescription: str = None, InferenceSpecification: Dict = None, ValidationSpecification: Dict = None, SourceAlgorithmSpecification: Dict = None, CertifyForMarketplace: bool = None) -> Dict:
        """
        Creates a model package that you can use to create Amazon SageMaker models or list on AWS Marketplace. Buyers can subscribe to model packages listed on AWS Marketplace to create models in Amazon SageMaker.
        To create a model package by specifying a Docker container that contains your inference code and the Amazon S3 location of your model artifacts, provide values for ``InferenceSpecification`` . To create a model from an algorithm resource that you created or subscribed to in AWS Marketplace, provide a value for ``SourceAlgorithmSpecification`` .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateModelPackage>`_
        
        **Request Syntax**
        ::
          response = client.create_model_package(
              ModelPackageName='string',
              ModelPackageDescription='string',
              InferenceSpecification={
                  'Containers': [
                      {
                          'ContainerHostname': 'string',
                          'Image': 'string',
                          'ImageDigest': 'string',
                          'ModelDataUrl': 'string',
                          'ProductId': 'string'
                      },
                  ],
                  'SupportedTransformInstanceTypes': [
                      'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge',
                  ],
                  'SupportedRealtimeInferenceInstanceTypes': [
                      'ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.large'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.large'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
                  ],
                  'SupportedContentTypes': [
                      'string',
                  ],
                  'SupportedResponseMIMETypes': [
                      'string',
                  ]
              },
              ValidationSpecification={
                  'ValidationRole': 'string',
                  'ValidationProfiles': [
                      {
                          'ProfileName': 'string',
                          'TransformJobDefinition': {
                              'MaxConcurrentTransforms': 123,
                              'MaxPayloadInMB': 123,
                              'BatchStrategy': 'MultiRecord'|'SingleRecord',
                              'Environment': {
                                  'string': 'string'
                              },
                              'TransformInput': {
                                  'DataSource': {
                                      'S3DataSource': {
                                          'S3DataType': 'ManifestFile'|'S3Prefix'|'AugmentedManifestFile',
                                          'S3Uri': 'string'
                                      }
                                  },
                                  'ContentType': 'string',
                                  'CompressionType': 'None'|'Gzip',
                                  'SplitType': 'None'|'Line'|'RecordIO'|'TFRecord'
                              },
                              'TransformOutput': {
                                  'S3OutputPath': 'string',
                                  'Accept': 'string',
                                  'AssembleWith': 'None'|'Line',
                                  'KmsKeyId': 'string'
                              },
                              'TransformResources': {
                                  'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge',
                                  'InstanceCount': 123,
                                  'VolumeKmsKeyId': 'string'
                              }
                          }
                      },
                  ]
              },
              SourceAlgorithmSpecification={
                  'SourceAlgorithms': [
                      {
                          'ModelDataUrl': 'string',
                          'AlgorithmName': 'string'
                      },
                  ]
              },
              CertifyForMarketplace=True|False
          )
        
        **Response Syntax**
        ::
            {
                'ModelPackageArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ModelPackageArn** *(string) --* 
              The Amazon Resource Name (ARN) of the new model package.
        :type ModelPackageName: string
        :param ModelPackageName: **[REQUIRED]**
          The name of the model package. The name must have 1 to 63 characters. Valid characters are a-z, A-Z, 0-9, and - (hyphen).
        :type ModelPackageDescription: string
        :param ModelPackageDescription:
          A description of the model package.
        :type InferenceSpecification: dict
        :param InferenceSpecification:
          Specifies details about inference jobs that can be run with models based on this model package, including the following:
          * The Amazon ECR paths of containers that contain the inference code and model artifacts.
          * The instance types that the model package supports for transform jobs and real-time endpoints used for inference.
          * The input and output content formats that the model package supports for inference.
          - **Containers** *(list) --* **[REQUIRED]**
            The Amazon ECR registry path of the Docker image that contains the inference code.
            - *(dict) --*
              Describes the Docker container for the model package.
              - **ContainerHostname** *(string) --*
                The DNS host name for the Docker container.
              - **Image** *(string) --* **[REQUIRED]**
                The Amazon EC2 Container Registry (Amazon ECR) path where inference code is stored.
                If you are using your own custom algorithm instead of an algorithm provided by Amazon SageMaker, the inference code must meet Amazon SageMaker requirements. Amazon SageMaker supports both ``registry/repository[:tag]`` and ``registry/repository[@digest]`` image path formats. For more information, see `Using Your Own Algorithms with Amazon SageMaker <https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__ .
              - **ImageDigest** *(string) --*
                An MD5 hash of the training algorithm that identifies the Docker image used for training.
              - **ModelDataUrl** *(string) --*
                The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single ``gzip`` compressed tar archive (``.tar.gz`` suffix).
              - **ProductId** *(string) --*
                The AWS Marketplace product ID of the model package.
          - **SupportedTransformInstanceTypes** *(list) --* **[REQUIRED]**
            A list of the instance types on which a transformation job can be run or on which an endpoint can be deployed.
            - *(string) --*
          - **SupportedRealtimeInferenceInstanceTypes** *(list) --* **[REQUIRED]**
            A list of the instance types that are used to generate inferences in real-time.
            - *(string) --*
          - **SupportedContentTypes** *(list) --* **[REQUIRED]**
            The supported MIME types for the input data.
            - *(string) --*
          - **SupportedResponseMIMETypes** *(list) --* **[REQUIRED]**
            The supported MIME types for the output data.
            - *(string) --*
        :type ValidationSpecification: dict
        :param ValidationSpecification:
          Specifies configurations for one or more transform jobs that Amazon SageMaker runs to test the model package.
          - **ValidationRole** *(string) --* **[REQUIRED]**
            The IAM roles to be used for the validation of the model package.
          - **ValidationProfiles** *(list) --* **[REQUIRED]**
            An array of ``ModelPackageValidationProfile`` objects, each of which specifies a batch transform job that Amazon SageMaker runs to validate your model package.
            - *(dict) --*
              Contains data, such as the inputs and targeted instance types that are used in the process of validating the model package.
              The data provided in the validation profile is made available to your buyers on AWS Marketplace.
              - **ProfileName** *(string) --* **[REQUIRED]**
                The name of the profile for the model package.
              - **TransformJobDefinition** *(dict) --* **[REQUIRED]**
                The ``TransformJobDefinition`` object that describes the transform job used for the validation of the model package.
                - **MaxConcurrentTransforms** *(integer) --*
                  The maximum number of parallel requests that can be sent to each instance in a transform job. The default value is 1.
                - **MaxPayloadInMB** *(integer) --*
                  The maximum payload size allowed, in MB. A payload is the data portion of a record (without metadata).
                - **BatchStrategy** *(string) --*
                  A string that determines the number of records included in a single mini-batch.
                   ``SingleRecord`` means only one record is used per mini-batch. ``MultiRecord`` means a mini-batch is set to contain as many records that can fit within the ``MaxPayloadInMB`` limit.
                - **Environment** *(dict) --*
                  The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.
                  - *(string) --*
                    - *(string) --*
                - **TransformInput** *(dict) --* **[REQUIRED]**
                  A description of the input source and the way the transform job consumes it.
                  - **DataSource** *(dict) --* **[REQUIRED]**
                    Describes the location of the channel data, which is, the S3 location of the input data that the model can consume.
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
                    If your transform data is compressed, specify the compression type. Amazon SageMaker automatically decompresses the data for the transform job accordingly. The default value is ``None`` .
                  - **SplitType** *(string) --*
                    The method to use to split the transform job\'s data files into smaller batches. Splitting is necessary when the total size of each object is too large to fit in a single request. You can also use data splitting to improve performance by processing multiple concurrent mini-batches. The default value for ``SplitType`` is ``None`` , which indicates that input data files are not split, and request payloads contain the entire contents of an input object. Set the value of this parameter to ``Line`` to split records on a newline character boundary. ``SplitType`` also supports a number of record-oriented binary data formats.
                    When splitting is enabled, the size of a mini-batch depends on the values of the ``BatchStrategy`` and ``MaxPayloadInMB`` parameters. When the value of ``BatchStrategy`` is ``MultiRecord`` , Amazon SageMaker sends the maximum number of records in each request, up to the ``MaxPayloadInMB`` limit. If the value of ``BatchStrategy`` is ``SingleRecord`` , Amazon SageMaker sends individual records in each request.
                    .. note::
                      Some data formats represent a record as a binary payload wrapped with extra padding bytes. When splitting is applied to a binary data format, padding is removed if the value of ``BatchStrategy`` is set to ``SingleRecord`` . Padding is not removed if the value of ``BatchStrategy`` is set to ``MultiRecord`` .
                      For more information about the RecordIO, see `Data Format <http://mxnet.io/architecture/note_data_loading.html#data-format>`__ in the MXNet documentation. For more information about the TFRecord, see `Consuming TFRecord data <https://www.tensorflow.org/guide/datasets#consuming_tfrecord_data>`__ in the TensorFlow documentation.
                - **TransformOutput** *(dict) --* **[REQUIRED]**
                  Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job.
                  - **S3OutputPath** *(string) --* **[REQUIRED]**
                    The Amazon S3 path where you want Amazon SageMaker to store the results of the transform job. For example, ``s3://bucket-name/key-name-prefix`` .
                    For every S3 object used as input for the transform job, batch transform stores the transformed data with an .``out`` suffix in a corresponding subfolder in the location in the output prefix. For example, for the input data stored at ``s3://bucket-name/input-name-prefix/dataset01/data.csv`` , batch transform stores the transformed data at ``s3://bucket-name/output-name-prefix/input-name-prefix/data.csv.out`` . Batch transform doesn\'t upload partially processed objects. For an input S3 object that contains multiple records, it creates an .``out`` file only if the transform job succeeds on the entire file. When the input contains multiple S3 objects, the batch transform job processes the listed S3 objects and uploads only the output for successfully processed objects. If any object fails in the transform job batch transform marks the job as failed to prompt investigation.
                  - **Accept** *(string) --*
                    The MIME type used to specify the output data. Amazon SageMaker uses the MIME type with each http call to transfer data from the transform job.
                  - **AssembleWith** *(string) --*
                    Defines how to assemble the results of the transform job as a single S3 object. Choose a format that is most convenient to you. To concatenate the results in binary format, specify ``None`` . To add a newline character at the end of every transformed record, specify ``Line`` .
                  - **KmsKeyId** *(string) --*
                    The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The ``KmsKeyId`` can be any of the following formats:
                    * // KMS Key ID  ``\"1234abcd-12ab-34cd-56ef-1234567890ab\"``
                    * // Amazon Resource Name (ARN) of a KMS Key  ``\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"``
                    * // KMS Key Alias  ``\"alias/ExampleAlias\"``
                    * // Amazon Resource Name (ARN) of a KMS Key Alias  ``\"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias\"``
                    If you don\'t provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role\'s account. For more information, see `KMS-Managed Encryption Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ in the *Amazon Simple Storage Service Developer Guide.*
                    The KMS key policy must grant permission to the IAM role that you specify in your ``CreateTramsformJob`` request. For more information, see `Using Key Policies in AWS KMS <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the *AWS Key Management Service Developer Guide* .
                - **TransformResources** *(dict) --* **[REQUIRED]**
                  Identifies the ML compute instances for the transform job.
                  - **InstanceType** *(string) --* **[REQUIRED]**
                    The ML compute instance type for the transform job. For using built-in algorithms to transform moderately sized datasets, ml.m4.xlarge or ``ml.m5.large`` should suffice. There is no default value for ``InstanceType`` .
                  - **InstanceCount** *(integer) --* **[REQUIRED]**
                    The number of ML compute instances to use in the transform job. For distributed transform, provide a value greater than 1. The default value is ``1`` .
                  - **VolumeKmsKeyId** *(string) --*
                    The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the batch transform job. The ``VolumeKmsKeyId`` can be any of the following formats:
                    * // KMS Key ID  ``\"1234abcd-12ab-34cd-56ef-1234567890ab\"``
                    * // Amazon Resource Name (ARN) of a KMS Key  ``\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"``
        :type SourceAlgorithmSpecification: dict
        :param SourceAlgorithmSpecification:
          Details about the algorithm that was used to create the model package.
          - **SourceAlgorithms** *(list) --* **[REQUIRED]**
            A list of the algorithms that were used to create a model package.
            - *(dict) --*
              Specifies an algorithm that was used to create the model package. The algorithm must be either an algorithm resource in your Amazon SageMaker account or an algorithm in AWS Marketplace that you are subscribed to.
              - **ModelDataUrl** *(string) --*
                The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single ``gzip`` compressed tar archive (``.tar.gz`` suffix).
              - **AlgorithmName** *(string) --* **[REQUIRED]**
                The name of an algorithm that was used to create the model package. The algorithm must be either an algorithm resource in your Amazon SageMaker account or an algorithm in AWS Marketplace that you are subscribed to.
        :type CertifyForMarketplace: boolean
        :param CertifyForMarketplace:
          Whether to certify the model package for listing on AWS Marketplace.
        :rtype: dict
        :returns:
        """
        pass

    def create_notebook_instance(self, NotebookInstanceName: str, InstanceType: str, RoleArn: str, SubnetId: str = None, SecurityGroupIds: List = None, KmsKeyId: str = None, Tags: List = None, LifecycleConfigName: str = None, DirectInternetAccess: str = None, VolumeSizeInGB: int = None, AcceleratorTypes: List = None, DefaultCodeRepository: str = None, AdditionalCodeRepositories: List = None, RootAccess: str = None) -> Dict:
        """
        Creates an Amazon SageMaker notebook instance. A notebook instance is a machine learning (ML) compute instance running on a Jupyter notebook. 
        In a ``CreateNotebookInstance`` request, specify the type of ML compute instance that you want to run. Amazon SageMaker launches the instance, installs common libraries that you can use to explore datasets for model training, and attaches an ML storage volume to the notebook instance. 
        Amazon SageMaker also provides a set of example notebooks. Each notebook demonstrates how to use Amazon SageMaker with a specific algorithm or with a machine learning framework. 
        After receiving the request, Amazon SageMaker does the following:
        * Creates a network interface in the Amazon SageMaker VPC. 
        * (Option) If you specified ``SubnetId`` , Amazon SageMaker creates a network interface in your own VPC, which is inferred from the subnet ID that you provide in the input. When creating this network interface, Amazon SageMaker attaches the security group that you specified in the request to the network interface that it creates in your VPC. 
        * Launches an EC2 instance of the type specified in the request in the Amazon SageMaker VPC. If you specified ``SubnetId`` of your VPC, Amazon SageMaker specifies both network interfaces when launching this instance. This enables inbound traffic from your own VPC to the notebook instance, assuming that the security groups allow it. 
        After creating the notebook instance, Amazon SageMaker returns its Amazon Resource Name (ARN).
        After Amazon SageMaker creates the notebook instance, you can connect to the Jupyter server and work in Jupyter notebooks. For example, you can write code to explore a dataset that you can use for model training, train a model, host models by creating Amazon SageMaker endpoints, and validate hosted models. 
        For more information, see `How It Works <https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html>`__ . 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateNotebookInstance>`_
        
        **Request Syntax**
        ::
          response = client.create_notebook_instance(
              NotebookInstanceName='string',
              InstanceType='ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.t3.medium'|'ml.t3.large'|'ml.t3.xlarge'|'ml.t3.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.c5d.xlarge'|'ml.c5d.2xlarge'|'ml.c5d.4xlarge'|'ml.c5d.9xlarge'|'ml.c5d.18xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge',
              SubnetId='string',
              SecurityGroupIds=[
                  'string',
              ],
              RoleArn='string',
              KmsKeyId='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              LifecycleConfigName='string',
              DirectInternetAccess='Enabled'|'Disabled',
              VolumeSizeInGB=123,
              AcceleratorTypes=[
                  'ml.eia1.medium'|'ml.eia1.large'|'ml.eia1.xlarge',
              ],
              DefaultCodeRepository='string',
              AdditionalCodeRepositories=[
                  'string',
              ],
              RootAccess='Enabled'|'Disabled'
          )
        
        **Response Syntax**
        ::
            {
                'NotebookInstanceArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **NotebookInstanceArn** *(string) --* 
              The Amazon Resource Name (ARN) of the notebook instance. 
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
          When you send any requests to AWS resources from the notebook instance, Amazon SageMaker assumes this role to perform tasks on your behalf. You must grant this role necessary permissions so Amazon SageMaker can perform these tasks. The policy must allow the Amazon SageMaker service principal (sagemaker.amazonaws.com) permissions to assume this role. For more information, see `Amazon SageMaker Roles <https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html>`__ .
          .. note::
            To be able to pass this role to Amazon SageMaker, the caller of this API must have the ``iam:PassRole`` permission.
        :type KmsKeyId: string
        :param KmsKeyId:
          If you provide a AWS KMS key ID, Amazon SageMaker uses it to encrypt data at rest on the ML storage volume that is attached to your notebook instance. The KMS key you provide must be enabled. For information, see `Enabling and Disabling Keys <http://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html>`__ in the *AWS Key Management Service Developer Guide* .
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
          The name of a lifecycle configuration to associate with the notebook instance. For information about lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
        :type DirectInternetAccess: string
        :param DirectInternetAccess:
          Sets whether Amazon SageMaker provides internet access to the notebook instance. If you set this to ``Disabled`` this notebook instance will be able to access resources only in your VPC, and will not be able to connect to Amazon SageMaker training and endpoint services unless your configure a NAT Gateway in your VPC.
          For more information, see `Notebook Instances Are Internet-Enabled by Default <https://docs.aws.amazon.com/sagemaker/latest/dg/appendix-additional-considerations.html#appendix-notebook-and-internet-access>`__ . You can set the value of this parameter to ``Disabled`` only if you set a value for the ``SubnetId`` parameter.
        :type VolumeSizeInGB: integer
        :param VolumeSizeInGB:
          The size, in GB, of the ML storage volume to attach to the notebook instance. The default value is 5 GB.
        :type AcceleratorTypes: list
        :param AcceleratorTypes:
          A list of Elastic Inference (EI) instance types to associate with this notebook instance. Currently, only one instance type can be associated with a notebook instance. For more information, see `Using Elastic Inference in Amazon SageMaker <http://docs.aws.amazon.com/sagemaker/latest/dg/ei.html>`__ .
          - *(string) --*
        :type DefaultCodeRepository: string
        :param DefaultCodeRepository:
          A Git repository to associate with the notebook instance as its default code repository. This can be either the name of a Git repository stored as a resource in your account, or the URL of a Git repository in `AWS CodeCommit <http://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html>`__ or in any other Git repository. When you open a notebook instance, it opens in the directory that contains this repository. For more information, see `Associating Git Repositories with Amazon SageMaker Notebook Instances <http://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html>`__ .
        :type AdditionalCodeRepositories: list
        :param AdditionalCodeRepositories:
          An array of up to three Git repositories to associate with the notebook instance. These can be either the names of Git repositories stored as resources in your account, or the URL of Git repositories in `AWS CodeCommit <http://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html>`__ or in any other Git repository. These repositories are cloned at the same level as the default repository of your notebook instance. For more information, see `Associating Git Repositories with Amazon SageMaker Notebook Instances <http://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html>`__ .
          - *(string) --*
        :type RootAccess: string
        :param RootAccess:
          Whether root access is enabled or disabled for users of the notebook instance. The default value is ``Enabled`` .
          .. note::
            Lifecycle configurations need root access to be able to set up a notebook instance. Because of this, lifecycle configurations associated with a notebook instance always run with root access even if you disable root access for users.
        :rtype: dict
        :returns:
        """
        pass

    def create_notebook_instance_lifecycle_config(self, NotebookInstanceLifecycleConfigName: str, OnCreate: List = None, OnStart: List = None) -> Dict:
        """
        Creates a lifecycle configuration that you can associate with a notebook instance. A *lifecycle configuration* is a collection of shell scripts that run when you create or start a notebook instance.
        Each lifecycle configuration script has a limit of 16384 characters.
        The value of the ``$PATH`` environment variable that is available to both scripts is ``/sbin:bin:/usr/sbin:/usr/bin`` .
        View CloudWatch Logs for notebook instance lifecycle configurations in log group ``/aws/sagemaker/NotebookInstances`` in log stream ``[notebook-instance-name]/[LifecycleConfigHook]`` .
        Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for longer than 5 minutes, it fails and the notebook instance is not created or started.
        For information about notebook instance lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateNotebookInstanceLifecycleConfig>`_
        
        **Request Syntax**
        ::
          response = client.create_notebook_instance_lifecycle_config(
              NotebookInstanceLifecycleConfigName='string',
              OnCreate=[
                  {
                      'Content': 'string'
                  },
              ],
              OnStart=[
                  {
                      'Content': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'NotebookInstanceLifecycleConfigArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **NotebookInstanceLifecycleConfigArn** *(string) --* 
              The Amazon Resource Name (ARN) of the lifecycle configuration.
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
            For information about notebook instance lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
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
            For information about notebook instance lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
            - **Content** *(string) --*
              A base64-encoded string that contains a shell script for a notebook instance lifecycle configuration.
        :rtype: dict
        :returns:
        """
        pass

    def create_presigned_notebook_instance_url(self, NotebookInstanceName: str, SessionExpirationDurationInSeconds: int = None) -> Dict:
        """
        Returns a URL that you can use to connect to the Jupyter server from a notebook instance. In the Amazon SageMaker console, when you choose ``Open`` next to a notebook instance, Amazon SageMaker opens a new tab showing the Jupyter server home page from the notebook instance. The console uses this API to get the URL and show the page.
        You can restrict access to this API and to the URL that it returns to a list of IP addresses that you specify. To restrict access, attach an IAM policy that denies access to this API unless the call comes from an IP address in the specified list to every AWS Identity and Access Management user, group, or role used to access the notebook instance. Use the ``NotIpAddress`` condition operator and the ``aws:SourceIP`` condition context key to specify the list of IP addresses that you want to have access to the notebook instance. For more information, see `Limit Access to a Notebook Instance by IP Address <https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-ip-filter.html>`__ .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreatePresignedNotebookInstanceUrl>`_
        
        **Request Syntax**
        ::
          response = client.create_presigned_notebook_instance_url(
              NotebookInstanceName='string',
              SessionExpirationDurationInSeconds=123
          )
        
        **Response Syntax**
        ::
            {
                'AuthorizedUrl': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AuthorizedUrl** *(string) --* 
              A JSON object that contains the URL string. 
        :type NotebookInstanceName: string
        :param NotebookInstanceName: **[REQUIRED]**
          The name of the notebook instance.
        :type SessionExpirationDurationInSeconds: integer
        :param SessionExpirationDurationInSeconds:
          The duration of the session, in seconds. The default is 12 hours.
        :rtype: dict
        :returns:
        """
        pass

    def create_training_job(self, TrainingJobName: str, AlgorithmSpecification: Dict, RoleArn: str, OutputDataConfig: Dict, ResourceConfig: Dict, StoppingCondition: Dict, HyperParameters: Dict = None, InputDataConfig: List = None, VpcConfig: Dict = None, Tags: List = None, EnableNetworkIsolation: bool = None, EnableInterContainerTrafficEncryption: bool = None) -> Dict:
        """
        Starts a model training job. After training completes, Amazon SageMaker saves the resulting model artifacts to an Amazon S3 location that you specify. 
        If you choose to host your model using Amazon SageMaker hosting services, you can use the resulting model artifacts as part of the model. You can also use the artifacts in a machine learning service other than Amazon SageMaker, provided that you know how to use them for inferences. 
        In the request body, you provide the following: 
        * ``AlgorithmSpecification`` - Identifies the training algorithm to use.  
        * ``HyperParameters`` - Specify these algorithm-specific parameters to influence the quality of the final model. For a list of hyperparameters for each training algorithm provided by Amazon SageMaker, see `Algorithms <https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ .  
        * ``InputDataConfig`` - Describes the training dataset and the Amazon S3 location where it is stored. 
        * ``OutputDataConfig`` - Identifies the Amazon S3 location where you want Amazon SageMaker to save the results of model training.   
        * ``ResourceConfig`` - Identifies the resources, ML compute instances, and ML storage volumes to deploy for model training. In distributed training, you specify more than one instance.  
        * ``RoleARN`` - The Amazon Resource Number (ARN) that Amazon SageMaker assumes to perform tasks on your behalf during model training. You must grant this role the necessary permissions so that Amazon SageMaker can successfully complete model training.  
        * ``StoppingCondition`` - Sets a duration for training. Use this parameter to cap model training costs.  
        For more information about Amazon SageMaker, see `How It Works <https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html>`__ . 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateTrainingJob>`_
        
        **Request Syntax**
        ::
          response = client.create_training_job(
              TrainingJobName='string',
              HyperParameters={
                  'string': 'string'
              },
              AlgorithmSpecification={
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
              RoleArn='string',
              InputDataConfig=[
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
              OutputDataConfig={
                  'KmsKeyId': 'string',
                  'S3OutputPath': 'string'
              },
              ResourceConfig={
                  'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
                  'InstanceCount': 123,
                  'VolumeSizeInGB': 123,
                  'VolumeKmsKeyId': 'string'
              },
              VpcConfig={
                  'SecurityGroupIds': [
                      'string',
                  ],
                  'Subnets': [
                      'string',
                  ]
              },
              StoppingCondition={
                  'MaxRuntimeInSeconds': 123
              },
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              EnableNetworkIsolation=True|False,
              EnableInterContainerTrafficEncryption=True|False
          )
        
        **Response Syntax**
        ::
            {
                'TrainingJobArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TrainingJobArn** *(string) --* 
              The Amazon Resource Name (ARN) of the training job.
        :type TrainingJobName: string
        :param TrainingJobName: **[REQUIRED]**
          The name of the training job. The name must be unique within an AWS Region in an AWS account.
        :type HyperParameters: dict
        :param HyperParameters:
          Algorithm-specific parameters that influence the quality of the model. You set hyperparameters before you start the learning process. For a list of hyperparameters for each training algorithm provided by Amazon SageMaker, see `Algorithms <https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ .
          You can specify a maximum of 100 hyperparameters. Each hyperparameter is a key-value pair. Each key and value is limited to 256 characters, as specified by the ``Length Constraint`` .
          - *(string) --*
            - *(string) --*
        :type AlgorithmSpecification: dict
        :param AlgorithmSpecification: **[REQUIRED]**
          The registry path of the Docker image that contains the training algorithm and algorithm-specific metadata, including the input mode. For more information about algorithms provided by Amazon SageMaker, see `Algorithms <https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ . For information about providing your own algorithms, see `Using Your Own Algorithms with Amazon SageMaker <https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__ .
          - **TrainingImage** *(string) --*
            The registry path of the Docker image that contains the training algorithm. For information about docker registry paths for built-in algorithms, see `Algorithms Provided by Amazon SageMaker\: Common Parameters <https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html>`__ . Amazon SageMaker supports both ``registry/repository[:tag]`` and ``registry/repository[@digest]`` image path formats. For more information, see `Using Your Own Algorithms with Amazon SageMaker <https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__ .
          - **AlgorithmName** *(string) --*
            The name of the algorithm resource to use for the training job. This must be an algorithm resource that you created or subscribe to on AWS Marketplace. If you specify a value for this parameter, you can\'t specify a value for ``TrainingImage`` .
          - **TrainingInputMode** *(string) --* **[REQUIRED]**
            The input mode that the algorithm supports. For the input modes that Amazon SageMaker algorithms support, see `Algorithms <https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ . If an algorithm supports the ``File`` input mode, Amazon SageMaker downloads the training data from S3 to the provisioned ML storage Volume, and mounts the directory to docker volume for training container. If an algorithm supports the ``Pipe`` input mode, Amazon SageMaker streams data directly from S3 to the container.
            In File mode, make sure you provision ML storage volume with sufficient capacity to accommodate the data download from S3. In addition to the training data, the ML storage volume also stores the output model. The algorithm container use ML storage volume to also store intermediate information, if any.
            For distributed algorithms using File mode, training data is distributed uniformly, and your training duration is predictable if the input data objects size is approximately same. Amazon SageMaker does not split the files any further for model training. If the object sizes are skewed, training won\'t be optimal as the data distribution is also skewed where one host in a training cluster is overloaded, thus becoming bottleneck in training.
          - **MetricDefinitions** *(list) --*
            A list of metric definition objects. Each object specifies the metric name and regular expressions used to parse algorithm logs. Amazon SageMaker publishes each metric to Amazon CloudWatch.
            - *(dict) --*
              Specifies a metric that the training algorithm writes to ``stderr`` or ``stdout`` . Amazon SageMakerhyperparameter tuning captures all defined metrics. You specify one metric that a hyperparameter tuning job uses as its objective metric to choose the best training job.
              - **Name** *(string) --* **[REQUIRED]**
                The name of the metric.
              - **Regex** *(string) --* **[REQUIRED]**
                A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see `Defining Objective Metrics <https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics.html>`__ .
        :type RoleArn: string
        :param RoleArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.
          During model training, Amazon SageMaker needs your permission to read input data from an S3 bucket, download a Docker image that contains training code, write model artifacts to an S3 bucket, write logs to Amazon CloudWatch Logs, and publish metrics to Amazon CloudWatch. You grant permissions for all of these tasks to an IAM role. For more information, see `Amazon SageMaker Roles <https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html>`__ .
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
                  If you choose ``S3Prefix`` , ``S3Uri`` identifies a key name prefix. Amazon SageMaker uses all objects that match the specified key name prefix for model training.
                  If you choose ``ManifestFile`` , ``S3Uri`` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for model training.
                  If you choose ``AugmentedManifestFile`` , S3Uri identifies an object that is an augmented manifest file in JSON lines format. This file contains the data you want to use for model training. ``AugmentedManifestFile`` can only be used if the Channel\'s input mode is ``Pipe`` .
                - **S3Uri** *(string) --* **[REQUIRED]**
                  Depending on the value specified for the ``S3DataType`` , identifies either a key name prefix or a manifest. For example:
                  * A key name prefix might look like this: ``s3://bucketname/exampleprefix`` .
                  * A manifest might look like this: ``s3://bucketname/example.manifest``   The manifest is an S3 object which is a JSON file with the following format:   ``[``    ``{\"prefix\": \"s3://customer_bucket/some/prefix/\"},``    ``\"relative/path/to/custdata-1\",``    ``\"relative/path/custdata-2\",``    ``...``    ``]``   The preceding JSON matches the following ``s3Uris`` :   ``s3://customer_bucket/some/prefix/relative/path/to/custdata-1``    ``s3://customer_bucket/some/prefix/relative/path/custdata-2``    ``...``   The complete set of ``s3uris`` in this manifest is the input data for the channel for this datasource. The object that each ``s3uris`` points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.
                - **S3DataDistributionType** *(string) --*
                  If you want Amazon SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify ``FullyReplicated`` .
                  If you want Amazon SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify ``ShardedByS3Key`` . If there are *n* ML compute instances launched for a training job, each instance gets approximately 1/*n* of the number of S3 objects. In this case, model training on each machine uses only the subset of training data.
                  Don\'t choose more ML compute instances for training than available S3 objects. If you do, some nodes won\'t get any data and you will pay for nodes that aren\'t getting any training data. This applies in both File and Pipe modes. Keep this in mind when developing algorithms.
                  In distributed training, where you use multiple ML compute EC2 instances, you might choose ``ShardedByS3Key`` . If the algorithm requires copying training data to the ML storage volume (when ``TrainingInputMode`` is set to ``File`` ), this copies 1/*n* of the number of objects.
                - **AttributeNames** *(list) --*
                  A list of one or more attribute names to use that are found in a specified augmented manifest file.
                  - *(string) --*
            - **ContentType** *(string) --*
              The MIME type of the data.
            - **CompressionType** *(string) --*
              If training data is compressed, the compression type. The default value is ``None`` . ``CompressionType`` is used only in Pipe input mode. In File mode, leave this field unset or set it to None.
            - **RecordWrapperType** *(string) --*
              Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format. In this case, Amazon SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you don\'t need to set this attribute. For more information, see `Create a Dataset Using RecordIO <https://mxnet.incubator.apache.org/architecture/note_data_loading.html#data-format>`__ .
              In File mode, leave this field unset or set it to None.
            - **InputMode** *(string) --*
              (Optional) The input mode to use for the data channel in a training job. If you don\'t set a value for ``InputMode`` , Amazon SageMaker uses the value set for ``TrainingInputMode`` . Use this parameter to override the ``TrainingInputMode`` setting in a  AlgorithmSpecification request when you have a channel that needs a different input mode from the training job\'s general setting. To download the data from Amazon Simple Storage Service (Amazon S3) to the provisioned ML storage volume, and mount the directory to a Docker volume, use ``File`` input mode. To stream data directly from Amazon S3 to the container, choose ``Pipe`` input mode.
              To use a model for incremental training, choose ``File`` input model.
            - **ShuffleConfig** *(dict) --*
              A configuration for a shuffle option for input data in a channel. If you use ``S3Prefix`` for ``S3DataType`` , this shuffles the results of the S3 key prefix matches. If you use ``ManifestFile`` , the order of the S3 object references in the ``ManifestFile`` is shuffled. If you use ``AugmentedManifestFile`` , the order of the JSON lines in the ``AugmentedManifestFile`` is shuffled. The shuffling order is determined using the ``Seed`` value.
              For Pipe input mode, shuffling is done at the start of every epoch. With large datasets this ensures that the order of the training data is different for each epoch, it helps reduce bias and possible overfitting. In a multi-node training job when ShuffleConfig is combined with ``S3DataDistributionType`` of ``ShardedByS3Key`` , the data is shuffled across nodes so that the content sent to a particular node on the first epoch might be sent to a different node on the second epoch.
              - **Seed** *(integer) --* **[REQUIRED]**
                Determines the shuffling order in ``ShuffleConfig`` value.
        :type OutputDataConfig: dict
        :param OutputDataConfig: **[REQUIRED]**
          Specifies the path to the S3 bucket where you want to store model artifacts. Amazon SageMaker creates subfolders for the artifacts.
          - **KmsKeyId** *(string) --*
            The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The ``KmsKeyId`` can be any of the following formats:
            * // KMS Key ID  ``\"1234abcd-12ab-34cd-56ef-1234567890ab\"``
            * // Amazon Resource Name (ARN) of a KMS Key  ``\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"``
            * // KMS Key Alias  ``\"alias/ExampleAlias\"``
            * // Amazon Resource Name (ARN) of a KMS Key Alias  ``\"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias\"``
            If you don\'t provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role\'s account. For more information, see `KMS-Managed Encryption Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ in the *Amazon Simple Storage Service Developer Guide.*
            The KMS key policy must grant permission to the IAM role that you specify in your ``CreateTramsformJob`` request. For more information, see `Using Key Policies in AWS KMS <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the *AWS Key Management Service Developer Guide* .
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
          A  VpcConfig object that specifies the VPC that you want your training job to connect to. Control access to and from your training container by configuring the VPC. For more information, see `Protect Training Jobs by Using an Amazon Virtual Private Cloud <https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html>`__ .
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
            The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 28 days.
        :type Tags: list
        :param Tags:
          An array of key-value pairs. For more information, see `Using Cost Allocation Tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what>`__ in the *AWS Billing and Cost Management User Guide* .
          - *(dict) --*
            Describes a tag.
            - **Key** *(string) --* **[REQUIRED]**
              The tag key.
            - **Value** *(string) --* **[REQUIRED]**
              The tag value.
        :type EnableNetworkIsolation: boolean
        :param EnableNetworkIsolation:
          Isolates the training container. No inbound or outbound network calls can be made, except for calls between peers within a training cluster for distributed training. If you enable network isolation for training jobs that are configured to use a VPC, Amazon SageMaker downloads and uploads customer data and model artifacts through the specified VPC, but the training container does not have network access.
          .. note::
            The Semantic Segmentation built-in algorithm does not support network isolation.
        :type EnableInterContainerTrafficEncryption: boolean
        :param EnableInterContainerTrafficEncryption:
          To encrypt all communications between ML compute instances in distributed training, choose ``True`` . Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithm in distributed training. For more information, see `Protect Communications Between ML Compute Instances in a Distributed Training Job <https://docs.aws.amazon.com/sagemaker/latest/dg/train-encrypt.html>`__ .
        :rtype: dict
        :returns:
        """
        pass

    def create_transform_job(self, TransformJobName: str, ModelName: str, TransformInput: Dict, TransformOutput: Dict, TransformResources: Dict, MaxConcurrentTransforms: int = None, MaxPayloadInMB: int = None, BatchStrategy: str = None, Environment: Dict = None, Tags: List = None) -> Dict:
        """
        Starts a transform job. A transform job uses a trained model to get inferences on a dataset and saves these results to an Amazon S3 location that you specify.
        To perform batch transformations, you create a transform job and use the data that you have readily available.
        In the request body, you provide the following:
        * ``TransformJobName`` - Identifies the transform job. The name must be unique within an AWS Region in an AWS account. 
        * ``ModelName`` - Identifies the model to use. ``ModelName`` must be the name of an existing Amazon SageMaker model in the same AWS Region and AWS account. For information on creating a model, see  CreateModel . 
        * ``TransformInput`` - Describes the dataset to be transformed and the Amazon S3 location where it is stored. 
        * ``TransformOutput`` - Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job. 
        * ``TransformResources`` - Identifies the ML compute instances for the transform job. 
        For more information about how batch transformation works Amazon SageMaker, see `How It Works <https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html>`__ . 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateTransformJob>`_
        
        **Request Syntax**
        ::
          response = client.create_transform_job(
              TransformJobName='string',
              ModelName='string',
              MaxConcurrentTransforms=123,
              MaxPayloadInMB=123,
              BatchStrategy='MultiRecord'|'SingleRecord',
              Environment={
                  'string': 'string'
              },
              TransformInput={
                  'DataSource': {
                      'S3DataSource': {
                          'S3DataType': 'ManifestFile'|'S3Prefix'|'AugmentedManifestFile',
                          'S3Uri': 'string'
                      }
                  },
                  'ContentType': 'string',
                  'CompressionType': 'None'|'Gzip',
                  'SplitType': 'None'|'Line'|'RecordIO'|'TFRecord'
              },
              TransformOutput={
                  'S3OutputPath': 'string',
                  'Accept': 'string',
                  'AssembleWith': 'None'|'Line',
                  'KmsKeyId': 'string'
              },
              TransformResources={
                  'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge',
                  'InstanceCount': 123,
                  'VolumeKmsKeyId': 'string'
              },
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'TransformJobArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TransformJobArn** *(string) --* 
              The Amazon Resource Name (ARN) of the transform job.
        :type TransformJobName: string
        :param TransformJobName: **[REQUIRED]**
          The name of the transform job. The name must be unique within an AWS Region in an AWS account.
        :type ModelName: string
        :param ModelName: **[REQUIRED]**
          The name of the model that you want to use for the transform job. ``ModelName`` must be the name of an existing Amazon SageMaker model within an AWS Region in an AWS account.
        :type MaxConcurrentTransforms: integer
        :param MaxConcurrentTransforms:
          The maximum number of parallel requests that can be sent to each instance in a transform job. The default value is ``1`` . To allow Amazon SageMaker to determine the appropriate number for ``MaxConcurrentTransforms`` , set the value to ``0`` .
        :type MaxPayloadInMB: integer
        :param MaxPayloadInMB:
          The maximum allowed size of the payload, in MB. A *payload* is the data portion of a record (without metadata). The value in ``MaxPayloadInMB`` must be greater than, or equal to, the size of a single record. To estimate the size of a record in MB, divide the size of your dataset by the number of records. To ensure that the records fit within the maximum payload size, we recommend using a slightly larger value. The default value is ``6`` MB.
          For cases where the payload might be arbitrarily large and is transmitted using HTTP chunked encoding, set the value to ``0`` . This feature works only in supported algorithms. Currently, Amazon SageMaker built-in algorithms do not support HTTP chunked encoding.
        :type BatchStrategy: string
        :param BatchStrategy:
          Specifies the number of records to include in a mini-batch for an HTTP inference request. A *record*  is a single unit of input data that inference can be made on. For example, a single line in a CSV file is a record.
          To enable the batch strategy, you must set ``SplitType`` to ``Line`` , ``RecordIO`` , or ``TFRecord`` .
          To use only one record when making an HTTP invocation request to a container, set ``BatchStrategy`` to ``SingleRecord`` and ``SplitType`` to ``Line`` .
          To fit as many records in a mini-batch as can fit within the ``MaxPayloadInMB`` limit, set ``BatchStrategy`` to ``MultiRecord`` and ``SplitType`` to ``Line`` .
        :type Environment: dict
        :param Environment:
          The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.
          - *(string) --*
            - *(string) --*
        :type TransformInput: dict
        :param TransformInput: **[REQUIRED]**
          Describes the input source and the way the transform job consumes it.
          - **DataSource** *(dict) --* **[REQUIRED]**
            Describes the location of the channel data, which is, the S3 location of the input data that the model can consume.
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
            If your transform data is compressed, specify the compression type. Amazon SageMaker automatically decompresses the data for the transform job accordingly. The default value is ``None`` .
          - **SplitType** *(string) --*
            The method to use to split the transform job\'s data files into smaller batches. Splitting is necessary when the total size of each object is too large to fit in a single request. You can also use data splitting to improve performance by processing multiple concurrent mini-batches. The default value for ``SplitType`` is ``None`` , which indicates that input data files are not split, and request payloads contain the entire contents of an input object. Set the value of this parameter to ``Line`` to split records on a newline character boundary. ``SplitType`` also supports a number of record-oriented binary data formats.
            When splitting is enabled, the size of a mini-batch depends on the values of the ``BatchStrategy`` and ``MaxPayloadInMB`` parameters. When the value of ``BatchStrategy`` is ``MultiRecord`` , Amazon SageMaker sends the maximum number of records in each request, up to the ``MaxPayloadInMB`` limit. If the value of ``BatchStrategy`` is ``SingleRecord`` , Amazon SageMaker sends individual records in each request.
            .. note::
              Some data formats represent a record as a binary payload wrapped with extra padding bytes. When splitting is applied to a binary data format, padding is removed if the value of ``BatchStrategy`` is set to ``SingleRecord`` . Padding is not removed if the value of ``BatchStrategy`` is set to ``MultiRecord`` .
              For more information about the RecordIO, see `Data Format <http://mxnet.io/architecture/note_data_loading.html#data-format>`__ in the MXNet documentation. For more information about the TFRecord, see `Consuming TFRecord data <https://www.tensorflow.org/guide/datasets#consuming_tfrecord_data>`__ in the TensorFlow documentation.
        :type TransformOutput: dict
        :param TransformOutput: **[REQUIRED]**
          Describes the results of the transform job.
          - **S3OutputPath** *(string) --* **[REQUIRED]**
            The Amazon S3 path where you want Amazon SageMaker to store the results of the transform job. For example, ``s3://bucket-name/key-name-prefix`` .
            For every S3 object used as input for the transform job, batch transform stores the transformed data with an .``out`` suffix in a corresponding subfolder in the location in the output prefix. For example, for the input data stored at ``s3://bucket-name/input-name-prefix/dataset01/data.csv`` , batch transform stores the transformed data at ``s3://bucket-name/output-name-prefix/input-name-prefix/data.csv.out`` . Batch transform doesn\'t upload partially processed objects. For an input S3 object that contains multiple records, it creates an .``out`` file only if the transform job succeeds on the entire file. When the input contains multiple S3 objects, the batch transform job processes the listed S3 objects and uploads only the output for successfully processed objects. If any object fails in the transform job batch transform marks the job as failed to prompt investigation.
          - **Accept** *(string) --*
            The MIME type used to specify the output data. Amazon SageMaker uses the MIME type with each http call to transfer data from the transform job.
          - **AssembleWith** *(string) --*
            Defines how to assemble the results of the transform job as a single S3 object. Choose a format that is most convenient to you. To concatenate the results in binary format, specify ``None`` . To add a newline character at the end of every transformed record, specify ``Line`` .
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
          (Optional) An array of key-value pairs. For more information, see `Using Cost Allocation Tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what>`__ in the *AWS Billing and Cost Management User Guide* .
          - *(dict) --*
            Describes a tag.
            - **Key** *(string) --* **[REQUIRED]**
              The tag key.
            - **Value** *(string) --* **[REQUIRED]**
              The tag value.
        :rtype: dict
        :returns:
        """
        pass

    def create_workteam(self, WorkteamName: str, MemberDefinitions: List, Description: str, Tags: List = None) -> Dict:
        """
        Creates a new work team for labeling your data. A work team is defined by one or more Amazon Cognito user pools. You must first create the user pools before you can create a work team.
        You cannot create more than 25 work teams in an account and region.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateWorkteam>`_
        
        **Request Syntax**
        ::
          response = client.create_workteam(
              WorkteamName='string',
              MemberDefinitions=[
                  {
                      'CognitoMemberDefinition': {
                          'UserPool': 'string',
                          'UserGroup': 'string',
                          'ClientId': 'string'
                      }
                  },
              ],
              Description='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'WorkteamArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **WorkteamArn** *(string) --* 
              The Amazon Resource Name (ARN) of the work team. You can use this ARN to identify the work team.
        :type WorkteamName: string
        :param WorkteamName: **[REQUIRED]**
          The name of the work team. Use this name to identify the work team.
        :type MemberDefinitions: list
        :param MemberDefinitions: **[REQUIRED]**
          A list of ``MemberDefinition`` objects that contains objects that identify the Amazon Cognito user pool that makes up the work team. For more information, see `Amazon Cognito User Pools <http://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html>`__ .
          All of the ``CognitoMemberDefinition`` objects that make up the member definition must have the same ``ClientId`` and ``UserPool`` values.
          - *(dict) --*
            Defines the Amazon Cognito user group that is part of a work team.
            - **CognitoMemberDefinition** *(dict) --*
              The Amazon Cognito user group that is part of the work team.
              - **UserPool** *(string) --* **[REQUIRED]**
                An identifier for a user pool. The user pool must be in the same region as the service that you are calling.
              - **UserGroup** *(string) --* **[REQUIRED]**
                An identifier for a user group.
              - **ClientId** *(string) --* **[REQUIRED]**
                An identifier for an application client. You must create the app client ID using Amazon Cognito.
        :type Description: string
        :param Description: **[REQUIRED]**
          A description of the work team.
        :type Tags: list
        :param Tags:
          - *(dict) --*
            Describes a tag.
            - **Key** *(string) --* **[REQUIRED]**
              The tag key.
            - **Value** *(string) --* **[REQUIRED]**
              The tag value.
        :rtype: dict
        :returns:
        """
        pass

    def delete_algorithm(self, AlgorithmName: str):
        """
        Removes the specified algorithm from your account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DeleteAlgorithm>`_
        
        **Request Syntax**
        ::
          response = client.delete_algorithm(
              AlgorithmName='string'
          )
        :type AlgorithmName: string
        :param AlgorithmName: **[REQUIRED]**
          The name of the algorithm to delete.
        :returns: None
        """
        pass

    def delete_code_repository(self, CodeRepositoryName: str):
        """
        Deletes the specified Git repository from your account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DeleteCodeRepository>`_
        
        **Request Syntax**
        ::
          response = client.delete_code_repository(
              CodeRepositoryName='string'
          )
        :type CodeRepositoryName: string
        :param CodeRepositoryName: **[REQUIRED]**
          The name of the Git repository to delete.
        :returns: None
        """
        pass

    def delete_endpoint(self, EndpointName: str):
        """
        Deletes an endpoint. Amazon SageMaker frees up all of the resources that were deployed when the endpoint was created. 
        Amazon SageMaker retires any custom KMS key grants associated with the endpoint, meaning you don't need to use the `RevokeGrant <http://docs.aws.amazon.com/kms/latest/APIReference/API_RevokeGrant.html>`__ API call.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DeleteEndpoint>`_
        
        **Request Syntax**
        ::
          response = client.delete_endpoint(
              EndpointName='string'
          )
        :type EndpointName: string
        :param EndpointName: **[REQUIRED]**
          The name of the endpoint that you want to delete.
        :returns: None
        """
        pass

    def delete_endpoint_config(self, EndpointConfigName: str):
        """
        Deletes an endpoint configuration. The ``DeleteEndpointConfig`` API deletes only the specified configuration. It does not delete endpoints created using the configuration. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DeleteEndpointConfig>`_
        
        **Request Syntax**
        ::
          response = client.delete_endpoint_config(
              EndpointConfigName='string'
          )
        :type EndpointConfigName: string
        :param EndpointConfigName: **[REQUIRED]**
          The name of the endpoint configuration that you want to delete.
        :returns: None
        """
        pass

    def delete_model(self, ModelName: str):
        """
        Deletes a model. The ``DeleteModel`` API deletes only the model entry that was created in Amazon SageMaker when you called the `CreateModel <https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateModel.html>`__ API. It does not delete model artifacts, inference code, or the IAM role that you specified when creating the model. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DeleteModel>`_
        
        **Request Syntax**
        ::
          response = client.delete_model(
              ModelName='string'
          )
        :type ModelName: string
        :param ModelName: **[REQUIRED]**
          The name of the model to delete.
        :returns: None
        """
        pass

    def delete_model_package(self, ModelPackageName: str):
        """
        Deletes a model package.
        A model package is used to create Amazon SageMaker models or list on AWS Marketplace. Buyers can subscribe to model packages listed on AWS Marketplace to create models in Amazon SageMaker.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DeleteModelPackage>`_
        
        **Request Syntax**
        ::
          response = client.delete_model_package(
              ModelPackageName='string'
          )
        :type ModelPackageName: string
        :param ModelPackageName: **[REQUIRED]**
          The name of the model package. The name must have 1 to 63 characters. Valid characters are a-z, A-Z, 0-9, and - (hyphen).
        :returns: None
        """
        pass

    def delete_notebook_instance(self, NotebookInstanceName: str):
        """
        Deletes an Amazon SageMaker notebook instance. Before you can delete a notebook instance, you must call the ``StopNotebookInstance`` API. 
        .. warning::
          When you delete a notebook instance, you lose all of your data. Amazon SageMaker removes the ML compute instance, and deletes the ML storage volume and the network interface associated with the notebook instance. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DeleteNotebookInstance>`_
        
        **Request Syntax**
        ::
          response = client.delete_notebook_instance(
              NotebookInstanceName='string'
          )
        :type NotebookInstanceName: string
        :param NotebookInstanceName: **[REQUIRED]**
          The name of the Amazon SageMaker notebook instance to delete.
        :returns: None
        """
        pass

    def delete_notebook_instance_lifecycle_config(self, NotebookInstanceLifecycleConfigName: str):
        """
        Deletes a notebook instance lifecycle configuration.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DeleteNotebookInstanceLifecycleConfig>`_
        
        **Request Syntax**
        ::
          response = client.delete_notebook_instance_lifecycle_config(
              NotebookInstanceLifecycleConfigName='string'
          )
        :type NotebookInstanceLifecycleConfigName: string
        :param NotebookInstanceLifecycleConfigName: **[REQUIRED]**
          The name of the lifecycle configuration to delete.
        :returns: None
        """
        pass

    def delete_tags(self, ResourceArn: str, TagKeys: List) -> Dict:
        """
        Deletes the specified tags from an Amazon SageMaker resource.
        To list a resource's tags, use the ``ListTags`` API. 
        .. note::
          When you call this API to delete tags from a hyperparameter tuning job, the deleted tags are not removed from training jobs that the hyperparameter tuning job launched before you called this API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DeleteTags>`_
        
        **Request Syntax**
        ::
          response = client.delete_tags(
              ResourceArn='string',
              TagKeys=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the resource whose tags you want to delete.
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**
          An array or one or more tag keys to delete.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def delete_workteam(self, WorkteamName: str) -> Dict:
        """
        Deletes an existing work team. This operation can't be undone.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DeleteWorkteam>`_
        
        **Request Syntax**
        ::
          response = client.delete_workteam(
              WorkteamName='string'
          )
        
        **Response Syntax**
        ::
            {
                'Success': True|False
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Success** *(boolean) --* 
              Returns ``true`` if the work team was successfully deleted; otherwise, returns ``false`` .
        :type WorkteamName: string
        :param WorkteamName: **[REQUIRED]**
          The name of the work team to delete.
        :rtype: dict
        :returns:
        """
        pass

    def describe_algorithm(self, AlgorithmName: str) -> Dict:
        """
        Returns a description of the specified algorithm that is in your account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeAlgorithm>`_
        
        **Request Syntax**
        ::
          response = client.describe_algorithm(
              AlgorithmName='string'
          )
        
        **Response Syntax**
        ::
            {
                'AlgorithmName': 'string',
                'AlgorithmArn': 'string',
                'AlgorithmDescription': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'TrainingSpecification': {
                    'TrainingImage': 'string',
                    'TrainingImageDigest': 'string',
                    'SupportedHyperParameters': [
                        {
                            'Name': 'string',
                            'Description': 'string',
                            'Type': 'Integer'|'Continuous'|'Categorical'|'FreeText',
                            'Range': {
                                'IntegerParameterRangeSpecification': {
                                    'MinValue': 'string',
                                    'MaxValue': 'string'
                                },
                                'ContinuousParameterRangeSpecification': {
                                    'MinValue': 'string',
                                    'MaxValue': 'string'
                                },
                                'CategoricalParameterRangeSpecification': {
                                    'Values': [
                                        'string',
                                    ]
                                }
                            },
                            'IsTunable': True|False,
                            'IsRequired': True|False,
                            'DefaultValue': 'string'
                        },
                    ],
                    'SupportedTrainingInstanceTypes': [
                        'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
                    ],
                    'SupportsDistributedTraining': True|False,
                    'MetricDefinitions': [
                        {
                            'Name': 'string',
                            'Regex': 'string'
                        },
                    ],
                    'TrainingChannels': [
                        {
                            'Name': 'string',
                            'Description': 'string',
                            'IsRequired': True|False,
                            'SupportedContentTypes': [
                                'string',
                            ],
                            'SupportedCompressionTypes': [
                                'None'|'Gzip',
                            ],
                            'SupportedInputModes': [
                                'Pipe'|'File',
                            ]
                        },
                    ],
                    'SupportedTuningJobObjectiveMetrics': [
                        {
                            'Type': 'Maximize'|'Minimize',
                            'MetricName': 'string'
                        },
                    ]
                },
                'InferenceSpecification': {
                    'Containers': [
                        {
                            'ContainerHostname': 'string',
                            'Image': 'string',
                            'ImageDigest': 'string',
                            'ModelDataUrl': 'string',
                            'ProductId': 'string'
                        },
                    ],
                    'SupportedTransformInstanceTypes': [
                        'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge',
                    ],
                    'SupportedRealtimeInferenceInstanceTypes': [
                        'ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.large'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.large'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
                    ],
                    'SupportedContentTypes': [
                        'string',
                    ],
                    'SupportedResponseMIMETypes': [
                        'string',
                    ]
                },
                'ValidationSpecification': {
                    'ValidationRole': 'string',
                    'ValidationProfiles': [
                        {
                            'ProfileName': 'string',
                            'TrainingJobDefinition': {
                                'TrainingInputMode': 'Pipe'|'File',
                                'HyperParameters': {
                                    'string': 'string'
                                },
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
                                'StoppingCondition': {
                                    'MaxRuntimeInSeconds': 123
                                }
                            },
                            'TransformJobDefinition': {
                                'MaxConcurrentTransforms': 123,
                                'MaxPayloadInMB': 123,
                                'BatchStrategy': 'MultiRecord'|'SingleRecord',
                                'Environment': {
                                    'string': 'string'
                                },
                                'TransformInput': {
                                    'DataSource': {
                                        'S3DataSource': {
                                            'S3DataType': 'ManifestFile'|'S3Prefix'|'AugmentedManifestFile',
                                            'S3Uri': 'string'
                                        }
                                    },
                                    'ContentType': 'string',
                                    'CompressionType': 'None'|'Gzip',
                                    'SplitType': 'None'|'Line'|'RecordIO'|'TFRecord'
                                },
                                'TransformOutput': {
                                    'S3OutputPath': 'string',
                                    'Accept': 'string',
                                    'AssembleWith': 'None'|'Line',
                                    'KmsKeyId': 'string'
                                },
                                'TransformResources': {
                                    'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge',
                                    'InstanceCount': 123,
                                    'VolumeKmsKeyId': 'string'
                                }
                            }
                        },
                    ]
                },
                'AlgorithmStatus': 'Pending'|'InProgress'|'Completed'|'Failed'|'Deleting',
                'AlgorithmStatusDetails': {
                    'ValidationStatuses': [
                        {
                            'Name': 'string',
                            'Status': 'NotStarted'|'InProgress'|'Completed'|'Failed',
                            'FailureReason': 'string'
                        },
                    ],
                    'ImageScanStatuses': [
                        {
                            'Name': 'string',
                            'Status': 'NotStarted'|'InProgress'|'Completed'|'Failed',
                            'FailureReason': 'string'
                        },
                    ]
                },
                'ProductId': 'string',
                'CertifyForMarketplace': True|False
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AlgorithmName** *(string) --* 
              The name of the algorithm being described.
            - **AlgorithmArn** *(string) --* 
              The Amazon Resource Name (ARN) of the algorithm.
            - **AlgorithmDescription** *(string) --* 
              A brief summary about the algorithm.
            - **CreationTime** *(datetime) --* 
              A timestamp specifying when the algorithm was created.
            - **TrainingSpecification** *(dict) --* 
              Details about training jobs run by this algorithm.
              - **TrainingImage** *(string) --* 
                The Amazon ECR registry path of the Docker image that contains the training algorithm.
              - **TrainingImageDigest** *(string) --* 
                An MD5 hash of the training algorithm that identifies the Docker image used for training.
              - **SupportedHyperParameters** *(list) --* 
                A list of the ``HyperParameterSpecification`` objects, that define the supported hyperparameters. This is required if the algorithm supports automatic model tuning.>
                - *(dict) --* 
                  Defines a hyperparameter to be used by an algorithm.
                  - **Name** *(string) --* 
                    The name of this hyperparameter. The name must be unique.
                  - **Description** *(string) --* 
                    A brief description of the hyperparameter.
                  - **Type** *(string) --* 
                    The type of this hyperparameter. The valid types are ``Integer`` , ``Continuous`` , ``Categorical`` , and ``FreeText`` .
                  - **Range** *(dict) --* 
                    The allowed range for this hyperparameter.
                    - **IntegerParameterRangeSpecification** *(dict) --* 
                      A ``IntegerParameterRangeSpecification`` object that defines the possible values for an integer hyperparameter.
                      - **MinValue** *(string) --* 
                        The minimum integer value allowed.
                      - **MaxValue** *(string) --* 
                        The maximum integer value allowed.
                    - **ContinuousParameterRangeSpecification** *(dict) --* 
                      A ``ContinuousParameterRangeSpecification`` object that defines the possible values for a continuous hyperparameter.
                      - **MinValue** *(string) --* 
                        The minimum floating-point value allowed.
                      - **MaxValue** *(string) --* 
                        The maximum floating-point value allowed.
                    - **CategoricalParameterRangeSpecification** *(dict) --* 
                      A ``CategoricalParameterRangeSpecification`` object that defines the possible values for a categorical hyperparameter.
                      - **Values** *(list) --* 
                        The allowed categories for the hyperparameter.
                        - *(string) --* 
                  - **IsTunable** *(boolean) --* 
                    Indicates whether this hyperparameter is tunable in a hyperparameter tuning job.
                  - **IsRequired** *(boolean) --* 
                    Indicates whether this hyperparameter is required.
                  - **DefaultValue** *(string) --* 
                    The default value for this hyperparameter. If a default value is specified, a hyperparameter cannot be required.
              - **SupportedTrainingInstanceTypes** *(list) --* 
                A list of the instance types that this algorithm can use for training.
                - *(string) --* 
              - **SupportsDistributedTraining** *(boolean) --* 
                Indicates whether the algorithm supports distributed training. If set to false, buyers can’t request more than one instance during training.
              - **MetricDefinitions** *(list) --* 
                A list of ``MetricDefinition`` objects, which are used for parsing metrics generated by the algorithm.
                - *(dict) --* 
                  Specifies a metric that the training algorithm writes to ``stderr`` or ``stdout`` . Amazon SageMakerhyperparameter tuning captures all defined metrics. You specify one metric that a hyperparameter tuning job uses as its objective metric to choose the best training job.
                  - **Name** *(string) --* 
                    The name of the metric.
                  - **Regex** *(string) --* 
                    A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see `Defining Objective Metrics <https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics.html>`__ .
              - **TrainingChannels** *(list) --* 
                A list of ``ChannelSpecification`` objects, which specify the input sources to be used by the algorithm.
                - *(dict) --* 
                  Defines a named input source, called a channel, to be used by an algorithm.
                  - **Name** *(string) --* 
                    The name of the channel.
                  - **Description** *(string) --* 
                    A brief description of the channel.
                  - **IsRequired** *(boolean) --* 
                    Indicates whether the channel is required by the algorithm.
                  - **SupportedContentTypes** *(list) --* 
                    The supported MIME types for the data.
                    - *(string) --* 
                  - **SupportedCompressionTypes** *(list) --* 
                    The allowed compression types, if data compression is used.
                    - *(string) --* 
                  - **SupportedInputModes** *(list) --* 
                    The allowed input mode, either FILE or PIPE.
                    In FILE mode, Amazon SageMaker copies the data from the input source onto the local Amazon Elastic Block Store (Amazon EBS) volumes before starting your training algorithm. This is the most commonly used input mode.
                    In PIPE mode, Amazon SageMaker streams input data from the source directly to your algorithm without using the EBS volume.
                    - *(string) --* 
              - **SupportedTuningJobObjectiveMetrics** *(list) --* 
                A list of the metrics that the algorithm emits that can be used as the objective metric in a hyperparameter tuning job.
                - *(dict) --* 
                  Defines the objective metric for a hyperparameter tuning job. Hyperparameter tuning uses the value of this metric to evaluate the training jobs it launches, and returns the training job that results in either the highest or lowest value for this metric, depending on the value you specify for the ``Type`` parameter.
                  - **Type** *(string) --* 
                    Whether to minimize or maximize the objective metric.
                  - **MetricName** *(string) --* 
                    The name of the metric to use for the objective metric.
            - **InferenceSpecification** *(dict) --* 
              Details about inference jobs that the algorithm runs.
              - **Containers** *(list) --* 
                The Amazon ECR registry path of the Docker image that contains the inference code.
                - *(dict) --* 
                  Describes the Docker container for the model package.
                  - **ContainerHostname** *(string) --* 
                    The DNS host name for the Docker container.
                  - **Image** *(string) --* 
                    The Amazon EC2 Container Registry (Amazon ECR) path where inference code is stored.
                    If you are using your own custom algorithm instead of an algorithm provided by Amazon SageMaker, the inference code must meet Amazon SageMaker requirements. Amazon SageMaker supports both ``registry/repository[:tag]`` and ``registry/repository[@digest]`` image path formats. For more information, see `Using Your Own Algorithms with Amazon SageMaker <https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__ .
                  - **ImageDigest** *(string) --* 
                    An MD5 hash of the training algorithm that identifies the Docker image used for training.
                  - **ModelDataUrl** *(string) --* 
                    The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single ``gzip`` compressed tar archive (``.tar.gz`` suffix).
                  - **ProductId** *(string) --* 
                    The AWS Marketplace product ID of the model package.
              - **SupportedTransformInstanceTypes** *(list) --* 
                A list of the instance types on which a transformation job can be run or on which an endpoint can be deployed.
                - *(string) --* 
              - **SupportedRealtimeInferenceInstanceTypes** *(list) --* 
                A list of the instance types that are used to generate inferences in real-time.
                - *(string) --* 
              - **SupportedContentTypes** *(list) --* 
                The supported MIME types for the input data.
                - *(string) --* 
              - **SupportedResponseMIMETypes** *(list) --* 
                The supported MIME types for the output data.
                - *(string) --* 
            - **ValidationSpecification** *(dict) --* 
              Details about configurations for one or more training jobs that Amazon SageMaker runs to test the algorithm.
              - **ValidationRole** *(string) --* 
                The IAM roles that Amazon SageMaker uses to run the training jobs.
              - **ValidationProfiles** *(list) --* 
                An array of ``AlgorithmValidationProfile`` objects, each of which specifies a training job and batch transform job that Amazon SageMaker runs to validate your algorithm.
                - *(dict) --* 
                  Defines a training job and a batch transform job that Amazon SageMaker runs to validate your algorithm.
                  The data provided in the validation profile is made available to your buyers on AWS Marketplace.
                  - **ProfileName** *(string) --* 
                    The name of the profile for the algorithm. The name must have 1 to 63 characters. Valid characters are a-z, A-Z, 0-9, and - (hyphen).
                  - **TrainingJobDefinition** *(dict) --* 
                    The ``TrainingJobDefinition`` object that describes the training job that Amazon SageMaker runs to validate your algorithm.
                    - **TrainingInputMode** *(string) --* 
                      The input mode used by the algorithm for the training job. For the input modes that Amazon SageMaker algorithms support, see `Algorithms <https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ .
                      If an algorithm supports the ``File`` input mode, Amazon SageMaker downloads the training data from S3 to the provisioned ML storage Volume, and mounts the directory to docker volume for training container. If an algorithm supports the ``Pipe`` input mode, Amazon SageMaker streams data directly from S3 to the container.
                    - **HyperParameters** *(dict) --* 
                      The hyperparameters used for the training job.
                      - *(string) --* 
                        - *(string) --* 
                    - **InputDataConfig** *(list) --* 
                      An array of ``Channel`` objects, each of which specifies an input source.
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
                      the path to the S3 bucket where you want to store model artifacts. Amazon SageMaker creates subfolders for the artifacts.
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
                      The resources, including the ML compute instances and ML storage volumes, to use for model training.
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
                    - **StoppingCondition** *(dict) --* 
                      Sets a duration for training. Use this parameter to cap model training costs.
                      To stop a job, Amazon SageMaker sends the algorithm the SIGTERM signal, which delays job termination for 120 seconds. Algorithms might use this 120-second window to save the model artifacts.
                      - **MaxRuntimeInSeconds** *(integer) --* 
                        The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 28 days.
                  - **TransformJobDefinition** *(dict) --* 
                    The ``TransformJobDefinition`` object that describes the transform job that Amazon SageMaker runs to validate your algorithm.
                    - **MaxConcurrentTransforms** *(integer) --* 
                      The maximum number of parallel requests that can be sent to each instance in a transform job. The default value is 1.
                    - **MaxPayloadInMB** *(integer) --* 
                      The maximum payload size allowed, in MB. A payload is the data portion of a record (without metadata).
                    - **BatchStrategy** *(string) --* 
                      A string that determines the number of records included in a single mini-batch.
                       ``SingleRecord`` means only one record is used per mini-batch. ``MultiRecord`` means a mini-batch is set to contain as many records that can fit within the ``MaxPayloadInMB`` limit.
                    - **Environment** *(dict) --* 
                      The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.
                      - *(string) --* 
                        - *(string) --* 
                    - **TransformInput** *(dict) --* 
                      A description of the input source and the way the transform job consumes it.
                      - **DataSource** *(dict) --* 
                        Describes the location of the channel data, which is, the S3 location of the input data that the model can consume.
                        - **S3DataSource** *(dict) --* 
                          The S3 location of the data source that is associated with a channel.
                          - **S3DataType** *(string) --* 
                            If you choose ``S3Prefix`` , ``S3Uri`` identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for batch transform. 
                            If you choose ``ManifestFile`` , ``S3Uri`` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for batch transform. 
                          - **S3Uri** *(string) --* 
                            Depending on the value specified for the ``S3DataType`` , identifies either a key name prefix or a manifest. For example:
                            * A key name prefix might look like this: ``s3://bucketname/exampleprefix`` .  
                            * A manifest might look like this: ``s3://bucketname/example.manifest``   The manifest is an S3 object which is a JSON file with the following format:   ``[``    ``{"prefix": "s3://customer_bucket/some/prefix/"},``    ``"relative/path/to/custdata-1",``    ``"relative/path/custdata-2",``    ``...``    ``]``   The preceding JSON matches the following ``S3Uris`` :   ``s3://customer_bucket/some/prefix/relative/path/to/custdata-1``    ``s3://customer_bucket/some/prefix/relative/path/custdata-1``    ``...``   The complete set of ``S3Uris`` in this manifest constitutes the input data for the channel for this datasource. The object that each ``S3Uris`` points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf. 
                      - **ContentType** *(string) --* 
                        The multipurpose internet mail extension (MIME) type of the data. Amazon SageMaker uses the MIME type with each http call to transfer data to the transform job.
                      - **CompressionType** *(string) --* 
                        If your transform data is compressed, specify the compression type. Amazon SageMaker automatically decompresses the data for the transform job accordingly. The default value is ``None`` .
                      - **SplitType** *(string) --* 
                        The method to use to split the transform job's data files into smaller batches. Splitting is necessary when the total size of each object is too large to fit in a single request. You can also use data splitting to improve performance by processing multiple concurrent mini-batches. The default value for ``SplitType`` is ``None`` , which indicates that input data files are not split, and request payloads contain the entire contents of an input object. Set the value of this parameter to ``Line`` to split records on a newline character boundary. ``SplitType`` also supports a number of record-oriented binary data formats.
                        When splitting is enabled, the size of a mini-batch depends on the values of the ``BatchStrategy`` and ``MaxPayloadInMB`` parameters. When the value of ``BatchStrategy`` is ``MultiRecord`` , Amazon SageMaker sends the maximum number of records in each request, up to the ``MaxPayloadInMB`` limit. If the value of ``BatchStrategy`` is ``SingleRecord`` , Amazon SageMaker sends individual records in each request.
                        .. note::
                          Some data formats represent a record as a binary payload wrapped with extra padding bytes. When splitting is applied to a binary data format, padding is removed if the value of ``BatchStrategy`` is set to ``SingleRecord`` . Padding is not removed if the value of ``BatchStrategy`` is set to ``MultiRecord`` .
                          For more information about the RecordIO, see `Data Format <http://mxnet.io/architecture/note_data_loading.html#data-format>`__ in the MXNet documentation. For more information about the TFRecord, see `Consuming TFRecord data <https://www.tensorflow.org/guide/datasets#consuming_tfrecord_data>`__ in the TensorFlow documentation.
                    - **TransformOutput** *(dict) --* 
                      Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job.
                      - **S3OutputPath** *(string) --* 
                        The Amazon S3 path where you want Amazon SageMaker to store the results of the transform job. For example, ``s3://bucket-name/key-name-prefix`` .
                        For every S3 object used as input for the transform job, batch transform stores the transformed data with an .``out`` suffix in a corresponding subfolder in the location in the output prefix. For example, for the input data stored at ``s3://bucket-name/input-name-prefix/dataset01/data.csv`` , batch transform stores the transformed data at ``s3://bucket-name/output-name-prefix/input-name-prefix/data.csv.out`` . Batch transform doesn't upload partially processed objects. For an input S3 object that contains multiple records, it creates an .``out`` file only if the transform job succeeds on the entire file. When the input contains multiple S3 objects, the batch transform job processes the listed S3 objects and uploads only the output for successfully processed objects. If any object fails in the transform job batch transform marks the job as failed to prompt investigation.
                      - **Accept** *(string) --* 
                        The MIME type used to specify the output data. Amazon SageMaker uses the MIME type with each http call to transfer data from the transform job.
                      - **AssembleWith** *(string) --* 
                        Defines how to assemble the results of the transform job as a single S3 object. Choose a format that is most convenient to you. To concatenate the results in binary format, specify ``None`` . To add a newline character at the end of every transformed record, specify ``Line`` .
                      - **KmsKeyId** *(string) --* 
                        The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The ``KmsKeyId`` can be any of the following formats: 
                        * // KMS Key ID  ``"1234abcd-12ab-34cd-56ef-1234567890ab"``   
                        * // Amazon Resource Name (ARN) of a KMS Key  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``   
                        * // KMS Key Alias  ``"alias/ExampleAlias"``   
                        * // Amazon Resource Name (ARN) of a KMS Key Alias  ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``   
                        If you don't provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role's account. For more information, see `KMS-Managed Encryption Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ in the *Amazon Simple Storage Service Developer Guide.*  
                        The KMS key policy must grant permission to the IAM role that you specify in your ``CreateTramsformJob`` request. For more information, see `Using Key Policies in AWS KMS <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the *AWS Key Management Service Developer Guide* .
                    - **TransformResources** *(dict) --* 
                      Identifies the ML compute instances for the transform job.
                      - **InstanceType** *(string) --* 
                        The ML compute instance type for the transform job. For using built-in algorithms to transform moderately sized datasets, ml.m4.xlarge or ``ml.m5.large`` should suffice. There is no default value for ``InstanceType`` .
                      - **InstanceCount** *(integer) --* 
                        The number of ML compute instances to use in the transform job. For distributed transform, provide a value greater than 1. The default value is ``1`` .
                      - **VolumeKmsKeyId** *(string) --* 
                        The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the batch transform job. The ``VolumeKmsKeyId`` can be any of the following formats:
                        * // KMS Key ID  ``"1234abcd-12ab-34cd-56ef-1234567890ab"``   
                        * // Amazon Resource Name (ARN) of a KMS Key  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``   
            - **AlgorithmStatus** *(string) --* 
              The current status of the algorithm.
            - **AlgorithmStatusDetails** *(dict) --* 
              Details about the current status of the algorithm.
              - **ValidationStatuses** *(list) --* 
                The status of algorithm validation.
                - *(dict) --* 
                  Represents the overall status of an algorithm.
                  - **Name** *(string) --* 
                    The name of the algorithm for which the overall status is being reported.
                  - **Status** *(string) --* 
                    The current status.
                  - **FailureReason** *(string) --* 
                    if the overall status is ``Failed`` , the reason for the failure.
              - **ImageScanStatuses** *(list) --* 
                The status of the scan of the algorithm's Docker image container.
                - *(dict) --* 
                  Represents the overall status of an algorithm.
                  - **Name** *(string) --* 
                    The name of the algorithm for which the overall status is being reported.
                  - **Status** *(string) --* 
                    The current status.
                  - **FailureReason** *(string) --* 
                    if the overall status is ``Failed`` , the reason for the failure.
            - **ProductId** *(string) --* 
              The product identifier of the algorithm.
            - **CertifyForMarketplace** *(boolean) --* 
              Whether the algorithm is certified to be listed in AWS Marketplace.
        :type AlgorithmName: string
        :param AlgorithmName: **[REQUIRED]**
          The name of the algorithm to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_code_repository(self, CodeRepositoryName: str) -> Dict:
        """
        Gets details about the specified Git repository.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeCodeRepository>`_
        
        **Request Syntax**
        ::
          response = client.describe_code_repository(
              CodeRepositoryName='string'
          )
        
        **Response Syntax**
        ::
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
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CodeRepositoryName** *(string) --* 
              The name of the Git repository.
            - **CodeRepositoryArn** *(string) --* 
              The Amazon Resource Name (ARN) of the Git repository.
            - **CreationTime** *(datetime) --* 
              The date and time that the repository was created.
            - **LastModifiedTime** *(datetime) --* 
              The date and time that the repository was last changed.
            - **GitConfig** *(dict) --* 
              Configuration details about the repository, including the URL where the repository is located, the default branch, and the Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the credentials used to access the repository.
              - **RepositoryUrl** *(string) --* 
                The URL where the Git repository is located.
              - **Branch** *(string) --* 
                The default branch for the Git repository.
              - **SecretArn** *(string) --* 
                The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the credentials used to access the git repository. The secret must have a staging label of ``AWSCURRENT`` and must be in the following format:
                 ``{"username": *UserName* , "password": *Password* }``  
        :type CodeRepositoryName: string
        :param CodeRepositoryName: **[REQUIRED]**
          The name of the Git repository to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_compilation_job(self, CompilationJobName: str) -> Dict:
        """
        Returns information about a model compilation job.
        To create a model compilation job, use  CreateCompilationJob . To get information about multiple model compilation jobs, use  ListCompilationJobs .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeCompilationJob>`_
        
        **Request Syntax**
        ::
          response = client.describe_compilation_job(
              CompilationJobName='string'
          )
        
        **Response Syntax**
        ::
            {
                'CompilationJobName': 'string',
                'CompilationJobArn': 'string',
                'CompilationJobStatus': 'INPROGRESS'|'COMPLETED'|'FAILED'|'STARTING'|'STOPPING'|'STOPPED',
                'CompilationStartTime': datetime(2015, 1, 1),
                'CompilationEndTime': datetime(2015, 1, 1),
                'StoppingCondition': {
                    'MaxRuntimeInSeconds': 123
                },
                'CreationTime': datetime(2015, 1, 1),
                'LastModifiedTime': datetime(2015, 1, 1),
                'FailureReason': 'string',
                'ModelArtifacts': {
                    'S3ModelArtifacts': 'string'
                },
                'RoleArn': 'string',
                'InputConfig': {
                    'S3Uri': 'string',
                    'DataInputConfig': 'string',
                    'Framework': 'TENSORFLOW'|'MXNET'|'ONNX'|'PYTORCH'|'XGBOOST'
                },
                'OutputConfig': {
                    'S3OutputLocation': 'string',
                    'TargetDevice': 'ml_m4'|'ml_m5'|'ml_c4'|'ml_c5'|'ml_p2'|'ml_p3'|'jetson_tx1'|'jetson_tx2'|'rasp3b'|'deeplens'|'rk3399'|'rk3288'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CompilationJobName** *(string) --* 
              The name of the model compilation job.
            - **CompilationJobArn** *(string) --* 
              The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker assumes to perform the model compilation job.
            - **CompilationJobStatus** *(string) --* 
              The status of the model compilation job.
            - **CompilationStartTime** *(datetime) --* 
              The time when the model compilation job started the ``CompilationJob`` instances. 
              You are billed for the time between this timestamp and the timestamp in the  DescribeCompilationJobResponse$CompilationEndTime field. In Amazon CloudWatch Logs, the start time might be later than this time. That's because it takes time to download the compilation job, which depends on the size of the compilation job container. 
            - **CompilationEndTime** *(datetime) --* 
              The time when the model compilation job on a compilation job instance ended. For a successful or stopped job, this is when the job's model artifacts have finished uploading. For a failed job, this is when Amazon SageMaker detected that the job failed. 
            - **StoppingCondition** *(dict) --* 
              The duration allowed for model compilation.
              - **MaxRuntimeInSeconds** *(integer) --* 
                The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 28 days.
            - **CreationTime** *(datetime) --* 
              The time that the model compilation job was created.
            - **LastModifiedTime** *(datetime) --* 
              The time that the status of the model compilation job was last modified.
            - **FailureReason** *(string) --* 
              If a model compilation job failed, the reason it failed. 
            - **ModelArtifacts** *(dict) --* 
              Information about the location in Amazon S3 that has been configured for storing the model artifacts used in the compilation job.
              - **S3ModelArtifacts** *(string) --* 
                The path of the S3 object that contains the model artifacts. For example, ``s3://bucket-name/keynameprefix/model.tar.gz`` .
            - **RoleArn** *(string) --* 
              The Amazon Resource Name (ARN) of the model compilation job.
            - **InputConfig** *(dict) --* 
              Information about the location in Amazon S3 of the input model artifacts, the name and shape of the expected data inputs, and the framework in which the model was trained.
              - **S3Uri** *(string) --* 
                The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).
              - **DataInputConfig** *(string) --* 
                Specifies the name and shape of the expected data inputs for your trained model with a JSON dictionary form. The data inputs are  InputConfig$Framework specific. 
                * ``TensorFlow`` : You must specify the name and shape (NHWC format) of the expected data inputs using a dictionary format for your trained model. The dictionary formats required for the console and CLI are different. 
                  * Examples for one input: 
                    * If using the console, ``{"input":[1,1024,1024,3]}``   
                    * If using the CLI, ``{\"input\":[1,1024,1024,3]}``   
                  * Examples for two inputs: 
                    * If using the console, ``{"data1": [1,28,28,1], "data2":[1,28,28,1]}``   
                    * If using the CLI, ``{\"data1\": [1,28,28,1], \"data2\":[1,28,28,1]}``   
                * ``MXNET/ONNX`` : You must specify the name and shape (NCHW format) of the expected data inputs in order using a dictionary format for your trained model. The dictionary formats required for the console and CLI are different. 
                  * Examples for one input: 
                    * If using the console, ``{"data":[1,3,1024,1024]}``   
                    * If using the CLI, ``{\"data\":[1,3,1024,1024]}``   
                  * Examples for two inputs: 
                    * If using the console, ``{"var1": [1,1,28,28], "var2":[1,1,28,28]}``   
                    * If using the CLI, ``{\"var1\": [1,1,28,28], \"var2\":[1,1,28,28]}``   
                * ``PyTorch`` : You can either specify the name and shape (NCHW format) of expected data inputs in order using a dictionary format for your trained model or you can specify the shape only using a list format. The dictionary formats required for the console and CLI are different. The list formats for the console and CLI are the same. 
                  * Examples for one input in dictionary format: 
                    * If using the console, ``{"input0":[1,3,224,224]}``   
                    * If using the CLI, ``{\"input0\":[1,3,224,224]}``   
                  * Example for one input in list format: ``[[1,3,224,224]]``   
                  * Examples for two inputs in dictionary format: 
                    * If using the console, ``{"input0":[1,3,224,224], "input1":[1,3,224,224]}``   
                    * If using the CLI, ``{\"input0\":[1,3,224,224], \"input1\":[1,3,224,224]}``   
                  * Example for two inputs in list format: ``[[1,3,224,224], [1,3,224,224]]``   
                * ``XGBOOST`` : input data name and shape are not needed. 
              - **Framework** *(string) --* 
                Identifies the framework in which the model was trained. For example: TENSORFLOW.
            - **OutputConfig** *(dict) --* 
              Information about the output location for the compiled model and the target device that the model runs on.
              - **S3OutputLocation** *(string) --* 
                Identifies the S3 path where you want Amazon SageMaker to store the model artifacts. For example, s3://bucket-name/key-name-prefix.
              - **TargetDevice** *(string) --* 
                Identifies the device that you want to run your model on after it has been compiled. For example: ml_c5.
        :type CompilationJobName: string
        :param CompilationJobName: **[REQUIRED]**
          The name of the model compilation job that you want information about.
        :rtype: dict
        :returns:
        """
        pass

    def describe_endpoint(self, EndpointName: str) -> Dict:
        """
        Returns the description of an endpoint.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeEndpoint>`_
        
        **Request Syntax**
        ::
          response = client.describe_endpoint(
              EndpointName='string'
          )
        
        **Response Syntax**
        ::
            {
                'EndpointName': 'string',
                'EndpointArn': 'string',
                'EndpointConfigName': 'string',
                'ProductionVariants': [
                    {
                        'VariantName': 'string',
                        'DeployedImages': [
                            {
                                'SpecifiedImage': 'string',
                                'ResolvedImage': 'string',
                                'ResolutionTime': datetime(2015, 1, 1)
                            },
                        ],
                        'CurrentWeight': ...,
                        'DesiredWeight': ...,
                        'CurrentInstanceCount': 123,
                        'DesiredInstanceCount': 123
                    },
                ],
                'EndpointStatus': 'OutOfService'|'Creating'|'Updating'|'SystemUpdating'|'RollingBack'|'InService'|'Deleting'|'Failed',
                'FailureReason': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LastModifiedTime': datetime(2015, 1, 1)
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
        :type EndpointName: string
        :param EndpointName: **[REQUIRED]**
          The name of the endpoint.
        :rtype: dict
        :returns:
        """
        pass

    def describe_endpoint_config(self, EndpointConfigName: str) -> Dict:
        """
        Returns the description of an endpoint configuration created using the ``CreateEndpointConfig`` API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeEndpointConfig>`_
        
        **Request Syntax**
        ::
          response = client.describe_endpoint_config(
              EndpointConfigName='string'
          )
        
        **Response Syntax**
        ::
            {
                'EndpointConfigName': 'string',
                'EndpointConfigArn': 'string',
                'ProductionVariants': [
                    {
                        'VariantName': 'string',
                        'ModelName': 'string',
                        'InitialInstanceCount': 123,
                        'InstanceType': 'ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.large'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.large'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
                        'InitialVariantWeight': ...,
                        'AcceleratorType': 'ml.eia1.medium'|'ml.eia1.large'|'ml.eia1.xlarge'
                    },
                ],
                'KmsKeyId': 'string',
                'CreationTime': datetime(2015, 1, 1)
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
                - **AcceleratorType** *(string) --* 
                  The size of the Elastic Inference (EI) instance to use for the production variant. EI instances provide on-demand GPU computing for inference. For more information, see `Using Elastic Inference in Amazon SageMaker <http://docs.aws.amazon.com/sagemaker/latest/dg/ei.html>`__ . For more information, see `Using Elastic Inference in Amazon SageMaker <http://docs.aws.amazon.com/sagemaker/latest/dg/ei.html>`__ .
            - **KmsKeyId** *(string) --* 
              AWS KMS key ID Amazon SageMaker uses to encrypt data when storing it on the ML storage volume attached to the instance.
            - **CreationTime** *(datetime) --* 
              A timestamp that shows when the endpoint configuration was created.
        :type EndpointConfigName: string
        :param EndpointConfigName: **[REQUIRED]**
          The name of the endpoint configuration.
        :rtype: dict
        :returns:
        """
        pass

    def describe_hyper_parameter_tuning_job(self, HyperParameterTuningJobName: str) -> Dict:
        """
        Gets a description of a hyperparameter tuning job.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeHyperParameterTuningJob>`_
        
        **Request Syntax**
        ::
          response = client.describe_hyper_parameter_tuning_job(
              HyperParameterTuningJobName='string'
          )
        
        **Response Syntax**
        ::
            {
                'HyperParameterTuningJobName': 'string',
                'HyperParameterTuningJobArn': 'string',
                'HyperParameterTuningJobConfig': {
                    'Strategy': 'Bayesian'|'Random',
                    'HyperParameterTuningJobObjective': {
                        'Type': 'Maximize'|'Minimize',
                        'MetricName': 'string'
                    },
                    'ResourceLimits': {
                        'MaxNumberOfTrainingJobs': 123,
                        'MaxParallelTrainingJobs': 123
                    },
                    'ParameterRanges': {
                        'IntegerParameterRanges': [
                            {
                                'Name': 'string',
                                'MinValue': 'string',
                                'MaxValue': 'string',
                                'ScalingType': 'Auto'|'Linear'|'Logarithmic'|'ReverseLogarithmic'
                            },
                        ],
                        'ContinuousParameterRanges': [
                            {
                                'Name': 'string',
                                'MinValue': 'string',
                                'MaxValue': 'string',
                                'ScalingType': 'Auto'|'Linear'|'Logarithmic'|'ReverseLogarithmic'
                            },
                        ],
                        'CategoricalParameterRanges': [
                            {
                                'Name': 'string',
                                'Values': [
                                    'string',
                                ]
                            },
                        ]
                    },
                    'TrainingJobEarlyStoppingType': 'Off'|'Auto'
                },
                'TrainingJobDefinition': {
                    'StaticHyperParameters': {
                        'string': 'string'
                    },
                    'AlgorithmSpecification': {
                        'TrainingImage': 'string',
                        'TrainingInputMode': 'Pipe'|'File',
                        'AlgorithmName': 'string',
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
                    'VpcConfig': {
                        'SecurityGroupIds': [
                            'string',
                        ],
                        'Subnets': [
                            'string',
                        ]
                    },
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
                    'StoppingCondition': {
                        'MaxRuntimeInSeconds': 123
                    },
                    'EnableNetworkIsolation': True|False,
                    'EnableInterContainerTrafficEncryption': True|False
                },
                'HyperParameterTuningJobStatus': 'Completed'|'InProgress'|'Failed'|'Stopped'|'Stopping',
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
                'BestTrainingJob': {
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
                'OverallBestTrainingJob': {
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
                'WarmStartConfig': {
                    'ParentHyperParameterTuningJobs': [
                        {
                            'HyperParameterTuningJobName': 'string'
                        },
                    ],
                    'WarmStartType': 'IdenticalDataAndAlgorithm'|'TransferLearning'
                },
                'FailureReason': 'string'
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
                Specifies how hyperparameter tuning chooses the combinations of hyperparameter values to use for the training job it launches. To use the Bayesian search stategy, set this to ``Bayesian`` . To randomly search, set it to ``Random`` . For information about search strategies, see `How Hyperparameter Tuning Works <http://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html>`__ .
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
                    - **ScalingType** *(string) --* 
                      The scale that hyperparameter tuning uses to search the hyperparameter range. For information about choosing a hyperparameter scale, see `Hyperparameter Range Scaling <http://docs.aws.amazon.com//sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type>`__ . One of the following values:
                        Auto  
                      Amazon SageMaker hyperparameter tuning chooses the best scale for the hyperparameter.
                        Linear  
                      Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.
                        Logarithmic  
                      Hyperparemeter tuning searches the values in the hyperparameter range by using a logarithmic scale.
                      Logarithmic scaling works only for ranges that have only values greater than 0.
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
                    - **ScalingType** *(string) --* 
                      The scale that hyperparameter tuning uses to search the hyperparameter range. For information about choosing a hyperparameter scale, see `Hyperparameter Range Scaling <http://docs.aws.amazon.com//sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type>`__ . One of the following values:
                        Auto  
                      Amazon SageMaker hyperparameter tuning chooses the best scale for the hyperparameter.
                        Linear  
                      Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.
                        Logarithmic  
                      Hyperparemeter tuning searches the values in the hyperparameter range by using a logarithmic scale.
                      Logarithmic scaling works only for ranges that have only values greater than 0.
                        ReverseLogarithmic  
                      Hyperparemeter tuning searches the values in the hyperparameter range by using a reverse logarithmic scale.
                      Reverse logarithmic scaling works only for ranges that are entirely within the range 0<=x<1.0.
                - **CategoricalParameterRanges** *(list) --* 
                  The array of  CategoricalParameterRange objects that specify ranges of categorical hyperparameters that a hyperparameter tuning job searches.
                  - *(dict) --* 
                    A list of categorical hyperparameters to tune.
                    - **Name** *(string) --* 
                      The name of the categorical hyperparameter to tune.
                    - **Values** *(list) --* 
                      A list of the categories for the hyperparameter.
                      - *(string) --* 
              - **TrainingJobEarlyStoppingType** *(string) --* 
                Specifies whether to use early stopping for training jobs launched by the hyperparameter tuning job. This can be one of the following values (the default value is ``OFF`` ):
                  OFF  
                Training jobs launched by the hyperparameter tuning job do not use early stopping.
                  AUTO  
                Amazon SageMaker stops training jobs launched by the hyperparameter tuning job when they are unlikely to perform better than previously completed training jobs. For more information, see `Stop Training Jobs Early <http://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-early-stopping.html>`__ .
            - **TrainingJobDefinition** *(dict) --* 
              The  HyperParameterTrainingJobDefinition object that specifies the definition of the training jobs that this tuning job launches.
              - **StaticHyperParameters** *(dict) --* 
                Specifies the values of hyperparameters that do not change for the tuning job.
                - *(string) --* 
                  - *(string) --* 
              - **AlgorithmSpecification** *(dict) --* 
                The  HyperParameterAlgorithmSpecification object that specifies the resource algorithm to use for the training jobs that the tuning job launches.
                - **TrainingImage** *(string) --* 
                  The registry path of the Docker image that contains the training algorithm. For information about Docker registry paths for built-in algorithms, see `Algorithms Provided by Amazon SageMaker\: Common Parameters <https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html>`__ . Amazon SageMaker supports both ``registry/repository[:tag]`` and ``registry/repository[@digest]`` image path formats. For more information, see `Using Your Own Algorithms with Amazon SageMaker <https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__ .
                - **TrainingInputMode** *(string) --* 
                  The input mode that the algorithm supports: File or Pipe. In File input mode, Amazon SageMaker downloads the training data from Amazon S3 to the storage volume that is attached to the training instance and mounts the directory to the Docker volume for the training container. In Pipe input mode, Amazon SageMaker streams data directly from Amazon S3 to the container. 
                  If you specify File mode, make sure that you provision the storage volume that is attached to the training instance with enough capacity to accommodate the training data downloaded from Amazon S3, the model artifacts, and intermediate information.
                  For more information about input modes, see `Algorithms <https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ . 
                - **AlgorithmName** *(string) --* 
                  The name of the resource algorithm to use for the hyperparameter tuning job. If you specify a value for this parameter, do not specify a value for ``TrainingImage`` .
                - **MetricDefinitions** *(list) --* 
                  An array of  MetricDefinition objects that specify the metrics that the algorithm emits.
                  - *(dict) --* 
                    Specifies a metric that the training algorithm writes to ``stderr`` or ``stdout`` . Amazon SageMakerhyperparameter tuning captures all defined metrics. You specify one metric that a hyperparameter tuning job uses as its objective metric to choose the best training job.
                    - **Name** *(string) --* 
                      The name of the metric.
                    - **Regex** *(string) --* 
                      A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see `Defining Objective Metrics <https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics.html>`__ .
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
              - **VpcConfig** *(dict) --* 
                The  VpcConfig object that specifies the VPC that you want the training jobs that this hyperparameter tuning job launches to connect to. Control access to and from your training container by configuring the VPC. For more information, see `Protect Training Jobs by Using an Amazon Virtual Private Cloud <https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html>`__ .
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
                  * // KMS Key ID  ``"1234abcd-12ab-34cd-56ef-1234567890ab"``   
                  * // Amazon Resource Name (ARN) of a KMS Key  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``   
                  * // KMS Key Alias  ``"alias/ExampleAlias"``   
                  * // Amazon Resource Name (ARN) of a KMS Key Alias  ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``   
                  If you don't provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role's account. For more information, see `KMS-Managed Encryption Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ in the *Amazon Simple Storage Service Developer Guide.*  
                  The KMS key policy must grant permission to the IAM role that you specify in your ``CreateTramsformJob`` request. For more information, see `Using Key Policies in AWS KMS <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the *AWS Key Management Service Developer Guide* .
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
                  * // KMS Key ID  ``"1234abcd-12ab-34cd-56ef-1234567890ab"``   
                  * // Amazon Resource Name (ARN) of a KMS Key  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``   
              - **StoppingCondition** *(dict) --* 
                Sets a maximum duration for the training jobs that the tuning job launches. Use this parameter to limit model training costs. 
                To stop a job, Amazon SageMaker sends the algorithm the ``SIGTERM`` signal. This delays job termination for 120 seconds. Algorithms might use this 120-second window to save the model artifacts.
                When Amazon SageMaker terminates a job because the stopping condition has been met, training algorithms provided by Amazon SageMaker save the intermediate results of the job.
                - **MaxRuntimeInSeconds** *(integer) --* 
                  The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 28 days.
              - **EnableNetworkIsolation** *(boolean) --* 
                Isolates the training container. No inbound or outbound network calls can be made, except for calls between peers within a training cluster for distributed training. If network isolation is used for training jobs that are configured to use a VPC, Amazon SageMaker downloads and uploads customer data and model artifacts through the specified VPC, but the training container does not have network access.
                .. note::
                  The Semantic Segmentation built-in algorithm does not support network isolation.
              - **EnableInterContainerTrafficEncryption** *(boolean) --* 
                To encrypt all communications between ML compute instances in distributed training, choose ``True`` . Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithm in distributed training.
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
            - **OverallBestTrainingJob** *(dict) --* 
              If the hyperparameter tuning job is an warm start tuning job with a ``WarmStartType`` of ``IDENTICAL_DATA_AND_ALGORITHM`` , this is the  TrainingJobSummary for the training job with the best objective metric value of all training jobs launched by this tuning job and all parent jobs specified for the warm start tuning job.
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
            - **WarmStartConfig** *(dict) --* 
              The configuration for starting the hyperparameter parameter tuning job using one or more previous tuning jobs as a starting point. The results of previous tuning jobs are used to inform which combinations of hyperparameters to search over in the new tuning job.
              - **ParentHyperParameterTuningJobs** *(list) --* 
                An array of hyperparameter tuning jobs that are used as the starting point for the new hyperparameter tuning job. For more information about warm starting a hyperparameter tuning job, see `Using a Previous Hyperparameter Tuning Job as a Starting Point <http://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-warm-start.html>`__ .
                Hyperparameter tuning jobs created before October 1, 2018 cannot be used as parent jobs for warm start tuning jobs.
                - *(dict) --* 
                  A previously completed or stopped hyperparameter tuning job to be used as a starting point for a new hyperparameter tuning job.
                  - **HyperParameterTuningJobName** *(string) --* 
                    The name of the hyperparameter tuning job to be used as a starting point for a new hyperparameter tuning job.
              - **WarmStartType** *(string) --* 
                Specifies one of the following:
                  IDENTICAL_DATA_AND_ALGORITHM  
                The new hyperparameter tuning job uses the same input data and training image as the parent tuning jobs. You can change the hyperparameter ranges to search and the maximum number of training jobs that the hyperparameter tuning job launches. You cannot use a new version of the training algorithm, unless the changes in the new version do not affect the algorithm itself. For example, changes that improve logging or adding support for a different data format are allowed. You can also change hyperparameters from tunable to static, and from static to tunable, but the total number of static plus tunable hyperparameters must remain the same as it is in all parent jobs. The objective metric for the new tuning job must be the same as for all parent jobs.
                  TRANSFER_LEARNING  
                The new hyperparameter tuning job can include input data, hyperparameter ranges, maximum number of concurrent training jobs, and maximum number of training jobs that are different than those of its parent hyperparameter tuning jobs. The training image can also be a different version from the version used in the parent hyperparameter tuning job. You can also change hyperparameters from tunable to static, and from static to tunable, but the total number of static plus tunable hyperparameters must remain the same as it is in all parent jobs. The objective metric for the new tuning job must be the same as for all parent jobs.
            - **FailureReason** *(string) --* 
              If the tuning job failed, the reason it failed.
        :type HyperParameterTuningJobName: string
        :param HyperParameterTuningJobName: **[REQUIRED]**
          The name of the tuning job to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_labeling_job(self, LabelingJobName: str) -> Dict:
        """
        Gets information about a labeling job.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeLabelingJob>`_
        
        **Request Syntax**
        ::
          response = client.describe_labeling_job(
              LabelingJobName='string'
          )
        
        **Response Syntax**
        ::
            {
                'LabelingJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
                'LabelCounters': {
                    'TotalLabeled': 123,
                    'HumanLabeled': 123,
                    'MachineLabeled': 123,
                    'FailedNonRetryableError': 123,
                    'Unlabeled': 123
                },
                'FailureReason': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LastModifiedTime': datetime(2015, 1, 1),
                'JobReferenceCode': 'string',
                'LabelingJobName': 'string',
                'LabelingJobArn': 'string',
                'LabelAttributeName': 'string',
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
                },
                'OutputConfig': {
                    'S3OutputPath': 'string',
                    'KmsKeyId': 'string'
                },
                'RoleArn': 'string',
                'LabelCategoryConfigS3Uri': 'string',
                'StoppingConditions': {
                    'MaxHumanLabeledObjectCount': 123,
                    'MaxPercentageOfInputDatasetLabeled': 123
                },
                'LabelingJobAlgorithmsConfig': {
                    'LabelingJobAlgorithmSpecificationArn': 'string',
                    'InitialActiveLearningModelArn': 'string',
                    'LabelingJobResourceConfig': {
                        'VolumeKmsKeyId': 'string'
                    }
                },
                'HumanTaskConfig': {
                    'WorkteamArn': 'string',
                    'UiConfig': {
                        'UiTemplateS3Uri': 'string'
                    },
                    'PreHumanTaskLambdaArn': 'string',
                    'TaskKeywords': [
                        'string',
                    ],
                    'TaskTitle': 'string',
                    'TaskDescription': 'string',
                    'NumberOfHumanWorkersPerDataObject': 123,
                    'TaskTimeLimitInSeconds': 123,
                    'TaskAvailabilityLifetimeInSeconds': 123,
                    'MaxConcurrentTaskCount': 123,
                    'AnnotationConsolidationConfig': {
                        'AnnotationConsolidationLambdaArn': 'string'
                    },
                    'PublicWorkforceTaskPrice': {
                        'AmountInUsd': {
                            'Dollars': 123,
                            'Cents': 123,
                            'TenthFractionsOfACent': 123
                        }
                    }
                },
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'LabelingJobOutput': {
                    'OutputDatasetS3Uri': 'string',
                    'FinalActiveLearningModelArn': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LabelingJobStatus** *(string) --* 
              The processing status of the labeling job. 
            - **LabelCounters** *(dict) --* 
              Provides a breakdown of the number of data objects labeled by humans, the number of objects labeled by machine, the number of objects than couldn't be labeled, and the total number of objects labeled. 
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
            - **FailureReason** *(string) --* 
              If the job failed, the reason that it failed. 
            - **CreationTime** *(datetime) --* 
              The date and time that the labeling job was created.
            - **LastModifiedTime** *(datetime) --* 
              The date and time that the labeling job was last updated.
            - **JobReferenceCode** *(string) --* 
              A unique identifier for work done as part of a labeling job.
            - **LabelingJobName** *(string) --* 
              The name assigned to the labeling job when it was created.
            - **LabelingJobArn** *(string) --* 
              The Amazon Resource Name (ARN) of the labeling job.
            - **LabelAttributeName** *(string) --* 
              The attribute used as the label in the output manifest file.
            - **InputConfig** *(dict) --* 
              Input configuration information for the labeling job, such as the Amazon S3 location of the data objects and the location of the manifest file that describes the data objects.
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
            - **OutputConfig** *(dict) --* 
              The location of the job's output data and the AWS Key Management Service key ID for the key used to encrypt the output data, if any.
              - **S3OutputPath** *(string) --* 
                The Amazon S3 location to write output data.
              - **KmsKeyId** *(string) --* 
                The AWS Key Management Service ID of the key used to encrypt the output data, if any.
            - **RoleArn** *(string) --* 
              The Amazon Resource Name (ARN) that Amazon SageMaker assumes to perform tasks on your behalf during data labeling.
            - **LabelCategoryConfigS3Uri** *(string) --* 
              The S3 location of the JSON file that defines the categories used to label data objects.
              The file is a JSON structure in the following format:
               ``{``  
               ``"document-version": "2018-11-28"``  
               ``"labels": [``  
               ``{``  
               ``"label": "*label 1* "``  
               ``},``  
               ``{``  
               ``"label": "*label 2* "``  
               ``},``  
               ``...``  
               ``{``  
               ``"label": "*label n* "``  
               ``}``  
               ``]``  
               ``}``  
            - **StoppingConditions** *(dict) --* 
              A set of conditions for stopping a labeling job. If any of the conditions are met, the job is automatically stopped.
              - **MaxHumanLabeledObjectCount** *(integer) --* 
                The maximum number of objects that can be labeled by human workers.
              - **MaxPercentageOfInputDatasetLabeled** *(integer) --* 
                The maximum number of input data objects that should be labeled.
            - **LabelingJobAlgorithmsConfig** *(dict) --* 
              Configuration information for automated data labeling.
              - **LabelingJobAlgorithmSpecificationArn** *(string) --* 
                Specifies the Amazon Resource Name (ARN) of the algorithm used for auto-labeling. You must select one of the following ARNs:
                * *Image classification*    ``arn:aws:sagemaker:*region* :027400017018:labeling-job-algorithm-specification/image-classification``   
                * *Text classification*    ``arn:aws:sagemaker:*region* :027400017018:labeling-job-algorithm-specification/text-classification``   
                * *Object detection*    ``arn:aws:sagemaker:*region* :027400017018:labeling-job-algorithm-specification/object-detection``   
              - **InitialActiveLearningModelArn** *(string) --* 
                At the end of an auto-label job Amazon SageMaker Ground Truth sends the Amazon Resource Nam (ARN) of the final model used for auto-labeling. You can use this model as the starting point for subsequent similar jobs by providing the ARN of the model here. 
              - **LabelingJobResourceConfig** *(dict) --* 
                Provides configuration information for a labeling job.
                - **VolumeKmsKeyId** *(string) --* 
                  The AWS Key Management Service key ID for the key used to encrypt the output data, if any.
            - **HumanTaskConfig** *(dict) --* 
              Configuration information required for human workers to complete a labeling task.
              - **WorkteamArn** *(string) --* 
                The Amazon Resource Name (ARN) of the work team assigned to complete the tasks.
              - **UiConfig** *(dict) --* 
                Information about the user interface that workers use to complete the labeling task.
                - **UiTemplateS3Uri** *(string) --* 
                  The Amazon S3 bucket location of the UI template. For more information about the contents of a UI template, see `Creating Your Custom Labeling Task Template <http://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates-step2.html>`__ .
              - **PreHumanTaskLambdaArn** *(string) --* 
                The Amazon Resource Name (ARN) of a Lambda function that is run before a data object is sent to a human worker. Use this function to provide input to a custom labeling job.
                For the built-in bounding box, image classification, semantic segmentation, and text classification task types, Amazon SageMaker Ground Truth provides the following Lambda functions:
        
        **US East (Northern Virginia) (us-east-1):**
                * ``arn:aws:lambda:us-east-1:432418664414:function:PRE-BoundingBox``   
                * ``arn:aws:lambda:us-east-1:432418664414:function:PRE-ImageMultiClass``   
                * ``arn:aws:lambda:us-east-1:432418664414:function:PRE-SemanticSegmentation``   
                * ``arn:aws:lambda:us-east-1:432418664414:function:PRE-TextMultiClass``   
        
        **US East (Ohio) (us-east-2):**
                * ``arn:aws:lambda:us-east-2:266458841044:function:PRE-BoundingBox``   
                * ``arn:aws:lambda:us-east-2:266458841044:function:PRE-ImageMultiClass``   
                * ``arn:aws:lambda:us-east-2:266458841044:function:PRE-SemanticSegmentation``   
                * ``arn:aws:lambda:us-east-2:266458841044:function:PRE-TextMultiClass``   
        
        **US West (Oregon) (us-west-2):**
                * ``arn:aws:lambda:us-west-2:081040173940:function:PRE-BoundingBox``   
                * ``arn:aws:lambda:us-west-2:081040173940:function:PRE-ImageMultiClass``   
                * ``arn:aws:lambda:us-west-2:081040173940:function:PRE-SemanticSegmentation``   
                * ``arn:aws:lambda:us-west-2:081040173940:function:PRE-TextMultiClass``   
        
        **EU (Ireland) (eu-west-1):**
                * ``arn:aws:lambda:eu-west-1:568282634449:function:PRE-BoundingBox``   
                * ``arn:aws:lambda:eu-west-1:568282634449:function:PRE-ImageMultiClass``   
                * ``arn:aws:lambda:eu-west-1:568282634449:function:PRE-SemanticSegmentation``   
                * ``arn:aws:lambda:eu-west-1:568282634449:function:PRE-TextMultiClass``   
        
        **Asia Pacific (Tokyo (ap-northeast-1):**
                * ``arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-BoundingBox``   
                * ``arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-ImageMultiClass``   
                * ``arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-SemanticSegmentation``   
                * ``arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-TextMultiClass``   
              - **TaskKeywords** *(list) --* 
                Keywords used to describe the task so that workers on Amazon Mechanical Turk can discover the task.
                - *(string) --* 
              - **TaskTitle** *(string) --* 
                A title for the task for your human workers.
              - **TaskDescription** *(string) --* 
                A description of the task for your human workers.
              - **NumberOfHumanWorkersPerDataObject** *(integer) --* 
                The number of human workers that will label an object. 
              - **TaskTimeLimitInSeconds** *(integer) --* 
                The amount of time that a worker has to complete a task.
              - **TaskAvailabilityLifetimeInSeconds** *(integer) --* 
                The length of time that a task remains available for labelling by human workers.
              - **MaxConcurrentTaskCount** *(integer) --* 
                Defines the maximum number of data objects that can be labeled by human workers at the same time. Each object may have more than one worker at one time.
              - **AnnotationConsolidationConfig** *(dict) --* 
                Configures how labels are consolidated across human workers.
                - **AnnotationConsolidationLambdaArn** *(string) --* 
                  The Amazon Resource Name (ARN) of a Lambda function implements the logic for annotation consolidation.
                  For the built-in bounding box, image classification, semantic segmentation, and text classification task types, Amazon SageMaker Ground Truth provides the following Lambda functions:
                  * *Bounding box* - Finds the most similar boxes from different workers based on the Jaccard index of the boxes.  ``arn:aws:lambda:us-east-1:432418664414:function:ACS-BoundingBox``    ``arn:aws:lambda:us-east-2:266458841044:function:ACS-BoundingBox``    ``arn:aws:lambda:us-west-2:081040173940:function:ACS-BoundingBox``    ``arn:aws:lambda:eu-west-1:568282634449:function:ACS-BoundingBox``    ``arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-BoundingBox``   
                  * *Image classification* - Uses a variant of the Expectation Maximization approach to estimate the true class of an image based on annotations from individual workers.  ``arn:aws:lambda:us-east-1:432418664414:function:ACS-ImageMultiClass``    ``arn:aws:lambda:us-east-2:266458841044:function:ACS-ImageMultiClass``    ``arn:aws:lambda:us-west-2:081040173940:function:ACS-ImageMultiClass``    ``arn:aws:lambda:eu-west-1:568282634449:function:ACS-ImageMultiClass``    ``arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-ImageMultiClass``   
                  * *Semantic segmentation* - Treats each pixel in an image as a multi-class classification and treats pixel annotations from workers as "votes" for the correct label.  ``arn:aws:lambda:us-east-1:432418664414:function:ACS-SemanticSegmentation``    ``arn:aws:lambda:us-east-2:266458841044:function:ACS-SemanticSegmentation``    ``arn:aws:lambda:us-west-2:081040173940:function:ACS-SemanticSegmentation``    ``arn:aws:lambda:eu-west-1:568282634449:function:ACS-SemanticSegmentation``    ``arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-SemanticSegmentation``   
                  * *Text classification* - Uses a variant of the Expectation Maximization approach to estimate the true class of text based on annotations from individual workers.  ``arn:aws:lambda:us-east-1:432418664414:function:ACS-TextMultiClass``    ``arn:aws:lambda:us-east-2:266458841044:function:ACS-TextMultiClass``    ``arn:aws:lambda:us-west-2:081040173940:function:ACS-TextMultiClass``    ``arn:aws:lambda:eu-west-1:568282634449:function:ACS-TextMultiClass``    ``arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-TextMultiClass``   
                  For more information, see `Annotation Consolidation <http://docs.aws.amazon.com/sagemaker/latest/dg/sms-annotation-consolidation.html>`__ .
              - **PublicWorkforceTaskPrice** *(dict) --* 
                The price that you pay for each task performed by a public worker.
                - **AmountInUsd** *(dict) --* 
                  Defines the amount of money paid to a worker in United States dollars.
                  - **Dollars** *(integer) --* 
                    The whole number of dollars in the amount.
                  - **Cents** *(integer) --* 
                    The fractional portion, in cents, of the amount. 
                  - **TenthFractionsOfACent** *(integer) --* 
                    Fractions of a cent, in tenths.
            - **Tags** *(list) --* 
              An array of key/value pairs. For more information, see `Using Cost Allocation Tags <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what>`__ in the *AWS Billing and Cost Management User Guide* .
              - *(dict) --* 
                Describes a tag. 
                - **Key** *(string) --* 
                  The tag key.
                - **Value** *(string) --* 
                  The tag value.
            - **LabelingJobOutput** *(dict) --* 
              The location of the output produced by the labeling job.
              - **OutputDatasetS3Uri** *(string) --* 
                The Amazon S3 bucket location of the manifest file for labeled data. 
              - **FinalActiveLearningModelArn** *(string) --* 
                The Amazon Resource Name (ARN) for the most recent Amazon SageMaker model trained as part of automated data labeling. 
        :type LabelingJobName: string
        :param LabelingJobName: **[REQUIRED]**
          The name of the labeling job to return information for.
        :rtype: dict
        :returns:
        """
        pass

    def describe_model(self, ModelName: str) -> Dict:
        """
        Describes a model that you created using the ``CreateModel`` API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeModel>`_
        
        **Request Syntax**
        ::
          response = client.describe_model(
              ModelName='string'
          )
        
        **Response Syntax**
        ::
            {
                'ModelName': 'string',
                'PrimaryContainer': {
                    'ContainerHostname': 'string',
                    'Image': 'string',
                    'ModelDataUrl': 'string',
                    'Environment': {
                        'string': 'string'
                    },
                    'ModelPackageName': 'string'
                },
                'Containers': [
                    {
                        'ContainerHostname': 'string',
                        'Image': 'string',
                        'ModelDataUrl': 'string',
                        'Environment': {
                            'string': 'string'
                        },
                        'ModelPackageName': 'string'
                    },
                ],
                'ExecutionRoleArn': 'string',
                'VpcConfig': {
                    'SecurityGroupIds': [
                        'string',
                    ],
                    'Subnets': [
                        'string',
                    ]
                },
                'CreationTime': datetime(2015, 1, 1),
                'ModelArn': 'string',
                'EnableNetworkIsolation': True|False
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ModelName** *(string) --* 
              Name of the Amazon SageMaker model.
            - **PrimaryContainer** *(dict) --* 
              The location of the primary inference code, associated artifacts, and custom environment map that the inference code uses when it is deployed in production. 
              - **ContainerHostname** *(string) --* 
                This parameter is ignored.
              - **Image** *(string) --* 
                The Amazon EC2 Container Registry (Amazon ECR) path where inference code is stored. If you are using your own custom algorithm instead of an algorithm provided by Amazon SageMaker, the inference code must meet Amazon SageMaker requirements. Amazon SageMaker supports both ``registry/repository[:tag]`` and ``registry/repository[@digest]`` image path formats. For more information, see `Using Your Own Algorithms with Amazon SageMaker <https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__  
              - **ModelDataUrl** *(string) --* 
                The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix). 
                If you provide a value for this parameter, Amazon SageMaker uses AWS Security Token Service to download model artifacts from the S3 path you provide. AWS STS is activated in your IAM user account by default. If you previously deactivated AWS STS for a region, you need to reactivate AWS STS for that region. For more information, see `Activating and Deactivating AWS STS in an AWS Region <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html>`__ in the *AWS Identity and Access Management User Guide* .
              - **Environment** *(dict) --* 
                The environment variables to set in the Docker container. Each key and value in the ``Environment`` string to string map can have length of up to 1024. We support up to 16 entries in the map. 
                - *(string) --* 
                  - *(string) --* 
              - **ModelPackageName** *(string) --* 
                The name of the model package to use to create the model.
            - **Containers** *(list) --* 
              The containers in the inference pipeline.
              - *(dict) --* 
                Describes the container, as part of model definition.
                - **ContainerHostname** *(string) --* 
                  This parameter is ignored.
                - **Image** *(string) --* 
                  The Amazon EC2 Container Registry (Amazon ECR) path where inference code is stored. If you are using your own custom algorithm instead of an algorithm provided by Amazon SageMaker, the inference code must meet Amazon SageMaker requirements. Amazon SageMaker supports both ``registry/repository[:tag]`` and ``registry/repository[@digest]`` image path formats. For more information, see `Using Your Own Algorithms with Amazon SageMaker <https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__  
                - **ModelDataUrl** *(string) --* 
                  The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix). 
                  If you provide a value for this parameter, Amazon SageMaker uses AWS Security Token Service to download model artifacts from the S3 path you provide. AWS STS is activated in your IAM user account by default. If you previously deactivated AWS STS for a region, you need to reactivate AWS STS for that region. For more information, see `Activating and Deactivating AWS STS in an AWS Region <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html>`__ in the *AWS Identity and Access Management User Guide* .
                - **Environment** *(dict) --* 
                  The environment variables to set in the Docker container. Each key and value in the ``Environment`` string to string map can have length of up to 1024. We support up to 16 entries in the map. 
                  - *(string) --* 
                    - *(string) --* 
                - **ModelPackageName** *(string) --* 
                  The name of the model package to use to create the model.
            - **ExecutionRoleArn** *(string) --* 
              The Amazon Resource Name (ARN) of the IAM role that you specified for the model.
            - **VpcConfig** *(dict) --* 
              A  VpcConfig object that specifies the VPC that this model has access to. For more information, see `Protect Endpoints by Using an Amazon Virtual Private Cloud <https://docs.aws.amazon.com/sagemaker/latest/dg/host-vpc.html>`__  
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
            - **EnableNetworkIsolation** *(boolean) --* 
              If ``True`` , no inbound or outbound network calls can be made to or from the model container.
              .. note::
                The Semantic Segmentation built-in algorithm does not support network isolation.
        :type ModelName: string
        :param ModelName: **[REQUIRED]**
          The name of the model.
        :rtype: dict
        :returns:
        """
        pass

    def describe_model_package(self, ModelPackageName: str) -> Dict:
        """
        Returns a description of the specified model package, which is used to create Amazon SageMaker models or list them on AWS Marketplace.
        To create models in Amazon SageMaker, buyers can subscribe to model packages listed on AWS Marketplace.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeModelPackage>`_
        
        **Request Syntax**
        ::
          response = client.describe_model_package(
              ModelPackageName='string'
          )
        
        **Response Syntax**
        ::
            {
                'ModelPackageName': 'string',
                'ModelPackageArn': 'string',
                'ModelPackageDescription': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'InferenceSpecification': {
                    'Containers': [
                        {
                            'ContainerHostname': 'string',
                            'Image': 'string',
                            'ImageDigest': 'string',
                            'ModelDataUrl': 'string',
                            'ProductId': 'string'
                        },
                    ],
                    'SupportedTransformInstanceTypes': [
                        'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge',
                    ],
                    'SupportedRealtimeInferenceInstanceTypes': [
                        'ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.large'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.large'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
                    ],
                    'SupportedContentTypes': [
                        'string',
                    ],
                    'SupportedResponseMIMETypes': [
                        'string',
                    ]
                },
                'SourceAlgorithmSpecification': {
                    'SourceAlgorithms': [
                        {
                            'ModelDataUrl': 'string',
                            'AlgorithmName': 'string'
                        },
                    ]
                },
                'ValidationSpecification': {
                    'ValidationRole': 'string',
                    'ValidationProfiles': [
                        {
                            'ProfileName': 'string',
                            'TransformJobDefinition': {
                                'MaxConcurrentTransforms': 123,
                                'MaxPayloadInMB': 123,
                                'BatchStrategy': 'MultiRecord'|'SingleRecord',
                                'Environment': {
                                    'string': 'string'
                                },
                                'TransformInput': {
                                    'DataSource': {
                                        'S3DataSource': {
                                            'S3DataType': 'ManifestFile'|'S3Prefix'|'AugmentedManifestFile',
                                            'S3Uri': 'string'
                                        }
                                    },
                                    'ContentType': 'string',
                                    'CompressionType': 'None'|'Gzip',
                                    'SplitType': 'None'|'Line'|'RecordIO'|'TFRecord'
                                },
                                'TransformOutput': {
                                    'S3OutputPath': 'string',
                                    'Accept': 'string',
                                    'AssembleWith': 'None'|'Line',
                                    'KmsKeyId': 'string'
                                },
                                'TransformResources': {
                                    'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge',
                                    'InstanceCount': 123,
                                    'VolumeKmsKeyId': 'string'
                                }
                            }
                        },
                    ]
                },
                'ModelPackageStatus': 'Pending'|'InProgress'|'Completed'|'Failed'|'Deleting',
                'ModelPackageStatusDetails': {
                    'ValidationStatuses': [
                        {
                            'Name': 'string',
                            'Status': 'NotStarted'|'InProgress'|'Completed'|'Failed',
                            'FailureReason': 'string'
                        },
                    ],
                    'ImageScanStatuses': [
                        {
                            'Name': 'string',
                            'Status': 'NotStarted'|'InProgress'|'Completed'|'Failed',
                            'FailureReason': 'string'
                        },
                    ]
                },
                'CertifyForMarketplace': True|False
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ModelPackageName** *(string) --* 
              The name of the model package being described.
            - **ModelPackageArn** *(string) --* 
              The Amazon Resource Name (ARN) of the model package.
            - **ModelPackageDescription** *(string) --* 
              A brief summary of the model package.
            - **CreationTime** *(datetime) --* 
              A timestamp specifying when the model package was created.
            - **InferenceSpecification** *(dict) --* 
              Details about inference jobs that can be run with models based on this model package.
              - **Containers** *(list) --* 
                The Amazon ECR registry path of the Docker image that contains the inference code.
                - *(dict) --* 
                  Describes the Docker container for the model package.
                  - **ContainerHostname** *(string) --* 
                    The DNS host name for the Docker container.
                  - **Image** *(string) --* 
                    The Amazon EC2 Container Registry (Amazon ECR) path where inference code is stored.
                    If you are using your own custom algorithm instead of an algorithm provided by Amazon SageMaker, the inference code must meet Amazon SageMaker requirements. Amazon SageMaker supports both ``registry/repository[:tag]`` and ``registry/repository[@digest]`` image path formats. For more information, see `Using Your Own Algorithms with Amazon SageMaker <https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__ .
                  - **ImageDigest** *(string) --* 
                    An MD5 hash of the training algorithm that identifies the Docker image used for training.
                  - **ModelDataUrl** *(string) --* 
                    The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single ``gzip`` compressed tar archive (``.tar.gz`` suffix).
                  - **ProductId** *(string) --* 
                    The AWS Marketplace product ID of the model package.
              - **SupportedTransformInstanceTypes** *(list) --* 
                A list of the instance types on which a transformation job can be run or on which an endpoint can be deployed.
                - *(string) --* 
              - **SupportedRealtimeInferenceInstanceTypes** *(list) --* 
                A list of the instance types that are used to generate inferences in real-time.
                - *(string) --* 
              - **SupportedContentTypes** *(list) --* 
                The supported MIME types for the input data.
                - *(string) --* 
              - **SupportedResponseMIMETypes** *(list) --* 
                The supported MIME types for the output data.
                - *(string) --* 
            - **SourceAlgorithmSpecification** *(dict) --* 
              Details about the algorithm that was used to create the model package.
              - **SourceAlgorithms** *(list) --* 
                A list of the algorithms that were used to create a model package.
                - *(dict) --* 
                  Specifies an algorithm that was used to create the model package. The algorithm must be either an algorithm resource in your Amazon SageMaker account or an algorithm in AWS Marketplace that you are subscribed to.
                  - **ModelDataUrl** *(string) --* 
                    The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single ``gzip`` compressed tar archive (``.tar.gz`` suffix).
                  - **AlgorithmName** *(string) --* 
                    The name of an algorithm that was used to create the model package. The algorithm must be either an algorithm resource in your Amazon SageMaker account or an algorithm in AWS Marketplace that you are subscribed to.
            - **ValidationSpecification** *(dict) --* 
              Configurations for one or more transform jobs that Amazon SageMaker runs to test the model package.
              - **ValidationRole** *(string) --* 
                The IAM roles to be used for the validation of the model package.
              - **ValidationProfiles** *(list) --* 
                An array of ``ModelPackageValidationProfile`` objects, each of which specifies a batch transform job that Amazon SageMaker runs to validate your model package.
                - *(dict) --* 
                  Contains data, such as the inputs and targeted instance types that are used in the process of validating the model package.
                  The data provided in the validation profile is made available to your buyers on AWS Marketplace.
                  - **ProfileName** *(string) --* 
                    The name of the profile for the model package.
                  - **TransformJobDefinition** *(dict) --* 
                    The ``TransformJobDefinition`` object that describes the transform job used for the validation of the model package.
                    - **MaxConcurrentTransforms** *(integer) --* 
                      The maximum number of parallel requests that can be sent to each instance in a transform job. The default value is 1.
                    - **MaxPayloadInMB** *(integer) --* 
                      The maximum payload size allowed, in MB. A payload is the data portion of a record (without metadata).
                    - **BatchStrategy** *(string) --* 
                      A string that determines the number of records included in a single mini-batch.
                       ``SingleRecord`` means only one record is used per mini-batch. ``MultiRecord`` means a mini-batch is set to contain as many records that can fit within the ``MaxPayloadInMB`` limit.
                    - **Environment** *(dict) --* 
                      The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.
                      - *(string) --* 
                        - *(string) --* 
                    - **TransformInput** *(dict) --* 
                      A description of the input source and the way the transform job consumes it.
                      - **DataSource** *(dict) --* 
                        Describes the location of the channel data, which is, the S3 location of the input data that the model can consume.
                        - **S3DataSource** *(dict) --* 
                          The S3 location of the data source that is associated with a channel.
                          - **S3DataType** *(string) --* 
                            If you choose ``S3Prefix`` , ``S3Uri`` identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for batch transform. 
                            If you choose ``ManifestFile`` , ``S3Uri`` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for batch transform. 
                          - **S3Uri** *(string) --* 
                            Depending on the value specified for the ``S3DataType`` , identifies either a key name prefix or a manifest. For example:
                            * A key name prefix might look like this: ``s3://bucketname/exampleprefix`` .  
                            * A manifest might look like this: ``s3://bucketname/example.manifest``   The manifest is an S3 object which is a JSON file with the following format:   ``[``    ``{"prefix": "s3://customer_bucket/some/prefix/"},``    ``"relative/path/to/custdata-1",``    ``"relative/path/custdata-2",``    ``...``    ``]``   The preceding JSON matches the following ``S3Uris`` :   ``s3://customer_bucket/some/prefix/relative/path/to/custdata-1``    ``s3://customer_bucket/some/prefix/relative/path/custdata-1``    ``...``   The complete set of ``S3Uris`` in this manifest constitutes the input data for the channel for this datasource. The object that each ``S3Uris`` points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf. 
                      - **ContentType** *(string) --* 
                        The multipurpose internet mail extension (MIME) type of the data. Amazon SageMaker uses the MIME type with each http call to transfer data to the transform job.
                      - **CompressionType** *(string) --* 
                        If your transform data is compressed, specify the compression type. Amazon SageMaker automatically decompresses the data for the transform job accordingly. The default value is ``None`` .
                      - **SplitType** *(string) --* 
                        The method to use to split the transform job's data files into smaller batches. Splitting is necessary when the total size of each object is too large to fit in a single request. You can also use data splitting to improve performance by processing multiple concurrent mini-batches. The default value for ``SplitType`` is ``None`` , which indicates that input data files are not split, and request payloads contain the entire contents of an input object. Set the value of this parameter to ``Line`` to split records on a newline character boundary. ``SplitType`` also supports a number of record-oriented binary data formats.
                        When splitting is enabled, the size of a mini-batch depends on the values of the ``BatchStrategy`` and ``MaxPayloadInMB`` parameters. When the value of ``BatchStrategy`` is ``MultiRecord`` , Amazon SageMaker sends the maximum number of records in each request, up to the ``MaxPayloadInMB`` limit. If the value of ``BatchStrategy`` is ``SingleRecord`` , Amazon SageMaker sends individual records in each request.
                        .. note::
                          Some data formats represent a record as a binary payload wrapped with extra padding bytes. When splitting is applied to a binary data format, padding is removed if the value of ``BatchStrategy`` is set to ``SingleRecord`` . Padding is not removed if the value of ``BatchStrategy`` is set to ``MultiRecord`` .
                          For more information about the RecordIO, see `Data Format <http://mxnet.io/architecture/note_data_loading.html#data-format>`__ in the MXNet documentation. For more information about the TFRecord, see `Consuming TFRecord data <https://www.tensorflow.org/guide/datasets#consuming_tfrecord_data>`__ in the TensorFlow documentation.
                    - **TransformOutput** *(dict) --* 
                      Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job.
                      - **S3OutputPath** *(string) --* 
                        The Amazon S3 path where you want Amazon SageMaker to store the results of the transform job. For example, ``s3://bucket-name/key-name-prefix`` .
                        For every S3 object used as input for the transform job, batch transform stores the transformed data with an .``out`` suffix in a corresponding subfolder in the location in the output prefix. For example, for the input data stored at ``s3://bucket-name/input-name-prefix/dataset01/data.csv`` , batch transform stores the transformed data at ``s3://bucket-name/output-name-prefix/input-name-prefix/data.csv.out`` . Batch transform doesn't upload partially processed objects. For an input S3 object that contains multiple records, it creates an .``out`` file only if the transform job succeeds on the entire file. When the input contains multiple S3 objects, the batch transform job processes the listed S3 objects and uploads only the output for successfully processed objects. If any object fails in the transform job batch transform marks the job as failed to prompt investigation.
                      - **Accept** *(string) --* 
                        The MIME type used to specify the output data. Amazon SageMaker uses the MIME type with each http call to transfer data from the transform job.
                      - **AssembleWith** *(string) --* 
                        Defines how to assemble the results of the transform job as a single S3 object. Choose a format that is most convenient to you. To concatenate the results in binary format, specify ``None`` . To add a newline character at the end of every transformed record, specify ``Line`` .
                      - **KmsKeyId** *(string) --* 
                        The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The ``KmsKeyId`` can be any of the following formats: 
                        * // KMS Key ID  ``"1234abcd-12ab-34cd-56ef-1234567890ab"``   
                        * // Amazon Resource Name (ARN) of a KMS Key  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``   
                        * // KMS Key Alias  ``"alias/ExampleAlias"``   
                        * // Amazon Resource Name (ARN) of a KMS Key Alias  ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``   
                        If you don't provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role's account. For more information, see `KMS-Managed Encryption Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ in the *Amazon Simple Storage Service Developer Guide.*  
                        The KMS key policy must grant permission to the IAM role that you specify in your ``CreateTramsformJob`` request. For more information, see `Using Key Policies in AWS KMS <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the *AWS Key Management Service Developer Guide* .
                    - **TransformResources** *(dict) --* 
                      Identifies the ML compute instances for the transform job.
                      - **InstanceType** *(string) --* 
                        The ML compute instance type for the transform job. For using built-in algorithms to transform moderately sized datasets, ml.m4.xlarge or ``ml.m5.large`` should suffice. There is no default value for ``InstanceType`` .
                      - **InstanceCount** *(integer) --* 
                        The number of ML compute instances to use in the transform job. For distributed transform, provide a value greater than 1. The default value is ``1`` .
                      - **VolumeKmsKeyId** *(string) --* 
                        The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the batch transform job. The ``VolumeKmsKeyId`` can be any of the following formats:
                        * // KMS Key ID  ``"1234abcd-12ab-34cd-56ef-1234567890ab"``   
                        * // Amazon Resource Name (ARN) of a KMS Key  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``   
            - **ModelPackageStatus** *(string) --* 
              The current status of the model package.
            - **ModelPackageStatusDetails** *(dict) --* 
              Details about the current status of the model package.
              - **ValidationStatuses** *(list) --* 
                The validation status of the model package.
                - *(dict) --* 
                  Represents the overall status of a model package.
                  - **Name** *(string) --* 
                    The name of the model package for which the overall status is being reported.
                  - **Status** *(string) --* 
                    The current status.
                  - **FailureReason** *(string) --* 
                    if the overall status is ``Failed`` , the reason for the failure.
              - **ImageScanStatuses** *(list) --* 
                The status of the scan of the Docker image container for the model package.
                - *(dict) --* 
                  Represents the overall status of a model package.
                  - **Name** *(string) --* 
                    The name of the model package for which the overall status is being reported.
                  - **Status** *(string) --* 
                    The current status.
                  - **FailureReason** *(string) --* 
                    if the overall status is ``Failed`` , the reason for the failure.
            - **CertifyForMarketplace** *(boolean) --* 
              Whether the model package is certified for listing on AWS Marketplace.
        :type ModelPackageName: string
        :param ModelPackageName: **[REQUIRED]**
          The name of the model package to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_notebook_instance(self, NotebookInstanceName: str) -> Dict:
        """
        Returns information about a notebook instance.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeNotebookInstance>`_
        
        **Request Syntax**
        ::
          response = client.describe_notebook_instance(
              NotebookInstanceName='string'
          )
        
        **Response Syntax**
        ::
            {
                'NotebookInstanceArn': 'string',
                'NotebookInstanceName': 'string',
                'NotebookInstanceStatus': 'Pending'|'InService'|'Stopping'|'Stopped'|'Failed'|'Deleting'|'Updating',
                'FailureReason': 'string',
                'Url': 'string',
                'InstanceType': 'ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.t3.medium'|'ml.t3.large'|'ml.t3.xlarge'|'ml.t3.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.c5d.xlarge'|'ml.c5d.2xlarge'|'ml.c5d.4xlarge'|'ml.c5d.9xlarge'|'ml.c5d.18xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge',
                'SubnetId': 'string',
                'SecurityGroups': [
                    'string',
                ],
                'RoleArn': 'string',
                'KmsKeyId': 'string',
                'NetworkInterfaceId': 'string',
                'LastModifiedTime': datetime(2015, 1, 1),
                'CreationTime': datetime(2015, 1, 1),
                'NotebookInstanceLifecycleConfigName': 'string',
                'DirectInternetAccess': 'Enabled'|'Disabled',
                'VolumeSizeInGB': 123,
                'AcceleratorTypes': [
                    'ml.eia1.medium'|'ml.eia1.large'|'ml.eia1.xlarge',
                ],
                'DefaultCodeRepository': 'string',
                'AdditionalCodeRepositories': [
                    'string',
                ],
                'RootAccess': 'Enabled'|'Disabled'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **NotebookInstanceArn** *(string) --* 
              The Amazon Resource Name (ARN) of the notebook instance.
            - **NotebookInstanceName** *(string) --* 
              The name of the Amazon SageMaker notebook instance. 
            - **NotebookInstanceStatus** *(string) --* 
              The status of the notebook instance.
            - **FailureReason** *(string) --* 
              If status is ``Failed`` , the reason it failed.
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
              The Amazon Resource Name (ARN) of the IAM role associated with the instance. 
            - **KmsKeyId** *(string) --* 
              The AWS KMS key ID Amazon SageMaker uses to encrypt data when storing it on the ML storage volume attached to the instance. 
            - **NetworkInterfaceId** *(string) --* 
              The network interface IDs that Amazon SageMaker created at the time of creating the instance. 
            - **LastModifiedTime** *(datetime) --* 
              A timestamp. Use this parameter to retrieve the time when the notebook instance was last modified. 
            - **CreationTime** *(datetime) --* 
              A timestamp. Use this parameter to return the time when the notebook instance was created
            - **NotebookInstanceLifecycleConfigName** *(string) --* 
              Returns the name of a notebook instance lifecycle configuration.
              For information about notebook instance lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__  
            - **DirectInternetAccess** *(string) --* 
              Describes whether Amazon SageMaker provides internet access to the notebook instance. If this value is set to *Disabled* , the notebook instance does not have internet access, and cannot connect to Amazon SageMaker training and endpoint services.
              For more information, see `Notebook Instances Are Internet-Enabled by Default <https://docs.aws.amazon.com/sagemaker/latest/dg/appendix-additional-considerations.html#appendix-notebook-and-internet-access>`__ .
            - **VolumeSizeInGB** *(integer) --* 
              The size, in GB, of the ML storage volume attached to the notebook instance.
            - **AcceleratorTypes** *(list) --* 
              A list of the Elastic Inference (EI) instance types associated with this notebook instance. Currently only one EI instance type can be associated with a notebook instance. For more information, see `Using Elastic Inference in Amazon SageMaker <http://docs.aws.amazon.com/sagemaker/latest/dg/ei.html>`__ .
              - *(string) --* 
            - **DefaultCodeRepository** *(string) --* 
              The Git repository associated with the notebook instance as its default code repository. This can be either the name of a Git repository stored as a resource in your account, or the URL of a Git repository in `AWS CodeCommit <http://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html>`__ or in any other Git repository. When you open a notebook instance, it opens in the directory that contains this repository. For more information, see `Associating Git Repositories with Amazon SageMaker Notebook Instances <http://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html>`__ .
            - **AdditionalCodeRepositories** *(list) --* 
              An array of up to three Git repositories associated with the notebook instance. These can be either the names of Git repositories stored as resources in your account, or the URL of Git repositories in `AWS CodeCommit <http://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html>`__ or in any other Git repository. These repositories are cloned at the same level as the default repository of your notebook instance. For more information, see `Associating Git Repositories with Amazon SageMaker Notebook Instances <http://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html>`__ .
              - *(string) --* 
            - **RootAccess** *(string) --* 
              Whether root access is enabled or disabled for users of the notebook instance.
              .. note::
                Lifecycle configurations need root access to be able to set up a notebook instance. Because of this, lifecycle configurations associated with a notebook instance always run with root access even if you disable root access for users.
        :type NotebookInstanceName: string
        :param NotebookInstanceName: **[REQUIRED]**
          The name of the notebook instance that you want information about.
        :rtype: dict
        :returns:
        """
        pass

    def describe_notebook_instance_lifecycle_config(self, NotebookInstanceLifecycleConfigName: str) -> Dict:
        """
        Returns a description of a notebook instance lifecycle configuration.
        For information about notebook instance lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeNotebookInstanceLifecycleConfig>`_
        
        **Request Syntax**
        ::
          response = client.describe_notebook_instance_lifecycle_config(
              NotebookInstanceLifecycleConfigName='string'
          )
        
        **Response Syntax**
        ::
            {
                'NotebookInstanceLifecycleConfigArn': 'string',
                'NotebookInstanceLifecycleConfigName': 'string',
                'OnCreate': [
                    {
                        'Content': 'string'
                    },
                ],
                'OnStart': [
                    {
                        'Content': 'string'
                    },
                ],
                'LastModifiedTime': datetime(2015, 1, 1),
                'CreationTime': datetime(2015, 1, 1)
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
                For information about notebook instance lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
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
                For information about notebook instance lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
                - **Content** *(string) --* 
                  A base64-encoded string that contains a shell script for a notebook instance lifecycle configuration.
            - **LastModifiedTime** *(datetime) --* 
              A timestamp that tells when the lifecycle configuration was last modified.
            - **CreationTime** *(datetime) --* 
              A timestamp that tells when the lifecycle configuration was created.
        :type NotebookInstanceLifecycleConfigName: string
        :param NotebookInstanceLifecycleConfigName: **[REQUIRED]**
          The name of the lifecycle configuration to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_subscribed_workteam(self, WorkteamArn: str) -> Dict:
        """
        Gets information about a work team provided by a vendor. It returns details about the subscription with a vendor in the AWS Marketplace.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeSubscribedWorkteam>`_
        
        **Request Syntax**
        ::
          response = client.describe_subscribed_workteam(
              WorkteamArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'SubscribedWorkteam': {
                    'WorkteamArn': 'string',
                    'MarketplaceTitle': 'string',
                    'SellerName': 'string',
                    'MarketplaceDescription': 'string',
                    'ListingId': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **SubscribedWorkteam** *(dict) --* 
              A ``Workteam`` instance that contains information about the work team.
              - **WorkteamArn** *(string) --* 
                The Amazon Resource Name (ARN) of the vendor that you have subscribed.
              - **MarketplaceTitle** *(string) --* 
                The title of the service provided by the vendor in the Amazon Marketplace.
              - **SellerName** *(string) --* 
                The name of the vendor in the Amazon Marketplace.
              - **MarketplaceDescription** *(string) --* 
                The description of the vendor from the Amazon Marketplace.
              - **ListingId** *(string) --* 
        :type WorkteamArn: string
        :param WorkteamArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the subscribed work team to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_training_job(self, TrainingJobName: str) -> Dict:
        """
        Returns information about a training job.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeTrainingJob>`_
        
        **Request Syntax**
        ::
          response = client.describe_training_job(
              TrainingJobName='string'
          )
        
        **Response Syntax**
        ::
            {
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
                'EnableInterContainerTrafficEncryption': True|False
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TrainingJobName** *(string) --* 
              Name of the model training job. 
            - **TrainingJobArn** *(string) --* 
              The Amazon Resource Name (ARN) of the training job.
            - **TuningJobArn** *(string) --* 
              The Amazon Resource Name (ARN) of the associated hyperparameter tuning job if the training job was launched by a hyperparameter tuning job.
            - **LabelingJobArn** *(string) --* 
              The Amazon Resource Name (ARN) of the Amazon SageMaker Ground Truth labeling job that created the transform or training job.
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
                The registry path of the Docker image that contains the training algorithm. For information about docker registry paths for built-in algorithms, see `Algorithms Provided by Amazon SageMaker\: Common Parameters <https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html>`__ . Amazon SageMaker supports both ``registry/repository[:tag]`` and ``registry/repository[@digest]`` image path formats. For more information, see `Using Your Own Algorithms with Amazon SageMaker <https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__ .
              - **AlgorithmName** *(string) --* 
                The name of the algorithm resource to use for the training job. This must be an algorithm resource that you created or subscribe to on AWS Marketplace. If you specify a value for this parameter, you can't specify a value for ``TrainingImage`` .
              - **TrainingInputMode** *(string) --* 
                The input mode that the algorithm supports. For the input modes that Amazon SageMaker algorithms support, see `Algorithms <https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ . If an algorithm supports the ``File`` input mode, Amazon SageMaker downloads the training data from S3 to the provisioned ML storage Volume, and mounts the directory to docker volume for training container. If an algorithm supports the ``Pipe`` input mode, Amazon SageMaker streams data directly from S3 to the container. 
                In File mode, make sure you provision ML storage volume with sufficient capacity to accommodate the data download from S3. In addition to the training data, the ML storage volume also stores the output model. The algorithm container use ML storage volume to also store intermediate information, if any. 
                For distributed algorithms using File mode, training data is distributed uniformly, and your training duration is predictable if the input data objects size is approximately same. Amazon SageMaker does not split the files any further for model training. If the object sizes are skewed, training won't be optimal as the data distribution is also skewed where one host in a training cluster is overloaded, thus becoming bottleneck in training. 
              - **MetricDefinitions** *(list) --* 
                A list of metric definition objects. Each object specifies the metric name and regular expressions used to parse algorithm logs. Amazon SageMaker publishes each metric to Amazon CloudWatch.
                - *(dict) --* 
                  Specifies a metric that the training algorithm writes to ``stderr`` or ``stdout`` . Amazon SageMakerhyperparameter tuning captures all defined metrics. You specify one metric that a hyperparameter tuning job uses as its objective metric to choose the best training job.
                  - **Name** *(string) --* 
                    The name of the metric.
                  - **Regex** *(string) --* 
                    A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see `Defining Objective Metrics <https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics.html>`__ .
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
              A  VpcConfig object that specifies the VPC that this training job has access to. For more information, see `Protect Training Jobs by Using an Amazon Virtual Private Cloud <https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html>`__ .
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
              A collection of ``MetricData`` objects that specify the names, values, and dates and times that the training algorithm emitted to Amazon CloudWatch.
              - *(dict) --* 
                The name, value, and date and time of a metric that was emitted to Amazon CloudWatch.
                - **MetricName** *(string) --* 
                  The name of the metric.
                - **Value** *(float) --* 
                  The value of the metric.
                - **Timestamp** *(datetime) --* 
                  The date and time that the algorithm emitted the metric.
            - **EnableNetworkIsolation** *(boolean) --* 
              If you want to allow inbound or outbound network calls, except for calls between peers within a training cluster for distributed training, choose ``True`` . If you enable network isolation for training jobs that are configured to use a VPC, Amazon SageMaker downloads and uploads customer data and model artifacts through the specified VPC, but the training container does not have network access.
              .. note::
                The Semantic Segmentation built-in algorithm does not support network isolation.
            - **EnableInterContainerTrafficEncryption** *(boolean) --* 
              To encrypt all communications between ML compute instances in distributed training, choose ``True`` . Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithm in distributed training.
        :type TrainingJobName: string
        :param TrainingJobName: **[REQUIRED]**
          The name of the training job.
        :rtype: dict
        :returns:
        """
        pass

    def describe_transform_job(self, TransformJobName: str) -> Dict:
        """
        Returns information about a transform job.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeTransformJob>`_
        
        **Request Syntax**
        ::
          response = client.describe_transform_job(
              TransformJobName='string'
          )
        
        **Response Syntax**
        ::
            {
                'TransformJobName': 'string',
                'TransformJobArn': 'string',
                'TransformJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
                'FailureReason': 'string',
                'ModelName': 'string',
                'MaxConcurrentTransforms': 123,
                'MaxPayloadInMB': 123,
                'BatchStrategy': 'MultiRecord'|'SingleRecord',
                'Environment': {
                    'string': 'string'
                },
                'TransformInput': {
                    'DataSource': {
                        'S3DataSource': {
                            'S3DataType': 'ManifestFile'|'S3Prefix'|'AugmentedManifestFile',
                            'S3Uri': 'string'
                        }
                    },
                    'ContentType': 'string',
                    'CompressionType': 'None'|'Gzip',
                    'SplitType': 'None'|'Line'|'RecordIO'|'TFRecord'
                },
                'TransformOutput': {
                    'S3OutputPath': 'string',
                    'Accept': 'string',
                    'AssembleWith': 'None'|'Line',
                    'KmsKeyId': 'string'
                },
                'TransformResources': {
                    'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge',
                    'InstanceCount': 123,
                    'VolumeKmsKeyId': 'string'
                },
                'CreationTime': datetime(2015, 1, 1),
                'TransformStartTime': datetime(2015, 1, 1),
                'TransformEndTime': datetime(2015, 1, 1),
                'LabelingJobArn': 'string'
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
              If the transform job failed, ``FailureReason`` describes why it failed. A transform job creates a log file, which includes error messages, and stores it as an Amazon S3 object. For more information, see `Log Amazon SageMaker Events with Amazon CloudWatch <http://docs.aws.amazon.com/sagemaker/latest/dg/logging-cloudwatch.html>`__ .
            - **ModelName** *(string) --* 
              The name of the model used in the transform job.
            - **MaxConcurrentTransforms** *(integer) --* 
              The maximum number of parallel requests on each instance node that can be launched in a transform job. The default value is 1.
            - **MaxPayloadInMB** *(integer) --* 
              The maximum payload size, in MB, used in the transform job.
            - **BatchStrategy** *(string) --* 
              Specifies the number of records to include in a mini-batch for an HTTP inference request. A *record*  is a single unit of input data that inference can be made on. For example, a single line in a CSV file is a record. 
              To enable the batch strategy, you must set ``SplitType`` to ``Line`` , ``RecordIO`` , or ``TFRecord`` .
            - **Environment** *(dict) --* 
              The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.
              - *(string) --* 
                - *(string) --* 
            - **TransformInput** *(dict) --* 
              Describes the dataset to be transformed and the Amazon S3 location where it is stored.
              - **DataSource** *(dict) --* 
                Describes the location of the channel data, which is, the S3 location of the input data that the model can consume.
                - **S3DataSource** *(dict) --* 
                  The S3 location of the data source that is associated with a channel.
                  - **S3DataType** *(string) --* 
                    If you choose ``S3Prefix`` , ``S3Uri`` identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for batch transform. 
                    If you choose ``ManifestFile`` , ``S3Uri`` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for batch transform. 
                  - **S3Uri** *(string) --* 
                    Depending on the value specified for the ``S3DataType`` , identifies either a key name prefix or a manifest. For example:
                    * A key name prefix might look like this: ``s3://bucketname/exampleprefix`` .  
                    * A manifest might look like this: ``s3://bucketname/example.manifest``   The manifest is an S3 object which is a JSON file with the following format:   ``[``    ``{"prefix": "s3://customer_bucket/some/prefix/"},``    ``"relative/path/to/custdata-1",``    ``"relative/path/custdata-2",``    ``...``    ``]``   The preceding JSON matches the following ``S3Uris`` :   ``s3://customer_bucket/some/prefix/relative/path/to/custdata-1``    ``s3://customer_bucket/some/prefix/relative/path/custdata-1``    ``...``   The complete set of ``S3Uris`` in this manifest constitutes the input data for the channel for this datasource. The object that each ``S3Uris`` points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf. 
              - **ContentType** *(string) --* 
                The multipurpose internet mail extension (MIME) type of the data. Amazon SageMaker uses the MIME type with each http call to transfer data to the transform job.
              - **CompressionType** *(string) --* 
                If your transform data is compressed, specify the compression type. Amazon SageMaker automatically decompresses the data for the transform job accordingly. The default value is ``None`` .
              - **SplitType** *(string) --* 
                The method to use to split the transform job's data files into smaller batches. Splitting is necessary when the total size of each object is too large to fit in a single request. You can also use data splitting to improve performance by processing multiple concurrent mini-batches. The default value for ``SplitType`` is ``None`` , which indicates that input data files are not split, and request payloads contain the entire contents of an input object. Set the value of this parameter to ``Line`` to split records on a newline character boundary. ``SplitType`` also supports a number of record-oriented binary data formats.
                When splitting is enabled, the size of a mini-batch depends on the values of the ``BatchStrategy`` and ``MaxPayloadInMB`` parameters. When the value of ``BatchStrategy`` is ``MultiRecord`` , Amazon SageMaker sends the maximum number of records in each request, up to the ``MaxPayloadInMB`` limit. If the value of ``BatchStrategy`` is ``SingleRecord`` , Amazon SageMaker sends individual records in each request.
                .. note::
                  Some data formats represent a record as a binary payload wrapped with extra padding bytes. When splitting is applied to a binary data format, padding is removed if the value of ``BatchStrategy`` is set to ``SingleRecord`` . Padding is not removed if the value of ``BatchStrategy`` is set to ``MultiRecord`` .
                  For more information about the RecordIO, see `Data Format <http://mxnet.io/architecture/note_data_loading.html#data-format>`__ in the MXNet documentation. For more information about the TFRecord, see `Consuming TFRecord data <https://www.tensorflow.org/guide/datasets#consuming_tfrecord_data>`__ in the TensorFlow documentation.
            - **TransformOutput** *(dict) --* 
              Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job.
              - **S3OutputPath** *(string) --* 
                The Amazon S3 path where you want Amazon SageMaker to store the results of the transform job. For example, ``s3://bucket-name/key-name-prefix`` .
                For every S3 object used as input for the transform job, batch transform stores the transformed data with an .``out`` suffix in a corresponding subfolder in the location in the output prefix. For example, for the input data stored at ``s3://bucket-name/input-name-prefix/dataset01/data.csv`` , batch transform stores the transformed data at ``s3://bucket-name/output-name-prefix/input-name-prefix/data.csv.out`` . Batch transform doesn't upload partially processed objects. For an input S3 object that contains multiple records, it creates an .``out`` file only if the transform job succeeds on the entire file. When the input contains multiple S3 objects, the batch transform job processes the listed S3 objects and uploads only the output for successfully processed objects. If any object fails in the transform job batch transform marks the job as failed to prompt investigation.
              - **Accept** *(string) --* 
                The MIME type used to specify the output data. Amazon SageMaker uses the MIME type with each http call to transfer data from the transform job.
              - **AssembleWith** *(string) --* 
                Defines how to assemble the results of the transform job as a single S3 object. Choose a format that is most convenient to you. To concatenate the results in binary format, specify ``None`` . To add a newline character at the end of every transformed record, specify ``Line`` .
              - **KmsKeyId** *(string) --* 
                The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The ``KmsKeyId`` can be any of the following formats: 
                * // KMS Key ID  ``"1234abcd-12ab-34cd-56ef-1234567890ab"``   
                * // Amazon Resource Name (ARN) of a KMS Key  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``   
                * // KMS Key Alias  ``"alias/ExampleAlias"``   
                * // Amazon Resource Name (ARN) of a KMS Key Alias  ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``   
                If you don't provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role's account. For more information, see `KMS-Managed Encryption Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ in the *Amazon Simple Storage Service Developer Guide.*  
                The KMS key policy must grant permission to the IAM role that you specify in your ``CreateTramsformJob`` request. For more information, see `Using Key Policies in AWS KMS <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the *AWS Key Management Service Developer Guide* .
            - **TransformResources** *(dict) --* 
              Describes the resources, including ML instance types and ML instance count, to use for the transform job.
              - **InstanceType** *(string) --* 
                The ML compute instance type for the transform job. For using built-in algorithms to transform moderately sized datasets, ml.m4.xlarge or ``ml.m5.large`` should suffice. There is no default value for ``InstanceType`` .
              - **InstanceCount** *(integer) --* 
                The number of ML compute instances to use in the transform job. For distributed transform, provide a value greater than 1. The default value is ``1`` .
              - **VolumeKmsKeyId** *(string) --* 
                The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the batch transform job. The ``VolumeKmsKeyId`` can be any of the following formats:
                * // KMS Key ID  ``"1234abcd-12ab-34cd-56ef-1234567890ab"``   
                * // Amazon Resource Name (ARN) of a KMS Key  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``   
            - **CreationTime** *(datetime) --* 
              A timestamp that shows when the transform Job was created.
            - **TransformStartTime** *(datetime) --* 
              Indicates when the transform job starts on ML instances. You are billed for the time interval between this time and the value of ``TransformEndTime`` .
            - **TransformEndTime** *(datetime) --* 
              Indicates when the transform job has been completed, or has stopped or failed. You are billed for the time interval between this time and the value of ``TransformStartTime`` .
            - **LabelingJobArn** *(string) --* 
              The Amazon Resource Name (ARN) of the Amazon SageMaker Ground Truth labeling job that created the transform or training job.
        :type TransformJobName: string
        :param TransformJobName: **[REQUIRED]**
          The name of the transform job that you want to view details of.
        :rtype: dict
        :returns:
        """
        pass

    def describe_workteam(self, WorkteamName: str) -> Dict:
        """
        Gets information about a specific work team. You can see information such as the create date, the last updated date, membership information, and the work team's Amazon Resource Name (ARN).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeWorkteam>`_
        
        **Request Syntax**
        ::
          response = client.describe_workteam(
              WorkteamName='string'
          )
        
        **Response Syntax**
        ::
            {
                'Workteam': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Workteam** *(dict) --* 
              A ``Workteam`` instance that contains information about the work team. 
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
        :type WorkteamName: string
        :param WorkteamName: **[REQUIRED]**
          The name of the work team to return a description of.
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

    def get_search_suggestions(self, Resource: str, SuggestionQuery: Dict = None) -> Dict:
        """
        An auto-complete API for the search functionality in the Amazon SageMaker console. It returns suggestions of possible matches for the property name to use in ``Search`` queries. Provides suggestions for ``HyperParameters`` , ``Tags`` , and ``Metrics`` .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/GetSearchSuggestions>`_
        
        **Request Syntax**
        ::
          response = client.get_search_suggestions(
              Resource='TrainingJob',
              SuggestionQuery={
                  'PropertyNameQuery': {
                      'PropertyNameHint': 'string'
                  }
              }
          )
        
        **Response Syntax**
        ::
            {
                'PropertyNameSuggestions': [
                    {
                        'PropertyName': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PropertyNameSuggestions** *(list) --* 
              A list of property names for a ``Resource`` that match a ``SuggestionQuery`` .
              - *(dict) --* 
                A property name returned from a ``GetSearchSuggestions`` call that specifies a value in the ``PropertyNameQuery`` field.
                - **PropertyName** *(string) --* 
                  A suggested property name based on what you entered in the search textbox in the Amazon SageMaker console.
        :type Resource: string
        :param Resource: **[REQUIRED]**
          The name of the Amazon SageMaker resource to Search for. The only valid ``Resource`` value is ``TrainingJob`` .
        :type SuggestionQuery: dict
        :param SuggestionQuery:
          Limits the property names that are included in the response.
          - **PropertyNameQuery** *(dict) --*
            A type of ``SuggestionQuery`` . Defines a property name hint. Only property names that match the specified hint are included in the response.
            - **PropertyNameHint** *(string) --* **[REQUIRED]**
              Text that is part of a property\'s name. The property names of hyperparameter, metric, and tag key names that begin with the specified text in the ``PropertyNameHint`` .
        :rtype: dict
        :returns:
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

    def list_algorithms(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, MaxResults: int = None, NameContains: str = None, NextToken: str = None, SortBy: str = None, SortOrder: str = None) -> Dict:
        """
        Lists the machine learning algorithms that have been created.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListAlgorithms>`_
        
        **Request Syntax**
        ::
          response = client.list_algorithms(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              MaxResults=123,
              NameContains='string',
              NextToken='string',
              SortBy='Name'|'CreationTime',
              SortOrder='Ascending'|'Descending'
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of algorithms, use it in the subsequent request.
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:
          A filter that returns only algorithms created after the specified time (timestamp).
        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:
          A filter that returns only algorithms created before the specified time (timestamp).
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of algorithms to return in the response.
        :type NameContains: string
        :param NameContains:
          A string in the algorithm name. This filter returns only algorithms whose name contains the specified string.
        :type NextToken: string
        :param NextToken:
          If the response to a previous ``ListAlgorithms`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of algorithms, use the token in the next request.
        :type SortBy: string
        :param SortBy:
          The parameter by which to sort the results. The default is ``CreationTime`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for the results. The default is ``Ascending`` .
        :rtype: dict
        :returns:
        """
        pass

    def list_code_repositories(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, MaxResults: int = None, NameContains: str = None, NextToken: str = None, SortBy: str = None, SortOrder: str = None) -> Dict:
        """
        Gets a list of the Git repositories in your account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListCodeRepositories>`_
        
        **Request Syntax**
        ::
          response = client.list_code_repositories(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              MaxResults=123,
              NameContains='string',
              NextToken='string',
              SortBy='Name'|'CreationTime'|'LastModifiedTime',
              SortOrder='Ascending'|'Descending'
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              If the result of a ``ListCodeRepositoriesOutput`` request was truncated, the response includes a ``NextToken`` . To get the next set of Git repositories, use the token in the next request.
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
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of Git repositories to return in the response.
        :type NameContains: string
        :param NameContains:
          A string in the Git repositories name. This filter returns only repositories whose name contains the specified string.
        :type NextToken: string
        :param NextToken:
          If the result of a ``ListCodeRepositoriesOutput`` request was truncated, the response includes a ``NextToken`` . To get the next set of Git repositories, use the token in the next request.
        :type SortBy: string
        :param SortBy:
          The field to sort results by. The default is ``Name`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for results. The default is ``Ascending`` .
        :rtype: dict
        :returns:
        """
        pass

    def list_compilation_jobs(self, NextToken: str = None, MaxResults: int = None, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None) -> Dict:
        """
        Lists model compilation jobs that satisfy various filters.
        To create a model compilation job, use  CreateCompilationJob . To get information about a particular model compilation job you have created, use  DescribeCompilationJob .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListCompilationJobs>`_
        
        **Request Syntax**
        ::
          response = client.list_compilation_jobs(
              NextToken='string',
              MaxResults=123,
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              NameContains='string',
              StatusEquals='INPROGRESS'|'COMPLETED'|'FAILED'|'STARTING'|'STOPPING'|'STOPPED',
              SortBy='Name'|'CreationTime'|'Status',
              SortOrder='Ascending'|'Descending'
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
                        'CompilationTargetDevice': 'ml_m4'|'ml_m5'|'ml_c4'|'ml_c5'|'ml_p2'|'ml_p3'|'jetson_tx1'|'jetson_tx2'|'rasp3b'|'deeplens'|'rk3399'|'rk3288',
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'CompilationJobStatus': 'INPROGRESS'|'COMPLETED'|'FAILED'|'STARTING'|'STOPPING'|'STOPPED'
                    },
                ],
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              If the response is truncated, Amazon SageMaker returns this ``NextToken`` . To retrieve the next set of model compilation jobs, use this token in the next request.
        :type NextToken: string
        :param NextToken:
          If the result of the previous ``ListCompilationJobs`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of model compilation jobs, use the token in the next request.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of model compilation jobs to return in the response.
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
        :rtype: dict
        :returns:
        """
        pass

    def list_endpoint_configs(self, SortBy: str = None, SortOrder: str = None, NextToken: str = None, MaxResults: int = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None) -> Dict:
        """
        Lists endpoint configurations.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListEndpointConfigs>`_
        
        **Request Syntax**
        ::
          response = client.list_endpoint_configs(
              SortBy='Name'|'CreationTime',
              SortOrder='Ascending'|'Descending',
              NextToken='string',
              MaxResults=123,
              NameContains='string',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1)
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
                'NextToken': 'string'
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
        :type SortBy: string
        :param SortBy:
          The field to sort results by. The default is ``CreationTime`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for results. The default is ``Descending`` .
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
        """
        pass

    def list_endpoints(self, SortBy: str = None, SortOrder: str = None, NextToken: str = None, MaxResults: int = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, StatusEquals: str = None) -> Dict:
        """
        Lists endpoints.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListEndpoints>`_
        
        **Request Syntax**
        ::
          response = client.list_endpoints(
              SortBy='Name'|'CreationTime'|'Status',
              SortOrder='Ascending'|'Descending',
              NextToken='string',
              MaxResults=123,
              NameContains='string',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              StatusEquals='OutOfService'|'Creating'|'Updating'|'SystemUpdating'|'RollingBack'|'InService'|'Deleting'|'Failed'
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
                'NextToken': 'string'
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
                  * ``SystemUpdating`` : Endpoint is undergoing maintenance and cannot be updated or deleted or re-scaled until it has completed. This maintenance operation does not change any customer-specified values such as VPC config, KMS encryption, model, instance type, or instance count. 
                  * ``RollingBack`` : Endpoint fails to scale up or down or change its variant weight and is in the process of rolling back to its previous configuration. Once the rollback completes, endpoint returns to an ``InService`` status. This transitional status only applies to an endpoint that has autoscaling enabled and is undergoing variant weight or capacity changes as part of an  UpdateEndpointWeightsAndCapacities call or when the  UpdateEndpointWeightsAndCapacities operation is called explicitly. 
                  * ``InService`` : Endpoint is available to process incoming requests. 
                  * ``Deleting`` :  DeleteEndpoint is executing. 
                  * ``Failed`` : Endpoint could not be created, updated, or re-scaled. Use  DescribeEndpointOutput$FailureReason for information about the failure.  DeleteEndpoint is the only operation that can be performed on a failed endpoint. 
                  To get a list of endpoints with a specified status, use the  ListEndpointsInput$StatusEquals filter.
            - **NextToken** *(string) --* 
              If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of training jobs, use it in the subsequent request. 
        :type SortBy: string
        :param SortBy:
          Sorts the list of results. The default is ``CreationTime`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for results. The default is ``Descending`` .
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
        """
        pass

    def list_hyper_parameter_tuning_jobs(self, NextToken: str = None, MaxResults: int = None, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, StatusEquals: str = None) -> Dict:
        """
        Gets a list of  HyperParameterTuningJobSummary objects that describe the hyperparameter tuning jobs launched in your account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListHyperParameterTuningJobs>`_
        
        **Request Syntax**
        ::
          response = client.list_hyper_parameter_tuning_jobs(
              NextToken='string',
              MaxResults=123,
              SortBy='Name'|'Status'|'CreationTime',
              SortOrder='Ascending'|'Descending',
              NameContains='string',
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              StatusEquals='Completed'|'InProgress'|'Failed'|'Stopped'|'Stopping'
          )
        
        **Response Syntax**
        ::
            {
                'HyperParameterTuningJobSummaries': [
                    {
                        'HyperParameterTuningJobName': 'string',
                        'HyperParameterTuningJobArn': 'string',
                        'HyperParameterTuningJobStatus': 'Completed'|'InProgress'|'Failed'|'Stopped'|'Stopping',
                        'Strategy': 'Bayesian'|'Random',
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              If the result of this ``ListHyperParameterTuningJobs`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of tuning jobs, use the token in the next request.
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
        """
        pass

    def list_labeling_jobs(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, MaxResults: int = None, NextToken: str = None, NameContains: str = None, SortBy: str = None, SortOrder: str = None, StatusEquals: str = None) -> Dict:
        """
        Gets a list of labeling jobs.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListLabelingJobs>`_
        
        **Request Syntax**
        ::
          response = client.list_labeling_jobs(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              MaxResults=123,
              NextToken='string',
              NameContains='string',
              SortBy='Name'|'CreationTime'|'Status',
              SortOrder='Ascending'|'Descending',
              StatusEquals='InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped'
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of labeling jobs, use it in the subsequent request.
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
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of labeling jobs to return in each page of the response.
        :type NextToken: string
        :param NextToken:
          If the result of the previous ``ListLabelingJobs`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of labeling jobs, use the token in the next request.
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
        :rtype: dict
        :returns:
        """
        pass

    def list_labeling_jobs_for_workteam(self, WorkteamArn: str, MaxResults: int = None, NextToken: str = None, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, JobReferenceCodeContains: str = None, SortBy: str = None, SortOrder: str = None) -> Dict:
        """
        Gets a list of labeling jobs assigned to a specified work team.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListLabelingJobsForWorkteam>`_
        
        **Request Syntax**
        ::
          response = client.list_labeling_jobs_for_workteam(
              WorkteamArn='string',
              MaxResults=123,
              NextToken='string',
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              JobReferenceCodeContains='string',
              SortBy='CreationTime',
              SortOrder='Ascending'|'Descending'
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of labeling jobs, use it in the subsequent request.
        :type WorkteamArn: string
        :param WorkteamArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the work team for which you want to see labeling jobs for.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of labeling jobs to return in each page of the response.
        :type NextToken: string
        :param NextToken:
          If the result of the previous ``ListLabelingJobsForWorkteam`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of labeling jobs, use the token in the next request.
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
        :rtype: dict
        :returns:
        """
        pass

    def list_model_packages(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, MaxResults: int = None, NameContains: str = None, NextToken: str = None, SortBy: str = None, SortOrder: str = None) -> Dict:
        """
        Lists the model packages that have been created.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListModelPackages>`_
        
        **Request Syntax**
        ::
          response = client.list_model_packages(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              MaxResults=123,
              NameContains='string',
              NextToken='string',
              SortBy='Name'|'CreationTime',
              SortOrder='Ascending'|'Descending'
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of model packages, use it in the subsequent request.
        :type CreationTimeAfter: datetime
        :param CreationTimeAfter:
          A filter that returns only model packages created after the specified time (timestamp).
        :type CreationTimeBefore: datetime
        :param CreationTimeBefore:
          A filter that returns only model packages created before the specified time (timestamp).
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of model packages to return in the response.
        :type NameContains: string
        :param NameContains:
          A string in the model package name. This filter returns only model packages whose name contains the specified string.
        :type NextToken: string
        :param NextToken:
          If the response to a previous ``ListModelPackages`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of model packages, use the token in the next request.
        :type SortBy: string
        :param SortBy:
          The parameter by which to sort the results. The default is ``CreationTime`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for the results. The default is ``Ascending`` .
        :rtype: dict
        :returns:
        """
        pass

    def list_models(self, SortBy: str = None, SortOrder: str = None, NextToken: str = None, MaxResults: int = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None) -> Dict:
        """
        Lists models created with the `CreateModel <https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateModel.html>`__ API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListModels>`_
        
        **Request Syntax**
        ::
          response = client.list_models(
              SortBy='Name'|'CreationTime',
              SortOrder='Ascending'|'Descending',
              NextToken='string',
              MaxResults=123,
              NameContains='string',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1)
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
                'NextToken': 'string'
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
        :type SortBy: string
        :param SortBy:
          Sorts the list of results. The default is ``CreationTime`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for results. The default is ``Descending`` .
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
        """
        pass

    def list_notebook_instance_lifecycle_configs(self, NextToken: str = None, MaxResults: int = None, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None) -> Dict:
        """
        Lists notebook instance lifestyle configurations created with the  CreateNotebookInstanceLifecycleConfig API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListNotebookInstanceLifecycleConfigs>`_
        
        **Request Syntax**
        ::
          response = client.list_notebook_instance_lifecycle_configs(
              NextToken='string',
              MaxResults=123,
              SortBy='Name'|'CreationTime'|'LastModifiedTime',
              SortOrder='Ascending'|'Descending',
              NameContains='string',
              CreationTimeBefore=datetime(2015, 1, 1),
              CreationTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1)
          )
        
        **Response Syntax**
        ::
            {
                'NextToken': 'string',
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
        """
        pass

    def list_notebook_instances(self, NextToken: str = None, MaxResults: int = None, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, StatusEquals: str = None, NotebookInstanceLifecycleConfigNameContains: str = None, DefaultCodeRepositoryContains: str = None, AdditionalCodeRepositoryEquals: str = None) -> Dict:
        """
        Returns a list of the Amazon SageMaker notebook instances in the requester's account in an AWS Region. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListNotebookInstances>`_
        
        **Request Syntax**
        ::
          response = client.list_notebook_instances(
              NextToken='string',
              MaxResults=123,
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
              AdditionalCodeRepositoryEquals='string'
          )
        
        **Response Syntax**
        ::
            {
                'NextToken': 'string',
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
                  For information about notebook instance lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
                - **DefaultCodeRepository** *(string) --* 
                  The Git repository associated with the notebook instance as its default code repository. This can be either the name of a Git repository stored as a resource in your account, or the URL of a Git repository in `AWS CodeCommit <http://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html>`__ or in any other Git repository. When you open a notebook instance, it opens in the directory that contains this repository. For more information, see `Associating Git Repositories with Amazon SageMaker Notebook Instances <http://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html>`__ .
                - **AdditionalCodeRepositories** *(list) --* 
                  An array of up to three Git repositories associated with the notebook instance. These can be either the names of Git repositories stored as resources in your account, or the URL of Git repositories in `AWS CodeCommit <http://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html>`__ or in any other Git repository. These repositories are cloned at the same level as the default repository of your notebook instance. For more information, see `Associating Git Repositories with Amazon SageMaker Notebook Instances <http://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html>`__ .
                  - *(string) --* 
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
        :type DefaultCodeRepositoryContains: string
        :param DefaultCodeRepositoryContains:
          A string in the name or URL of a Git repository associated with this notebook instance. This filter returns only notebook instances associated with a git repository with a name that contains the specified string.
        :type AdditionalCodeRepositoryEquals: string
        :param AdditionalCodeRepositoryEquals:
          A filter that returns only notebook instances with associated with the specified git repository.
        :rtype: dict
        :returns:
        """
        pass

    def list_subscribed_workteams(self, NameContains: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Gets a list of the work teams that you are subscribed to in the AWS Marketplace. The list may be empty if no work team satisfies the filter specified in the ``NameContains`` parameter.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListSubscribedWorkteams>`_
        
        **Request Syntax**
        ::
          response = client.list_subscribed_workteams(
              NameContains='string',
              NextToken='string',
              MaxResults=123
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of work teams, use it in the subsequent request.
        :type NameContains: string
        :param NameContains:
          A string in the work team name. This filter returns only work teams whose name contains the specified string.
        :type NextToken: string
        :param NextToken:
          If the result of the previous ``ListSubscribedWorkteams`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of labeling jobs, use the token in the next request.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of work teams to return in each page of the response.
        :rtype: dict
        :returns:
        """
        pass

    def list_tags(self, ResourceArn: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Returns the tags for the specified Amazon SageMaker resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTags>`_
        
        **Request Syntax**
        ::
          response = client.list_tags(
              ResourceArn='string',
              NextToken='string',
              MaxResults=123
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
                'NextToken': 'string'
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
        """
        pass

    def list_training_jobs(self, NextToken: str = None, MaxResults: int = None, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None) -> Dict:
        """
        Lists training jobs.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTrainingJobs>`_
        
        **Request Syntax**
        ::
          response = client.list_training_jobs(
              NextToken='string',
              MaxResults=123,
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              NameContains='string',
              StatusEquals='InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
              SortBy='Name'|'CreationTime'|'Status',
              SortOrder='Ascending'|'Descending'
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
                'NextToken': 'string'
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
        """
        pass

    def list_training_jobs_for_hyper_parameter_tuning_job(self, HyperParameterTuningJobName: str, NextToken: str = None, MaxResults: int = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None) -> Dict:
        """
        Gets a list of  TrainingJobSummary objects that describe the training jobs that a hyperparameter tuning job launched.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTrainingJobsForHyperParameterTuningJob>`_
        
        **Request Syntax**
        ::
          response = client.list_training_jobs_for_hyper_parameter_tuning_job(
              HyperParameterTuningJobName='string',
              NextToken='string',
              MaxResults=123,
              StatusEquals='InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
              SortBy='Name'|'CreationTime'|'Status'|'FinalObjectiveMetricValue',
              SortOrder='Ascending'|'Descending'
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              If the result of this ``ListTrainingJobsForHyperParameterTuningJob`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of training jobs, use the token in the next request.
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
        """
        pass

    def list_transform_jobs(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Lists transform jobs.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTransformJobs>`_
        
        **Request Syntax**
        ::
          response = client.list_transform_jobs(
              CreationTimeAfter=datetime(2015, 1, 1),
              CreationTimeBefore=datetime(2015, 1, 1),
              LastModifiedTimeAfter=datetime(2015, 1, 1),
              LastModifiedTimeBefore=datetime(2015, 1, 1),
              NameContains='string',
              StatusEquals='InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
              SortBy='Name'|'CreationTime'|'Status',
              SortOrder='Ascending'|'Descending',
              NextToken='string',
              MaxResults=123
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of transform jobs, use it in the next request.
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
        """
        pass

    def list_workteams(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Gets a list of work teams that you have defined in a region. The list may be empty if no work team satisfies the filter specified in the ``NameContains`` parameter.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListWorkteams>`_
        
        **Request Syntax**
        ::
          response = client.list_workteams(
              SortBy='Name'|'CreateDate',
              SortOrder='Ascending'|'Descending',
              NameContains='string',
              NextToken='string',
              MaxResults=123
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of work teams, use it in the subsequent request.
        :type SortBy: string
        :param SortBy:
          The field to sort results by. The default is ``CreationTime`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order for results. The default is ``Ascending`` .
        :type NameContains: string
        :param NameContains:
          A string in the work team\'s name. This filter returns only work teams whose name contains the specified string.
        :type NextToken: string
        :param NextToken:
          If the result of the previous ``ListWorkteams`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of labeling jobs, use the token in the next request.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of work teams to return in each page of the response.
        :rtype: dict
        :returns:
        """
        pass

    def render_ui_template(self, UiTemplate: Dict, Task: Dict, RoleArn: str) -> Dict:
        """
        Renders the UI template so that you can preview the worker's experience. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/RenderUiTemplate>`_
        
        **Request Syntax**
        ::
          response = client.render_ui_template(
              UiTemplate={
                  'Content': 'string'
              },
              Task={
                  'Input': 'string'
              },
              RoleArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'RenderedContent': 'string',
                'Errors': [
                    {
                        'Code': 'string',
                        'Message': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RenderedContent** *(string) --* 
              A Liquid template that renders the HTML for the worker UI.
            - **Errors** *(list) --* 
              A list of one or more ``RenderingError`` objects if any were encountered while rendering the template. If there were no errors, the list is empty.
              - *(dict) --* 
                A description of an error that occurred while rendering the template.
                - **Code** *(string) --* 
                  A unique identifier for a specific class of errors.
                - **Message** *(string) --* 
                  A human-readable message describing the error.
        :type UiTemplate: dict
        :param UiTemplate: **[REQUIRED]**
          A ``Template`` object containing the worker UI template to render.
          - **Content** *(string) --* **[REQUIRED]**
            The content of the Liquid template for the worker user interface.
        :type Task: dict
        :param Task: **[REQUIRED]**
          A ``RenderableTask`` object containing a representative task to render.
          - **Input** *(string) --* **[REQUIRED]**
            A JSON object that contains values for the variables defined in the template. It is made available to the template under the substitution variable ``task.input`` . For example, if you define a variable ``task.input.text`` in your template, you can supply the variable in the JSON object as ``\"text\": \"sample text\"`` .
        :type RoleArn: string
        :param RoleArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) that has access to the S3 objects that are used by the template.
        :rtype: dict
        :returns:
        """
        pass

    def search(self, Resource: str, SearchExpression: Dict = None, SortBy: str = None, SortOrder: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Finds Amazon SageMaker resources that match a search query. Matching resource objects are returned as a list of ``SearchResult`` objects in the response. You can sort the search results by any resource property in a ascending or descending order.
        You can query against the following value types: numerical, text, Booleans, and timestamps.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/Search>`_
        
        **Request Syntax**
        ::
          response = client.search(
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
              NextToken='string',
              MaxResults=123
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
                            'EnableInterContainerTrafficEncryption': True|False,
                            'Tags': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ]
                        }
                    },
                ],
                'NextToken': 'string'
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
                      The registry path of the Docker image that contains the training algorithm. For information about docker registry paths for built-in algorithms, see `Algorithms Provided by Amazon SageMaker\: Common Parameters <https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html>`__ . Amazon SageMaker supports both ``registry/repository[:tag]`` and ``registry/repository[@digest]`` image path formats. For more information, see `Using Your Own Algorithms with Amazon SageMaker <https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__ .
                    - **AlgorithmName** *(string) --* 
                      The name of the algorithm resource to use for the training job. This must be an algorithm resource that you created or subscribe to on AWS Marketplace. If you specify a value for this parameter, you can't specify a value for ``TrainingImage`` .
                    - **TrainingInputMode** *(string) --* 
                      The input mode that the algorithm supports. For the input modes that Amazon SageMaker algorithms support, see `Algorithms <https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ . If an algorithm supports the ``File`` input mode, Amazon SageMaker downloads the training data from S3 to the provisioned ML storage Volume, and mounts the directory to docker volume for training container. If an algorithm supports the ``Pipe`` input mode, Amazon SageMaker streams data directly from S3 to the container. 
                      In File mode, make sure you provision ML storage volume with sufficient capacity to accommodate the data download from S3. In addition to the training data, the ML storage volume also stores the output model. The algorithm container use ML storage volume to also store intermediate information, if any. 
                      For distributed algorithms using File mode, training data is distributed uniformly, and your training duration is predictable if the input data objects size is approximately same. Amazon SageMaker does not split the files any further for model training. If the object sizes are skewed, training won't be optimal as the data distribution is also skewed where one host in a training cluster is overloaded, thus becoming bottleneck in training. 
                    - **MetricDefinitions** *(list) --* 
                      A list of metric definition objects. Each object specifies the metric name and regular expressions used to parse algorithm logs. Amazon SageMaker publishes each metric to Amazon CloudWatch.
                      - *(dict) --* 
                        Specifies a metric that the training algorithm writes to ``stderr`` or ``stdout`` . Amazon SageMakerhyperparameter tuning captures all defined metrics. You specify one metric that a hyperparameter tuning job uses as its objective metric to choose the best training job.
                        - **Name** *(string) --* 
                          The name of the metric.
                        - **Regex** *(string) --* 
                          A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see `Defining Objective Metrics <https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics.html>`__ .
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
                    A  VpcConfig object that specifies the VPC that this training job has access to. For more information, see `Protect Training Jobs by Using an Amazon Virtual Private Cloud <https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html>`__ .
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
                  - **EnableInterContainerTrafficEncryption** *(boolean) --* 
                    To encrypt all communications between ML compute instances in distributed training, choose ``True`` . Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithm in distributed training.
                  - **Tags** *(list) --* 
                    An array of key-value pairs. For more information, see `Using Cost Allocation Tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what>`__ in the *AWS Billing and Cost Management User Guide* .
                    - *(dict) --* 
                      Describes a tag. 
                      - **Key** *(string) --* 
                        The tag key.
                      - **Value** *(string) --* 
                        The tag value.
            - **NextToken** *(string) --* 
              If the result of the previous ``Search`` request was truncated, the response includes a NextToken. To retrieve the next set of results, use the token in the next request.
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
        :type NextToken: string
        :param NextToken:
          If more than ``MaxResults`` resource objects match the specified ``SearchExpression`` , the ``SearchResponse`` includes a ``NextToken`` . The ``NextToken`` can be passed to the next ``SearchRequest`` to continue retrieving results for the specified ``SearchExpression`` and ``Sort`` parameters.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of results to return in a ``SearchResponse`` .
        :rtype: dict
        :returns:
        """
        pass

    def start_notebook_instance(self, NotebookInstanceName: str):
        """
        Launches an ML compute instance with the latest version of the libraries and attaches your ML storage volume. After configuring the notebook instance, Amazon SageMaker sets the notebook instance status to ``InService`` . A notebook instance's status must be ``InService`` before you can connect to your Jupyter notebook. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/StartNotebookInstance>`_
        
        **Request Syntax**
        ::
          response = client.start_notebook_instance(
              NotebookInstanceName='string'
          )
        :type NotebookInstanceName: string
        :param NotebookInstanceName: **[REQUIRED]**
          The name of the notebook instance to start.
        :returns: None
        """
        pass

    def stop_compilation_job(self, CompilationJobName: str):
        """
        Stops a model compilation job.
        To stop a job, Amazon SageMaker sends the algorithm the SIGTERM signal. This gracefully shuts the job down. If the job hasn't stopped, it sends the SIGKILL signal.
        When it receives a ``StopCompilationJob`` request, Amazon SageMaker changes the  CompilationJobSummary$CompilationJobStatus of the job to ``Stopping`` . After Amazon SageMaker stops the job, it sets the  CompilationJobSummary$CompilationJobStatus to ``Stopped`` . 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/StopCompilationJob>`_
        
        **Request Syntax**
        ::
          response = client.stop_compilation_job(
              CompilationJobName='string'
          )
        :type CompilationJobName: string
        :param CompilationJobName: **[REQUIRED]**
          The name of the model compilation job to stop.
        :returns: None
        """
        pass

    def stop_hyper_parameter_tuning_job(self, HyperParameterTuningJobName: str):
        """
        Stops a running hyperparameter tuning job and all running training jobs that the tuning job launched.
        All model artifacts output from the training jobs are stored in Amazon Simple Storage Service (Amazon S3). All data that the training jobs write to Amazon CloudWatch Logs are still available in CloudWatch. After the tuning job moves to the ``Stopped`` state, it releases all reserved resources for the tuning job.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/StopHyperParameterTuningJob>`_
        
        **Request Syntax**
        ::
          response = client.stop_hyper_parameter_tuning_job(
              HyperParameterTuningJobName='string'
          )
        :type HyperParameterTuningJobName: string
        :param HyperParameterTuningJobName: **[REQUIRED]**
          The name of the tuning job to stop.
        :returns: None
        """
        pass

    def stop_labeling_job(self, LabelingJobName: str):
        """
        Stops a running labeling job. A job that is stopped cannot be restarted. Any results obtained before the job is stopped are placed in the Amazon S3 output bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/StopLabelingJob>`_
        
        **Request Syntax**
        ::
          response = client.stop_labeling_job(
              LabelingJobName='string'
          )
        :type LabelingJobName: string
        :param LabelingJobName: **[REQUIRED]**
          The name of the labeling job to stop.
        :returns: None
        """
        pass

    def stop_notebook_instance(self, NotebookInstanceName: str):
        """
        Terminates the ML compute instance. Before terminating the instance, Amazon SageMaker disconnects the ML storage volume from it. Amazon SageMaker preserves the ML storage volume. 
        To access data on the ML storage volume for a notebook instance that has been terminated, call the ``StartNotebookInstance`` API. ``StartNotebookInstance`` launches another ML compute instance, configures it, and attaches the preserved ML storage volume so you can continue your work. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/StopNotebookInstance>`_
        
        **Request Syntax**
        ::
          response = client.stop_notebook_instance(
              NotebookInstanceName='string'
          )
        :type NotebookInstanceName: string
        :param NotebookInstanceName: **[REQUIRED]**
          The name of the notebook instance to terminate.
        :returns: None
        """
        pass

    def stop_training_job(self, TrainingJobName: str):
        """
        Stops a training job. To stop a job, Amazon SageMaker sends the algorithm the ``SIGTERM`` signal, which delays job termination for 120 seconds. Algorithms might use this 120-second window to save the model artifacts, so the results of the training is not lost. 
        When it receives a ``StopTrainingJob`` request, Amazon SageMaker changes the status of the job to ``Stopping`` . After Amazon SageMaker stops the job, it sets the status to ``Stopped`` .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/StopTrainingJob>`_
        
        **Request Syntax**
        ::
          response = client.stop_training_job(
              TrainingJobName='string'
          )
        :type TrainingJobName: string
        :param TrainingJobName: **[REQUIRED]**
          The name of the training job to stop.
        :returns: None
        """
        pass

    def stop_transform_job(self, TransformJobName: str):
        """
        Stops a transform job.
        When Amazon SageMaker receives a ``StopTransformJob`` request, the status of the job changes to ``Stopping`` . After Amazon SageMaker stops the job, the status is set to ``Stopped`` . When you stop a transform job before it is completed, Amazon SageMaker doesn't store the job's output in Amazon S3.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/StopTransformJob>`_
        
        **Request Syntax**
        ::
          response = client.stop_transform_job(
              TransformJobName='string'
          )
        :type TransformJobName: string
        :param TransformJobName: **[REQUIRED]**
          The name of the transform job to stop.
        :returns: None
        """
        pass

    def update_code_repository(self, CodeRepositoryName: str, GitConfig: Dict = None) -> Dict:
        """
        Updates the specified Git repository with the specified values.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/UpdateCodeRepository>`_
        
        **Request Syntax**
        ::
          response = client.update_code_repository(
              CodeRepositoryName='string',
              GitConfig={
                  'SecretArn': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'CodeRepositoryArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CodeRepositoryArn** *(string) --* 
              The ARN of the Git repository.
        :type CodeRepositoryName: string
        :param CodeRepositoryName: **[REQUIRED]**
          The name of the Git repository to update.
        :type GitConfig: dict
        :param GitConfig:
          The configuration of the git repository, including the URL and the Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the credentials used to access the repository. The secret must have a staging label of ``AWSCURRENT`` and must be in the following format:
           ``{\"username\": *UserName* , \"password\": *Password* }``
          - **SecretArn** *(string) --*
            The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the credentials used to access the git repository. The secret must have a staging label of ``AWSCURRENT`` and must be in the following format:
             ``{\"username\": *UserName* , \"password\": *Password* }``
        :rtype: dict
        :returns:
        """
        pass

    def update_endpoint(self, EndpointName: str, EndpointConfigName: str) -> Dict:
        """
        Deploys the new ``EndpointConfig`` specified in the request, switches to using newly created endpoint, and then deletes resources provisioned for the endpoint using the previous ``EndpointConfig`` (there is no availability loss). 
        When Amazon SageMaker receives the request, it sets the endpoint status to ``Updating`` . After updating the endpoint, it sets the status to ``InService`` . To check the status of an endpoint, use the `DescribeEndpoint <https://docs.aws.amazon.com/sagemaker/latest/dg/API_DescribeEndpoint.html>`__ API. 
        .. note::
          You cannot update an endpoint with the current ``EndpointConfig`` . To update an endpoint, you must create a new ``EndpointConfig`` .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/UpdateEndpoint>`_
        
        **Request Syntax**
        ::
          response = client.update_endpoint(
              EndpointName='string',
              EndpointConfigName='string'
          )
        
        **Response Syntax**
        ::
            {
                'EndpointArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **EndpointArn** *(string) --* 
              The Amazon Resource Name (ARN) of the endpoint.
        :type EndpointName: string
        :param EndpointName: **[REQUIRED]**
          The name of the endpoint whose configuration you want to update.
        :type EndpointConfigName: string
        :param EndpointConfigName: **[REQUIRED]**
          The name of the new endpoint configuration.
        :rtype: dict
        :returns:
        """
        pass

    def update_endpoint_weights_and_capacities(self, EndpointName: str, DesiredWeightsAndCapacities: List) -> Dict:
        """
        Updates variant weight of one or more variants associated with an existing endpoint, or capacity of one variant associated with an existing endpoint. When it receives the request, Amazon SageMaker sets the endpoint status to ``Updating`` . After updating the endpoint, it sets the status to ``InService`` . To check the status of an endpoint, use the `DescribeEndpoint <https://docs.aws.amazon.com/sagemaker/latest/dg/API_DescribeEndpoint.html>`__ API. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/UpdateEndpointWeightsAndCapacities>`_
        
        **Request Syntax**
        ::
          response = client.update_endpoint_weights_and_capacities(
              EndpointName='string',
              DesiredWeightsAndCapacities=[
                  {
                      'VariantName': 'string',
                      'DesiredWeight': ...,
                      'DesiredInstanceCount': 123
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'EndpointArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **EndpointArn** *(string) --* 
              The Amazon Resource Name (ARN) of the updated endpoint.
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
        """
        pass

    def update_notebook_instance(self, NotebookInstanceName: str, InstanceType: str = None, RoleArn: str = None, LifecycleConfigName: str = None, DisassociateLifecycleConfig: bool = None, VolumeSizeInGB: int = None, DefaultCodeRepository: str = None, AdditionalCodeRepositories: List = None, AcceleratorTypes: List = None, DisassociateAcceleratorTypes: bool = None, DisassociateDefaultCodeRepository: bool = None, DisassociateAdditionalCodeRepositories: bool = None, RootAccess: str = None) -> Dict:
        """
        Updates a notebook instance. NotebookInstance updates include upgrading or downgrading the ML compute instance used for your notebook instance to accommodate changes in your workload requirements. You can also update the VPC security groups.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/UpdateNotebookInstance>`_
        
        **Request Syntax**
        ::
          response = client.update_notebook_instance(
              NotebookInstanceName='string',
              InstanceType='ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.t3.medium'|'ml.t3.large'|'ml.t3.xlarge'|'ml.t3.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.c5d.xlarge'|'ml.c5d.2xlarge'|'ml.c5d.4xlarge'|'ml.c5d.9xlarge'|'ml.c5d.18xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge',
              RoleArn='string',
              LifecycleConfigName='string',
              DisassociateLifecycleConfig=True|False,
              VolumeSizeInGB=123,
              DefaultCodeRepository='string',
              AdditionalCodeRepositories=[
                  'string',
              ],
              AcceleratorTypes=[
                  'ml.eia1.medium'|'ml.eia1.large'|'ml.eia1.xlarge',
              ],
              DisassociateAcceleratorTypes=True|False,
              DisassociateDefaultCodeRepository=True|False,
              DisassociateAdditionalCodeRepositories=True|False,
              RootAccess='Enabled'|'Disabled'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type NotebookInstanceName: string
        :param NotebookInstanceName: **[REQUIRED]**
          The name of the notebook instance to update.
        :type InstanceType: string
        :param InstanceType:
          The Amazon ML compute instance type.
        :type RoleArn: string
        :param RoleArn:
          The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker can assume to access the notebook instance. For more information, see `Amazon SageMaker Roles <https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html>`__ .
          .. note::
            To be able to pass this role to Amazon SageMaker, the caller of this API must have the ``iam:PassRole`` permission.
        :type LifecycleConfigName: string
        :param LifecycleConfigName:
          The name of a lifecycle configuration to associate with the notebook instance. For information about lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
        :type DisassociateLifecycleConfig: boolean
        :param DisassociateLifecycleConfig:
          Set to ``true`` to remove the notebook instance lifecycle configuration currently associated with the notebook instance.
        :type VolumeSizeInGB: integer
        :param VolumeSizeInGB:
          The size, in GB, of the ML storage volume to attach to the notebook instance. The default value is 5 GB.
        :type DefaultCodeRepository: string
        :param DefaultCodeRepository:
          The Git repository to associate with the notebook instance as its default code repository. This can be either the name of a Git repository stored as a resource in your account, or the URL of a Git repository in `AWS CodeCommit <http://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html>`__ or in any other Git repository. When you open a notebook instance, it opens in the directory that contains this repository. For more information, see `Associating Git Repositories with Amazon SageMaker Notebook Instances <http://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html>`__ .
        :type AdditionalCodeRepositories: list
        :param AdditionalCodeRepositories:
          An array of up to three Git repositories to associate with the notebook instance. These can be either the names of Git repositories stored as resources in your account, or the URL of Git repositories in `AWS CodeCommit <http://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html>`__ or in any other Git repository. These repositories are cloned at the same level as the default repository of your notebook instance. For more information, see `Associating Git Repositories with Amazon SageMaker Notebook Instances <http://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html>`__ .
          - *(string) --*
        :type AcceleratorTypes: list
        :param AcceleratorTypes:
          A list of the Elastic Inference (EI) instance types to associate with this notebook instance. Currently only one EI instance type can be associated with a notebook instance. For more information, see `Using Elastic Inference in Amazon SageMaker <http://docs.aws.amazon.com/sagemaker/latest/dg/ei.html>`__ .
          - *(string) --*
        :type DisassociateAcceleratorTypes: boolean
        :param DisassociateAcceleratorTypes:
          A list of the Elastic Inference (EI) instance types to remove from this notebook instance.
        :type DisassociateDefaultCodeRepository: boolean
        :param DisassociateDefaultCodeRepository:
          The name or URL of the default Git repository to remove from this notebook instance.
        :type DisassociateAdditionalCodeRepositories: boolean
        :param DisassociateAdditionalCodeRepositories:
          A list of names or URLs of the default Git repositories to remove from this notebook instance.
        :type RootAccess: string
        :param RootAccess:
          Whether root access is enabled or disabled for users of the notebook instance. The default value is ``Enabled`` .
          .. note::
            If you set this to ``Disabled`` , users don\'t have root access on the notebook instance, but lifecycle configuration scripts still run with root permissions.
        :rtype: dict
        :returns:
        """
        pass

    def update_notebook_instance_lifecycle_config(self, NotebookInstanceLifecycleConfigName: str, OnCreate: List = None, OnStart: List = None) -> Dict:
        """
        Updates a notebook instance lifecycle configuration created with the  CreateNotebookInstanceLifecycleConfig API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/UpdateNotebookInstanceLifecycleConfig>`_
        
        **Request Syntax**
        ::
          response = client.update_notebook_instance_lifecycle_config(
              NotebookInstanceLifecycleConfigName='string',
              OnCreate=[
                  {
                      'Content': 'string'
                  },
              ],
              OnStart=[
                  {
                      'Content': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
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
            For information about notebook instance lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
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
            For information about notebook instance lifestyle configurations, see `Step 2.1\: (Optional) Customize a Notebook Instance <https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__ .
            - **Content** *(string) --*
              A base64-encoded string that contains a shell script for a notebook instance lifecycle configuration.
        :rtype: dict
        :returns:
        """
        pass

    def update_workteam(self, WorkteamName: str, MemberDefinitions: List = None, Description: str = None) -> Dict:
        """
        Updates an existing work team with new member definitions or description.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/UpdateWorkteam>`_
        
        **Request Syntax**
        ::
          response = client.update_workteam(
              WorkteamName='string',
              MemberDefinitions=[
                  {
                      'CognitoMemberDefinition': {
                          'UserPool': 'string',
                          'UserGroup': 'string',
                          'ClientId': 'string'
                      }
                  },
              ],
              Description='string'
          )
        
        **Response Syntax**
        ::
            {
                'Workteam': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Workteam** *(dict) --* 
              A ``Workteam`` object that describes the updated work team.
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
        :type WorkteamName: string
        :param WorkteamName: **[REQUIRED]**
          The name of the work team to update.
        :type MemberDefinitions: list
        :param MemberDefinitions:
          A list of ``MemberDefinition`` objects that contain the updated work team members.
          - *(dict) --*
            Defines the Amazon Cognito user group that is part of a work team.
            - **CognitoMemberDefinition** *(dict) --*
              The Amazon Cognito user group that is part of the work team.
              - **UserPool** *(string) --* **[REQUIRED]**
                An identifier for a user pool. The user pool must be in the same region as the service that you are calling.
              - **UserGroup** *(string) --* **[REQUIRED]**
                An identifier for a user group.
              - **ClientId** *(string) --* **[REQUIRED]**
                An identifier for an application client. You must create the app client ID using Amazon Cognito.
        :type Description: string
        :param Description:
          An updated description for the work team.
        :rtype: dict
        :returns:
        """
        pass
