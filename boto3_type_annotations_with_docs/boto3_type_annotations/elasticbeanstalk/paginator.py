from typing import Dict
from typing import List
from datetime import datetime
from botocore.paginate import Paginator


class DescribeApplicationVersions(Paginator):
    def paginate(self, ApplicationName: str = None, VersionLabels: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ElasticBeanstalk.Client.describe_application_versions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribeApplicationVersions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ApplicationName='string',
              VersionLabels=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ApplicationVersions': [
                    {
                        'ApplicationVersionArn': 'string',
                        'ApplicationName': 'string',
                        'Description': 'string',
                        'VersionLabel': 'string',
                        'SourceBuildInformation': {
                            'SourceType': 'Git'|'Zip',
                            'SourceRepository': 'CodeCommit'|'S3',
                            'SourceLocation': 'string'
                        },
                        'BuildArn': 'string',
                        'SourceBundle': {
                            'S3Bucket': 'string',
                            'S3Key': 'string'
                        },
                        'DateCreated': datetime(2015, 1, 1),
                        'DateUpdated': datetime(2015, 1, 1),
                        'Status': 'Processed'|'Unprocessed'|'Failed'|'Processing'|'Building'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Result message wrapping a list of application version descriptions.
            - **ApplicationVersions** *(list) --* 
              List of ``ApplicationVersionDescription`` objects sorted in order of creation.
              - *(dict) --* 
                Describes the properties of an application version.
                - **ApplicationVersionArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the application version.
                - **ApplicationName** *(string) --* 
                  The name of the application to which the application version belongs.
                - **Description** *(string) --* 
                  The description of the application version.
                - **VersionLabel** *(string) --* 
                  A unique identifier for the application version.
                - **SourceBuildInformation** *(dict) --* 
                  If the version's source code was retrieved from AWS CodeCommit, the location of the source code for the application version.
                  - **SourceType** *(string) --* 
                    The type of repository.
                    * ``Git``   
                    * ``Zip``   
                  - **SourceRepository** *(string) --* 
                    Location where the repository is stored.
                    * ``CodeCommit``   
                    * ``S3``   
                  - **SourceLocation** *(string) --* 
                    The location of the source code, as a formatted string, depending on the value of ``SourceRepository``  
                    * For ``CodeCommit`` , the format is the repository name and commit ID, separated by a forward slash. For example, ``my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a`` . 
                    * For ``S3`` , the format is the S3 bucket name and object key, separated by a forward slash. For example, ``my-s3-bucket/Folders/my-source-file`` . 
                - **BuildArn** *(string) --* 
                  Reference to the artifact from the AWS CodeBuild build.
                - **SourceBundle** *(dict) --* 
                  The storage location of the application version's source bundle in Amazon S3.
                  - **S3Bucket** *(string) --* 
                    The Amazon S3 bucket where the data is located.
                  - **S3Key** *(string) --* 
                    The Amazon S3 key where the data is located.
                - **DateCreated** *(datetime) --* 
                  The creation date of the application version.
                - **DateUpdated** *(datetime) --* 
                  The last modified date of the application version.
                - **Status** *(string) --* 
                  The processing status of the application version. Reflects the state of the application version during its creation. Many of the values are only applicable if you specified ``True`` for the ``Process`` parameter of the ``CreateApplicationVersion`` action. The following list describes the possible values.
                  * ``Unprocessed`` – Application version wasn't pre-processed or validated. Elastic Beanstalk will validate configuration files during deployment of the application version to an environment. 
                  * ``Processing`` – Elastic Beanstalk is currently processing the application version. 
                  * ``Building`` – Application version is currently undergoing an AWS CodeBuild build. 
                  * ``Processed`` – Elastic Beanstalk was successfully pre-processed and validated. 
                  * ``Failed`` – Either the AWS CodeBuild build failed or configuration files didn't pass validation. This application version isn't usable. 
        :type ApplicationName: string
        :param ApplicationName:
          Specify an application name to show only application versions for that application.
        :type VersionLabels: list
        :param VersionLabels:
          Specify a version label to show a specific application version.
          - *(string) --*
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


class DescribeEnvironmentManagedActionHistory(Paginator):
    def paginate(self, EnvironmentId: str = None, EnvironmentName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ElasticBeanstalk.Client.describe_environment_managed_action_history`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribeEnvironmentManagedActionHistory>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              EnvironmentId='string',
              EnvironmentName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ManagedActionHistoryItems': [
                    {
                        'ActionId': 'string',
                        'ActionType': 'InstanceRefresh'|'PlatformUpdate'|'Unknown',
                        'ActionDescription': 'string',
                        'FailureType': 'UpdateCancelled'|'CancellationFailed'|'RollbackFailed'|'RollbackSuccessful'|'InternalFailure'|'InvalidEnvironmentState'|'PermissionsError',
                        'Status': 'Completed'|'Failed'|'Unknown',
                        'FailureDescription': 'string',
                        'ExecutedTime': datetime(2015, 1, 1),
                        'FinishedTime': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            A result message containing a list of completed and failed managed actions.
            - **ManagedActionHistoryItems** *(list) --* 
              A list of completed and failed managed actions.
              - *(dict) --* 
                The record of a completed or failed managed action.
                - **ActionId** *(string) --* 
                  A unique identifier for the managed action.
                - **ActionType** *(string) --* 
                  The type of the managed action.
                - **ActionDescription** *(string) --* 
                  A description of the managed action.
                - **FailureType** *(string) --* 
                  If the action failed, the type of failure.
                - **Status** *(string) --* 
                  The status of the action.
                - **FailureDescription** *(string) --* 
                  If the action failed, a description of the failure.
                - **ExecutedTime** *(datetime) --* 
                  The date and time that the action started executing.
                - **FinishedTime** *(datetime) --* 
                  The date and time that the action finished executing.
        :type EnvironmentId: string
        :param EnvironmentId:
          The environment ID of the target environment.
        :type EnvironmentName: string
        :param EnvironmentName:
          The name of the target environment.
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


class DescribeEnvironments(Paginator):
    def paginate(self, ApplicationName: str = None, VersionLabel: str = None, EnvironmentIds: List = None, EnvironmentNames: List = None, IncludeDeleted: bool = None, IncludedDeletedBackTo: datetime = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ElasticBeanstalk.Client.describe_environments`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribeEnvironments>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ApplicationName='string',
              VersionLabel='string',
              EnvironmentIds=[
                  'string',
              ],
              EnvironmentNames=[
                  'string',
              ],
              IncludeDeleted=True|False,
              IncludedDeletedBackTo=datetime(2015, 1, 1),
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Environments': [
                    {
                        'EnvironmentName': 'string',
                        'EnvironmentId': 'string',
                        'ApplicationName': 'string',
                        'VersionLabel': 'string',
                        'SolutionStackName': 'string',
                        'PlatformArn': 'string',
                        'TemplateName': 'string',
                        'Description': 'string',
                        'EndpointURL': 'string',
                        'CNAME': 'string',
                        'DateCreated': datetime(2015, 1, 1),
                        'DateUpdated': datetime(2015, 1, 1),
                        'Status': 'Launching'|'Updating'|'Ready'|'Terminating'|'Terminated',
                        'AbortableOperationInProgress': True|False,
                        'Health': 'Green'|'Yellow'|'Red'|'Grey',
                        'HealthStatus': 'NoData'|'Unknown'|'Pending'|'Ok'|'Info'|'Warning'|'Degraded'|'Severe'|'Suspended',
                        'Resources': {
                            'LoadBalancer': {
                                'LoadBalancerName': 'string',
                                'Domain': 'string',
                                'Listeners': [
                                    {
                                        'Protocol': 'string',
                                        'Port': 123
                                    },
                                ]
                            }
                        },
                        'Tier': {
                            'Name': 'string',
                            'Type': 'string',
                            'Version': 'string'
                        },
                        'EnvironmentLinks': [
                            {
                                'LinkName': 'string',
                                'EnvironmentName': 'string'
                            },
                        ],
                        'EnvironmentArn': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Result message containing a list of environment descriptions.
            - **Environments** *(list) --* 
              Returns an  EnvironmentDescription list. 
              - *(dict) --* 
                Describes the properties of an environment.
                - **EnvironmentName** *(string) --* 
                  The name of this environment.
                - **EnvironmentId** *(string) --* 
                  The ID of this environment.
                - **ApplicationName** *(string) --* 
                  The name of the application associated with this environment.
                - **VersionLabel** *(string) --* 
                  The application version deployed in this environment.
                - **SolutionStackName** *(string) --* 
                  The name of the ``SolutionStack`` deployed with this environment. 
                - **PlatformArn** *(string) --* 
                  The ARN of the platform.
                - **TemplateName** *(string) --* 
                  The name of the configuration template used to originally launch this environment.
                - **Description** *(string) --* 
                  Describes this environment.
                - **EndpointURL** *(string) --* 
                  For load-balanced, autoscaling environments, the URL to the LoadBalancer. For single-instance environments, the IP address of the instance.
                - **CNAME** *(string) --* 
                  The URL to the CNAME for this environment.
                - **DateCreated** *(datetime) --* 
                  The creation date for this environment.
                - **DateUpdated** *(datetime) --* 
                  The last modified date for this environment.
                - **Status** *(string) --* 
                  The current operational status of the environment:
                  * ``Launching`` : Environment is in the process of initial deployment. 
                  * ``Updating`` : Environment is in the process of updating its configuration settings or application version. 
                  * ``Ready`` : Environment is available to have an action performed on it, such as update or terminate. 
                  * ``Terminating`` : Environment is in the shut-down process. 
                  * ``Terminated`` : Environment is not running. 
                - **AbortableOperationInProgress** *(boolean) --* 
                  Indicates if there is an in-progress environment configuration update or application version deployment that you can cancel.
                   ``true:`` There is an update in progress. 
                   ``false:`` There are no updates currently in progress. 
                - **Health** *(string) --* 
                  Describes the health status of the environment. AWS Elastic Beanstalk indicates the failure levels for a running environment:
                  * ``Red`` : Indicates the environment is not responsive. Occurs when three or more consecutive failures occur for an environment. 
                  * ``Yellow`` : Indicates that something is wrong. Occurs when two consecutive failures occur for an environment. 
                  * ``Green`` : Indicates the environment is healthy and fully functional. 
                  * ``Grey`` : Default health for a new environment. The environment is not fully launched and health checks have not started or health checks are suspended during an ``UpdateEnvironment`` or ``RestartEnvironment`` request. 
                  Default: ``Grey``  
                - **HealthStatus** *(string) --* 
                  Returns the health status of the application running in your environment. For more information, see `Health Colors and Statuses <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ .
                - **Resources** *(dict) --* 
                  The description of the AWS resources used by this environment.
                  - **LoadBalancer** *(dict) --* 
                    Describes the LoadBalancer.
                    - **LoadBalancerName** *(string) --* 
                      The name of the LoadBalancer.
                    - **Domain** *(string) --* 
                      The domain name of the LoadBalancer.
                    - **Listeners** *(list) --* 
                      A list of Listeners used by the LoadBalancer.
                      - *(dict) --* 
                        Describes the properties of a Listener for the LoadBalancer.
                        - **Protocol** *(string) --* 
                          The protocol that is used by the Listener.
                        - **Port** *(integer) --* 
                          The port that is used by the Listener.
                - **Tier** *(dict) --* 
                  Describes the current tier of this environment.
                  - **Name** *(string) --* 
                    The name of this environment tier.
                    Valid values:
                    * For *Web server tier* – ``WebServer``   
                    * For *Worker tier* – ``Worker``   
                  - **Type** *(string) --* 
                    The type of this environment tier.
                    Valid values:
                    * For *Web server tier* – ``Standard``   
                    * For *Worker tier* – ``SQS/HTTP``   
                  - **Version** *(string) --* 
                    The version of this environment tier. When you don't set a value to it, Elastic Beanstalk uses the latest compatible worker tier version.
                    .. note::
                      This member is deprecated. Any specific version that you set may become out of date. We recommend leaving it unspecified.
                - **EnvironmentLinks** *(list) --* 
                  A list of links to other environments in the same group.
                  - *(dict) --* 
                    A link to another environment, defined in the environment's manifest. Links provide connection information in system properties that can be used to connect to another environment in the same group. See `Environment Manifest (env.yaml) <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__ for details.
                    - **LinkName** *(string) --* 
                      The name of the link.
                    - **EnvironmentName** *(string) --* 
                      The name of the linked environment (the dependency).
                - **EnvironmentArn** *(string) --* 
                  The environment's Amazon Resource Name (ARN), which can be used in other API requests that require an ARN.
        :type ApplicationName: string
        :param ApplicationName:
          If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that are associated with this application.
        :type VersionLabel: string
        :param VersionLabel:
          If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that are associated with this application version.
        :type EnvironmentIds: list
        :param EnvironmentIds:
          If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that have the specified IDs.
          - *(string) --*
        :type EnvironmentNames: list
        :param EnvironmentNames:
          If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that have the specified names.
          - *(string) --*
        :type IncludeDeleted: boolean
        :param IncludeDeleted:
          Indicates whether to include deleted environments:
           ``true`` : Environments that have been deleted after ``IncludedDeletedBackTo`` are displayed.
           ``false`` : Do not include deleted environments.
        :type IncludedDeletedBackTo: datetime
        :param IncludedDeletedBackTo:
          If specified when ``IncludeDeleted`` is set to ``true`` , then environments deleted after this date are displayed.
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


class DescribeEvents(Paginator):
    def paginate(self, ApplicationName: str = None, VersionLabel: str = None, TemplateName: str = None, EnvironmentId: str = None, EnvironmentName: str = None, PlatformArn: str = None, RequestId: str = None, Severity: str = None, StartTime: datetime = None, EndTime: datetime = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ElasticBeanstalk.Client.describe_events`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribeEvents>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ApplicationName='string',
              VersionLabel='string',
              TemplateName='string',
              EnvironmentId='string',
              EnvironmentName='string',
              PlatformArn='string',
              RequestId='string',
              Severity='TRACE'|'DEBUG'|'INFO'|'WARN'|'ERROR'|'FATAL',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Events': [
                    {
                        'EventDate': datetime(2015, 1, 1),
                        'Message': 'string',
                        'ApplicationName': 'string',
                        'VersionLabel': 'string',
                        'TemplateName': 'string',
                        'EnvironmentName': 'string',
                        'PlatformArn': 'string',
                        'RequestId': 'string',
                        'Severity': 'TRACE'|'DEBUG'|'INFO'|'WARN'|'ERROR'|'FATAL'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Result message wrapping a list of event descriptions.
            - **Events** *(list) --* 
              A list of  EventDescription . 
              - *(dict) --* 
                Describes an event.
                - **EventDate** *(datetime) --* 
                  The date when the event occurred.
                - **Message** *(string) --* 
                  The event message.
                - **ApplicationName** *(string) --* 
                  The application associated with the event.
                - **VersionLabel** *(string) --* 
                  The release label for the application version associated with this event.
                - **TemplateName** *(string) --* 
                  The name of the configuration associated with this event.
                - **EnvironmentName** *(string) --* 
                  The name of the environment associated with this event.
                - **PlatformArn** *(string) --* 
                  The ARN of the platform.
                - **RequestId** *(string) --* 
                  The web service request ID for the activity of this event.
                - **Severity** *(string) --* 
                  The severity level of this event.
        :type ApplicationName: string
        :param ApplicationName:
          If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those associated with this application.
        :type VersionLabel: string
        :param VersionLabel:
          If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this application version.
        :type TemplateName: string
        :param TemplateName:
          If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that are associated with this environment configuration.
        :type EnvironmentId: string
        :param EnvironmentId:
          If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this environment.
        :type EnvironmentName: string
        :param EnvironmentName:
          If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this environment.
        :type PlatformArn: string
        :param PlatformArn:
          The ARN of the version of the custom platform.
        :type RequestId: string
        :param RequestId:
          If specified, AWS Elastic Beanstalk restricts the described events to include only those associated with this request ID.
        :type Severity: string
        :param Severity:
          If specified, limits the events returned from this call to include only those with the specified severity or higher.
        :type StartTime: datetime
        :param StartTime:
          If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that occur on or after this time.
        :type EndTime: datetime
        :param EndTime:
          If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that occur up to, but not including, the ``EndTime`` .
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


class ListPlatformVersions(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ElasticBeanstalk.Client.list_platform_versions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/ListPlatformVersions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Type': 'string',
                      'Operator': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'PlatformSummaryList': [
                    {
                        'PlatformArn': 'string',
                        'PlatformOwner': 'string',
                        'PlatformStatus': 'Creating'|'Failed'|'Ready'|'Deleting'|'Deleted',
                        'PlatformCategory': 'string',
                        'OperatingSystemName': 'string',
                        'OperatingSystemVersion': 'string',
                        'SupportedTierList': [
                            'string',
                        ],
                        'SupportedAddonList': [
                            'string',
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PlatformSummaryList** *(list) --* 
              Detailed information about the platforms.
              - *(dict) --* 
                Detailed information about a platform.
                - **PlatformArn** *(string) --* 
                  The ARN of the platform.
                - **PlatformOwner** *(string) --* 
                  The AWS account ID of the person who created the platform.
                - **PlatformStatus** *(string) --* 
                  The status of the platform. You can create an environment from the platform once it is ready.
                - **PlatformCategory** *(string) --* 
                  The category of platform.
                - **OperatingSystemName** *(string) --* 
                  The operating system used by the platform.
                - **OperatingSystemVersion** *(string) --* 
                  The version of the operating system used by the platform.
                - **SupportedTierList** *(list) --* 
                  The tiers in which the platform runs.
                  - *(string) --* 
                - **SupportedAddonList** *(list) --* 
                  The additions associated with the platform.
                  - *(string) --* 
        :type Filters: list
        :param Filters:
          List only the platforms where the platform member value relates to one of the supplied values.
          - *(dict) --*
            Specify criteria to restrict the results when listing custom platforms.
            The filter is evaluated as the expression:
             ``Type``  ``Operator``  ``Values[i]``
            - **Type** *(string) --*
              The custom platform attribute to which the filter values are applied.
              Valid Values: ``PlatformName`` | ``PlatformVersion`` | ``PlatformStatus`` | ``PlatformOwner``
            - **Operator** *(string) --*
              The operator to apply to the ``Type`` with each of the ``Values`` .
              Valid Values: ``=`` (equal to) | ``!=`` (not equal to) | ``<`` (less than) | ``<=`` (less than or equal to) | ``>`` (greater than) | ``>=`` (greater than or equal to) | ``contains`` | ``begins_with`` | ``ends_with``
            - **Values** *(list) --*
              The list of values applied to the custom platform attribute.
              - *(string) --*
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
