from typing import Dict
from botocore.paginate import Paginator


class ListActionTypes(Paginator):
    def paginate(self, actionOwnerFilter: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CodePipeline.Client.list_action_types`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/ListActionTypes>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              actionOwnerFilter='AWS'|'ThirdParty'|'Custom',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'actionTypes': [
                    {
                        'id': {
                            'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                            'owner': 'AWS'|'ThirdParty'|'Custom',
                            'provider': 'string',
                            'version': 'string'
                        },
                        'settings': {
                            'thirdPartyConfigurationUrl': 'string',
                            'entityUrlTemplate': 'string',
                            'executionUrlTemplate': 'string',
                            'revisionUrlTemplate': 'string'
                        },
                        'actionConfigurationProperties': [
                            {
                                'name': 'string',
                                'required': True|False,
                                'key': True|False,
                                'secret': True|False,
                                'queryable': True|False,
                                'description': 'string',
                                'type': 'String'|'Number'|'Boolean'
                            },
                        ],
                        'inputArtifactDetails': {
                            'minimumCount': 123,
                            'maximumCount': 123
                        },
                        'outputArtifactDetails': {
                            'minimumCount': 123,
                            'maximumCount': 123
                        }
                    },
                ],
                'NextToken': 'string'
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
                    The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. To reference a list of action providers by action type, see `Valid Action Types and Providers in CodePipeline <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers>`__ .
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type actionOwnerFilter: string
        :param actionOwnerFilter:
          Filters the list of action types to those created by a specified entity.
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


class ListPipelineExecutions(Paginator):
    def paginate(self, pipelineName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CodePipeline.Client.list_pipeline_executions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/ListPipelineExecutions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              pipelineName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'pipelineExecutionSummaries': [
                    {
                        'pipelineExecutionId': 'string',
                        'status': 'InProgress'|'Succeeded'|'Superseded'|'Failed',
                        'startTime': datetime(2015, 1, 1),
                        'lastUpdateTime': datetime(2015, 1, 1),
                        'sourceRevisions': [
                            {
                                'actionName': 'string',
                                'revisionId': 'string',
                                'revisionSummary': 'string',
                                'revisionUrl': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]**
          The name of the pipeline for which you want to get execution summary information.
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


class ListPipelines(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CodePipeline.Client.list_pipelines`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/ListPipelines>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'pipelines': [
                    {
                        'name': 'string',
                        'version': 123,
                        'created': datetime(2015, 1, 1),
                        'updated': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListWebhooks(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CodePipeline.Client.list_webhooks`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/ListWebhooks>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'webhooks': [
                    {
                        'definition': {
                            'name': 'string',
                            'targetPipeline': 'string',
                            'targetAction': 'string',
                            'filters': [
                                {
                                    'jsonPath': 'string',
                                    'matchEquals': 'string'
                                },
                            ],
                            'authentication': 'GITHUB_HMAC'|'IP'|'UNAUTHENTICATED',
                            'authenticationConfiguration': {
                                'AllowedIPRange': 'string',
                                'SecretToken': 'string'
                            }
                        },
                        'url': 'string',
                        'errorMessage': 'string',
                        'errorCode': 'string',
                        'lastTriggered': datetime(2015, 1, 1),
                        'arn': 'string'
                    },
                ],
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
                        The value selected by the JsonPath expression must match what is supplied in the MatchEquals field, otherwise the request will be ignored. Properties from the target action configuration can be included as placeholders in this value by surrounding the action configuration key with curly braces. For example, if the value supplied here is "refs/heads/{Branch}" and the target action has an action configuration property called "Branch" with a value of "master", the MatchEquals value will be evaluated as "refs/heads/master". A list of action configuration properties for built-in action types can be found here: `Pipeline Structure Reference Action Requirements <https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements>`__ .
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
