from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def acknowledge_job(self, jobId: str, nonce: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/AcknowledgeJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.acknowledge_job(
              jobId=\'string\',
              nonce=\'string\'
          )
        :type jobId: string
        :param jobId: **[REQUIRED]** 
        
          The unique system-generated ID of the job for which you want to confirm receipt.
        
        :type nonce: string
        :param nonce: **[REQUIRED]** 
        
          A system-generated random number that AWS CodePipeline uses to ensure that the job is being worked on by only one job worker. Get this number from the response of the  PollForJobs request that returned this job.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'status\': \'Created\'|\'Queued\'|\'Dispatched\'|\'InProgress\'|\'TimedOut\'|\'Succeeded\'|\'Failed\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of an AcknowledgeJob action.
        
            - **status** *(string) --* 
        
              Whether the job worker has received the specified job.
        
        """
        pass

    def acknowledge_third_party_job(self, jobId: str, nonce: str, clientToken: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/AcknowledgeThirdPartyJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.acknowledge_third_party_job(
              jobId=\'string\',
              nonce=\'string\',
              clientToken=\'string\'
          )
        :type jobId: string
        :param jobId: **[REQUIRED]** 
        
          The unique system-generated ID of the job.
        
        :type nonce: string
        :param nonce: **[REQUIRED]** 
        
          A system-generated random number that AWS CodePipeline uses to ensure that the job is being worked on by only one job worker. Get this number from the response to a  GetThirdPartyJobDetails request.
        
        :type clientToken: string
        :param clientToken: **[REQUIRED]** 
        
          The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'status\': \'Created\'|\'Queued\'|\'Dispatched\'|\'InProgress\'|\'TimedOut\'|\'Succeeded\'|\'Failed\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of an AcknowledgeThirdPartyJob action.
        
            - **status** *(string) --* 
        
              The status information for the third party job, if any.
        
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

    def create_custom_action_type(self, category: str, provider: str, version: str, inputArtifactDetails: Dict, outputArtifactDetails: Dict, settings: Dict = None, configurationProperties: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/CreateCustomActionType>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_custom_action_type(
              category=\'Source\'|\'Build\'|\'Deploy\'|\'Test\'|\'Invoke\'|\'Approval\',
              provider=\'string\',
              version=\'string\',
              settings={
                  \'thirdPartyConfigurationUrl\': \'string\',
                  \'entityUrlTemplate\': \'string\',
                  \'executionUrlTemplate\': \'string\',
                  \'revisionUrlTemplate\': \'string\'
              },
              configurationProperties=[
                  {
                      \'name\': \'string\',
                      \'required\': True|False,
                      \'key\': True|False,
                      \'secret\': True|False,
                      \'queryable\': True|False,
                      \'description\': \'string\',
                      \'type\': \'String\'|\'Number\'|\'Boolean\'
                  },
              ],
              inputArtifactDetails={
                  \'minimumCount\': 123,
                  \'maximumCount\': 123
              },
              outputArtifactDetails={
                  \'minimumCount\': 123,
                  \'maximumCount\': 123
              }
          )
        :type category: string
        :param category: **[REQUIRED]** 
        
          The category of the custom action, such as a build action or a test action.
        
          .. note::
        
            Although Source and Approval are listed as valid values, they are not currently functional. These values are reserved for future use.
        
        :type provider: string
        :param provider: **[REQUIRED]** 
        
          The provider of the service used in the custom action, such as AWS CodeDeploy.
        
        :type version: string
        :param version: **[REQUIRED]** 
        
          The version identifier of the custom action.
        
        :type settings: dict
        :param settings: 
        
          Returns information about the settings for an action type.
        
          - **thirdPartyConfigurationUrl** *(string) --* 
        
            The URL of a sign-up page where users can sign up for an external service and perform initial configuration of the action provided by that service.
        
          - **entityUrlTemplate** *(string) --* 
        
            The URL returned to the AWS CodePipeline console that provides a deep link to the resources of the external system, such as the configuration page for an AWS CodeDeploy deployment group. This link is provided as part of the action display within the pipeline.
        
          - **executionUrlTemplate** *(string) --* 
        
            The URL returned to the AWS CodePipeline console that contains a link to the top-level landing page for the external system, such as console page for AWS CodeDeploy. This link is shown on the pipeline view page in the AWS CodePipeline console and provides a link to the execution entity of the external action.
        
          - **revisionUrlTemplate** *(string) --* 
        
            The URL returned to the AWS CodePipeline console that contains a link to the page where customers can update or change the configuration of the external action.
        
        :type configurationProperties: list
        :param configurationProperties: 
        
          The configuration properties for the custom action.
        
          .. note::
        
            You can refer to a name in the configuration properties of the custom action within the URL templates by following the format of {Config:name}, as long as the configuration property is both required and not secret. For more information, see `Create a Custom Action for a Pipeline <http://docs.aws.amazon.com/codepipeline/latest/userguide/how-to-create-custom-action.html>`__ .
        
          - *(dict) --* 
        
            Represents information about an action configuration property.
        
            - **name** *(string) --* **[REQUIRED]** 
        
              The name of the action configuration property.
        
            - **required** *(boolean) --* **[REQUIRED]** 
        
              Whether the configuration property is a required value.
        
            - **key** *(boolean) --* **[REQUIRED]** 
        
              Whether the configuration property is a key.
        
            - **secret** *(boolean) --* **[REQUIRED]** 
        
              Whether the configuration property is secret. Secrets are hidden from all calls except for GetJobDetails, GetThirdPartyJobDetails, PollForJobs, and PollForThirdPartyJobs.
        
              When updating a pipeline, passing * * * * * without changing any other values of the action will preserve the prior value of the secret.
        
            - **queryable** *(boolean) --* 
        
              Indicates that the property will be used in conjunction with PollForJobs. When creating a custom action, an action can have up to one queryable property. If it has one, that property must be both required and not secret.
        
              If you create a pipeline with a custom action type, and that custom action contains a queryable property, the value for that configuration property is subject to additional restrictions. The value must be less than or equal to twenty (20) characters. The value can contain only alphanumeric characters, underscores, and hyphens.
        
            - **description** *(string) --* 
        
              The description of the action configuration property that will be displayed to users.
        
            - **type** *(string) --* 
        
              The type of the configuration property.
        
        :type inputArtifactDetails: dict
        :param inputArtifactDetails: **[REQUIRED]** 
        
          The details of the input artifact for the action, such as its commit ID.
        
          - **minimumCount** *(integer) --* **[REQUIRED]** 
        
            The minimum number of artifacts allowed for the action type.
        
          - **maximumCount** *(integer) --* **[REQUIRED]** 
        
            The maximum number of artifacts allowed for the action type.
        
        :type outputArtifactDetails: dict
        :param outputArtifactDetails: **[REQUIRED]** 
        
          The details of the output artifact of the action, such as its commit ID.
        
          - **minimumCount** *(integer) --* **[REQUIRED]** 
        
            The minimum number of artifacts allowed for the action type.
        
          - **maximumCount** *(integer) --* **[REQUIRED]** 
        
            The maximum number of artifacts allowed for the action type.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'actionType\': {
                    \'id\': {
                        \'category\': \'Source\'|\'Build\'|\'Deploy\'|\'Test\'|\'Invoke\'|\'Approval\',
                        \'owner\': \'AWS\'|\'ThirdParty\'|\'Custom\',
                        \'provider\': \'string\',
                        \'version\': \'string\'
                    },
                    \'settings\': {
                        \'thirdPartyConfigurationUrl\': \'string\',
                        \'entityUrlTemplate\': \'string\',
                        \'executionUrlTemplate\': \'string\',
                        \'revisionUrlTemplate\': \'string\'
                    },
                    \'actionConfigurationProperties\': [
                        {
                            \'name\': \'string\',
                            \'required\': True|False,
                            \'key\': True|False,
                            \'secret\': True|False,
                            \'queryable\': True|False,
                            \'description\': \'string\',
                            \'type\': \'String\'|\'Number\'|\'Boolean\'
                        },
                    ],
                    \'inputArtifactDetails\': {
                        \'minimumCount\': 123,
                        \'maximumCount\': 123
                    },
                    \'outputArtifactDetails\': {
                        \'minimumCount\': 123,
                        \'maximumCount\': 123
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a CreateCustomActionType operation.
        
            - **actionType** *(dict) --* 
        
              Returns information about the details of an action type.
        
              - **id** *(dict) --* 
        
                Represents information about an action type.
        
                - **category** *(string) --* 
        
                  A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
        
                - **owner** *(string) --* 
        
                  The creator of the action being called.
        
                - **provider** *(string) --* 
        
                  The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
        
                - **version** *(string) --* 
        
                  A string that describes the action version.
        
              - **settings** *(dict) --* 
        
                The settings for the action type.
        
                - **thirdPartyConfigurationUrl** *(string) --* 
        
                  The URL of a sign-up page where users can sign up for an external service and perform initial configuration of the action provided by that service.
        
                - **entityUrlTemplate** *(string) --* 
        
                  The URL returned to the AWS CodePipeline console that provides a deep link to the resources of the external system, such as the configuration page for an AWS CodeDeploy deployment group. This link is provided as part of the action display within the pipeline.
        
                - **executionUrlTemplate** *(string) --* 
        
                  The URL returned to the AWS CodePipeline console that contains a link to the top-level landing page for the external system, such as console page for AWS CodeDeploy. This link is shown on the pipeline view page in the AWS CodePipeline console and provides a link to the execution entity of the external action.
        
                - **revisionUrlTemplate** *(string) --* 
        
                  The URL returned to the AWS CodePipeline console that contains a link to the page where customers can update or change the configuration of the external action.
        
              - **actionConfigurationProperties** *(list) --* 
        
                The configuration properties for the action type.
        
                - *(dict) --* 
        
                  Represents information about an action configuration property.
        
                  - **name** *(string) --* 
        
                    The name of the action configuration property.
        
                  - **required** *(boolean) --* 
        
                    Whether the configuration property is a required value.
        
                  - **key** *(boolean) --* 
        
                    Whether the configuration property is a key.
        
                  - **secret** *(boolean) --* 
        
                    Whether the configuration property is secret. Secrets are hidden from all calls except for GetJobDetails, GetThirdPartyJobDetails, PollForJobs, and PollForThirdPartyJobs.
        
                    When updating a pipeline, passing * * * * * without changing any other values of the action will preserve the prior value of the secret.
        
                  - **queryable** *(boolean) --* 
        
                    Indicates that the property will be used in conjunction with PollForJobs. When creating a custom action, an action can have up to one queryable property. If it has one, that property must be both required and not secret.
        
                    If you create a pipeline with a custom action type, and that custom action contains a queryable property, the value for that configuration property is subject to additional restrictions. The value must be less than or equal to twenty (20) characters. The value can contain only alphanumeric characters, underscores, and hyphens.
        
                  - **description** *(string) --* 
        
                    The description of the action configuration property that will be displayed to users.
        
                  - **type** *(string) --* 
        
                    The type of the configuration property.
        
              - **inputArtifactDetails** *(dict) --* 
        
                The details of the input artifact for the action, such as its commit ID.
        
                - **minimumCount** *(integer) --* 
        
                  The minimum number of artifacts allowed for the action type.
        
                - **maximumCount** *(integer) --* 
        
                  The maximum number of artifacts allowed for the action type.
        
              - **outputArtifactDetails** *(dict) --* 
        
                The details of the output artifact of the action, such as its commit ID.
        
                - **minimumCount** *(integer) --* 
        
                  The minimum number of artifacts allowed for the action type.
        
                - **maximumCount** *(integer) --* 
        
                  The maximum number of artifacts allowed for the action type.
        
        """
        pass

    def create_pipeline(self, pipeline: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/CreatePipeline>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_pipeline(
              pipeline={
                  \'name\': \'string\',
                  \'roleArn\': \'string\',
                  \'artifactStore\': {
                      \'type\': \'S3\',
                      \'location\': \'string\',
                      \'encryptionKey\': {
                          \'id\': \'string\',
                          \'type\': \'KMS\'
                      }
                  },
                  \'artifactStores\': {
                      \'string\': {
                          \'type\': \'S3\',
                          \'location\': \'string\',
                          \'encryptionKey\': {
                              \'id\': \'string\',
                              \'type\': \'KMS\'
                          }
                      }
                  },
                  \'stages\': [
                      {
                          \'name\': \'string\',
                          \'blockers\': [
                              {
                                  \'name\': \'string\',
                                  \'type\': \'Schedule\'
                              },
                          ],
                          \'actions\': [
                              {
                                  \'name\': \'string\',
                                  \'actionTypeId\': {
                                      \'category\': \'Source\'|\'Build\'|\'Deploy\'|\'Test\'|\'Invoke\'|\'Approval\',
                                      \'owner\': \'AWS\'|\'ThirdParty\'|\'Custom\',
                                      \'provider\': \'string\',
                                      \'version\': \'string\'
                                  },
                                  \'runOrder\': 123,
                                  \'configuration\': {
                                      \'string\': \'string\'
                                  },
                                  \'outputArtifacts\': [
                                      {
                                          \'name\': \'string\'
                                      },
                                  ],
                                  \'inputArtifacts\': [
                                      {
                                          \'name\': \'string\'
                                      },
                                  ],
                                  \'roleArn\': \'string\',
                                  \'region\': \'string\'
                              },
                          ]
                      },
                  ],
                  \'version\': 123
              }
          )
        :type pipeline: dict
        :param pipeline: **[REQUIRED]** 
        
          Represents the structure of actions and stages to be performed in the pipeline. 
        
          - **name** *(string) --* **[REQUIRED]** 
        
            The name of the action to be performed.
        
          - **roleArn** *(string) --* **[REQUIRED]** 
        
            The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with no actionRoleArn, or to use to assume roles for actions with an actionRoleArn.
        
          - **artifactStore** *(dict) --* 
        
            Represents information about the Amazon S3 bucket where artifacts are stored for the pipeline. 
        
            - **type** *(string) --* **[REQUIRED]** 
        
              The type of the artifact store, such as S3.
        
            - **location** *(string) --* **[REQUIRED]** 
        
              The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder within the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any Amazon S3 bucket in the same AWS Region as the pipeline to store your pipeline artifacts.
        
            - **encryptionKey** *(dict) --* 
        
              The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.
        
              - **id** *(string) --* **[REQUIRED]** 
        
                The ID used to identify the key. For an AWS KMS key, this is the key ID or key ARN.
        
              - **type** *(string) --* **[REQUIRED]** 
        
                The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.
        
          - **artifactStores** *(dict) --* 
        
            A mapping of artifactStore objects and their corresponding regions. There must be an artifact store for the pipeline region and for each cross-region action within the pipeline. You can only use either artifactStore or artifactStores, not both.
        
            If you create a cross-region action in your pipeline, you must use artifactStores.
        
            - *(string) --* 
        
              - *(dict) --* 
        
                The Amazon S3 bucket where artifacts are stored for the pipeline.
        
                - **type** *(string) --* **[REQUIRED]** 
        
                  The type of the artifact store, such as S3.
        
                - **location** *(string) --* **[REQUIRED]** 
        
                  The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder within the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any Amazon S3 bucket in the same AWS Region as the pipeline to store your pipeline artifacts.
        
                - **encryptionKey** *(dict) --* 
        
                  The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.
        
                  - **id** *(string) --* **[REQUIRED]** 
        
                    The ID used to identify the key. For an AWS KMS key, this is the key ID or key ARN.
        
                  - **type** *(string) --* **[REQUIRED]** 
        
                    The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.
        
          - **stages** *(list) --* **[REQUIRED]** 
        
            The stage in which to perform the action.
        
            - *(dict) --* 
        
              Represents information about a stage and its definition.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the stage.
        
              - **blockers** *(list) --* 
        
                Reserved for future use.
        
                - *(dict) --* 
        
                  Reserved for future use.
        
                  - **name** *(string) --* **[REQUIRED]** 
        
                    Reserved for future use.
        
                  - **type** *(string) --* **[REQUIRED]** 
        
                    Reserved for future use.
        
              - **actions** *(list) --* **[REQUIRED]** 
        
                The actions included in a stage.
        
                - *(dict) --* 
        
                  Represents information about an action declaration.
        
                  - **name** *(string) --* **[REQUIRED]** 
        
                    The action declaration\'s name.
        
                  - **actionTypeId** *(dict) --* **[REQUIRED]** 
        
                    The configuration information for the action type.
        
                    - **category** *(string) --* **[REQUIRED]** 
        
                      A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
        
                    - **owner** *(string) --* **[REQUIRED]** 
        
                      The creator of the action being called.
        
                    - **provider** *(string) --* **[REQUIRED]** 
        
                      The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
        
                    - **version** *(string) --* **[REQUIRED]** 
        
                      A string that describes the action version.
        
                  - **runOrder** *(integer) --* 
        
                    The order in which actions are run.
        
                  - **configuration** *(dict) --* 
        
                    The action declaration\'s configuration.
        
                    - *(string) --* 
        
                      - *(string) --* 
        
                  - **outputArtifacts** *(list) --* 
        
                    The name or ID of the result of the action declaration, such as a test or build artifact.
        
                    - *(dict) --* 
        
                      Represents information about the output of an action.
        
                      - **name** *(string) --* **[REQUIRED]** 
        
                        The name of the output of an artifact, such as \"My App\".
        
                        The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
        
                        Output artifact names must be unique within a pipeline.
        
                  - **inputArtifacts** *(list) --* 
        
                    The name or ID of the artifact consumed by the action, such as a test or build artifact.
        
                    - *(dict) --* 
        
                      Represents information about an artifact to be worked on, such as a test or build artifact.
        
                      - **name** *(string) --* **[REQUIRED]** 
        
                        The name of the artifact to be worked on, for example, \"My App\".
        
                        The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
        
                  - **roleArn** *(string) --* 
        
                    The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.
        
                  - **region** *(string) --* 
        
                    The action declaration\'s AWS Region, such as us-east-1.
        
          - **version** *(integer) --* 
        
            The version number of the pipeline. A new pipeline always has a version number of 1. This number is automatically incremented when a pipeline is updated.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'pipeline\': {
                    \'name\': \'string\',
                    \'roleArn\': \'string\',
                    \'artifactStore\': {
                        \'type\': \'S3\',
                        \'location\': \'string\',
                        \'encryptionKey\': {
                            \'id\': \'string\',
                            \'type\': \'KMS\'
                        }
                    },
                    \'artifactStores\': {
                        \'string\': {
                            \'type\': \'S3\',
                            \'location\': \'string\',
                            \'encryptionKey\': {
                                \'id\': \'string\',
                                \'type\': \'KMS\'
                            }
                        }
                    },
                    \'stages\': [
                        {
                            \'name\': \'string\',
                            \'blockers\': [
                                {
                                    \'name\': \'string\',
                                    \'type\': \'Schedule\'
                                },
                            ],
                            \'actions\': [
                                {
                                    \'name\': \'string\',
                                    \'actionTypeId\': {
                                        \'category\': \'Source\'|\'Build\'|\'Deploy\'|\'Test\'|\'Invoke\'|\'Approval\',
                                        \'owner\': \'AWS\'|\'ThirdParty\'|\'Custom\',
                                        \'provider\': \'string\',
                                        \'version\': \'string\'
                                    },
                                    \'runOrder\': 123,
                                    \'configuration\': {
                                        \'string\': \'string\'
                                    },
                                    \'outputArtifacts\': [
                                        {
                                            \'name\': \'string\'
                                        },
                                    ],
                                    \'inputArtifacts\': [
                                        {
                                            \'name\': \'string\'
                                        },
                                    ],
                                    \'roleArn\': \'string\',
                                    \'region\': \'string\'
                                },
                            ]
                        },
                    ],
                    \'version\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a CreatePipeline action.
        
            - **pipeline** *(dict) --* 
        
              Represents the structure of actions and stages to be performed in the pipeline. 
        
              - **name** *(string) --* 
        
                The name of the action to be performed.
        
              - **roleArn** *(string) --* 
        
                The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with no actionRoleArn, or to use to assume roles for actions with an actionRoleArn.
        
              - **artifactStore** *(dict) --* 
        
                Represents information about the Amazon S3 bucket where artifacts are stored for the pipeline. 
        
                - **type** *(string) --* 
        
                  The type of the artifact store, such as S3.
        
                - **location** *(string) --* 
        
                  The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder within the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any Amazon S3 bucket in the same AWS Region as the pipeline to store your pipeline artifacts.
        
                - **encryptionKey** *(dict) --* 
        
                  The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.
        
                  - **id** *(string) --* 
        
                    The ID used to identify the key. For an AWS KMS key, this is the key ID or key ARN.
        
                  - **type** *(string) --* 
        
                    The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.
        
              - **artifactStores** *(dict) --* 
        
                A mapping of artifactStore objects and their corresponding regions. There must be an artifact store for the pipeline region and for each cross-region action within the pipeline. You can only use either artifactStore or artifactStores, not both.
        
                If you create a cross-region action in your pipeline, you must use artifactStores.
        
                - *(string) --* 
                  
                  - *(dict) --* 
        
                    The Amazon S3 bucket where artifacts are stored for the pipeline.
        
                    - **type** *(string) --* 
        
                      The type of the artifact store, such as S3.
        
                    - **location** *(string) --* 
        
                      The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder within the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any Amazon S3 bucket in the same AWS Region as the pipeline to store your pipeline artifacts.
        
                    - **encryptionKey** *(dict) --* 
        
                      The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.
        
                      - **id** *(string) --* 
        
                        The ID used to identify the key. For an AWS KMS key, this is the key ID or key ARN.
        
                      - **type** *(string) --* 
        
                        The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.
        
              - **stages** *(list) --* 
        
                The stage in which to perform the action.
        
                - *(dict) --* 
        
                  Represents information about a stage and its definition.
        
                  - **name** *(string) --* 
        
                    The name of the stage.
        
                  - **blockers** *(list) --* 
        
                    Reserved for future use.
        
                    - *(dict) --* 
        
                      Reserved for future use.
        
                      - **name** *(string) --* 
        
                        Reserved for future use.
        
                      - **type** *(string) --* 
        
                        Reserved for future use.
        
                  - **actions** *(list) --* 
        
                    The actions included in a stage.
        
                    - *(dict) --* 
        
                      Represents information about an action declaration.
        
                      - **name** *(string) --* 
        
                        The action declaration\'s name.
        
                      - **actionTypeId** *(dict) --* 
        
                        The configuration information for the action type.
        
                        - **category** *(string) --* 
        
                          A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
        
                        - **owner** *(string) --* 
        
                          The creator of the action being called.
        
                        - **provider** *(string) --* 
        
                          The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
        
                        - **version** *(string) --* 
        
                          A string that describes the action version.
        
                      - **runOrder** *(integer) --* 
        
                        The order in which actions are run.
        
                      - **configuration** *(dict) --* 
        
                        The action declaration\'s configuration.
        
                        - *(string) --* 
                          
                          - *(string) --* 
                    
                      - **outputArtifacts** *(list) --* 
        
                        The name or ID of the result of the action declaration, such as a test or build artifact.
        
                        - *(dict) --* 
        
                          Represents information about the output of an action.
        
                          - **name** *(string) --* 
        
                            The name of the output of an artifact, such as \"My App\".
        
                            The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
        
                            Output artifact names must be unique within a pipeline.
        
                      - **inputArtifacts** *(list) --* 
        
                        The name or ID of the artifact consumed by the action, such as a test or build artifact.
        
                        - *(dict) --* 
        
                          Represents information about an artifact to be worked on, such as a test or build artifact.
        
                          - **name** *(string) --* 
        
                            The name of the artifact to be worked on, for example, \"My App\".
        
                            The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
        
                      - **roleArn** *(string) --* 
        
                        The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.
        
                      - **region** *(string) --* 
        
                        The action declaration\'s AWS Region, such as us-east-1.
        
              - **version** *(integer) --* 
        
                The version number of the pipeline. A new pipeline always has a version number of 1. This number is automatically incremented when a pipeline is updated.
        
        """
        pass

    def delete_custom_action_type(self, category: str, provider: str, version: str) -> NoReturn:
        """
        
        .. warning::
        
          To re-create a custom action after it has been deleted you must use a string in the version field that has never been used before. This string can be an incremented version number, for example. To restore a deleted custom action, use a JSON file that is identical to the deleted action, including the original string in the version field.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/DeleteCustomActionType>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_custom_action_type(
              category=\'Source\'|\'Build\'|\'Deploy\'|\'Test\'|\'Invoke\'|\'Approval\',
              provider=\'string\',
              version=\'string\'
          )
        :type category: string
        :param category: **[REQUIRED]** 
        
          The category of the custom action that you want to delete, such as source or deploy.
        
        :type provider: string
        :param provider: **[REQUIRED]** 
        
          The provider of the service used in the custom action, such as AWS CodeDeploy.
        
        :type version: string
        :param version: **[REQUIRED]** 
        
          The version of the custom action to delete.
        
        :returns: None
        """
        pass

    def delete_pipeline(self, name: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/DeletePipeline>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_pipeline(
              name=\'string\'
          )
        :type name: string
        :param name: **[REQUIRED]** 
        
          The name of the pipeline to be deleted.
        
        :returns: None
        """
        pass

    def delete_webhook(self, name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/DeleteWebhook>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_webhook(
              name=\'string\'
          )
        :type name: string
        :param name: **[REQUIRED]** 
        
          The name of the webhook you want to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def deregister_webhook_with_third_party(self, webhookName: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/DeregisterWebhookWithThirdParty>`_
        
        **Request Syntax** 
        ::
        
          response = client.deregister_webhook_with_third_party(
              webhookName=\'string\'
          )
        :type webhookName: string
        :param webhookName: 
        
          The name of the webhook you want to deregister.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def disable_stage_transition(self, pipelineName: str, stageName: str, transitionType: str, reason: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/DisableStageTransition>`_
        
        **Request Syntax** 
        ::
        
          response = client.disable_stage_transition(
              pipelineName=\'string\',
              stageName=\'string\',
              transitionType=\'Inbound\'|\'Outbound\',
              reason=\'string\'
          )
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]** 
        
          The name of the pipeline in which you want to disable the flow of artifacts from one stage to another.
        
        :type stageName: string
        :param stageName: **[REQUIRED]** 
        
          The name of the stage where you want to disable the inbound or outbound transition of artifacts.
        
        :type transitionType: string
        :param transitionType: **[REQUIRED]** 
        
          Specifies whether artifacts will be prevented from transitioning into the stage and being processed by the actions in that stage (inbound), or prevented from transitioning from the stage after they have been processed by the actions in that stage (outbound).
        
        :type reason: string
        :param reason: **[REQUIRED]** 
        
          The reason given to the user why a stage is disabled, such as waiting for manual approval or manual tests. This message is displayed in the pipeline console UI.
        
        :returns: None
        """
        pass

    def enable_stage_transition(self, pipelineName: str, stageName: str, transitionType: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/EnableStageTransition>`_
        
        **Request Syntax** 
        ::
        
          response = client.enable_stage_transition(
              pipelineName=\'string\',
              stageName=\'string\',
              transitionType=\'Inbound\'|\'Outbound\'
          )
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]** 
        
          The name of the pipeline in which you want to enable the flow of artifacts from one stage to another.
        
        :type stageName: string
        :param stageName: **[REQUIRED]** 
        
          The name of the stage where you want to enable the transition of artifacts, either into the stage (inbound) or from that stage to the next stage (outbound).
        
        :type transitionType: string
        :param transitionType: **[REQUIRED]** 
        
          Specifies whether artifacts will be allowed to enter the stage and be processed by the actions in that stage (inbound) or whether already-processed artifacts will be allowed to transition to the next stage (outbound).
        
        :returns: None
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

    def get_job_details(self, jobId: str) -> Dict:
        """
        
        .. warning::
        
          When this API is called, AWS CodePipeline returns temporary credentials for the Amazon S3 bucket used to store artifacts for the pipeline, if the action requires access to that Amazon S3 bucket for input or output artifacts. Additionally, this API returns any secret values defined for the action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/GetJobDetails>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_job_details(
              jobId=\'string\'
          )
        :type jobId: string
        :param jobId: **[REQUIRED]** 
        
          The unique system-generated ID for the job.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'jobDetails\': {
                    \'id\': \'string\',
                    \'data\': {
                        \'actionTypeId\': {
                            \'category\': \'Source\'|\'Build\'|\'Deploy\'|\'Test\'|\'Invoke\'|\'Approval\',
                            \'owner\': \'AWS\'|\'ThirdParty\'|\'Custom\',
                            \'provider\': \'string\',
                            \'version\': \'string\'
                        },
                        \'actionConfiguration\': {
                            \'configuration\': {
                                \'string\': \'string\'
                            }
                        },
                        \'pipelineContext\': {
                            \'pipelineName\': \'string\',
                            \'stage\': {
                                \'name\': \'string\'
                            },
                            \'action\': {
                                \'name\': \'string\'
                            }
                        },
                        \'inputArtifacts\': [
                            {
                                \'name\': \'string\',
                                \'revision\': \'string\',
                                \'location\': {
                                    \'type\': \'S3\',
                                    \'s3Location\': {
                                        \'bucketName\': \'string\',
                                        \'objectKey\': \'string\'
                                    }
                                }
                            },
                        ],
                        \'outputArtifacts\': [
                            {
                                \'name\': \'string\',
                                \'revision\': \'string\',
                                \'location\': {
                                    \'type\': \'S3\',
                                    \'s3Location\': {
                                        \'bucketName\': \'string\',
                                        \'objectKey\': \'string\'
                                    }
                                }
                            },
                        ],
                        \'artifactCredentials\': {
                            \'accessKeyId\': \'string\',
                            \'secretAccessKey\': \'string\',
                            \'sessionToken\': \'string\'
                        },
                        \'continuationToken\': \'string\',
                        \'encryptionKey\': {
                            \'id\': \'string\',
                            \'type\': \'KMS\'
                        }
                    },
                    \'accountId\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a GetJobDetails action.
        
            - **jobDetails** *(dict) --* 
        
              The details of the job.
        
              .. note::
        
                If AWSSessionCredentials is used, a long-running job can call GetJobDetails again to obtain new credentials.
        
              - **id** *(string) --* 
        
                The unique system-generated ID of the job.
        
              - **data** *(dict) --* 
        
                Represents additional information about a job required for a job worker to complete the job. 
        
                - **actionTypeId** *(dict) --* 
        
                  Represents information about an action type.
        
                  - **category** *(string) --* 
        
                    A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
        
                  - **owner** *(string) --* 
        
                    The creator of the action being called.
        
                  - **provider** *(string) --* 
        
                    The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
        
                  - **version** *(string) --* 
        
                    A string that describes the action version.
        
                - **actionConfiguration** *(dict) --* 
        
                  Represents information about an action configuration.
        
                  - **configuration** *(dict) --* 
        
                    The configuration data for the action.
        
                    - *(string) --* 
                      
                      - *(string) --* 
                
                - **pipelineContext** *(dict) --* 
        
                  Represents information about a pipeline to a job worker.
        
                  - **pipelineName** *(string) --* 
        
                    The name of the pipeline. This is a user-specified value. Pipeline names must be unique across all pipeline names under an Amazon Web Services account.
        
                  - **stage** *(dict) --* 
        
                    The stage of the pipeline.
        
                    - **name** *(string) --* 
        
                      The name of the stage.
        
                  - **action** *(dict) --* 
        
                    The context of an action to a job worker within the stage of a pipeline.
        
                    - **name** *(string) --* 
        
                      The name of the action within the context of a job.
        
                - **inputArtifacts** *(list) --* 
        
                  The artifact supplied to the job.
        
                  - *(dict) --* 
        
                    Represents information about an artifact that will be worked upon by actions in the pipeline.
        
                    - **name** *(string) --* 
        
                      The artifact\'s name.
        
                    - **revision** *(string) --* 
        
                      The artifact\'s revision ID. Depending on the type of object, this could be a commit ID (GitHub) or a revision ID (Amazon S3).
        
                    - **location** *(dict) --* 
        
                      The location of an artifact.
        
                      - **type** *(string) --* 
        
                        The type of artifact in the location.
        
                      - **s3Location** *(dict) --* 
        
                        The Amazon S3 bucket that contains the artifact.
        
                        - **bucketName** *(string) --* 
        
                          The name of the Amazon S3 bucket.
        
                        - **objectKey** *(string) --* 
        
                          The key of the object in the Amazon S3 bucket, which uniquely identifies the object in the bucket.
        
                - **outputArtifacts** *(list) --* 
        
                  The output of the job.
        
                  - *(dict) --* 
        
                    Represents information about an artifact that will be worked upon by actions in the pipeline.
        
                    - **name** *(string) --* 
        
                      The artifact\'s name.
        
                    - **revision** *(string) --* 
        
                      The artifact\'s revision ID. Depending on the type of object, this could be a commit ID (GitHub) or a revision ID (Amazon S3).
        
                    - **location** *(dict) --* 
        
                      The location of an artifact.
        
                      - **type** *(string) --* 
        
                        The type of artifact in the location.
        
                      - **s3Location** *(dict) --* 
        
                        The Amazon S3 bucket that contains the artifact.
        
                        - **bucketName** *(string) --* 
        
                          The name of the Amazon S3 bucket.
        
                        - **objectKey** *(string) --* 
        
                          The key of the object in the Amazon S3 bucket, which uniquely identifies the object in the bucket.
        
                - **artifactCredentials** *(dict) --* 
        
                  Represents an AWS session credentials object. These credentials are temporary credentials that are issued by AWS Secure Token Service (STS). They can be used to access input and output artifacts in the Amazon S3 bucket used to store artifact for the pipeline in AWS CodePipeline.
        
                  - **accessKeyId** *(string) --* 
        
                    The access key for the session.
        
                  - **secretAccessKey** *(string) --* 
        
                    The secret access key for the session.
        
                  - **sessionToken** *(string) --* 
        
                    The token for the session.
        
                - **continuationToken** *(string) --* 
        
                  A system-generated token, such as a AWS CodeDeploy deployment ID, that a job requires in order to continue the job asynchronously.
        
                - **encryptionKey** *(dict) --* 
        
                  Represents information about the key used to encrypt data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. 
        
                  - **id** *(string) --* 
        
                    The ID used to identify the key. For an AWS KMS key, this is the key ID or key ARN.
        
                  - **type** *(string) --* 
        
                    The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.
        
              - **accountId** *(string) --* 
        
                The AWS account ID associated with the job.
        
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

    def get_pipeline(self, name: str, version: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/GetPipeline>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_pipeline(
              name=\'string\',
              version=123
          )
        :type name: string
        :param name: **[REQUIRED]** 
        
          The name of the pipeline for which you want to get information. Pipeline names must be unique under an Amazon Web Services (AWS) user account.
        
        :type version: integer
        :param version: 
        
          The version number of the pipeline. If you do not specify a version, defaults to the most current version.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'pipeline\': {
                    \'name\': \'string\',
                    \'roleArn\': \'string\',
                    \'artifactStore\': {
                        \'type\': \'S3\',
                        \'location\': \'string\',
                        \'encryptionKey\': {
                            \'id\': \'string\',
                            \'type\': \'KMS\'
                        }
                    },
                    \'artifactStores\': {
                        \'string\': {
                            \'type\': \'S3\',
                            \'location\': \'string\',
                            \'encryptionKey\': {
                                \'id\': \'string\',
                                \'type\': \'KMS\'
                            }
                        }
                    },
                    \'stages\': [
                        {
                            \'name\': \'string\',
                            \'blockers\': [
                                {
                                    \'name\': \'string\',
                                    \'type\': \'Schedule\'
                                },
                            ],
                            \'actions\': [
                                {
                                    \'name\': \'string\',
                                    \'actionTypeId\': {
                                        \'category\': \'Source\'|\'Build\'|\'Deploy\'|\'Test\'|\'Invoke\'|\'Approval\',
                                        \'owner\': \'AWS\'|\'ThirdParty\'|\'Custom\',
                                        \'provider\': \'string\',
                                        \'version\': \'string\'
                                    },
                                    \'runOrder\': 123,
                                    \'configuration\': {
                                        \'string\': \'string\'
                                    },
                                    \'outputArtifacts\': [
                                        {
                                            \'name\': \'string\'
                                        },
                                    ],
                                    \'inputArtifacts\': [
                                        {
                                            \'name\': \'string\'
                                        },
                                    ],
                                    \'roleArn\': \'string\',
                                    \'region\': \'string\'
                                },
                            ]
                        },
                    ],
                    \'version\': 123
                },
                \'metadata\': {
                    \'pipelineArn\': \'string\',
                    \'created\': datetime(2015, 1, 1),
                    \'updated\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a GetPipeline action.
        
            - **pipeline** *(dict) --* 
        
              Represents the structure of actions and stages to be performed in the pipeline. 
        
              - **name** *(string) --* 
        
                The name of the action to be performed.
        
              - **roleArn** *(string) --* 
        
                The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with no actionRoleArn, or to use to assume roles for actions with an actionRoleArn.
        
              - **artifactStore** *(dict) --* 
        
                Represents information about the Amazon S3 bucket where artifacts are stored for the pipeline. 
        
                - **type** *(string) --* 
        
                  The type of the artifact store, such as S3.
        
                - **location** *(string) --* 
        
                  The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder within the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any Amazon S3 bucket in the same AWS Region as the pipeline to store your pipeline artifacts.
        
                - **encryptionKey** *(dict) --* 
        
                  The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.
        
                  - **id** *(string) --* 
        
                    The ID used to identify the key. For an AWS KMS key, this is the key ID or key ARN.
        
                  - **type** *(string) --* 
        
                    The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.
        
              - **artifactStores** *(dict) --* 
        
                A mapping of artifactStore objects and their corresponding regions. There must be an artifact store for the pipeline region and for each cross-region action within the pipeline. You can only use either artifactStore or artifactStores, not both.
        
                If you create a cross-region action in your pipeline, you must use artifactStores.
        
                - *(string) --* 
                  
                  - *(dict) --* 
        
                    The Amazon S3 bucket where artifacts are stored for the pipeline.
        
                    - **type** *(string) --* 
        
                      The type of the artifact store, such as S3.
        
                    - **location** *(string) --* 
        
                      The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder within the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any Amazon S3 bucket in the same AWS Region as the pipeline to store your pipeline artifacts.
        
                    - **encryptionKey** *(dict) --* 
        
                      The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.
        
                      - **id** *(string) --* 
        
                        The ID used to identify the key. For an AWS KMS key, this is the key ID or key ARN.
        
                      - **type** *(string) --* 
        
                        The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.
        
              - **stages** *(list) --* 
        
                The stage in which to perform the action.
        
                - *(dict) --* 
        
                  Represents information about a stage and its definition.
        
                  - **name** *(string) --* 
        
                    The name of the stage.
        
                  - **blockers** *(list) --* 
        
                    Reserved for future use.
        
                    - *(dict) --* 
        
                      Reserved for future use.
        
                      - **name** *(string) --* 
        
                        Reserved for future use.
        
                      - **type** *(string) --* 
        
                        Reserved for future use.
        
                  - **actions** *(list) --* 
        
                    The actions included in a stage.
        
                    - *(dict) --* 
        
                      Represents information about an action declaration.
        
                      - **name** *(string) --* 
        
                        The action declaration\'s name.
        
                      - **actionTypeId** *(dict) --* 
        
                        The configuration information for the action type.
        
                        - **category** *(string) --* 
        
                          A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
        
                        - **owner** *(string) --* 
        
                          The creator of the action being called.
        
                        - **provider** *(string) --* 
        
                          The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
        
                        - **version** *(string) --* 
        
                          A string that describes the action version.
        
                      - **runOrder** *(integer) --* 
        
                        The order in which actions are run.
        
                      - **configuration** *(dict) --* 
        
                        The action declaration\'s configuration.
        
                        - *(string) --* 
                          
                          - *(string) --* 
                    
                      - **outputArtifacts** *(list) --* 
        
                        The name or ID of the result of the action declaration, such as a test or build artifact.
        
                        - *(dict) --* 
        
                          Represents information about the output of an action.
        
                          - **name** *(string) --* 
        
                            The name of the output of an artifact, such as \"My App\".
        
                            The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
        
                            Output artifact names must be unique within a pipeline.
        
                      - **inputArtifacts** *(list) --* 
        
                        The name or ID of the artifact consumed by the action, such as a test or build artifact.
        
                        - *(dict) --* 
        
                          Represents information about an artifact to be worked on, such as a test or build artifact.
        
                          - **name** *(string) --* 
        
                            The name of the artifact to be worked on, for example, \"My App\".
        
                            The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
        
                      - **roleArn** *(string) --* 
        
                        The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.
        
                      - **region** *(string) --* 
        
                        The action declaration\'s AWS Region, such as us-east-1.
        
              - **version** *(integer) --* 
        
                The version number of the pipeline. A new pipeline always has a version number of 1. This number is automatically incremented when a pipeline is updated.
        
            - **metadata** *(dict) --* 
        
              Represents the pipeline metadata information returned as part of the output of a GetPipeline action.
        
              - **pipelineArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the pipeline.
        
              - **created** *(datetime) --* 
        
                The date and time the pipeline was created, in timestamp format.
        
              - **updated** *(datetime) --* 
        
                The date and time the pipeline was last updated, in timestamp format.
        
        """
        pass

    def get_pipeline_execution(self, pipelineName: str, pipelineExecutionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/GetPipelineExecution>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_pipeline_execution(
              pipelineName=\'string\',
              pipelineExecutionId=\'string\'
          )
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]** 
        
          The name of the pipeline about which you want to get execution details.
        
        :type pipelineExecutionId: string
        :param pipelineExecutionId: **[REQUIRED]** 
        
          The ID of the pipeline execution about which you want to get execution details.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'pipelineExecution\': {
                    \'pipelineName\': \'string\',
                    \'pipelineVersion\': 123,
                    \'pipelineExecutionId\': \'string\',
                    \'status\': \'InProgress\'|\'Succeeded\'|\'Superseded\'|\'Failed\',
                    \'artifactRevisions\': [
                        {
                            \'name\': \'string\',
                            \'revisionId\': \'string\',
                            \'revisionChangeIdentifier\': \'string\',
                            \'revisionSummary\': \'string\',
                            \'created\': datetime(2015, 1, 1),
                            \'revisionUrl\': \'string\'
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a GetPipelineExecution action.
        
            - **pipelineExecution** *(dict) --* 
        
              Represents information about the execution of a pipeline.
        
              - **pipelineName** *(string) --* 
        
                The name of the pipeline that was executed.
        
              - **pipelineVersion** *(integer) --* 
        
                The version number of the pipeline that was executed.
        
              - **pipelineExecutionId** *(string) --* 
        
                The ID of the pipeline execution.
        
              - **status** *(string) --* 
        
                The status of the pipeline execution.
        
                * InProgress: The pipeline execution is currently running. 
                 
                * Succeeded: The pipeline execution was completed successfully.  
                 
                * Superseded: While this pipeline execution was waiting for the next stage to be completed, a newer pipeline execution advanced and continued through the pipeline instead.  
                 
                * Failed: The pipeline execution was not completed successfully. 
                 
              - **artifactRevisions** *(list) --* 
        
                A list of ArtifactRevision objects included in a pipeline execution.
        
                - *(dict) --* 
        
                  Represents revision details of an artifact. 
        
                  - **name** *(string) --* 
        
                    The name of an artifact. This name might be system-generated, such as \"MyApp\", or might be defined by the user when an action is created.
        
                  - **revisionId** *(string) --* 
        
                    The revision ID of the artifact.
        
                  - **revisionChangeIdentifier** *(string) --* 
        
                    An additional identifier for a revision, such as a commit date or, for artifacts stored in Amazon S3 buckets, the ETag value.
        
                  - **revisionSummary** *(string) --* 
        
                    Summary information about the most recent revision of the artifact. For GitHub and AWS CodeCommit repositories, the commit message. For Amazon S3 buckets or actions, the user-provided content of a ``codepipeline-artifact-revision-summary`` key specified in the object metadata.
        
                  - **created** *(datetime) --* 
        
                    The date and time when the most recent revision of the artifact was created, in timestamp format.
        
                  - **revisionUrl** *(string) --* 
        
                    The commit ID for the artifact revision. For artifacts stored in GitHub or AWS CodeCommit repositories, the commit ID is linked to a commit details page.
        
        """
        pass

    def get_pipeline_state(self, name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/GetPipelineState>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_pipeline_state(
              name=\'string\'
          )
        :type name: string
        :param name: **[REQUIRED]** 
        
          The name of the pipeline about which you want to get information.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'pipelineName\': \'string\',
                \'pipelineVersion\': 123,
                \'stageStates\': [
                    {
                        \'stageName\': \'string\',
                        \'inboundTransitionState\': {
                            \'enabled\': True|False,
                            \'lastChangedBy\': \'string\',
                            \'lastChangedAt\': datetime(2015, 1, 1),
                            \'disabledReason\': \'string\'
                        },
                        \'actionStates\': [
                            {
                                \'actionName\': \'string\',
                                \'currentRevision\': {
                                    \'revisionId\': \'string\',
                                    \'revisionChangeId\': \'string\',
                                    \'created\': datetime(2015, 1, 1)
                                },
                                \'latestExecution\': {
                                    \'status\': \'InProgress\'|\'Succeeded\'|\'Failed\',
                                    \'summary\': \'string\',
                                    \'lastStatusChange\': datetime(2015, 1, 1),
                                    \'token\': \'string\',
                                    \'lastUpdatedBy\': \'string\',
                                    \'externalExecutionId\': \'string\',
                                    \'externalExecutionUrl\': \'string\',
                                    \'percentComplete\': 123,
                                    \'errorDetails\': {
                                        \'code\': \'string\',
                                        \'message\': \'string\'
                                    }
                                },
                                \'entityUrl\': \'string\',
                                \'revisionUrl\': \'string\'
                            },
                        ],
                        \'latestExecution\': {
                            \'pipelineExecutionId\': \'string\',
                            \'status\': \'InProgress\'|\'Failed\'|\'Succeeded\'
                        }
                    },
                ],
                \'created\': datetime(2015, 1, 1),
                \'updated\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a GetPipelineState action.
        
            - **pipelineName** *(string) --* 
        
              The name of the pipeline for which you want to get the state.
        
            - **pipelineVersion** *(integer) --* 
        
              The version number of the pipeline.
        
              .. note::
        
                A newly-created pipeline is always assigned a version number of ``1`` .
        
            - **stageStates** *(list) --* 
        
              A list of the pipeline stage output information, including stage name, state, most recent run details, whether the stage is disabled, and other data.
        
              - *(dict) --* 
        
                Represents information about the state of the stage.
        
                - **stageName** *(string) --* 
        
                  The name of the stage.
        
                - **inboundTransitionState** *(dict) --* 
        
                  The state of the inbound transition, which is either enabled or disabled.
        
                  - **enabled** *(boolean) --* 
        
                    Whether the transition between stages is enabled (true) or disabled (false).
        
                  - **lastChangedBy** *(string) --* 
        
                    The ID of the user who last changed the transition state.
        
                  - **lastChangedAt** *(datetime) --* 
        
                    The timestamp when the transition state was last changed.
        
                  - **disabledReason** *(string) --* 
        
                    The user-specified reason why the transition between two stages of a pipeline was disabled.
        
                - **actionStates** *(list) --* 
        
                  The state of the stage.
        
                  - *(dict) --* 
        
                    Represents information about the state of an action.
        
                    - **actionName** *(string) --* 
        
                      The name of the action.
        
                    - **currentRevision** *(dict) --* 
        
                      Represents information about the version (or revision) of an action.
        
                      - **revisionId** *(string) --* 
        
                        The system-generated unique ID that identifies the revision number of the action.
        
                      - **revisionChangeId** *(string) --* 
        
                        The unique identifier of the change that set the state to this revision, for example a deployment ID or timestamp.
        
                      - **created** *(datetime) --* 
        
                        The date and time when the most recent version of the action was created, in timestamp format.
        
                    - **latestExecution** *(dict) --* 
        
                      Represents information about the run of an action.
        
                      - **status** *(string) --* 
        
                        The status of the action, or for a completed action, the last status of the action.
        
                      - **summary** *(string) --* 
        
                        A summary of the run of the action.
        
                      - **lastStatusChange** *(datetime) --* 
        
                        The last status change of the action.
        
                      - **token** *(string) --* 
        
                        The system-generated token used to identify a unique approval request. The token for each open approval request can be obtained using the GetPipelineState command and is used to validate that the approval request corresponding to this token is still valid.
        
                      - **lastUpdatedBy** *(string) --* 
        
                        The ARN of the user who last changed the pipeline.
        
                      - **externalExecutionId** *(string) --* 
        
                        The external ID of the run of the action.
        
                      - **externalExecutionUrl** *(string) --* 
        
                        The URL of a resource external to AWS that will be used when running the action, for example an external repository URL.
        
                      - **percentComplete** *(integer) --* 
        
                        A percentage of completeness of the action as it runs.
        
                      - **errorDetails** *(dict) --* 
        
                        The details of an error returned by a URL external to AWS.
        
                        - **code** *(string) --* 
        
                          The system ID or error number code of the error.
        
                        - **message** *(string) --* 
        
                          The text of the error message.
        
                    - **entityUrl** *(string) --* 
        
                      A URL link for more information about the state of the action, such as a deployment group details page.
        
                    - **revisionUrl** *(string) --* 
        
                      A URL link for more information about the revision, such as a commit details page.
        
                - **latestExecution** *(dict) --* 
        
                  Information about the latest execution in the stage, including its ID and status.
        
                  - **pipelineExecutionId** *(string) --* 
        
                    The ID of the pipeline execution associated with the stage.
        
                  - **status** *(string) --* 
        
                    The status of the stage, or for a completed stage, the last status of the stage.
        
            - **created** *(datetime) --* 
        
              The date and time the pipeline was created, in timestamp format.
        
            - **updated** *(datetime) --* 
        
              The date and time the pipeline was last updated, in timestamp format.
        
        """
        pass

    def get_third_party_job_details(self, jobId: str, clientToken: str) -> Dict:
        """
        
        .. warning::
        
          When this API is called, AWS CodePipeline returns temporary credentials for the Amazon S3 bucket used to store artifacts for the pipeline, if the action requires access to that Amazon S3 bucket for input or output artifacts. Additionally, this API returns any secret values defined for the action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/GetThirdPartyJobDetails>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_third_party_job_details(
              jobId=\'string\',
              clientToken=\'string\'
          )
        :type jobId: string
        :param jobId: **[REQUIRED]** 
        
          The unique system-generated ID used for identifying the job.
        
        :type clientToken: string
        :param clientToken: **[REQUIRED]** 
        
          The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'jobDetails\': {
                    \'id\': \'string\',
                    \'data\': {
                        \'actionTypeId\': {
                            \'category\': \'Source\'|\'Build\'|\'Deploy\'|\'Test\'|\'Invoke\'|\'Approval\',
                            \'owner\': \'AWS\'|\'ThirdParty\'|\'Custom\',
                            \'provider\': \'string\',
                            \'version\': \'string\'
                        },
                        \'actionConfiguration\': {
                            \'configuration\': {
                                \'string\': \'string\'
                            }
                        },
                        \'pipelineContext\': {
                            \'pipelineName\': \'string\',
                            \'stage\': {
                                \'name\': \'string\'
                            },
                            \'action\': {
                                \'name\': \'string\'
                            }
                        },
                        \'inputArtifacts\': [
                            {
                                \'name\': \'string\',
                                \'revision\': \'string\',
                                \'location\': {
                                    \'type\': \'S3\',
                                    \'s3Location\': {
                                        \'bucketName\': \'string\',
                                        \'objectKey\': \'string\'
                                    }
                                }
                            },
                        ],
                        \'outputArtifacts\': [
                            {
                                \'name\': \'string\',
                                \'revision\': \'string\',
                                \'location\': {
                                    \'type\': \'S3\',
                                    \'s3Location\': {
                                        \'bucketName\': \'string\',
                                        \'objectKey\': \'string\'
                                    }
                                }
                            },
                        ],
                        \'artifactCredentials\': {
                            \'accessKeyId\': \'string\',
                            \'secretAccessKey\': \'string\',
                            \'sessionToken\': \'string\'
                        },
                        \'continuationToken\': \'string\',
                        \'encryptionKey\': {
                            \'id\': \'string\',
                            \'type\': \'KMS\'
                        }
                    },
                    \'nonce\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a GetThirdPartyJobDetails action.
        
            - **jobDetails** *(dict) --* 
        
              The details of the job, including any protected values defined for the job.
        
              - **id** *(string) --* 
        
                The identifier used to identify the job details in AWS CodePipeline.
        
              - **data** *(dict) --* 
        
                The data to be returned by the third party job worker.
        
                - **actionTypeId** *(dict) --* 
        
                  Represents information about an action type.
        
                  - **category** *(string) --* 
        
                    A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
        
                  - **owner** *(string) --* 
        
                    The creator of the action being called.
        
                  - **provider** *(string) --* 
        
                    The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
        
                  - **version** *(string) --* 
        
                    A string that describes the action version.
        
                - **actionConfiguration** *(dict) --* 
        
                  Represents information about an action configuration.
        
                  - **configuration** *(dict) --* 
        
                    The configuration data for the action.
        
                    - *(string) --* 
                      
                      - *(string) --* 
                
                - **pipelineContext** *(dict) --* 
        
                  Represents information about a pipeline to a job worker.
        
                  - **pipelineName** *(string) --* 
        
                    The name of the pipeline. This is a user-specified value. Pipeline names must be unique across all pipeline names under an Amazon Web Services account.
        
                  - **stage** *(dict) --* 
        
                    The stage of the pipeline.
        
                    - **name** *(string) --* 
        
                      The name of the stage.
        
                  - **action** *(dict) --* 
        
                    The context of an action to a job worker within the stage of a pipeline.
        
                    - **name** *(string) --* 
        
                      The name of the action within the context of a job.
        
                - **inputArtifacts** *(list) --* 
        
                  The name of the artifact that will be worked upon by the action, if any. This name might be system-generated, such as \"MyApp\", or might be defined by the user when the action is created. The input artifact name must match the name of an output artifact generated by an action in an earlier action or stage of the pipeline.
        
                  - *(dict) --* 
        
                    Represents information about an artifact that will be worked upon by actions in the pipeline.
        
                    - **name** *(string) --* 
        
                      The artifact\'s name.
        
                    - **revision** *(string) --* 
        
                      The artifact\'s revision ID. Depending on the type of object, this could be a commit ID (GitHub) or a revision ID (Amazon S3).
        
                    - **location** *(dict) --* 
        
                      The location of an artifact.
        
                      - **type** *(string) --* 
        
                        The type of artifact in the location.
        
                      - **s3Location** *(dict) --* 
        
                        The Amazon S3 bucket that contains the artifact.
        
                        - **bucketName** *(string) --* 
        
                          The name of the Amazon S3 bucket.
        
                        - **objectKey** *(string) --* 
        
                          The key of the object in the Amazon S3 bucket, which uniquely identifies the object in the bucket.
        
                - **outputArtifacts** *(list) --* 
        
                  The name of the artifact that will be the result of the action, if any. This name might be system-generated, such as \"MyBuiltApp\", or might be defined by the user when the action is created.
        
                  - *(dict) --* 
        
                    Represents information about an artifact that will be worked upon by actions in the pipeline.
        
                    - **name** *(string) --* 
        
                      The artifact\'s name.
        
                    - **revision** *(string) --* 
        
                      The artifact\'s revision ID. Depending on the type of object, this could be a commit ID (GitHub) or a revision ID (Amazon S3).
        
                    - **location** *(dict) --* 
        
                      The location of an artifact.
        
                      - **type** *(string) --* 
        
                        The type of artifact in the location.
        
                      - **s3Location** *(dict) --* 
        
                        The Amazon S3 bucket that contains the artifact.
        
                        - **bucketName** *(string) --* 
        
                          The name of the Amazon S3 bucket.
        
                        - **objectKey** *(string) --* 
        
                          The key of the object in the Amazon S3 bucket, which uniquely identifies the object in the bucket.
        
                - **artifactCredentials** *(dict) --* 
        
                  Represents an AWS session credentials object. These credentials are temporary credentials that are issued by AWS Secure Token Service (STS). They can be used to access input and output artifacts in the Amazon S3 bucket used to store artifact for the pipeline in AWS CodePipeline. 
        
                  - **accessKeyId** *(string) --* 
        
                    The access key for the session.
        
                  - **secretAccessKey** *(string) --* 
        
                    The secret access key for the session.
        
                  - **sessionToken** *(string) --* 
        
                    The token for the session.
        
                - **continuationToken** *(string) --* 
        
                  A system-generated token, such as a AWS CodeDeploy deployment ID, that a job requires in order to continue the job asynchronously.
        
                - **encryptionKey** *(dict) --* 
        
                  The encryption key used to encrypt and decrypt data in the artifact store for the pipeline, such as an AWS Key Management Service (AWS KMS) key. This is optional and might not be present.
        
                  - **id** *(string) --* 
        
                    The ID used to identify the key. For an AWS KMS key, this is the key ID or key ARN.
        
                  - **type** *(string) --* 
        
                    The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.
        
              - **nonce** *(string) --* 
        
                A system-generated random number that AWS CodePipeline uses to ensure that the job is being worked on by only one job worker. Use this number in an  AcknowledgeThirdPartyJob request.
        
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

    def list_action_types(self, actionOwnerFilter: str = None, nextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/ListActionTypes>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_action_types(
              actionOwnerFilter=\'AWS\'|\'ThirdParty\'|\'Custom\',
              nextToken=\'string\'
          )
        :type actionOwnerFilter: string
        :param actionOwnerFilter: 
        
          Filters the list of action types to those created by a specified entity.
        
        :type nextToken: string
        :param nextToken: 
        
          An identifier that was returned from the previous list action types call, which can be used to return the next set of action types in the list.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'actionTypes\': [
                    {
                        \'id\': {
                            \'category\': \'Source\'|\'Build\'|\'Deploy\'|\'Test\'|\'Invoke\'|\'Approval\',
                            \'owner\': \'AWS\'|\'ThirdParty\'|\'Custom\',
                            \'provider\': \'string\',
                            \'version\': \'string\'
                        },
                        \'settings\': {
                            \'thirdPartyConfigurationUrl\': \'string\',
                            \'entityUrlTemplate\': \'string\',
                            \'executionUrlTemplate\': \'string\',
                            \'revisionUrlTemplate\': \'string\'
                        },
                        \'actionConfigurationProperties\': [
                            {
                                \'name\': \'string\',
                                \'required\': True|False,
                                \'key\': True|False,
                                \'secret\': True|False,
                                \'queryable\': True|False,
                                \'description\': \'string\',
                                \'type\': \'String\'|\'Number\'|\'Boolean\'
                            },
                        ],
                        \'inputArtifactDetails\': {
                            \'minimumCount\': 123,
                            \'maximumCount\': 123
                        },
                        \'outputArtifactDetails\': {
                            \'minimumCount\': 123,
                            \'maximumCount\': 123
                        }
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ListActionTypes action.
        
            - **actionTypes** *(list) --* 
        
              Provides details of the action types.
        
              - *(dict) --* 
        
                Returns information about the details of an action type.
        
                - **id** *(dict) --* 
        
                  Represents information about an action type.
        
                  - **category** *(string) --* 
        
                    A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
        
                  - **owner** *(string) --* 
        
                    The creator of the action being called.
        
                  - **provider** *(string) --* 
        
                    The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
        
                  - **version** *(string) --* 
        
                    A string that describes the action version.
        
                - **settings** *(dict) --* 
        
                  The settings for the action type.
        
                  - **thirdPartyConfigurationUrl** *(string) --* 
        
                    The URL of a sign-up page where users can sign up for an external service and perform initial configuration of the action provided by that service.
        
                  - **entityUrlTemplate** *(string) --* 
        
                    The URL returned to the AWS CodePipeline console that provides a deep link to the resources of the external system, such as the configuration page for an AWS CodeDeploy deployment group. This link is provided as part of the action display within the pipeline.
        
                  - **executionUrlTemplate** *(string) --* 
        
                    The URL returned to the AWS CodePipeline console that contains a link to the top-level landing page for the external system, such as console page for AWS CodeDeploy. This link is shown on the pipeline view page in the AWS CodePipeline console and provides a link to the execution entity of the external action.
        
                  - **revisionUrlTemplate** *(string) --* 
        
                    The URL returned to the AWS CodePipeline console that contains a link to the page where customers can update or change the configuration of the external action.
        
                - **actionConfigurationProperties** *(list) --* 
        
                  The configuration properties for the action type.
        
                  - *(dict) --* 
        
                    Represents information about an action configuration property.
        
                    - **name** *(string) --* 
        
                      The name of the action configuration property.
        
                    - **required** *(boolean) --* 
        
                      Whether the configuration property is a required value.
        
                    - **key** *(boolean) --* 
        
                      Whether the configuration property is a key.
        
                    - **secret** *(boolean) --* 
        
                      Whether the configuration property is secret. Secrets are hidden from all calls except for GetJobDetails, GetThirdPartyJobDetails, PollForJobs, and PollForThirdPartyJobs.
        
                      When updating a pipeline, passing * * * * * without changing any other values of the action will preserve the prior value of the secret.
        
                    - **queryable** *(boolean) --* 
        
                      Indicates that the property will be used in conjunction with PollForJobs. When creating a custom action, an action can have up to one queryable property. If it has one, that property must be both required and not secret.
        
                      If you create a pipeline with a custom action type, and that custom action contains a queryable property, the value for that configuration property is subject to additional restrictions. The value must be less than or equal to twenty (20) characters. The value can contain only alphanumeric characters, underscores, and hyphens.
        
                    - **description** *(string) --* 
        
                      The description of the action configuration property that will be displayed to users.
        
                    - **type** *(string) --* 
        
                      The type of the configuration property.
        
                - **inputArtifactDetails** *(dict) --* 
        
                  The details of the input artifact for the action, such as its commit ID.
        
                  - **minimumCount** *(integer) --* 
        
                    The minimum number of artifacts allowed for the action type.
        
                  - **maximumCount** *(integer) --* 
        
                    The maximum number of artifacts allowed for the action type.
        
                - **outputArtifactDetails** *(dict) --* 
        
                  The details of the output artifact of the action, such as its commit ID.
        
                  - **minimumCount** *(integer) --* 
        
                    The minimum number of artifacts allowed for the action type.
        
                  - **maximumCount** *(integer) --* 
        
                    The maximum number of artifacts allowed for the action type.
        
            - **nextToken** *(string) --* 
        
              If the amount of returned information is significantly large, an identifier is also returned which can be used in a subsequent list action types call to return the next set of action types in the list.
        
        """
        pass

    def list_pipeline_executions(self, pipelineName: str, maxResults: int = None, nextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/ListPipelineExecutions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_pipeline_executions(
              pipelineName=\'string\',
              maxResults=123,
              nextToken=\'string\'
          )
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]** 
        
          The name of the pipeline for which you want to get execution summary information.
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value. The available pipeline execution history is limited to the most recent 12 months, based on pipeline execution start times. Default value is 100.
        
        :type nextToken: string
        :param nextToken: 
        
          The token that was returned from the previous ListPipelineExecutions call, which can be used to return the next set of pipeline executions in the list.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'pipelineExecutionSummaries\': [
                    {
                        \'pipelineExecutionId\': \'string\',
                        \'status\': \'InProgress\'|\'Succeeded\'|\'Superseded\'|\'Failed\',
                        \'startTime\': datetime(2015, 1, 1),
                        \'lastUpdateTime\': datetime(2015, 1, 1),
                        \'sourceRevisions\': [
                            {
                                \'actionName\': \'string\',
                                \'revisionId\': \'string\',
                                \'revisionSummary\': \'string\',
                                \'revisionUrl\': \'string\'
                            },
                        ]
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ListPipelineExecutions action.
        
            - **pipelineExecutionSummaries** *(list) --* 
        
              A list of executions in the history of a pipeline.
        
              - *(dict) --* 
        
                Summary information about a pipeline execution.
        
                - **pipelineExecutionId** *(string) --* 
        
                  The ID of the pipeline execution.
        
                - **status** *(string) --* 
        
                  The status of the pipeline execution.
        
                  * InProgress: The pipeline execution is currently running. 
                   
                  * Succeeded: The pipeline execution was completed successfully.  
                   
                  * Superseded: While this pipeline execution was waiting for the next stage to be completed, a newer pipeline execution advanced and continued through the pipeline instead.  
                   
                  * Failed: The pipeline execution was not completed successfully. 
                   
                - **startTime** *(datetime) --* 
        
                  The date and time when the pipeline execution began, in timestamp format.
        
                - **lastUpdateTime** *(datetime) --* 
        
                  The date and time of the last change to the pipeline execution, in timestamp format.
        
                - **sourceRevisions** *(list) --* 
        
                  A list of the source artifact revisions that initiated a pipeline execution.
        
                  - *(dict) --* 
        
                    Information about the version (or revision) of a source artifact that initiated a pipeline execution.
        
                    - **actionName** *(string) --* 
        
                      The name of the action that processed the revision to the source artifact.
        
                    - **revisionId** *(string) --* 
        
                      The system-generated unique ID that identifies the revision number of the artifact.
        
                    - **revisionSummary** *(string) --* 
        
                      Summary information about the most recent revision of the artifact. For GitHub and AWS CodeCommit repositories, the commit message. For Amazon S3 buckets or actions, the user-provided content of a ``codepipeline-artifact-revision-summary`` key specified in the object metadata.
        
                    - **revisionUrl** *(string) --* 
        
                      The commit ID for the artifact revision. For artifacts stored in GitHub or AWS CodeCommit repositories, the commit ID is linked to a commit details page.
        
            - **nextToken** *(string) --* 
        
              A token that can be used in the next ListPipelineExecutions call. To view all items in the list, continue to call this operation with each subsequent token until no more nextToken values are returned.
        
        """
        pass

    def list_pipelines(self, nextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/ListPipelines>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_pipelines(
              nextToken=\'string\'
          )
        :type nextToken: string
        :param nextToken: 
        
          An identifier that was returned from the previous list pipelines call, which can be used to return the next set of pipelines in the list.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'pipelines\': [
                    {
                        \'name\': \'string\',
                        \'version\': 123,
                        \'created\': datetime(2015, 1, 1),
                        \'updated\': datetime(2015, 1, 1)
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ListPipelines action.
        
            - **pipelines** *(list) --* 
        
              The list of pipelines.
        
              - *(dict) --* 
        
                Returns a summary of a pipeline.
        
                - **name** *(string) --* 
        
                  The name of the pipeline.
        
                - **version** *(integer) --* 
        
                  The version number of the pipeline.
        
                - **created** *(datetime) --* 
        
                  The date and time the pipeline was created, in timestamp format.
        
                - **updated** *(datetime) --* 
        
                  The date and time of the last update to the pipeline, in timestamp format.
        
            - **nextToken** *(string) --* 
        
              If the amount of returned information is significantly large, an identifier is also returned which can be used in a subsequent list pipelines call to return the next set of pipelines in the list.
        
        """
        pass

    def list_webhooks(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/ListWebhooks>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_webhooks(
              NextToken=\'string\',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken: 
        
          The token that was returned from the previous ListWebhooks call, which can be used to return the next set of webhooks in the list.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'webhooks\': [
                    {
                        \'definition\': {
                            \'name\': \'string\',
                            \'targetPipeline\': \'string\',
                            \'targetAction\': \'string\',
                            \'filters\': [
                                {
                                    \'jsonPath\': \'string\',
                                    \'matchEquals\': \'string\'
                                },
                            ],
                            \'authentication\': \'GITHUB_HMAC\'|\'IP\'|\'UNAUTHENTICATED\',
                            \'authenticationConfiguration\': {
                                \'AllowedIPRange\': \'string\',
                                \'SecretToken\': \'string\'
                            }
                        },
                        \'url\': \'string\',
                        \'errorMessage\': \'string\',
                        \'errorCode\': \'string\',
                        \'lastTriggered\': datetime(2015, 1, 1),
                        \'arn\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **webhooks** *(list) --* 
        
              The JSON detail returned for each webhook in the list output for the ListWebhooks call.
        
              - *(dict) --* 
        
                The detail returned for each webhook after listing webhooks, such as the webhook URL, the webhook name, and the webhook ARN.
        
                - **definition** *(dict) --* 
        
                  The detail returned for each webhook, such as the webhook authentication type and filter rules.
        
                  - **name** *(string) --* 
        
                    The name of the webhook.
        
                  - **targetPipeline** *(string) --* 
        
                    The name of the pipeline you want to connect to the webhook.
        
                  - **targetAction** *(string) --* 
        
                    The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.
        
                  - **filters** *(list) --* 
        
                    A list of rules applied to the body/payload sent in the POST request to a webhook URL. All defined rules must pass for the request to be accepted and the pipeline started.
        
                    - *(dict) --* 
        
                      The event criteria that specify when a webhook notification is sent to your URL.
        
                      - **jsonPath** *(string) --* 
        
                        A JsonPath expression that will be applied to the body/payload of the webhook. The value selected by JsonPath expression must match the value specified in the matchEquals field, otherwise the request will be ignored. More information on JsonPath expressions can be found here: https://github.com/json-path/JsonPath.
        
                      - **matchEquals** *(string) --* 
        
                        The value selected by the JsonPath expression must match what is supplied in the MatchEquals field, otherwise the request will be ignored. Properties from the target action configuration can be included as placeholders in this value by surrounding the action configuration key with curly braces. For example, if the value supplied here is \"refs/heads/{Branch}\" and the target action has an action configuration property called \"Branch\" with a value of \"master\", the MatchEquals value will be evaluated as \"refs/heads/master\". A list of action configuration properties for built-in action types can be found here: `Pipeline Structure Reference Action Requirements <http://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__ .
        
                  - **authentication** *(string) --* 
        
                    Supported options are GITHUB_HMAC, IP and UNAUTHENTICATED.
        
                    * GITHUB_HMAC implements the authentication scheme described here: https://developer.github.com/webhooks/securing/ 
                     
                    * IP will reject webhooks trigger requests unless they originate from an IP within the IP range whitelisted in the authentication configuration. 
                     
                    * UNAUTHENTICATED will accept all webhook trigger requests regardless of origin. 
                     
                  - **authenticationConfiguration** *(dict) --* 
        
                    Properties that configure the authentication applied to incoming webhook trigger requests. The required properties depend on the authentication type. For GITHUB_HMAC, only the SecretToken property must be set. For IP, only the AllowedIPRange property must be set to a valid CIDR range. For UNAUTHENTICATED, no properties can be set.
        
                    - **AllowedIPRange** *(string) --* 
        
                      The property used to configure acceptance of webhooks within a specific IP range. For IP, only the AllowedIPRange property must be set, and this property must be set to a valid CIDR range.
        
                    - **SecretToken** *(string) --* 
        
                      The property used to configure GitHub authentication. For GITHUB_HMAC, only the SecretToken property must be set.
        
                - **url** *(string) --* 
        
                  A unique URL generated by CodePipeline. When a POST request is made to this URL, the defined pipeline is started as long as the body of the post request satisfies the defined authentication and filtering conditions. Deleting and re-creating a webhook will make the old URL invalid and generate a new URL.
        
                - **errorMessage** *(string) --* 
        
                  The text of the error message about the webhook.
        
                - **errorCode** *(string) --* 
        
                  The number code of the error.
        
                - **lastTriggered** *(datetime) --* 
        
                  The date and time a webhook was last successfully triggered, in timestamp format.
        
                - **arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the webhook.
        
            - **NextToken** *(string) --* 
        
              If the amount of returned information is significantly large, an identifier is also returned and can be used in a subsequent ListWebhooks call to return the next set of webhooks in the list. 
        
        """
        pass

    def poll_for_jobs(self, actionTypeId: Dict, maxBatchSize: int = None, queryParam: Dict = None) -> Dict:
        """
        
        .. warning::
        
          When this API is called, AWS CodePipeline returns temporary credentials for the Amazon S3 bucket used to store artifacts for the pipeline, if the action requires access to that Amazon S3 bucket for input or output artifacts. Additionally, this API returns any secret values defined for the action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/PollForJobs>`_
        
        **Request Syntax** 
        ::
        
          response = client.poll_for_jobs(
              actionTypeId={
                  \'category\': \'Source\'|\'Build\'|\'Deploy\'|\'Test\'|\'Invoke\'|\'Approval\',
                  \'owner\': \'AWS\'|\'ThirdParty\'|\'Custom\',
                  \'provider\': \'string\',
                  \'version\': \'string\'
              },
              maxBatchSize=123,
              queryParam={
                  \'string\': \'string\'
              }
          )
        :type actionTypeId: dict
        :param actionTypeId: **[REQUIRED]** 
        
          Represents information about an action type.
        
          - **category** *(string) --* **[REQUIRED]** 
        
            A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
        
          - **owner** *(string) --* **[REQUIRED]** 
        
            The creator of the action being called.
        
          - **provider** *(string) --* **[REQUIRED]** 
        
            The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
        
          - **version** *(string) --* **[REQUIRED]** 
        
            A string that describes the action version.
        
        :type maxBatchSize: integer
        :param maxBatchSize: 
        
          The maximum number of jobs to return in a poll for jobs call.
        
        :type queryParam: dict
        :param queryParam: 
        
          A map of property names and values. For an action type with no queryable properties, this value must be null or an empty map. For an action type with a queryable property, you must supply that property as a key in the map. Only jobs whose action configuration matches the mapped value will be returned.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'jobs\': [
                    {
                        \'id\': \'string\',
                        \'data\': {
                            \'actionTypeId\': {
                                \'category\': \'Source\'|\'Build\'|\'Deploy\'|\'Test\'|\'Invoke\'|\'Approval\',
                                \'owner\': \'AWS\'|\'ThirdParty\'|\'Custom\',
                                \'provider\': \'string\',
                                \'version\': \'string\'
                            },
                            \'actionConfiguration\': {
                                \'configuration\': {
                                    \'string\': \'string\'
                                }
                            },
                            \'pipelineContext\': {
                                \'pipelineName\': \'string\',
                                \'stage\': {
                                    \'name\': \'string\'
                                },
                                \'action\': {
                                    \'name\': \'string\'
                                }
                            },
                            \'inputArtifacts\': [
                                {
                                    \'name\': \'string\',
                                    \'revision\': \'string\',
                                    \'location\': {
                                        \'type\': \'S3\',
                                        \'s3Location\': {
                                            \'bucketName\': \'string\',
                                            \'objectKey\': \'string\'
                                        }
                                    }
                                },
                            ],
                            \'outputArtifacts\': [
                                {
                                    \'name\': \'string\',
                                    \'revision\': \'string\',
                                    \'location\': {
                                        \'type\': \'S3\',
                                        \'s3Location\': {
                                            \'bucketName\': \'string\',
                                            \'objectKey\': \'string\'
                                        }
                                    }
                                },
                            ],
                            \'artifactCredentials\': {
                                \'accessKeyId\': \'string\',
                                \'secretAccessKey\': \'string\',
                                \'sessionToken\': \'string\'
                            },
                            \'continuationToken\': \'string\',
                            \'encryptionKey\': {
                                \'id\': \'string\',
                                \'type\': \'KMS\'
                            }
                        },
                        \'nonce\': \'string\',
                        \'accountId\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a PollForJobs action.
        
            - **jobs** *(list) --* 
        
              Information about the jobs to take action on.
        
              - *(dict) --* 
        
                Represents information about a job.
        
                - **id** *(string) --* 
        
                  The unique system-generated ID of the job.
        
                - **data** *(dict) --* 
        
                  Additional data about a job.
        
                  - **actionTypeId** *(dict) --* 
        
                    Represents information about an action type.
        
                    - **category** *(string) --* 
        
                      A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
        
                    - **owner** *(string) --* 
        
                      The creator of the action being called.
        
                    - **provider** *(string) --* 
        
                      The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
        
                    - **version** *(string) --* 
        
                      A string that describes the action version.
        
                  - **actionConfiguration** *(dict) --* 
        
                    Represents information about an action configuration.
        
                    - **configuration** *(dict) --* 
        
                      The configuration data for the action.
        
                      - *(string) --* 
                        
                        - *(string) --* 
                  
                  - **pipelineContext** *(dict) --* 
        
                    Represents information about a pipeline to a job worker.
        
                    - **pipelineName** *(string) --* 
        
                      The name of the pipeline. This is a user-specified value. Pipeline names must be unique across all pipeline names under an Amazon Web Services account.
        
                    - **stage** *(dict) --* 
        
                      The stage of the pipeline.
        
                      - **name** *(string) --* 
        
                        The name of the stage.
        
                    - **action** *(dict) --* 
        
                      The context of an action to a job worker within the stage of a pipeline.
        
                      - **name** *(string) --* 
        
                        The name of the action within the context of a job.
        
                  - **inputArtifacts** *(list) --* 
        
                    The artifact supplied to the job.
        
                    - *(dict) --* 
        
                      Represents information about an artifact that will be worked upon by actions in the pipeline.
        
                      - **name** *(string) --* 
        
                        The artifact\'s name.
        
                      - **revision** *(string) --* 
        
                        The artifact\'s revision ID. Depending on the type of object, this could be a commit ID (GitHub) or a revision ID (Amazon S3).
        
                      - **location** *(dict) --* 
        
                        The location of an artifact.
        
                        - **type** *(string) --* 
        
                          The type of artifact in the location.
        
                        - **s3Location** *(dict) --* 
        
                          The Amazon S3 bucket that contains the artifact.
        
                          - **bucketName** *(string) --* 
        
                            The name of the Amazon S3 bucket.
        
                          - **objectKey** *(string) --* 
        
                            The key of the object in the Amazon S3 bucket, which uniquely identifies the object in the bucket.
        
                  - **outputArtifacts** *(list) --* 
        
                    The output of the job.
        
                    - *(dict) --* 
        
                      Represents information about an artifact that will be worked upon by actions in the pipeline.
        
                      - **name** *(string) --* 
        
                        The artifact\'s name.
        
                      - **revision** *(string) --* 
        
                        The artifact\'s revision ID. Depending on the type of object, this could be a commit ID (GitHub) or a revision ID (Amazon S3).
        
                      - **location** *(dict) --* 
        
                        The location of an artifact.
        
                        - **type** *(string) --* 
        
                          The type of artifact in the location.
        
                        - **s3Location** *(dict) --* 
        
                          The Amazon S3 bucket that contains the artifact.
        
                          - **bucketName** *(string) --* 
        
                            The name of the Amazon S3 bucket.
        
                          - **objectKey** *(string) --* 
        
                            The key of the object in the Amazon S3 bucket, which uniquely identifies the object in the bucket.
        
                  - **artifactCredentials** *(dict) --* 
        
                    Represents an AWS session credentials object. These credentials are temporary credentials that are issued by AWS Secure Token Service (STS). They can be used to access input and output artifacts in the Amazon S3 bucket used to store artifact for the pipeline in AWS CodePipeline.
        
                    - **accessKeyId** *(string) --* 
        
                      The access key for the session.
        
                    - **secretAccessKey** *(string) --* 
        
                      The secret access key for the session.
        
                    - **sessionToken** *(string) --* 
        
                      The token for the session.
        
                  - **continuationToken** *(string) --* 
        
                    A system-generated token, such as a AWS CodeDeploy deployment ID, that a job requires in order to continue the job asynchronously.
        
                  - **encryptionKey** *(dict) --* 
        
                    Represents information about the key used to encrypt data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. 
        
                    - **id** *(string) --* 
        
                      The ID used to identify the key. For an AWS KMS key, this is the key ID or key ARN.
        
                    - **type** *(string) --* 
        
                      The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.
        
                - **nonce** *(string) --* 
        
                  A system-generated random number that AWS CodePipeline uses to ensure that the job is being worked on by only one job worker. Use this number in an  AcknowledgeJob request.
        
                - **accountId** *(string) --* 
        
                  The ID of the AWS account to use when performing the job.
        
        """
        pass

    def poll_for_third_party_jobs(self, actionTypeId: Dict, maxBatchSize: int = None) -> Dict:
        """
        
        .. warning::
        
          When this API is called, AWS CodePipeline returns temporary credentials for the Amazon S3 bucket used to store artifacts for the pipeline, if the action requires access to that Amazon S3 bucket for input or output artifacts.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/PollForThirdPartyJobs>`_
        
        **Request Syntax** 
        ::
        
          response = client.poll_for_third_party_jobs(
              actionTypeId={
                  \'category\': \'Source\'|\'Build\'|\'Deploy\'|\'Test\'|\'Invoke\'|\'Approval\',
                  \'owner\': \'AWS\'|\'ThirdParty\'|\'Custom\',
                  \'provider\': \'string\',
                  \'version\': \'string\'
              },
              maxBatchSize=123
          )
        :type actionTypeId: dict
        :param actionTypeId: **[REQUIRED]** 
        
          Represents information about an action type.
        
          - **category** *(string) --* **[REQUIRED]** 
        
            A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
        
          - **owner** *(string) --* **[REQUIRED]** 
        
            The creator of the action being called.
        
          - **provider** *(string) --* **[REQUIRED]** 
        
            The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
        
          - **version** *(string) --* **[REQUIRED]** 
        
            A string that describes the action version.
        
        :type maxBatchSize: integer
        :param maxBatchSize: 
        
          The maximum number of jobs to return in a poll for jobs call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'jobs\': [
                    {
                        \'clientId\': \'string\',
                        \'jobId\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a PollForThirdPartyJobs action.
        
            - **jobs** *(list) --* 
        
              Information about the jobs to take action on.
        
              - *(dict) --* 
        
                A response to a PollForThirdPartyJobs request returned by AWS CodePipeline when there is a job to be worked upon by a partner action.
        
                - **clientId** *(string) --* 
        
                  The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.
        
                - **jobId** *(string) --* 
        
                  The identifier used to identify the job in AWS CodePipeline.
        
        """
        pass

    def put_action_revision(self, pipelineName: str, stageName: str, actionName: str, actionRevision: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/PutActionRevision>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_action_revision(
              pipelineName=\'string\',
              stageName=\'string\',
              actionName=\'string\',
              actionRevision={
                  \'revisionId\': \'string\',
                  \'revisionChangeId\': \'string\',
                  \'created\': datetime(2015, 1, 1)
              }
          )
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]** 
        
          The name of the pipeline that will start processing the revision to the source.
        
        :type stageName: string
        :param stageName: **[REQUIRED]** 
        
          The name of the stage that contains the action that will act upon the revision.
        
        :type actionName: string
        :param actionName: **[REQUIRED]** 
        
          The name of the action that will process the revision.
        
        :type actionRevision: dict
        :param actionRevision: **[REQUIRED]** 
        
          Represents information about the version (or revision) of an action.
        
          - **revisionId** *(string) --* **[REQUIRED]** 
        
            The system-generated unique ID that identifies the revision number of the action.
        
          - **revisionChangeId** *(string) --* **[REQUIRED]** 
        
            The unique identifier of the change that set the state to this revision, for example a deployment ID or timestamp.
        
          - **created** *(datetime) --* **[REQUIRED]** 
        
            The date and time when the most recent version of the action was created, in timestamp format.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'newRevision\': True|False,
                \'pipelineExecutionId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a PutActionRevision action.
        
            - **newRevision** *(boolean) --* 
        
              Indicates whether the artifact revision was previously used in an execution of the specified pipeline.
        
            - **pipelineExecutionId** *(string) --* 
        
              The ID of the current workflow state of the pipeline.
        
        """
        pass

    def put_approval_result(self, pipelineName: str, stageName: str, actionName: str, result: Dict, token: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/PutApprovalResult>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_approval_result(
              pipelineName=\'string\',
              stageName=\'string\',
              actionName=\'string\',
              result={
                  \'summary\': \'string\',
                  \'status\': \'Approved\'|\'Rejected\'
              },
              token=\'string\'
          )
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]** 
        
          The name of the pipeline that contains the action. 
        
        :type stageName: string
        :param stageName: **[REQUIRED]** 
        
          The name of the stage that contains the action.
        
        :type actionName: string
        :param actionName: **[REQUIRED]** 
        
          The name of the action for which approval is requested.
        
        :type result: dict
        :param result: **[REQUIRED]** 
        
          Represents information about the result of the approval request.
        
          - **summary** *(string) --* **[REQUIRED]** 
        
            The summary of the current status of the approval request.
        
          - **status** *(string) --* **[REQUIRED]** 
        
            The response submitted by a reviewer assigned to an approval action request.
        
        :type token: string
        :param token: **[REQUIRED]** 
        
          The system-generated token used to identify a unique approval request. The token for each open approval request can be obtained using the  GetPipelineState action and is used to validate that the approval request corresponding to this token is still valid.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'approvedAt\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a PutApprovalResult action.
        
            - **approvedAt** *(datetime) --* 
        
              The timestamp showing when the approval or rejection was submitted.
        
        """
        pass

    def put_job_failure_result(self, jobId: str, failureDetails: Dict) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/PutJobFailureResult>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_job_failure_result(
              jobId=\'string\',
              failureDetails={
                  \'type\': \'JobFailed\'|\'ConfigurationError\'|\'PermissionError\'|\'RevisionOutOfSync\'|\'RevisionUnavailable\'|\'SystemUnavailable\',
                  \'message\': \'string\',
                  \'externalExecutionId\': \'string\'
              }
          )
        :type jobId: string
        :param jobId: **[REQUIRED]** 
        
          The unique system-generated ID of the job that failed. This is the same ID returned from PollForJobs.
        
        :type failureDetails: dict
        :param failureDetails: **[REQUIRED]** 
        
          The details about the failure of a job.
        
          - **type** *(string) --* **[REQUIRED]** 
        
            The type of the failure.
        
          - **message** *(string) --* **[REQUIRED]** 
        
            The message about the failure.
        
          - **externalExecutionId** *(string) --* 
        
            The external ID of the run of the action that failed.
        
        :returns: None
        """
        pass

    def put_job_success_result(self, jobId: str, currentRevision: Dict = None, continuationToken: str = None, executionDetails: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/PutJobSuccessResult>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_job_success_result(
              jobId=\'string\',
              currentRevision={
                  \'revision\': \'string\',
                  \'changeIdentifier\': \'string\',
                  \'created\': datetime(2015, 1, 1),
                  \'revisionSummary\': \'string\'
              },
              continuationToken=\'string\',
              executionDetails={
                  \'summary\': \'string\',
                  \'externalExecutionId\': \'string\',
                  \'percentComplete\': 123
              }
          )
        :type jobId: string
        :param jobId: **[REQUIRED]** 
        
          The unique system-generated ID of the job that succeeded. This is the same ID returned from PollForJobs.
        
        :type currentRevision: dict
        :param currentRevision: 
        
          The ID of the current revision of the artifact successfully worked upon by the job.
        
          - **revision** *(string) --* **[REQUIRED]** 
        
            The revision ID of the current version of an artifact.
        
          - **changeIdentifier** *(string) --* **[REQUIRED]** 
        
            The change identifier for the current revision.
        
          - **created** *(datetime) --* 
        
            The date and time when the most recent revision of the artifact was created, in timestamp format.
        
          - **revisionSummary** *(string) --* 
        
            The summary of the most recent revision of the artifact.
        
        :type continuationToken: string
        :param continuationToken: 
        
          A token generated by a job worker, such as an AWS CodeDeploy deployment ID, that a successful job provides to identify a custom action in progress. Future jobs will use this token in order to identify the running instance of the action. It can be reused to return additional information about the progress of the custom action. When the action is complete, no continuation token should be supplied.
        
        :type executionDetails: dict
        :param executionDetails: 
        
          The execution details of the successful job, such as the actions taken by the job worker.
        
          - **summary** *(string) --* 
        
            The summary of the current status of the actions.
        
          - **externalExecutionId** *(string) --* 
        
            The system-generated unique ID of this action used to identify this job worker in any external systems, such as AWS CodeDeploy.
        
          - **percentComplete** *(integer) --* 
        
            The percentage of work completed on the action, represented on a scale of zero to one hundred percent.
        
        :returns: None
        """
        pass

    def put_third_party_job_failure_result(self, jobId: str, clientToken: str, failureDetails: Dict) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/PutThirdPartyJobFailureResult>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_third_party_job_failure_result(
              jobId=\'string\',
              clientToken=\'string\',
              failureDetails={
                  \'type\': \'JobFailed\'|\'ConfigurationError\'|\'PermissionError\'|\'RevisionOutOfSync\'|\'RevisionUnavailable\'|\'SystemUnavailable\',
                  \'message\': \'string\',
                  \'externalExecutionId\': \'string\'
              }
          )
        :type jobId: string
        :param jobId: **[REQUIRED]** 
        
          The ID of the job that failed. This is the same ID returned from PollForThirdPartyJobs.
        
        :type clientToken: string
        :param clientToken: **[REQUIRED]** 
        
          The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.
        
        :type failureDetails: dict
        :param failureDetails: **[REQUIRED]** 
        
          Represents information about failure details.
        
          - **type** *(string) --* **[REQUIRED]** 
        
            The type of the failure.
        
          - **message** *(string) --* **[REQUIRED]** 
        
            The message about the failure.
        
          - **externalExecutionId** *(string) --* 
        
            The external ID of the run of the action that failed.
        
        :returns: None
        """
        pass

    def put_third_party_job_success_result(self, jobId: str, clientToken: str, currentRevision: Dict = None, continuationToken: str = None, executionDetails: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/PutThirdPartyJobSuccessResult>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_third_party_job_success_result(
              jobId=\'string\',
              clientToken=\'string\',
              currentRevision={
                  \'revision\': \'string\',
                  \'changeIdentifier\': \'string\',
                  \'created\': datetime(2015, 1, 1),
                  \'revisionSummary\': \'string\'
              },
              continuationToken=\'string\',
              executionDetails={
                  \'summary\': \'string\',
                  \'externalExecutionId\': \'string\',
                  \'percentComplete\': 123
              }
          )
        :type jobId: string
        :param jobId: **[REQUIRED]** 
        
          The ID of the job that successfully completed. This is the same ID returned from PollForThirdPartyJobs.
        
        :type clientToken: string
        :param clientToken: **[REQUIRED]** 
        
          The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.
        
        :type currentRevision: dict
        :param currentRevision: 
        
          Represents information about a current revision.
        
          - **revision** *(string) --* **[REQUIRED]** 
        
            The revision ID of the current version of an artifact.
        
          - **changeIdentifier** *(string) --* **[REQUIRED]** 
        
            The change identifier for the current revision.
        
          - **created** *(datetime) --* 
        
            The date and time when the most recent revision of the artifact was created, in timestamp format.
        
          - **revisionSummary** *(string) --* 
        
            The summary of the most recent revision of the artifact.
        
        :type continuationToken: string
        :param continuationToken: 
        
          A token generated by a job worker, such as an AWS CodeDeploy deployment ID, that a successful job provides to identify a partner action in progress. Future jobs will use this token in order to identify the running instance of the action. It can be reused to return additional information about the progress of the partner action. When the action is complete, no continuation token should be supplied.
        
        :type executionDetails: dict
        :param executionDetails: 
        
          The details of the actions taken and results produced on an artifact as it passes through stages in the pipeline. 
        
          - **summary** *(string) --* 
        
            The summary of the current status of the actions.
        
          - **externalExecutionId** *(string) --* 
        
            The system-generated unique ID of this action used to identify this job worker in any external systems, such as AWS CodeDeploy.
        
          - **percentComplete** *(integer) --* 
        
            The percentage of work completed on the action, represented on a scale of zero to one hundred percent.
        
        :returns: None
        """
        pass

    def put_webhook(self, webhook: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/PutWebhook>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_webhook(
              webhook={
                  \'name\': \'string\',
                  \'targetPipeline\': \'string\',
                  \'targetAction\': \'string\',
                  \'filters\': [
                      {
                          \'jsonPath\': \'string\',
                          \'matchEquals\': \'string\'
                      },
                  ],
                  \'authentication\': \'GITHUB_HMAC\'|\'IP\'|\'UNAUTHENTICATED\',
                  \'authenticationConfiguration\': {
                      \'AllowedIPRange\': \'string\',
                      \'SecretToken\': \'string\'
                  }
              }
          )
        :type webhook: dict
        :param webhook: **[REQUIRED]** 
        
          The detail provided in an input file to create the webhook, such as the webhook name, the pipeline name, and the action name. Give the webhook a unique name which identifies the webhook being defined. You may choose to name the webhook after the pipeline and action it targets so that you can easily recognize what it\'s used for later.
        
          - **name** *(string) --* **[REQUIRED]** 
        
            The name of the webhook.
        
          - **targetPipeline** *(string) --* **[REQUIRED]** 
        
            The name of the pipeline you want to connect to the webhook.
        
          - **targetAction** *(string) --* **[REQUIRED]** 
        
            The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.
        
          - **filters** *(list) --* **[REQUIRED]** 
        
            A list of rules applied to the body/payload sent in the POST request to a webhook URL. All defined rules must pass for the request to be accepted and the pipeline started.
        
            - *(dict) --* 
        
              The event criteria that specify when a webhook notification is sent to your URL.
        
              - **jsonPath** *(string) --* **[REQUIRED]** 
        
                A JsonPath expression that will be applied to the body/payload of the webhook. The value selected by JsonPath expression must match the value specified in the matchEquals field, otherwise the request will be ignored. More information on JsonPath expressions can be found here: https://github.com/json-path/JsonPath.
        
              - **matchEquals** *(string) --* 
        
                The value selected by the JsonPath expression must match what is supplied in the MatchEquals field, otherwise the request will be ignored. Properties from the target action configuration can be included as placeholders in this value by surrounding the action configuration key with curly braces. For example, if the value supplied here is \"refs/heads/{Branch}\" and the target action has an action configuration property called \"Branch\" with a value of \"master\", the MatchEquals value will be evaluated as \"refs/heads/master\". A list of action configuration properties for built-in action types can be found here: `Pipeline Structure Reference Action Requirements <http://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__ .
        
          - **authentication** *(string) --* **[REQUIRED]** 
        
            Supported options are GITHUB_HMAC, IP and UNAUTHENTICATED.
        
            * GITHUB_HMAC implements the authentication scheme described here: https://developer.github.com/webhooks/securing/ 
             
            * IP will reject webhooks trigger requests unless they originate from an IP within the IP range whitelisted in the authentication configuration. 
             
            * UNAUTHENTICATED will accept all webhook trigger requests regardless of origin. 
             
          - **authenticationConfiguration** *(dict) --* **[REQUIRED]** 
        
            Properties that configure the authentication applied to incoming webhook trigger requests. The required properties depend on the authentication type. For GITHUB_HMAC, only the SecretToken property must be set. For IP, only the AllowedIPRange property must be set to a valid CIDR range. For UNAUTHENTICATED, no properties can be set.
        
            - **AllowedIPRange** *(string) --* 
        
              The property used to configure acceptance of webhooks within a specific IP range. For IP, only the AllowedIPRange property must be set, and this property must be set to a valid CIDR range.
        
            - **SecretToken** *(string) --* 
        
              The property used to configure GitHub authentication. For GITHUB_HMAC, only the SecretToken property must be set.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'webhook\': {
                    \'definition\': {
                        \'name\': \'string\',
                        \'targetPipeline\': \'string\',
                        \'targetAction\': \'string\',
                        \'filters\': [
                            {
                                \'jsonPath\': \'string\',
                                \'matchEquals\': \'string\'
                            },
                        ],
                        \'authentication\': \'GITHUB_HMAC\'|\'IP\'|\'UNAUTHENTICATED\',
                        \'authenticationConfiguration\': {
                            \'AllowedIPRange\': \'string\',
                            \'SecretToken\': \'string\'
                        }
                    },
                    \'url\': \'string\',
                    \'errorMessage\': \'string\',
                    \'errorCode\': \'string\',
                    \'lastTriggered\': datetime(2015, 1, 1),
                    \'arn\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **webhook** *(dict) --* 
        
              The detail returned from creating the webhook, such as the webhook name, webhook URL, and webhook ARN.
        
              - **definition** *(dict) --* 
        
                The detail returned for each webhook, such as the webhook authentication type and filter rules.
        
                - **name** *(string) --* 
        
                  The name of the webhook.
        
                - **targetPipeline** *(string) --* 
        
                  The name of the pipeline you want to connect to the webhook.
        
                - **targetAction** *(string) --* 
        
                  The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.
        
                - **filters** *(list) --* 
        
                  A list of rules applied to the body/payload sent in the POST request to a webhook URL. All defined rules must pass for the request to be accepted and the pipeline started.
        
                  - *(dict) --* 
        
                    The event criteria that specify when a webhook notification is sent to your URL.
        
                    - **jsonPath** *(string) --* 
        
                      A JsonPath expression that will be applied to the body/payload of the webhook. The value selected by JsonPath expression must match the value specified in the matchEquals field, otherwise the request will be ignored. More information on JsonPath expressions can be found here: https://github.com/json-path/JsonPath.
        
                    - **matchEquals** *(string) --* 
        
                      The value selected by the JsonPath expression must match what is supplied in the MatchEquals field, otherwise the request will be ignored. Properties from the target action configuration can be included as placeholders in this value by surrounding the action configuration key with curly braces. For example, if the value supplied here is \"refs/heads/{Branch}\" and the target action has an action configuration property called \"Branch\" with a value of \"master\", the MatchEquals value will be evaluated as \"refs/heads/master\". A list of action configuration properties for built-in action types can be found here: `Pipeline Structure Reference Action Requirements <http://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__ .
        
                - **authentication** *(string) --* 
        
                  Supported options are GITHUB_HMAC, IP and UNAUTHENTICATED.
        
                  * GITHUB_HMAC implements the authentication scheme described here: https://developer.github.com/webhooks/securing/ 
                   
                  * IP will reject webhooks trigger requests unless they originate from an IP within the IP range whitelisted in the authentication configuration. 
                   
                  * UNAUTHENTICATED will accept all webhook trigger requests regardless of origin. 
                   
                - **authenticationConfiguration** *(dict) --* 
        
                  Properties that configure the authentication applied to incoming webhook trigger requests. The required properties depend on the authentication type. For GITHUB_HMAC, only the SecretToken property must be set. For IP, only the AllowedIPRange property must be set to a valid CIDR range. For UNAUTHENTICATED, no properties can be set.
        
                  - **AllowedIPRange** *(string) --* 
        
                    The property used to configure acceptance of webhooks within a specific IP range. For IP, only the AllowedIPRange property must be set, and this property must be set to a valid CIDR range.
        
                  - **SecretToken** *(string) --* 
        
                    The property used to configure GitHub authentication. For GITHUB_HMAC, only the SecretToken property must be set.
        
              - **url** *(string) --* 
        
                A unique URL generated by CodePipeline. When a POST request is made to this URL, the defined pipeline is started as long as the body of the post request satisfies the defined authentication and filtering conditions. Deleting and re-creating a webhook will make the old URL invalid and generate a new URL.
        
              - **errorMessage** *(string) --* 
        
                The text of the error message about the webhook.
        
              - **errorCode** *(string) --* 
        
                The number code of the error.
        
              - **lastTriggered** *(datetime) --* 
        
                The date and time a webhook was last successfully triggered, in timestamp format.
        
              - **arn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the webhook.
        
        """
        pass

    def register_webhook_with_third_party(self, webhookName: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/RegisterWebhookWithThirdParty>`_
        
        **Request Syntax** 
        ::
        
          response = client.register_webhook_with_third_party(
              webhookName=\'string\'
          )
        :type webhookName: string
        :param webhookName: 
        
          The name of an existing webhook created with PutWebhook to register with a supported third party. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def retry_stage_execution(self, pipelineName: str, stageName: str, pipelineExecutionId: str, retryMode: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/RetryStageExecution>`_
        
        **Request Syntax** 
        ::
        
          response = client.retry_stage_execution(
              pipelineName=\'string\',
              stageName=\'string\',
              pipelineExecutionId=\'string\',
              retryMode=\'FAILED_ACTIONS\'
          )
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]** 
        
          The name of the pipeline that contains the failed stage.
        
        :type stageName: string
        :param stageName: **[REQUIRED]** 
        
          The name of the failed stage to be retried.
        
        :type pipelineExecutionId: string
        :param pipelineExecutionId: **[REQUIRED]** 
        
          The ID of the pipeline execution in the failed stage to be retried. Use the  GetPipelineState action to retrieve the current pipelineExecutionId of the failed stage
        
        :type retryMode: string
        :param retryMode: **[REQUIRED]** 
        
          The scope of the retry attempt. Currently, the only supported value is FAILED_ACTIONS.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'pipelineExecutionId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a RetryStageExecution action.
        
            - **pipelineExecutionId** *(string) --* 
        
              The ID of the current workflow execution in the failed stage.
        
        """
        pass

    def start_pipeline_execution(self, name: str, clientRequestToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/StartPipelineExecution>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_pipeline_execution(
              name=\'string\',
              clientRequestToken=\'string\'
          )
        :type name: string
        :param name: **[REQUIRED]** 
        
          The name of the pipeline to start.
        
        :type clientRequestToken: string
        :param clientRequestToken: 
        
          The system-generated unique ID used to identify a unique execution request.
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'pipelineExecutionId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a StartPipelineExecution action.
        
            - **pipelineExecutionId** *(string) --* 
        
              The unique system-generated ID of the pipeline execution that was started.
        
        """
        pass

    def update_pipeline(self, pipeline: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/UpdatePipeline>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_pipeline(
              pipeline={
                  \'name\': \'string\',
                  \'roleArn\': \'string\',
                  \'artifactStore\': {
                      \'type\': \'S3\',
                      \'location\': \'string\',
                      \'encryptionKey\': {
                          \'id\': \'string\',
                          \'type\': \'KMS\'
                      }
                  },
                  \'artifactStores\': {
                      \'string\': {
                          \'type\': \'S3\',
                          \'location\': \'string\',
                          \'encryptionKey\': {
                              \'id\': \'string\',
                              \'type\': \'KMS\'
                          }
                      }
                  },
                  \'stages\': [
                      {
                          \'name\': \'string\',
                          \'blockers\': [
                              {
                                  \'name\': \'string\',
                                  \'type\': \'Schedule\'
                              },
                          ],
                          \'actions\': [
                              {
                                  \'name\': \'string\',
                                  \'actionTypeId\': {
                                      \'category\': \'Source\'|\'Build\'|\'Deploy\'|\'Test\'|\'Invoke\'|\'Approval\',
                                      \'owner\': \'AWS\'|\'ThirdParty\'|\'Custom\',
                                      \'provider\': \'string\',
                                      \'version\': \'string\'
                                  },
                                  \'runOrder\': 123,
                                  \'configuration\': {
                                      \'string\': \'string\'
                                  },
                                  \'outputArtifacts\': [
                                      {
                                          \'name\': \'string\'
                                      },
                                  ],
                                  \'inputArtifacts\': [
                                      {
                                          \'name\': \'string\'
                                      },
                                  ],
                                  \'roleArn\': \'string\',
                                  \'region\': \'string\'
                              },
                          ]
                      },
                  ],
                  \'version\': 123
              }
          )
        :type pipeline: dict
        :param pipeline: **[REQUIRED]** 
        
          The name of the pipeline to be updated.
        
          - **name** *(string) --* **[REQUIRED]** 
        
            The name of the action to be performed.
        
          - **roleArn** *(string) --* **[REQUIRED]** 
        
            The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with no actionRoleArn, or to use to assume roles for actions with an actionRoleArn.
        
          - **artifactStore** *(dict) --* 
        
            Represents information about the Amazon S3 bucket where artifacts are stored for the pipeline. 
        
            - **type** *(string) --* **[REQUIRED]** 
        
              The type of the artifact store, such as S3.
        
            - **location** *(string) --* **[REQUIRED]** 
        
              The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder within the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any Amazon S3 bucket in the same AWS Region as the pipeline to store your pipeline artifacts.
        
            - **encryptionKey** *(dict) --* 
        
              The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.
        
              - **id** *(string) --* **[REQUIRED]** 
        
                The ID used to identify the key. For an AWS KMS key, this is the key ID or key ARN.
        
              - **type** *(string) --* **[REQUIRED]** 
        
                The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.
        
          - **artifactStores** *(dict) --* 
        
            A mapping of artifactStore objects and their corresponding regions. There must be an artifact store for the pipeline region and for each cross-region action within the pipeline. You can only use either artifactStore or artifactStores, not both.
        
            If you create a cross-region action in your pipeline, you must use artifactStores.
        
            - *(string) --* 
        
              - *(dict) --* 
        
                The Amazon S3 bucket where artifacts are stored for the pipeline.
        
                - **type** *(string) --* **[REQUIRED]** 
        
                  The type of the artifact store, such as S3.
        
                - **location** *(string) --* **[REQUIRED]** 
        
                  The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder within the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any Amazon S3 bucket in the same AWS Region as the pipeline to store your pipeline artifacts.
        
                - **encryptionKey** *(dict) --* 
        
                  The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.
        
                  - **id** *(string) --* **[REQUIRED]** 
        
                    The ID used to identify the key. For an AWS KMS key, this is the key ID or key ARN.
        
                  - **type** *(string) --* **[REQUIRED]** 
        
                    The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.
        
          - **stages** *(list) --* **[REQUIRED]** 
        
            The stage in which to perform the action.
        
            - *(dict) --* 
        
              Represents information about a stage and its definition.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the stage.
        
              - **blockers** *(list) --* 
        
                Reserved for future use.
        
                - *(dict) --* 
        
                  Reserved for future use.
        
                  - **name** *(string) --* **[REQUIRED]** 
        
                    Reserved for future use.
        
                  - **type** *(string) --* **[REQUIRED]** 
        
                    Reserved for future use.
        
              - **actions** *(list) --* **[REQUIRED]** 
        
                The actions included in a stage.
        
                - *(dict) --* 
        
                  Represents information about an action declaration.
        
                  - **name** *(string) --* **[REQUIRED]** 
        
                    The action declaration\'s name.
        
                  - **actionTypeId** *(dict) --* **[REQUIRED]** 
        
                    The configuration information for the action type.
        
                    - **category** *(string) --* **[REQUIRED]** 
        
                      A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
        
                    - **owner** *(string) --* **[REQUIRED]** 
        
                      The creator of the action being called.
        
                    - **provider** *(string) --* **[REQUIRED]** 
        
                      The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
        
                    - **version** *(string) --* **[REQUIRED]** 
        
                      A string that describes the action version.
        
                  - **runOrder** *(integer) --* 
        
                    The order in which actions are run.
        
                  - **configuration** *(dict) --* 
        
                    The action declaration\'s configuration.
        
                    - *(string) --* 
        
                      - *(string) --* 
        
                  - **outputArtifacts** *(list) --* 
        
                    The name or ID of the result of the action declaration, such as a test or build artifact.
        
                    - *(dict) --* 
        
                      Represents information about the output of an action.
        
                      - **name** *(string) --* **[REQUIRED]** 
        
                        The name of the output of an artifact, such as \"My App\".
        
                        The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
        
                        Output artifact names must be unique within a pipeline.
        
                  - **inputArtifacts** *(list) --* 
        
                    The name or ID of the artifact consumed by the action, such as a test or build artifact.
        
                    - *(dict) --* 
        
                      Represents information about an artifact to be worked on, such as a test or build artifact.
        
                      - **name** *(string) --* **[REQUIRED]** 
        
                        The name of the artifact to be worked on, for example, \"My App\".
        
                        The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
        
                  - **roleArn** *(string) --* 
        
                    The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.
        
                  - **region** *(string) --* 
        
                    The action declaration\'s AWS Region, such as us-east-1.
        
          - **version** *(integer) --* 
        
            The version number of the pipeline. A new pipeline always has a version number of 1. This number is automatically incremented when a pipeline is updated.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'pipeline\': {
                    \'name\': \'string\',
                    \'roleArn\': \'string\',
                    \'artifactStore\': {
                        \'type\': \'S3\',
                        \'location\': \'string\',
                        \'encryptionKey\': {
                            \'id\': \'string\',
                            \'type\': \'KMS\'
                        }
                    },
                    \'artifactStores\': {
                        \'string\': {
                            \'type\': \'S3\',
                            \'location\': \'string\',
                            \'encryptionKey\': {
                                \'id\': \'string\',
                                \'type\': \'KMS\'
                            }
                        }
                    },
                    \'stages\': [
                        {
                            \'name\': \'string\',
                            \'blockers\': [
                                {
                                    \'name\': \'string\',
                                    \'type\': \'Schedule\'
                                },
                            ],
                            \'actions\': [
                                {
                                    \'name\': \'string\',
                                    \'actionTypeId\': {
                                        \'category\': \'Source\'|\'Build\'|\'Deploy\'|\'Test\'|\'Invoke\'|\'Approval\',
                                        \'owner\': \'AWS\'|\'ThirdParty\'|\'Custom\',
                                        \'provider\': \'string\',
                                        \'version\': \'string\'
                                    },
                                    \'runOrder\': 123,
                                    \'configuration\': {
                                        \'string\': \'string\'
                                    },
                                    \'outputArtifacts\': [
                                        {
                                            \'name\': \'string\'
                                        },
                                    ],
                                    \'inputArtifacts\': [
                                        {
                                            \'name\': \'string\'
                                        },
                                    ],
                                    \'roleArn\': \'string\',
                                    \'region\': \'string\'
                                },
                            ]
                        },
                    ],
                    \'version\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of an UpdatePipeline action.
        
            - **pipeline** *(dict) --* 
        
              The structure of the updated pipeline.
        
              - **name** *(string) --* 
        
                The name of the action to be performed.
        
              - **roleArn** *(string) --* 
        
                The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with no actionRoleArn, or to use to assume roles for actions with an actionRoleArn.
        
              - **artifactStore** *(dict) --* 
        
                Represents information about the Amazon S3 bucket where artifacts are stored for the pipeline. 
        
                - **type** *(string) --* 
        
                  The type of the artifact store, such as S3.
        
                - **location** *(string) --* 
        
                  The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder within the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any Amazon S3 bucket in the same AWS Region as the pipeline to store your pipeline artifacts.
        
                - **encryptionKey** *(dict) --* 
        
                  The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.
        
                  - **id** *(string) --* 
        
                    The ID used to identify the key. For an AWS KMS key, this is the key ID or key ARN.
        
                  - **type** *(string) --* 
        
                    The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.
        
              - **artifactStores** *(dict) --* 
        
                A mapping of artifactStore objects and their corresponding regions. There must be an artifact store for the pipeline region and for each cross-region action within the pipeline. You can only use either artifactStore or artifactStores, not both.
        
                If you create a cross-region action in your pipeline, you must use artifactStores.
        
                - *(string) --* 
                  
                  - *(dict) --* 
        
                    The Amazon S3 bucket where artifacts are stored for the pipeline.
        
                    - **type** *(string) --* 
        
                      The type of the artifact store, such as S3.
        
                    - **location** *(string) --* 
        
                      The Amazon S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder within the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any Amazon S3 bucket in the same AWS Region as the pipeline to store your pipeline artifacts.
        
                    - **encryptionKey** *(dict) --* 
        
                      The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.
        
                      - **id** *(string) --* 
        
                        The ID used to identify the key. For an AWS KMS key, this is the key ID or key ARN.
        
                      - **type** *(string) --* 
        
                        The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.
        
              - **stages** *(list) --* 
        
                The stage in which to perform the action.
        
                - *(dict) --* 
        
                  Represents information about a stage and its definition.
        
                  - **name** *(string) --* 
        
                    The name of the stage.
        
                  - **blockers** *(list) --* 
        
                    Reserved for future use.
        
                    - *(dict) --* 
        
                      Reserved for future use.
        
                      - **name** *(string) --* 
        
                        Reserved for future use.
        
                      - **type** *(string) --* 
        
                        Reserved for future use.
        
                  - **actions** *(list) --* 
        
                    The actions included in a stage.
        
                    - *(dict) --* 
        
                      Represents information about an action declaration.
        
                      - **name** *(string) --* 
        
                        The action declaration\'s name.
        
                      - **actionTypeId** *(dict) --* 
        
                        The configuration information for the action type.
        
                        - **category** *(string) --* 
        
                          A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
        
                        - **owner** *(string) --* 
        
                          The creator of the action being called.
        
                        - **provider** *(string) --* 
        
                          The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
        
                        - **version** *(string) --* 
        
                          A string that describes the action version.
        
                      - **runOrder** *(integer) --* 
        
                        The order in which actions are run.
        
                      - **configuration** *(dict) --* 
        
                        The action declaration\'s configuration.
        
                        - *(string) --* 
                          
                          - *(string) --* 
                    
                      - **outputArtifacts** *(list) --* 
        
                        The name or ID of the result of the action declaration, such as a test or build artifact.
        
                        - *(dict) --* 
        
                          Represents information about the output of an action.
        
                          - **name** *(string) --* 
        
                            The name of the output of an artifact, such as \"My App\".
        
                            The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
        
                            Output artifact names must be unique within a pipeline.
        
                      - **inputArtifacts** *(list) --* 
        
                        The name or ID of the artifact consumed by the action, such as a test or build artifact.
        
                        - *(dict) --* 
        
                          Represents information about an artifact to be worked on, such as a test or build artifact.
        
                          - **name** *(string) --* 
        
                            The name of the artifact to be worked on, for example, \"My App\".
        
                            The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
        
                      - **roleArn** *(string) --* 
        
                        The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.
        
                      - **region** *(string) --* 
        
                        The action declaration\'s AWS Region, such as us-east-1.
        
              - **version** *(integer) --* 
        
                The version number of the pipeline. A new pipeline always has a version number of 1. This number is automatically incremented when a pipeline is updated.
        
        """
        pass
