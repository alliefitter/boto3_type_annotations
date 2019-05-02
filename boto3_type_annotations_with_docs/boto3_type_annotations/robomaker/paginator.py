from typing import Dict
from typing import List
from botocore.paginate import Paginator


class ListDeploymentJobs(Paginator):
    def paginate(self, filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`RoboMaker.Client.list_deployment_jobs`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/ListDeploymentJobs>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              filters=[
                  {
                      'name': 'string',
                      'values': [
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
                'deploymentJobs': [
                    {
                        'arn': 'string',
                        'fleet': 'string',
                        'status': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded',
                        'deploymentApplicationConfigs': [
                            {
                                'application': 'string',
                                'applicationVersion': 'string',
                                'launchConfig': {
                                    'packageName': 'string',
                                    'preLaunchFile': 'string',
                                    'launchFile': 'string',
                                    'postLaunchFile': 'string',
                                    'environmentVariables': {
                                        'string': 'string'
                                    }
                                }
                            },
                        ],
                        'deploymentConfig': {
                            'concurrentDeploymentPercentage': 123,
                            'failureThresholdPercentage': 123
                        },
                        'failureReason': 'string',
                        'failureCode': 'ResourceNotFound'|'EnvironmentSetupError'|'EtagMismatch'|'FailureThresholdBreached'|'RobotDeploymentNoResponse'|'RobotAgentConnectionTimeout'|'GreengrassDeploymentFailed'|'MissingRobotArchitecture'|'MissingRobotApplicationArchitecture'|'MissingRobotDeploymentResource'|'GreengrassGroupVersionDoesNotExist'|'ExtractingBundleFailure'|'PreLaunchFileFailure'|'PostLaunchFileFailure'|'BadPermissionError'|'InternalServerError',
                        'createdAt': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **deploymentJobs** *(list) --* 
              A list of deployment jobs that meet the criteria of the request.
              - *(dict) --* 
                Information about a deployment job.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the deployment job.
                - **fleet** *(string) --* 
                  The Amazon Resource Name (ARN) of the fleet.
                - **status** *(string) --* 
                  The status of the deployment job.
                - **deploymentApplicationConfigs** *(list) --* 
                  The deployment application configuration.
                  - *(dict) --* 
                    Information about a deployment application configuration.
                    - **application** *(string) --* 
                      The Amazon Resource Name (ARN) of the robot application.
                    - **applicationVersion** *(string) --* 
                      The version of the application.
                    - **launchConfig** *(dict) --* 
                      The launch configuration.
                      - **packageName** *(string) --* 
                        The package name.
                      - **preLaunchFile** *(string) --* 
                        The deployment pre-launch file. This file will be executed prior to the launch file.
                      - **launchFile** *(string) --* 
                        The launch file name.
                      - **postLaunchFile** *(string) --* 
                        The deployment post-launch file. This file will be executed after the launch file.
                      - **environmentVariables** *(dict) --* 
                        An array of key/value pairs specifying environment variables for the robot application
                        - *(string) --* 
                          - *(string) --* 
                - **deploymentConfig** *(dict) --* 
                  The deployment configuration.
                  - **concurrentDeploymentPercentage** *(integer) --* 
                    The percentage of robots receiving the deployment at the same time.
                  - **failureThresholdPercentage** *(integer) --* 
                    The percentage of deployments that need to fail before stopping deployment.
                - **failureReason** *(string) --* 
                  A short description of the reason why the deployment job failed.
                - **failureCode** *(string) --* 
                  The deployment job failure code.
                - **createdAt** *(datetime) --* 
                  The time, in milliseconds since the epoch, when the deployment job was created.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type filters: list
        :param filters:
          Optional filters to limit results.
          The filter names ``status`` and ``fleetName`` are supported. When filtering, you must use the complete value of the filtered item. You can use up to three filters, but they must be for the same named item. For example, if you are looking for items with the status ``InProgress`` or the status ``Pending`` .
          - *(dict) --*
            Information about a filter.
            - **name** *(string) --*
              The name of the filter.
            - **values** *(list) --*
              A list of values.
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


class ListFleets(Paginator):
    def paginate(self, filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`RoboMaker.Client.list_fleets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/ListFleets>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              filters=[
                  {
                      'name': 'string',
                      'values': [
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
                'fleetDetails': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastDeploymentStatus': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded',
                        'lastDeploymentJob': 'string',
                        'lastDeploymentTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **fleetDetails** *(list) --* 
              A list of fleet details meeting the request criteria.
              - *(dict) --* 
                Information about a fleet.
                - **name** *(string) --* 
                  The name of the fleet.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the fleet.
                - **createdAt** *(datetime) --* 
                  The time, in milliseconds since the epoch, when the fleet was created.
                - **lastDeploymentStatus** *(string) --* 
                  The status of the last fleet deployment.
                - **lastDeploymentJob** *(string) --* 
                  The Amazon Resource Name (ARN) of the last deployment job.
                - **lastDeploymentTime** *(datetime) --* 
                  The time of the last deployment.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type filters: list
        :param filters:
          Optional filters to limit results.
          The filter name ``name`` is supported. When filtering, you must use the complete value of the filtered item. You can use up to three filters.
          - *(dict) --*
            Information about a filter.
            - **name** *(string) --*
              The name of the filter.
            - **values** *(list) --*
              A list of values.
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


class ListRobotApplications(Paginator):
    def paginate(self, versionQualifier: str = None, filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`RoboMaker.Client.list_robot_applications`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/ListRobotApplications>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              versionQualifier='string',
              filters=[
                  {
                      'name': 'string',
                      'values': [
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
                'robotApplicationSummaries': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'version': 'string',
                        'lastUpdatedAt': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **robotApplicationSummaries** *(list) --* 
              A list of robot application summaries that meet the criteria of the request.
              - *(dict) --* 
                Summary information for a robot application.
                - **name** *(string) --* 
                  The name of the robot application.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the robot.
                - **version** *(string) --* 
                  The version of the robot application.
                - **lastUpdatedAt** *(datetime) --* 
                  The time, in milliseconds since the epoch, when the robot application was last updated.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type versionQualifier: string
        :param versionQualifier:
          The version qualifier of the robot application.
        :type filters: list
        :param filters:
          Optional filters to limit results.
          The filter name ``name`` is supported. When filtering, you must use the complete value of the filtered item. You can use up to three filters.
          - *(dict) --*
            Information about a filter.
            - **name** *(string) --*
              The name of the filter.
            - **values** *(list) --*
              A list of values.
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


class ListRobots(Paginator):
    def paginate(self, filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`RoboMaker.Client.list_robots`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/ListRobots>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              filters=[
                  {
                      'name': 'string',
                      'values': [
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
                'robots': [
                    {
                        'arn': 'string',
                        'name': 'string',
                        'fleetArn': 'string',
                        'status': 'Available'|'Registered'|'PendingNewDeployment'|'Deploying'|'Failed'|'InSync'|'NoResponse',
                        'greenGrassGroupId': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'architecture': 'X86_64'|'ARM64'|'ARMHF',
                        'lastDeploymentJob': 'string',
                        'lastDeploymentTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **robots** *(list) --* 
              A list of robots that meet the criteria of the request.
              - *(dict) --* 
                Information about a robot.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the robot.
                - **name** *(string) --* 
                  The name of the robot.
                - **fleetArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the fleet.
                - **status** *(string) --* 
                  The status of the robot.
                - **greenGrassGroupId** *(string) --* 
                  The Greengrass group associated with the robot.
                - **createdAt** *(datetime) --* 
                  The time, in milliseconds since the epoch, when the robot was created.
                - **architecture** *(string) --* 
                  The architecture of the robot.
                - **lastDeploymentJob** *(string) --* 
                  The Amazon Resource Name (ARN) of the last deployment job.
                - **lastDeploymentTime** *(datetime) --* 
                  The time of the last deployment.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type filters: list
        :param filters:
          Optional filters to limit results.
          The filter names ``status`` and ``fleetName`` are supported. When filtering, you must use the complete value of the filtered item. You can use up to three filters, but they must be for the same named item. For example, if you are looking for items with the status ``Registered`` or the status ``Available`` .
          - *(dict) --*
            Information about a filter.
            - **name** *(string) --*
              The name of the filter.
            - **values** *(list) --*
              A list of values.
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


class ListSimulationApplications(Paginator):
    def paginate(self, versionQualifier: str = None, filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`RoboMaker.Client.list_simulation_applications`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/ListSimulationApplications>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              versionQualifier='string',
              filters=[
                  {
                      'name': 'string',
                      'values': [
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
                'simulationApplicationSummaries': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'version': 'string',
                        'lastUpdatedAt': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **simulationApplicationSummaries** *(list) --* 
              A list of simulation application summaries that meet the criteria of the request.
              - *(dict) --* 
                Summary information for a simulation application.
                - **name** *(string) --* 
                  The name of the simulation application.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the simulation application.
                - **version** *(string) --* 
                  The version of the simulation application.
                - **lastUpdatedAt** *(datetime) --* 
                  The time, in milliseconds since the epoch, when the simulation application was last updated.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type versionQualifier: string
        :param versionQualifier:
          The version qualifier of the simulation application.
        :type filters: list
        :param filters:
          Optional list of filters to limit results.
          The filter name ``name`` is supported. When filtering, you must use the complete value of the filtered item. You can use up to three filters.
          - *(dict) --*
            Information about a filter.
            - **name** *(string) --*
              The name of the filter.
            - **values** *(list) --*
              A list of values.
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


class ListSimulationJobs(Paginator):
    def paginate(self, filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`RoboMaker.Client.list_simulation_jobs`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/ListSimulationJobs>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              filters=[
                  {
                      'name': 'string',
                      'values': [
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
                'simulationJobSummaries': [
                    {
                        'arn': 'string',
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'name': 'string',
                        'status': 'Pending'|'Preparing'|'Running'|'Restarting'|'Completed'|'Failed'|'RunningFailed'|'Terminating'|'Terminated'|'Canceled',
                        'simulationApplicationNames': [
                            'string',
                        ],
                        'robotApplicationNames': [
                            'string',
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **simulationJobSummaries** *(list) --* 
              A list of simulation job summaries that meet the criteria of the request.
              - *(dict) --* 
                Summary information for a simulation job.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the simulation job.
                - **lastUpdatedAt** *(datetime) --* 
                  The time, in milliseconds since the epoch, when the simulation job was last updated.
                - **name** *(string) --* 
                  The name of the simulation job.
                - **status** *(string) --* 
                  The status of the simulation job.
                - **simulationApplicationNames** *(list) --* 
                  A list of simulation job simulation application names.
                  - *(string) --* 
                - **robotApplicationNames** *(list) --* 
                  A list of simulation job robot application names.
                  - *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type filters: list
        :param filters:
          Optional filters to limit results.
          The filter names ``status`` and ``simulationApplicationName`` and ``robotApplicationName`` are supported. When filtering, you must use the complete value of the filtered item. You can use up to three filters, but they must be for the same named item. For example, if you are looking for items with the status ``Preparing`` or the status ``Running`` .
          - *(dict) --*
            Information about a filter.
            - **name** *(string) --*
              The name of the filter.
            - **values** *(list) --*
              A list of values.
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
