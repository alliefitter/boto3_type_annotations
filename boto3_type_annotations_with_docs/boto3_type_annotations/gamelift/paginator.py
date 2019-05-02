from typing import Dict
from typing import List
from datetime import datetime
from botocore.paginate import Paginator


class DescribeFleetAttributes(Paginator):
    def paginate(self, FleetIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`GameLift.Client.describe_fleet_attributes`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeFleetAttributes>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              FleetIds=[
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
                'FleetAttributes': [
                    {
                        'FleetId': 'string',
                        'FleetArn': 'string',
                        'FleetType': 'ON_DEMAND'|'SPOT',
                        'InstanceType': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge',
                        'Description': 'string',
                        'Name': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'TerminationTime': datetime(2015, 1, 1),
                        'Status': 'NEW'|'DOWNLOADING'|'VALIDATING'|'BUILDING'|'ACTIVATING'|'ACTIVE'|'DELETING'|'ERROR'|'TERMINATED',
                        'BuildId': 'string',
                        'ScriptId': 'string',
                        'ServerLaunchPath': 'string',
                        'ServerLaunchParameters': 'string',
                        'LogPaths': [
                            'string',
                        ],
                        'NewGameSessionProtectionPolicy': 'NoProtection'|'FullProtection',
                        'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX',
                        'ResourceCreationLimitPolicy': {
                            'NewGameSessionsPerCreator': 123,
                            'PolicyPeriodInMinutes': 123
                        },
                        'MetricGroups': [
                            'string',
                        ],
                        'StoppedActions': [
                            'AUTO_SCALING',
                        ],
                        'InstanceRoleArn': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the returned data in response to a request action.
            - **FleetAttributes** *(list) --* 
              Collection of objects containing attribute metadata for each requested fleet ID.
              - *(dict) --* 
                General properties describing a fleet.
                *  CreateFleet   
                *  ListFleets   
                *  DeleteFleet   
                * Describe fleets: 
                  *  DescribeFleetAttributes   
                  *  DescribeFleetCapacity   
                  *  DescribeFleetPortSettings   
                  *  DescribeFleetUtilization   
                  *  DescribeRuntimeConfiguration   
                  *  DescribeEC2InstanceLimits   
                  *  DescribeFleetEvents   
                * Update fleets: 
                  *  UpdateFleetAttributes   
                  *  UpdateFleetCapacity   
                  *  UpdateFleetPortSettings   
                  *  UpdateRuntimeConfiguration   
                * Manage fleet actions: 
                  *  StartFleetActions   
                  *  StopFleetActions   
                - **FleetId** *(string) --* 
                  Unique identifier for a fleet.
                - **FleetArn** *(string) --* 
                  Identifier for a fleet that is unique across all regions.
                - **FleetType** *(string) --* 
                  Indicates whether the fleet uses on-demand or spot instances. A spot instance in use may be interrupted with a two-minute notification.
                - **InstanceType** *(string) --* 
                  EC2 instance type indicating the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. See `Amazon EC2 Instance Types <http://aws.amazon.com/ec2/instance-types/>`__ for detailed descriptions.
                - **Description** *(string) --* 
                  Human-readable description of the fleet.
                - **Name** *(string) --* 
                  Descriptive label that is associated with a fleet. Fleet names do not need to be unique.
                - **CreationTime** *(datetime) --* 
                  Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").
                - **TerminationTime** *(datetime) --* 
                  Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").
                - **Status** *(string) --* 
                  Current status of the fleet.
                  Possible fleet statuses include the following:
                  * **NEW** -- A new fleet has been defined and desired instances is set to 1.  
                  * **DOWNLOADING/VALIDATING/BUILDING/ACTIVATING** -- Amazon GameLift is setting up the new fleet, creating new instances with the game build or Realtime script and starting server processes. 
                  * **ACTIVE** -- Hosts can now accept game sessions. 
                  * **ERROR** -- An error occurred when downloading, validating, building, or activating the fleet. 
                  * **DELETING** -- Hosts are responding to a delete fleet request. 
                  * **TERMINATED** -- The fleet no longer exists. 
                - **BuildId** *(string) --* 
                  Unique identifier for a build.
                - **ScriptId** *(string) --* 
                  Unique identifier for a Realtime script.
                - **ServerLaunchPath** *(string) --* 
                  Path to a game server executable in the fleet's build, specified for fleets created before 2016-08-04 (or AWS SDK v. 0.12.16). Server launch paths for fleets created after this date are specified in the fleet's  RuntimeConfiguration .
                - **ServerLaunchParameters** *(string) --* 
                  Game server launch parameters specified for fleets created before 2016-08-04 (or AWS SDK v. 0.12.16). Server launch parameters for fleets created after this date are specified in the fleet's  RuntimeConfiguration .
                - **LogPaths** *(list) --* 
                  Location of default log files. When a server process is shut down, Amazon GameLift captures and stores any log files in this location. These logs are in addition to game session logs; see more on game session logs in the `Amazon GameLift Developer Guide <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-api-server-code>`__ . If no default log path for a fleet is specified, Amazon GameLift automatically uploads logs that are stored on each instance at ``C:\game\logs`` (for Windows) or ``/local/game/logs`` (for Linux). Use the Amazon GameLift console to access stored logs. 
                  - *(string) --* 
                - **NewGameSessionProtectionPolicy** *(string) --* 
                  Type of game session protection to set for all new instances started in the fleet.
                  * **NoProtection** -- The game session can be terminated during a scale-down event. 
                  * **FullProtection** -- If the game session is in an ``ACTIVE`` status, it cannot be terminated during a scale-down event. 
                - **OperatingSystem** *(string) --* 
                  Operating system of the fleet's computing resources. A fleet's operating system depends on the OS specified for the build that is deployed on this fleet.
                - **ResourceCreationLimitPolicy** *(dict) --* 
                  Fleet policy to limit the number of game sessions an individual player can create over a span of time.
                  - **NewGameSessionsPerCreator** *(integer) --* 
                    Maximum number of game sessions that an individual can create during the policy period. 
                  - **PolicyPeriodInMinutes** *(integer) --* 
                    Time span used in evaluating the resource creation limit policy. 
                - **MetricGroups** *(list) --* 
                  Names of metric groups that this fleet is included in. In Amazon CloudWatch, you can view metrics for an individual fleet or aggregated metrics for fleets that are in a fleet metric group. A fleet can be included in only one metric group at a time.
                  - *(string) --* 
                - **StoppedActions** *(list) --* 
                  List of fleet actions that have been suspended using  StopFleetActions . This includes auto-scaling.
                  - *(string) --* 
                - **InstanceRoleArn** *(string) --* 
                  Unique identifier for an AWS IAM role that manages access to your AWS services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, daemons (background processes). Create a role or look up a role's ARN using the `IAM dashboard <https://console.aws.amazon.com/iam/>`__ in the AWS Management Console. Learn more about using on-box credentials for your game servers at `Access external resources from a game server <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`__ .
        :type FleetIds: list
        :param FleetIds:
          Unique identifier for a fleet(s) to retrieve attributes for. To request attributes for all fleets, leave this parameter empty.
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


class DescribeFleetCapacity(Paginator):
    def paginate(self, FleetIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`GameLift.Client.describe_fleet_capacity`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeFleetCapacity>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              FleetIds=[
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
                'FleetCapacity': [
                    {
                        'FleetId': 'string',
                        'InstanceType': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge',
                        'InstanceCounts': {
                            'DESIRED': 123,
                            'MINIMUM': 123,
                            'MAXIMUM': 123,
                            'PENDING': 123,
                            'ACTIVE': 123,
                            'IDLE': 123,
                            'TERMINATING': 123
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the returned data in response to a request action.
            - **FleetCapacity** *(list) --* 
              Collection of objects containing capacity information for each requested fleet ID. Leave this parameter empty to retrieve capacity information for all fleets.
              - *(dict) --* 
                Information about the fleet's capacity. Fleet capacity is measured in EC2 instances. By default, new fleets have a capacity of one instance, but can be updated as needed. The maximum number of instances for a fleet is determined by the fleet's instance type.
                *  CreateFleet   
                *  ListFleets   
                *  DeleteFleet   
                * Describe fleets: 
                  *  DescribeFleetAttributes   
                  *  DescribeFleetCapacity   
                  *  DescribeFleetPortSettings   
                  *  DescribeFleetUtilization   
                  *  DescribeRuntimeConfiguration   
                  *  DescribeEC2InstanceLimits   
                  *  DescribeFleetEvents   
                * Update fleets: 
                  *  UpdateFleetAttributes   
                  *  UpdateFleetCapacity   
                  *  UpdateFleetPortSettings   
                  *  UpdateRuntimeConfiguration   
                * Manage fleet actions: 
                  *  StartFleetActions   
                  *  StopFleetActions   
                - **FleetId** *(string) --* 
                  Unique identifier for a fleet.
                - **InstanceType** *(string) --* 
                  Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Amazon GameLift supports the following EC2 instance types. See `Amazon EC2 Instance Types <http://aws.amazon.com/ec2/instance-types/>`__ for detailed descriptions.
                - **InstanceCounts** *(dict) --* 
                  Current status of fleet capacity.
                  - **DESIRED** *(integer) --* 
                    Ideal number of active instances in the fleet.
                  - **MINIMUM** *(integer) --* 
                    Minimum value allowed for the fleet's instance count.
                  - **MAXIMUM** *(integer) --* 
                    Maximum value allowed for the fleet's instance count.
                  - **PENDING** *(integer) --* 
                    Number of instances in the fleet that are starting but not yet active.
                  - **ACTIVE** *(integer) --* 
                    Actual number of active instances in the fleet.
                  - **IDLE** *(integer) --* 
                    Number of active instances in the fleet that are not currently hosting a game session.
                  - **TERMINATING** *(integer) --* 
                    Number of instances in the fleet that are no longer active but haven't yet been terminated.
        :type FleetIds: list
        :param FleetIds:
          Unique identifier for a fleet(s) to retrieve capacity information for. To request capacity information for all fleets, leave this parameter empty.
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


class DescribeFleetEvents(Paginator):
    def paginate(self, FleetId: str, StartTime: datetime = None, EndTime: datetime = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`GameLift.Client.describe_fleet_events`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeFleetEvents>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              FleetId='string',
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
                        'EventId': 'string',
                        'ResourceId': 'string',
                        'EventCode': 'GENERIC_EVENT'|'FLEET_CREATED'|'FLEET_DELETED'|'FLEET_SCALING_EVENT'|'FLEET_STATE_DOWNLOADING'|'FLEET_STATE_VALIDATING'|'FLEET_STATE_BUILDING'|'FLEET_STATE_ACTIVATING'|'FLEET_STATE_ACTIVE'|'FLEET_STATE_ERROR'|'FLEET_INITIALIZATION_FAILED'|'FLEET_BINARY_DOWNLOAD_FAILED'|'FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND'|'FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE'|'FLEET_VALIDATION_TIMED_OUT'|'FLEET_ACTIVATION_FAILED'|'FLEET_ACTIVATION_FAILED_NO_INSTANCES'|'FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED'|'SERVER_PROCESS_INVALID_PATH'|'SERVER_PROCESS_SDK_INITIALIZATION_TIMEOUT'|'SERVER_PROCESS_PROCESS_READY_TIMEOUT'|'SERVER_PROCESS_CRASHED'|'SERVER_PROCESS_TERMINATED_UNHEALTHY'|'SERVER_PROCESS_FORCE_TERMINATED'|'SERVER_PROCESS_PROCESS_EXIT_TIMEOUT'|'GAME_SESSION_ACTIVATION_TIMEOUT'|'FLEET_CREATION_EXTRACTING_BUILD'|'FLEET_CREATION_RUNNING_INSTALLER'|'FLEET_CREATION_VALIDATING_RUNTIME_CONFIG'|'FLEET_VPC_PEERING_SUCCEEDED'|'FLEET_VPC_PEERING_FAILED'|'FLEET_VPC_PEERING_DELETED'|'INSTANCE_INTERRUPTED',
                        'Message': 'string',
                        'EventTime': datetime(2015, 1, 1),
                        'PreSignedLogUrl': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the returned data in response to a request action.
            - **Events** *(list) --* 
              Collection of objects containing event log entries for the specified fleet.
              - *(dict) --* 
                Log entry describing an event that involves Amazon GameLift resources (such as a fleet). In addition to tracking activity, event codes and messages can provide additional information for troubleshooting and debugging problems.
                - **EventId** *(string) --* 
                  Unique identifier for a fleet event.
                - **ResourceId** *(string) --* 
                  Unique identifier for an event resource, such as a fleet ID.
                - **EventCode** *(string) --* 
                  Type of event being logged. The following events are currently in use:
        
        **Fleet creation events:**
                  * FLEET_CREATED -- A fleet record was successfully created with a status of ``NEW`` . Event messaging includes the fleet ID. 
                  * FLEET_STATE_DOWNLOADING -- Fleet status changed from ``NEW`` to ``DOWNLOADING`` . The compressed build has started downloading to a fleet instance for installation. 
                  * FLEET_BINARY_DOWNLOAD_FAILED -- The build failed to download to the fleet instance. 
                  * FLEET_CREATION_EXTRACTING_BUILD – The game server build was successfully downloaded to an instance, and the build files are now being extracted from the uploaded build and saved to an instance. Failure at this stage prevents a fleet from moving to ``ACTIVE`` status. Logs for this stage display a list of the files that are extracted and saved on the instance. Access the logs by using the URL in *PreSignedLogUrl* . 
                  * FLEET_CREATION_RUNNING_INSTALLER – The game server build files were successfully extracted, and the Amazon GameLift is now running the build's install script (if one is included). Failure in this stage prevents a fleet from moving to ``ACTIVE`` status. Logs for this stage list the installation steps and whether or not the install completed successfully. Access the logs by using the URL in *PreSignedLogUrl* .  
                  * FLEET_CREATION_VALIDATING_RUNTIME_CONFIG -- The build process was successful, and the Amazon GameLift is now verifying that the game server launch paths, which are specified in the fleet's run-time configuration, exist. If any listed launch path exists, Amazon GameLift tries to launch a game server process and waits for the process to report ready. Failures in this stage prevent a fleet from moving to ``ACTIVE`` status. Logs for this stage list the launch paths in the run-time configuration and indicate whether each is found. Access the logs by using the URL in *PreSignedLogUrl* .  
                  * FLEET_STATE_VALIDATING -- Fleet status changed from ``DOWNLOADING`` to ``VALIDATING`` . 
                  * FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND -- Validation of the run-time configuration failed because the executable specified in a launch path does not exist on the instance. 
                  * FLEET_STATE_BUILDING -- Fleet status changed from ``VALIDATING`` to ``BUILDING`` . 
                  * FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE -- Validation of the run-time configuration failed because the executable specified in a launch path failed to run on the fleet instance. 
                  * FLEET_STATE_ACTIVATING -- Fleet status changed from ``BUILDING`` to ``ACTIVATING`` .  
                  * FLEET_ACTIVATION_FAILED - The fleet failed to successfully complete one of the steps in the fleet activation process. This event code indicates that the game build was successfully downloaded to a fleet instance, built, and validated, but was not able to start a server process. A possible reason for failure is that the game server is not reporting "process ready" to the Amazon GameLift service. 
                  * FLEET_STATE_ACTIVE -- The fleet's status changed from ``ACTIVATING`` to ``ACTIVE`` . The fleet is now ready to host game sessions. 
        
        **VPC peering events:**
                  * FLEET_VPC_PEERING_SUCCEEDED -- A VPC peering connection has been established between the VPC for an Amazon GameLift fleet and a VPC in your AWS account. 
                  * FLEET_VPC_PEERING_FAILED -- A requested VPC peering connection has failed. Event details and status information (see  DescribeVpcPeeringConnections ) provide additional detail. A common reason for peering failure is that the two VPCs have overlapping CIDR blocks of IPv4 addresses. To resolve this, change the CIDR block for the VPC in your AWS account. For more information on VPC peering failures, see `https\://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide/invalid-peering-configurations.html <https://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide/invalid-peering-configurations.html>`__   
                  * FLEET_VPC_PEERING_DELETED -- A VPC peering connection has been successfully deleted. 
        
        **Spot instance events:**
                  * INSTANCE_INTERRUPTED -- A spot instance was interrupted by EC2 with a two-minute notification. 
        
        **Other fleet events:**
                  * FLEET_SCALING_EVENT -- A change was made to the fleet's capacity settings (desired instances, minimum/maximum scaling limits). Event messaging includes the new capacity settings. 
                  * FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED -- A change was made to the fleet's game session protection policy setting. Event messaging includes both the old and new policy setting.  
                  * FLEET_DELETED -- A request to delete a fleet was initiated. 
                  * GENERIC_EVENT -- An unspecified event has occurred. 
                - **Message** *(string) --* 
                  Additional information related to the event.
                - **EventTime** *(datetime) --* 
                  Time stamp indicating when this event occurred. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").
                - **PreSignedLogUrl** *(string) --* 
                  Location of stored logs with additional detail that is related to the event. This is useful for debugging issues. The URL is valid for 15 minutes. You can also access fleet creation logs through the Amazon GameLift console.
        :type FleetId: string
        :param FleetId: **[REQUIRED]**
          Unique identifier for a fleet to get event logs for.
        :type StartTime: datetime
        :param StartTime:
          Earliest date to retrieve event logs for. If no start time is specified, this call returns entries starting from when the fleet was created to the specified end time. Format is a number expressed in Unix time as milliseconds (ex: \"1469498468.057\").
        :type EndTime: datetime
        :param EndTime:
          Most recent date to retrieve event logs for. If no end time is specified, this call returns entries from the specified start time up to the present. Format is a number expressed in Unix time as milliseconds (ex: \"1469498468.057\").
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


class DescribeFleetUtilization(Paginator):
    def paginate(self, FleetIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`GameLift.Client.describe_fleet_utilization`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeFleetUtilization>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              FleetIds=[
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
                'FleetUtilization': [
                    {
                        'FleetId': 'string',
                        'ActiveServerProcessCount': 123,
                        'ActiveGameSessionCount': 123,
                        'CurrentPlayerSessionCount': 123,
                        'MaximumPlayerSessionCount': 123
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the returned data in response to a request action.
            - **FleetUtilization** *(list) --* 
              Collection of objects containing utilization information for each requested fleet ID.
              - *(dict) --* 
                Current status of fleet utilization, including the number of game and player sessions being hosted.
                *  CreateFleet   
                *  ListFleets   
                *  DeleteFleet   
                * Describe fleets: 
                  *  DescribeFleetAttributes   
                  *  DescribeFleetCapacity   
                  *  DescribeFleetPortSettings   
                  *  DescribeFleetUtilization   
                  *  DescribeRuntimeConfiguration   
                  *  DescribeEC2InstanceLimits   
                  *  DescribeFleetEvents   
                * Update fleets: 
                  *  UpdateFleetAttributes   
                  *  UpdateFleetCapacity   
                  *  UpdateFleetPortSettings   
                  *  UpdateRuntimeConfiguration   
                * Manage fleet actions: 
                  *  StartFleetActions   
                  *  StopFleetActions   
                - **FleetId** *(string) --* 
                  Unique identifier for a fleet.
                - **ActiveServerProcessCount** *(integer) --* 
                  Number of server processes in an ``ACTIVE`` status currently running across all instances in the fleet
                - **ActiveGameSessionCount** *(integer) --* 
                  Number of active game sessions currently being hosted on all instances in the fleet.
                - **CurrentPlayerSessionCount** *(integer) --* 
                  Number of active player sessions currently being hosted on all instances in the fleet.
                - **MaximumPlayerSessionCount** *(integer) --* 
                  Maximum players allowed across all game sessions currently being hosted on all instances in the fleet.
        :type FleetIds: list
        :param FleetIds:
          Unique identifier for a fleet(s) to retrieve utilization data for. To request utilization data for all fleets, leave this parameter empty.
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


class DescribeGameSessionDetails(Paginator):
    def paginate(self, FleetId: str = None, GameSessionId: str = None, AliasId: str = None, StatusFilter: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`GameLift.Client.describe_game_session_details`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeGameSessionDetails>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              FleetId='string',
              GameSessionId='string',
              AliasId='string',
              StatusFilter='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'GameSessionDetails': [
                    {
                        'GameSession': {
                            'GameSessionId': 'string',
                            'Name': 'string',
                            'FleetId': 'string',
                            'CreationTime': datetime(2015, 1, 1),
                            'TerminationTime': datetime(2015, 1, 1),
                            'CurrentPlayerSessionCount': 123,
                            'MaximumPlayerSessionCount': 123,
                            'Status': 'ACTIVE'|'ACTIVATING'|'TERMINATED'|'TERMINATING'|'ERROR',
                            'StatusReason': 'INTERRUPTED',
                            'GameProperties': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ],
                            'IpAddress': 'string',
                            'Port': 123,
                            'PlayerSessionCreationPolicy': 'ACCEPT_ALL'|'DENY_ALL',
                            'CreatorId': 'string',
                            'GameSessionData': 'string',
                            'MatchmakerData': 'string'
                        },
                        'ProtectionPolicy': 'NoProtection'|'FullProtection'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the returned data in response to a request action.
            - **GameSessionDetails** *(list) --* 
              Collection of objects containing game session properties and the protection policy currently in force for each session matching the request.
              - *(dict) --* 
                A game session's properties plus the protection policy currently in force.
                - **GameSession** *(dict) --* 
                  Object that describes a game session.
                  - **GameSessionId** *(string) --* 
                    Unique identifier for the game session. A game session ARN has the following format: ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token>`` .
                  - **Name** *(string) --* 
                    Descriptive label that is associated with a game session. Session names do not need to be unique.
                  - **FleetId** *(string) --* 
                    Unique identifier for a fleet that the game session is running on.
                  - **CreationTime** *(datetime) --* 
                    Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").
                  - **TerminationTime** *(datetime) --* 
                    Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").
                  - **CurrentPlayerSessionCount** *(integer) --* 
                    Number of players currently in the game session.
                  - **MaximumPlayerSessionCount** *(integer) --* 
                    Maximum number of players that can be connected simultaneously to the game session.
                  - **Status** *(string) --* 
                    Current status of the game session. A game session must have an ``ACTIVE`` status to have player sessions.
                  - **StatusReason** *(string) --* 
                    Provides additional information about game session status. ``INTERRUPTED`` indicates that the game session was hosted on a spot instance that was reclaimed, causing the active game session to be terminated.
                  - **GameProperties** *(list) --* 
                    Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ). You can search for active game sessions based on this custom data with  SearchGameSessions .
                    - *(dict) --* 
                      Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the `Amazon GameLift Developer Guide <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__ .
                      - **Key** *(string) --* 
                        Game property identifier.
                      - **Value** *(string) --* 
                        Game property value.
                  - **IpAddress** *(string) --* 
                    IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
                  - **Port** *(integer) --* 
                    Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
                  - **PlayerSessionCreationPolicy** *(string) --* 
                    Indicates whether or not the game session is accepting new players.
                  - **CreatorId** *(string) --* 
                    Unique identifier for a player. This ID is used to enforce a resource protection policy (if one exists), that limits the number of game sessions a player can create.
                  - **GameSessionData** *(string) --* 
                    Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ).
                  - **MatchmakerData** *(string) --* 
                    Information about the matchmaking process that was used to create the game session. It is in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see `Match Data <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__ . Matchmaker data is useful when requesting match backfills, and is updated whenever new players are added during a successful backfill (see  StartMatchBackfill ). 
                - **ProtectionPolicy** *(string) --* 
                  Current status of protection for the game session.
                  * **NoProtection** -- The game session can be terminated during a scale-down event. 
                  * **FullProtection** -- If the game session is in an ``ACTIVE`` status, it cannot be terminated during a scale-down event. 
        :type FleetId: string
        :param FleetId:
          Unique identifier for a fleet to retrieve all game sessions active on the fleet.
        :type GameSessionId: string
        :param GameSessionId:
          Unique identifier for the game session to retrieve.
        :type AliasId: string
        :param AliasId:
          Unique identifier for an alias associated with the fleet to retrieve all game sessions for.
        :type StatusFilter: string
        :param StatusFilter:
          Game session status to filter results on. Possible game session statuses include ``ACTIVE`` , ``TERMINATED`` , ``ACTIVATING`` and ``TERMINATING`` (the last two are transitory).
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


class DescribeGameSessionQueues(Paginator):
    def paginate(self, Names: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`GameLift.Client.describe_game_session_queues`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeGameSessionQueues>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Names=[
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
                'GameSessionQueues': [
                    {
                        'Name': 'string',
                        'GameSessionQueueArn': 'string',
                        'TimeoutInSeconds': 123,
                        'PlayerLatencyPolicies': [
                            {
                                'MaximumIndividualPlayerLatencyMilliseconds': 123,
                                'PolicyDurationSeconds': 123
                            },
                        ],
                        'Destinations': [
                            {
                                'DestinationArn': 'string'
                            },
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the returned data in response to a request action.
            - **GameSessionQueues** *(list) --* 
              Collection of objects that describes the requested game session queues.
              - *(dict) --* 
                Configuration of a queue that is used to process game session placement requests. The queue configuration identifies several game features:
                * The destinations where a new game session can potentially be hosted. Amazon GameLift tries these destinations in an order based on either the queue's default order or player latency information, if provided in a placement request. With latency information, Amazon GameLift can place game sessions where the majority of players are reporting the lowest possible latency.  
                * The length of time that placement requests can wait in the queue before timing out.  
                * A set of optional latency policies that protect individual players from high latencies, preventing game sessions from being placed where any individual player is reporting latency higher than a policy's maximum. 
                *  CreateGameSessionQueue   
                *  DescribeGameSessionQueues   
                *  UpdateGameSessionQueue   
                *  DeleteGameSessionQueue   
                - **Name** *(string) --* 
                  Descriptive label that is associated with game session queue. Queue names must be unique within each region.
                - **GameSessionQueueArn** *(string) --* 
                  Amazon Resource Name (`ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned to a game session queue and uniquely identifies it. Format is ``arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`` .
                - **TimeoutInSeconds** *(integer) --* 
                  Maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a ``TIMED_OUT`` status.
                - **PlayerLatencyPolicies** *(list) --* 
                  Collection of latency policies to apply when processing game sessions placement requests with player latency information. Multiple policies are evaluated in order of the maximum latency value, starting with the lowest latency values. With just one policy, it is enforced at the start of the game session placement for the duration period. With multiple policies, each policy is enforced consecutively for its duration period. For example, a queue might enforce a 60-second policy followed by a 120-second policy, and then no policy for the remainder of the placement. 
                  - *(dict) --* 
                    Queue setting that determines the highest latency allowed for individual players when placing a game session. When a latency policy is in force, a game session cannot be placed at any destination in a region where a player is reporting latency higher than the cap. Latency policies are only enforced when the placement request contains player latency information.
                    *  CreateGameSessionQueue   
                    *  DescribeGameSessionQueues   
                    *  UpdateGameSessionQueue   
                    *  DeleteGameSessionQueue   
                    - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --* 
                      The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.
                    - **PolicyDurationSeconds** *(integer) --* 
                      The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.
                - **Destinations** *(list) --* 
                  List of fleets that can be used to fulfill game session placement requests in the queue. Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed in default preference order.
                  - *(dict) --* 
                    Fleet designated in a game session queue. Requests for new game sessions in the queue are fulfilled by starting a new game session on any destination configured for a queue. 
                    *  CreateGameSessionQueue   
                    *  DescribeGameSessionQueues   
                    *  UpdateGameSessionQueue   
                    *  DeleteGameSessionQueue   
                    - **DestinationArn** *(string) --* 
                      Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a region name, provide a unique identifier across all regions. 
        :type Names: list
        :param Names:
          List of queue names to retrieve information for. To request settings for all queues, leave this parameter empty.
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


class DescribeGameSessions(Paginator):
    def paginate(self, FleetId: str = None, GameSessionId: str = None, AliasId: str = None, StatusFilter: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`GameLift.Client.describe_game_sessions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeGameSessions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              FleetId='string',
              GameSessionId='string',
              AliasId='string',
              StatusFilter='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'GameSessions': [
                    {
                        'GameSessionId': 'string',
                        'Name': 'string',
                        'FleetId': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'TerminationTime': datetime(2015, 1, 1),
                        'CurrentPlayerSessionCount': 123,
                        'MaximumPlayerSessionCount': 123,
                        'Status': 'ACTIVE'|'ACTIVATING'|'TERMINATED'|'TERMINATING'|'ERROR',
                        'StatusReason': 'INTERRUPTED',
                        'GameProperties': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'IpAddress': 'string',
                        'Port': 123,
                        'PlayerSessionCreationPolicy': 'ACCEPT_ALL'|'DENY_ALL',
                        'CreatorId': 'string',
                        'GameSessionData': 'string',
                        'MatchmakerData': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the returned data in response to a request action.
            - **GameSessions** *(list) --* 
              Collection of objects containing game session properties for each session matching the request.
              - *(dict) --* 
                Properties describing a game session.
                A game session in ACTIVE status can host players. When a game session ends, its status is set to ``TERMINATED`` . 
                Once the session ends, the game session object is retained for 30 days. This means you can reuse idempotency token values after this time. Game session logs are retained for 14 days.
                *  CreateGameSession   
                *  DescribeGameSessions   
                *  DescribeGameSessionDetails   
                *  SearchGameSessions   
                *  UpdateGameSession   
                *  GetGameSessionLogUrl   
                * Game session placements 
                  *  StartGameSessionPlacement   
                  *  DescribeGameSessionPlacement   
                  *  StopGameSessionPlacement   
                - **GameSessionId** *(string) --* 
                  Unique identifier for the game session. A game session ARN has the following format: ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token>`` .
                - **Name** *(string) --* 
                  Descriptive label that is associated with a game session. Session names do not need to be unique.
                - **FleetId** *(string) --* 
                  Unique identifier for a fleet that the game session is running on.
                - **CreationTime** *(datetime) --* 
                  Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").
                - **TerminationTime** *(datetime) --* 
                  Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").
                - **CurrentPlayerSessionCount** *(integer) --* 
                  Number of players currently in the game session.
                - **MaximumPlayerSessionCount** *(integer) --* 
                  Maximum number of players that can be connected simultaneously to the game session.
                - **Status** *(string) --* 
                  Current status of the game session. A game session must have an ``ACTIVE`` status to have player sessions.
                - **StatusReason** *(string) --* 
                  Provides additional information about game session status. ``INTERRUPTED`` indicates that the game session was hosted on a spot instance that was reclaimed, causing the active game session to be terminated.
                - **GameProperties** *(list) --* 
                  Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ). You can search for active game sessions based on this custom data with  SearchGameSessions .
                  - *(dict) --* 
                    Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the `Amazon GameLift Developer Guide <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__ .
                    - **Key** *(string) --* 
                      Game property identifier.
                    - **Value** *(string) --* 
                      Game property value.
                - **IpAddress** *(string) --* 
                  IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
                - **Port** *(integer) --* 
                  Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
                - **PlayerSessionCreationPolicy** *(string) --* 
                  Indicates whether or not the game session is accepting new players.
                - **CreatorId** *(string) --* 
                  Unique identifier for a player. This ID is used to enforce a resource protection policy (if one exists), that limits the number of game sessions a player can create.
                - **GameSessionData** *(string) --* 
                  Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ).
                - **MatchmakerData** *(string) --* 
                  Information about the matchmaking process that was used to create the game session. It is in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see `Match Data <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__ . Matchmaker data is useful when requesting match backfills, and is updated whenever new players are added during a successful backfill (see  StartMatchBackfill ). 
        :type FleetId: string
        :param FleetId:
          Unique identifier for a fleet to retrieve all game sessions for.
        :type GameSessionId: string
        :param GameSessionId:
          Unique identifier for the game session to retrieve. You can use either a ``GameSessionId`` or ``GameSessionArn`` value.
        :type AliasId: string
        :param AliasId:
          Unique identifier for an alias associated with the fleet to retrieve all game sessions for.
        :type StatusFilter: string
        :param StatusFilter:
          Game session status to filter results on. Possible game session statuses include ``ACTIVE`` , ``TERMINATED`` , ``ACTIVATING`` , and ``TERMINATING`` (the last two are transitory).
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


class DescribeInstances(Paginator):
    def paginate(self, FleetId: str, InstanceId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`GameLift.Client.describe_instances`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeInstances>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              FleetId='string',
              InstanceId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Instances': [
                    {
                        'FleetId': 'string',
                        'InstanceId': 'string',
                        'IpAddress': 'string',
                        'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX',
                        'Type': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge',
                        'Status': 'PENDING'|'ACTIVE'|'TERMINATING',
                        'CreationTime': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the returned data in response to a request action.
            - **Instances** *(list) --* 
              Collection of objects containing properties for each instance returned.
              - *(dict) --* 
                Properties that describe an instance of a virtual computing resource that hosts one or more game servers. A fleet may contain zero or more instances.
                - **FleetId** *(string) --* 
                  Unique identifier for a fleet that the instance is in.
                - **InstanceId** *(string) --* 
                  Unique identifier for an instance.
                - **IpAddress** *(string) --* 
                  IP address assigned to the instance.
                - **OperatingSystem** *(string) --* 
                  Operating system that is running on this instance. 
                - **Type** *(string) --* 
                  EC2 instance type that defines the computing resources of this instance. 
                - **Status** *(string) --* 
                  Current status of the instance. Possible statuses include the following:
                  * **PENDING** -- The instance is in the process of being created and launching server processes as defined in the fleet's run-time configuration.  
                  * **ACTIVE** -- The instance has been successfully created and at least one server process has successfully launched and reported back to Amazon GameLift that it is ready to host a game session. The instance is now considered ready to host game sessions.  
                  * **TERMINATING** -- The instance is in the process of shutting down. This may happen to reduce capacity during a scaling down event or to recycle resources in the event of a problem. 
                - **CreationTime** *(datetime) --* 
                  Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").
        :type FleetId: string
        :param FleetId: **[REQUIRED]**
          Unique identifier for a fleet to retrieve instance information for.
        :type InstanceId: string
        :param InstanceId:
          Unique identifier for an instance to retrieve. Specify an instance ID or leave blank to retrieve all instances in the fleet.
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


class DescribeMatchmakingConfigurations(Paginator):
    def paginate(self, Names: List = None, RuleSetName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`GameLift.Client.describe_matchmaking_configurations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeMatchmakingConfigurations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Names=[
                  'string',
              ],
              RuleSetName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Configurations': [
                    {
                        'Name': 'string',
                        'Description': 'string',
                        'GameSessionQueueArns': [
                            'string',
                        ],
                        'RequestTimeoutSeconds': 123,
                        'AcceptanceTimeoutSeconds': 123,
                        'AcceptanceRequired': True|False,
                        'RuleSetName': 'string',
                        'NotificationTarget': 'string',
                        'AdditionalPlayerCount': 123,
                        'CustomEventData': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'GameProperties': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'GameSessionData': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the returned data in response to a request action.
            - **Configurations** *(list) --* 
              Collection of requested matchmaking configuration objects.
              - *(dict) --* 
                Guidelines for use with FlexMatch to match players into games. All matchmaking requests must specify a matchmaking configuration.
                - **Name** *(string) --* 
                  Unique identifier for a matchmaking configuration. This name is used to identify the configuration associated with a matchmaking request or ticket.
                - **Description** *(string) --* 
                  Descriptive label that is associated with matchmaking configuration.
                - **GameSessionQueueArns** *(list) --* 
                  Amazon Resource Name (`ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned to a game session queue and uniquely identifies it. Format is ``arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`` . These queues are used when placing game sessions for matches that are created with this matchmaking configuration. Queues can be located in any region.
                  - *(string) --* 
                - **RequestTimeoutSeconds** *(integer) --* 
                  Maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that time out can be resubmitted as needed.
                - **AcceptanceTimeoutSeconds** *(integer) --* 
                  Length of time (in seconds) to wait for players to accept a proposed match. If any player rejects the match or fails to accept before the timeout, the ticket continues to look for an acceptable match.
                - **AcceptanceRequired** *(boolean) --* 
                  Flag that determines whether or not a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to TRUE.
                - **RuleSetName** *(string) --* 
                  Unique identifier for a matchmaking rule set to use with this configuration. A matchmaking configuration can only use rule sets that are defined in the same region.
                - **NotificationTarget** *(string) --* 
                  SNS topic ARN that is set up to receive matchmaking notifications.
                - **AdditionalPlayerCount** *(integer) --* 
                  Number of player slots in a match to keep open for future players. For example, if the configuration's rule set specifies a match for a single 12-person team, and the additional player count is set to 2, only 10 players are selected for the match.
                - **CustomEventData** *(string) --* 
                  Information to attached to all events related to the matchmaking configuration. 
                - **CreationTime** *(datetime) --* 
                  Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").
                - **GameProperties** *(list) --* 
                  Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ). This information is added to the new  GameSession object that is created for a successful match. 
                  - *(dict) --* 
                    Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the `Amazon GameLift Developer Guide <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__ .
                    - **Key** *(string) --* 
                      Game property identifier.
                    - **Value** *(string) --* 
                      Game property value.
                - **GameSessionData** *(string) --* 
                  Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ). This information is added to the new  GameSession object that is created for a successful match. 
        :type Names: list
        :param Names:
          Unique identifier for a matchmaking configuration(s) to retrieve. To request all existing configurations, leave this parameter empty.
          - *(string) --*
        :type RuleSetName: string
        :param RuleSetName:
          Unique identifier for a matchmaking rule set. Use this parameter to retrieve all matchmaking configurations that use this rule set.
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


class DescribeMatchmakingRuleSets(Paginator):
    def paginate(self, Names: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`GameLift.Client.describe_matchmaking_rule_sets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeMatchmakingRuleSets>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Names=[
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
                'RuleSets': [
                    {
                        'RuleSetName': 'string',
                        'RuleSetBody': 'string',
                        'CreationTime': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the returned data in response to a request action.
            - **RuleSets** *(list) --* 
              Collection of requested matchmaking rule set objects. 
              - *(dict) --* 
                Set of rule statements, used with FlexMatch, that determine how to build a certain kind of player match. Each rule set describes a type of group to be created and defines the parameters for acceptable player matches. Rule sets are used in  MatchmakingConfiguration objects.
                A rule set may define the following elements for a match. For detailed information and examples showing how to construct a rule set, see `Build a FlexMatch Rule Set <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-rulesets.html>`__ . 
                * Teams -- Required. A rule set must define one or multiple teams for the match and set minimum and maximum team sizes. For example, a rule set might describe a 4x4 match that requires all eight slots to be filled.  
                * Player attributes -- Optional. These attributes specify a set of player characteristics to evaluate when looking for a match. Matchmaking requests that use a rule set with player attributes must provide the corresponding attribute values. For example, an attribute might specify a player's skill or level. 
                * Rules -- Optional. Rules define how to evaluate potential players for a match based on player attributes. A rule might specify minimum requirements for individual players, teams, or entire matches. For example, a rule might require each player to meet a certain skill level, each team to have at least one player in a certain role, or the match to have a minimum average skill level. or may describe an entire group--such as all teams must be evenly matched or have at least one player in a certain role.  
                * Expansions -- Optional. Expansions allow you to relax the rules after a period of time when no acceptable matches are found. This feature lets you balance getting players into games in a reasonable amount of time instead of making them wait indefinitely for the best possible match. For example, you might use an expansion to increase the maximum skill variance between players after 30 seconds. 
                - **RuleSetName** *(string) --* 
                  Unique identifier for a matchmaking rule set
                - **RuleSetBody** *(string) --* 
                  Collection of matchmaking rules, formatted as a JSON string. (Note that comments14 are not allowed in JSON, but most elements support a description field.)
                - **CreationTime** *(datetime) --* 
                  Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").
        :type Names: list
        :param Names:
          List of one or more matchmaking rule set names to retrieve details for. (Note: The rule set name is different from the optional \"name\" field in the rule set body.)
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


class DescribePlayerSessions(Paginator):
    def paginate(self, GameSessionId: str = None, PlayerId: str = None, PlayerSessionId: str = None, PlayerSessionStatusFilter: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`GameLift.Client.describe_player_sessions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribePlayerSessions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              GameSessionId='string',
              PlayerId='string',
              PlayerSessionId='string',
              PlayerSessionStatusFilter='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'PlayerSessions': [
                    {
                        'PlayerSessionId': 'string',
                        'PlayerId': 'string',
                        'GameSessionId': 'string',
                        'FleetId': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'TerminationTime': datetime(2015, 1, 1),
                        'Status': 'RESERVED'|'ACTIVE'|'COMPLETED'|'TIMEDOUT',
                        'IpAddress': 'string',
                        'Port': 123,
                        'PlayerData': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the returned data in response to a request action.
            - **PlayerSessions** *(list) --* 
              Collection of objects containing properties for each player session that matches the request.
              - *(dict) --* 
                Properties describing a player session. Player session objects are created either by creating a player session for a specific game session, or as part of a game session placement. A player session represents either a player reservation for a game session (status ``RESERVED`` ) or actual player activity in a game session (status ``ACTIVE`` ). A player session object (including player data) is automatically passed to a game session when the player connects to the game session and is validated.
                When a player disconnects, the player session status changes to ``COMPLETED`` . Once the session ends, the player session object is retained for 30 days and then removed.
                *  CreatePlayerSession   
                *  CreatePlayerSessions   
                *  DescribePlayerSessions   
                * Game session placements 
                  *  StartGameSessionPlacement   
                  *  DescribeGameSessionPlacement   
                  *  StopGameSessionPlacement   
                - **PlayerSessionId** *(string) --* 
                  Unique identifier for a player session.
                - **PlayerId** *(string) --* 
                  Unique identifier for a player that is associated with this player session.
                - **GameSessionId** *(string) --* 
                  Unique identifier for the game session that the player session is connected to.
                - **FleetId** *(string) --* 
                  Unique identifier for a fleet that the player's game session is running on.
                - **CreationTime** *(datetime) --* 
                  Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").
                - **TerminationTime** *(datetime) --* 
                  Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").
                - **Status** *(string) --* 
                  Current status of the player session.
                  Possible player session statuses include the following:
                  * **RESERVED** -- The player session request has been received, but the player has not yet connected to the server process and/or been validated.  
                  * **ACTIVE** -- The player has been validated by the server process and is currently connected. 
                  * **COMPLETED** -- The player connection has been dropped. 
                  * **TIMEDOUT** -- A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds). 
                - **IpAddress** *(string) --* 
                  IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
                - **Port** *(integer) --* 
                  Port number for the game session. To connect to a Amazon GameLift server process, an app needs both the IP address and port number.
                - **PlayerData** *(string) --* 
                  Developer-defined information related to a player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game. 
        :type GameSessionId: string
        :param GameSessionId:
          Unique identifier for the game session to retrieve player sessions for.
        :type PlayerId: string
        :param PlayerId:
          Unique identifier for a player to retrieve player sessions for.
        :type PlayerSessionId: string
        :param PlayerSessionId:
          Unique identifier for a player session to retrieve.
        :type PlayerSessionStatusFilter: string
        :param PlayerSessionStatusFilter:
          Player session status to filter results on.
          Possible player session statuses include the following:
          * **RESERVED** -- The player session request has been received, but the player has not yet connected to the server process and/or been validated.
          * **ACTIVE** -- The player has been validated by the server process and is currently connected.
          * **COMPLETED** -- The player connection has been dropped.
          * **TIMEDOUT** -- A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds).
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


class DescribeScalingPolicies(Paginator):
    def paginate(self, FleetId: str, StatusFilter: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`GameLift.Client.describe_scaling_policies`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeScalingPolicies>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              FleetId='string',
              StatusFilter='ACTIVE'|'UPDATE_REQUESTED'|'UPDATING'|'DELETE_REQUESTED'|'DELETING'|'DELETED'|'ERROR',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ScalingPolicies': [
                    {
                        'FleetId': 'string',
                        'Name': 'string',
                        'Status': 'ACTIVE'|'UPDATE_REQUESTED'|'UPDATING'|'DELETE_REQUESTED'|'DELETING'|'DELETED'|'ERROR',
                        'ScalingAdjustment': 123,
                        'ScalingAdjustmentType': 'ChangeInCapacity'|'ExactCapacity'|'PercentChangeInCapacity',
                        'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
                        'Threshold': 123.0,
                        'EvaluationPeriods': 123,
                        'MetricName': 'ActivatingGameSessions'|'ActiveGameSessions'|'ActiveInstances'|'AvailableGameSessions'|'AvailablePlayerSessions'|'CurrentPlayerSessions'|'IdleInstances'|'PercentAvailableGameSessions'|'PercentIdleInstances'|'QueueDepth'|'WaitTime',
                        'PolicyType': 'RuleBased'|'TargetBased',
                        'TargetConfiguration': {
                            'TargetValue': 123.0
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the returned data in response to a request action.
            - **ScalingPolicies** *(list) --* 
              Collection of objects containing the scaling policies matching the request.
              - *(dict) --* 
                Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the combination of name and fleet ID.
                *  DescribeFleetCapacity   
                *  UpdateFleetCapacity   
                *  DescribeEC2InstanceLimits   
                * Manage scaling policies: 
                  *  PutScalingPolicy (auto-scaling) 
                  *  DescribeScalingPolicies (auto-scaling) 
                  *  DeleteScalingPolicy (auto-scaling) 
                * Manage fleet actions: 
                  *  StartFleetActions   
                  *  StopFleetActions   
                - **FleetId** *(string) --* 
                  Unique identifier for a fleet that is associated with this scaling policy.
                - **Name** *(string) --* 
                  Descriptive label that is associated with a scaling policy. Policy names do not need to be unique.
                - **Status** *(string) --* 
                  Current status of the scaling policy. The scaling policy can be in force only when in an ``ACTIVE`` status. Scaling policies can be suspended for individual fleets (see  StopFleetActions ; if suspended for a fleet, the policy status does not change. View a fleet's stopped actions by calling  DescribeFleetCapacity .
                  * **ACTIVE** -- The scaling policy can be used for auto-scaling a fleet. 
                  * **UPDATE_REQUESTED** -- A request to update the scaling policy has been received. 
                  * **UPDATING** -- A change is being made to the scaling policy. 
                  * **DELETE_REQUESTED** -- A request to delete the scaling policy has been received. 
                  * **DELETING** -- The scaling policy is being deleted. 
                  * **DELETED** -- The scaling policy has been deleted. 
                  * **ERROR** -- An error occurred in creating the policy. It should be removed and recreated. 
                - **ScalingAdjustment** *(integer) --* 
                  Amount of adjustment to make, based on the scaling adjustment type.
                - **ScalingAdjustmentType** *(string) --* 
                  Type of adjustment to make to a fleet's instance count (see  FleetCapacity ):
                  * **ChangeInCapacity** -- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down. 
                  * **ExactCapacity** -- set the instance count to the scaling adjustment value. 
                  * **PercentChangeInCapacity** -- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down. 
                - **ComparisonOperator** *(string) --* 
                  Comparison operator to use when measuring a metric against the threshold value.
                - **Threshold** *(float) --* 
                  Metric value used to trigger a scaling event.
                - **EvaluationPeriods** *(integer) --* 
                  Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.
                - **MetricName** *(string) --* 
                  Name of the Amazon GameLift-defined metric that is used to trigger a scaling adjustment. For detailed descriptions of fleet metrics, see `Monitor Amazon GameLift with Amazon CloudWatch <https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html>`__ . 
                  * **ActivatingGameSessions** -- Game sessions in the process of being created. 
                  * **ActiveGameSessions** -- Game sessions that are currently running. 
                  * **ActiveInstances** -- Fleet instances that are currently running at least one game session. 
                  * **AvailableGameSessions** -- Additional game sessions that fleet could host simultaneously, given current capacity. 
                  * **AvailablePlayerSessions** -- Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included. 
                  * **CurrentPlayerSessions** -- Player slots in active game sessions that are being used by a player or are reserved for a player.  
                  * **IdleInstances** -- Active instances that are currently hosting zero game sessions.  
                  * **PercentAvailableGameSessions** -- Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy. 
                  * **PercentIdleInstances** -- Percentage of the total number of active instances that are hosting zero game sessions. 
                  * **QueueDepth** -- Pending game session placement requests, in any queue, where the current fleet is the top-priority destination. 
                  * **WaitTime** -- Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination.  
                - **PolicyType** *(string) --* 
                  Type of scaling policy to create. For a target-based policy, set the parameter *MetricName* to 'PercentAvailableGameSessions' and specify a *TargetConfiguration* . For a rule-based policy set the following parameters: *MetricName* , *ComparisonOperator* , *Threshold* , *EvaluationPeriods* , *ScalingAdjustmentType* , and *ScalingAdjustment* .
                - **TargetConfiguration** *(dict) --* 
                  Object that contains settings for a target-based scaling policy.
                  - **TargetValue** *(float) --* 
                    Desired value to use with a target-based scaling policy. The value must be relevant for whatever metric the scaling policy is using. For example, in a policy using the metric PercentAvailableGameSessions, the target value should be the preferred size of the fleet's buffer (the percent of capacity that should be idle and ready for new game sessions).
        :type FleetId: string
        :param FleetId: **[REQUIRED]**
          Unique identifier for a fleet to retrieve scaling policies for.
        :type StatusFilter: string
        :param StatusFilter:
          Scaling policy status to filter results on. A scaling policy is only in force when in an ``ACTIVE`` status.
          * **ACTIVE** -- The scaling policy is currently in force.
          * **UPDATEREQUESTED** -- A request to update the scaling policy has been received.
          * **UPDATING** -- A change is being made to the scaling policy.
          * **DELETEREQUESTED** -- A request to delete the scaling policy has been received.
          * **DELETING** -- The scaling policy is being deleted.
          * **DELETED** -- The scaling policy has been deleted.
          * **ERROR** -- An error occurred in creating the policy. It should be removed and recreated.
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


class ListAliases(Paginator):
    def paginate(self, RoutingStrategyType: str = None, Name: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`GameLift.Client.list_aliases`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/ListAliases>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              RoutingStrategyType='SIMPLE'|'TERMINAL',
              Name='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Aliases': [
                    {
                        'AliasId': 'string',
                        'Name': 'string',
                        'AliasArn': 'string',
                        'Description': 'string',
                        'RoutingStrategy': {
                            'Type': 'SIMPLE'|'TERMINAL',
                            'FleetId': 'string',
                            'Message': 'string'
                        },
                        'CreationTime': datetime(2015, 1, 1),
                        'LastUpdatedTime': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the returned data in response to a request action.
            - **Aliases** *(list) --* 
              Collection of alias records that match the list request.
              - *(dict) --* 
                Properties describing a fleet alias.
                *  CreateAlias   
                *  ListAliases   
                *  DescribeAlias   
                *  UpdateAlias   
                *  DeleteAlias   
                *  ResolveAlias   
                - **AliasId** *(string) --* 
                  Unique identifier for an alias; alias IDs are unique within a region.
                - **Name** *(string) --* 
                  Descriptive label that is associated with an alias. Alias names do not need to be unique.
                - **AliasArn** *(string) --* 
                  Unique identifier for an alias; alias ARNs are unique across all regions.
                - **Description** *(string) --* 
                  Human-readable description of an alias.
                - **RoutingStrategy** *(dict) --* 
                  Alias configuration for the alias, including routing type and settings.
                  - **Type** *(string) --* 
                    Type of routing strategy.
                    Possible routing types include the following:
                    * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to active fleets. 
                    * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded. 
                  - **FleetId** *(string) --* 
                    Unique identifier for a fleet that the alias points to.
                  - **Message** *(string) --* 
                    Message text to be used with a terminal routing strategy.
                - **CreationTime** *(datetime) --* 
                  Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").
                - **LastUpdatedTime** *(datetime) --* 
                  Time stamp indicating when this data object was last modified. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").
        :type RoutingStrategyType: string
        :param RoutingStrategyType:
          Type of routing to filter results on. Use this parameter to retrieve only aliases of a certain type. To retrieve all aliases, leave this parameter empty.
          Possible routing types include the following:
          * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to active fleets.
          * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded.
        :type Name: string
        :param Name:
          Descriptive label that is associated with an alias. Alias names do not need to be unique.
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


class ListBuilds(Paginator):
    def paginate(self, Status: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`GameLift.Client.list_builds`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/ListBuilds>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Status='INITIALIZED'|'READY'|'FAILED',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Builds': [
                    {
                        'BuildId': 'string',
                        'Name': 'string',
                        'Version': 'string',
                        'Status': 'INITIALIZED'|'READY'|'FAILED',
                        'SizeOnDisk': 123,
                        'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX',
                        'CreationTime': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the returned data in response to a request action.
            - **Builds** *(list) --* 
              Collection of build records that match the request.
              - *(dict) --* 
                Properties describing a custom game build.
        
        **Related operations**
                *  CreateBuild   
                *  ListBuilds   
                *  DescribeBuild   
                *  UpdateBuild   
                *  DeleteBuild   
                - **BuildId** *(string) --* 
                  Unique identifier for a build.
                - **Name** *(string) --* 
                  Descriptive label that is associated with a build. Build names do not need to be unique. It can be set using  CreateBuild or  UpdateBuild .
                - **Version** *(string) --* 
                  Version that is associated with a build or script. Version strings do not need to be unique. This value can be set using  CreateBuild or  UpdateBuild .
                - **Status** *(string) --* 
                  Current status of the build.
                  Possible build statuses include the following:
                  * **INITIALIZED** -- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.  
                  * **READY** -- The game build has been successfully uploaded. You can now create new fleets for this build. 
                  * **FAILED** -- The game build upload failed. You cannot create new fleets for this build.  
                - **SizeOnDisk** *(integer) --* 
                  File size of the uploaded game build, expressed in bytes. When the build status is ``INITIALIZED`` , this value is 0.
                - **OperatingSystem** *(string) --* 
                  Operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build.
                - **CreationTime** *(datetime) --* 
                  Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").
        :type Status: string
        :param Status:
          Build status to filter results by. To retrieve all builds, leave this parameter empty.
          Possible build statuses include the following:
          * **INITIALIZED** -- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.
          * **READY** -- The game build has been successfully uploaded. You can now create new fleets for this build.
          * **FAILED** -- The game build upload failed. You cannot create new fleets for this build.
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
    def paginate(self, BuildId: str = None, ScriptId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`GameLift.Client.list_fleets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/ListFleets>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              BuildId='string',
              ScriptId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'FleetIds': [
                    'string',
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the returned data in response to a request action.
            - **FleetIds** *(list) --* 
              Set of fleet IDs matching the list request. You can retrieve additional information about all returned fleets by passing this result set to a call to  DescribeFleetAttributes ,  DescribeFleetCapacity , or  DescribeFleetUtilization .
              - *(string) --* 
        :type BuildId: string
        :param BuildId:
          Unique identifier for a build to return fleets for. Use this parameter to return only fleets using the specified build. To retrieve all fleets, leave this parameter empty.
        :type ScriptId: string
        :param ScriptId:
          Unique identifier for a Realtime script to return fleets for. Use this parameter to return only fleets using the specified script. To retrieve all fleets, leave this parameter empty.
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


class SearchGameSessions(Paginator):
    def paginate(self, FleetId: str = None, AliasId: str = None, FilterExpression: str = None, SortExpression: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`GameLift.Client.search_game_sessions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/SearchGameSessions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              FleetId='string',
              AliasId='string',
              FilterExpression='string',
              SortExpression='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'GameSessions': [
                    {
                        'GameSessionId': 'string',
                        'Name': 'string',
                        'FleetId': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'TerminationTime': datetime(2015, 1, 1),
                        'CurrentPlayerSessionCount': 123,
                        'MaximumPlayerSessionCount': 123,
                        'Status': 'ACTIVE'|'ACTIVATING'|'TERMINATED'|'TERMINATING'|'ERROR',
                        'StatusReason': 'INTERRUPTED',
                        'GameProperties': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'IpAddress': 'string',
                        'Port': 123,
                        'PlayerSessionCreationPolicy': 'ACCEPT_ALL'|'DENY_ALL',
                        'CreatorId': 'string',
                        'GameSessionData': 'string',
                        'MatchmakerData': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the returned data in response to a request action.
            - **GameSessions** *(list) --* 
              Collection of objects containing game session properties for each session matching the request.
              - *(dict) --* 
                Properties describing a game session.
                A game session in ACTIVE status can host players. When a game session ends, its status is set to ``TERMINATED`` . 
                Once the session ends, the game session object is retained for 30 days. This means you can reuse idempotency token values after this time. Game session logs are retained for 14 days.
                *  CreateGameSession   
                *  DescribeGameSessions   
                *  DescribeGameSessionDetails   
                *  SearchGameSessions   
                *  UpdateGameSession   
                *  GetGameSessionLogUrl   
                * Game session placements 
                  *  StartGameSessionPlacement   
                  *  DescribeGameSessionPlacement   
                  *  StopGameSessionPlacement   
                - **GameSessionId** *(string) --* 
                  Unique identifier for the game session. A game session ARN has the following format: ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token>`` .
                - **Name** *(string) --* 
                  Descriptive label that is associated with a game session. Session names do not need to be unique.
                - **FleetId** *(string) --* 
                  Unique identifier for a fleet that the game session is running on.
                - **CreationTime** *(datetime) --* 
                  Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").
                - **TerminationTime** *(datetime) --* 
                  Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").
                - **CurrentPlayerSessionCount** *(integer) --* 
                  Number of players currently in the game session.
                - **MaximumPlayerSessionCount** *(integer) --* 
                  Maximum number of players that can be connected simultaneously to the game session.
                - **Status** *(string) --* 
                  Current status of the game session. A game session must have an ``ACTIVE`` status to have player sessions.
                - **StatusReason** *(string) --* 
                  Provides additional information about game session status. ``INTERRUPTED`` indicates that the game session was hosted on a spot instance that was reclaimed, causing the active game session to be terminated.
                - **GameProperties** *(list) --* 
                  Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ). You can search for active game sessions based on this custom data with  SearchGameSessions .
                  - *(dict) --* 
                    Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the `Amazon GameLift Developer Guide <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__ .
                    - **Key** *(string) --* 
                      Game property identifier.
                    - **Value** *(string) --* 
                      Game property value.
                - **IpAddress** *(string) --* 
                  IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
                - **Port** *(integer) --* 
                  Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.
                - **PlayerSessionCreationPolicy** *(string) --* 
                  Indicates whether or not the game session is accepting new players.
                - **CreatorId** *(string) --* 
                  Unique identifier for a player. This ID is used to enforce a resource protection policy (if one exists), that limits the number of game sessions a player can create.
                - **GameSessionData** *(string) --* 
                  Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__ ).
                - **MatchmakerData** *(string) --* 
                  Information about the matchmaking process that was used to create the game session. It is in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see `Match Data <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__ . Matchmaker data is useful when requesting match backfills, and is updated whenever new players are added during a successful backfill (see  StartMatchBackfill ). 
        :type FleetId: string
        :param FleetId:
          Unique identifier for a fleet to search for active game sessions. Each request must reference either a fleet ID or alias ID, but not both.
        :type AliasId: string
        :param AliasId:
          Unique identifier for an alias associated with the fleet to search for active game sessions. Each request must reference either a fleet ID or alias ID, but not both.
        :type FilterExpression: string
        :param FilterExpression:
          String containing the search criteria for the session search. If no filter expression is included, the request returns results for all game sessions in the fleet that are in ``ACTIVE`` status.
          A filter expression can contain one or multiple conditions. Each condition consists of the following:
          * **Operand** -- Name of a game session attribute. Valid values are ``gameSessionName`` , ``gameSessionId`` , ``gameSessionProperties`` , ``maximumSessions`` , ``creationTimeMillis`` , ``playerSessionCount`` , ``hasAvailablePlayerSessions`` .
          * **Comparator** -- Valid comparators are: ``=`` , ``<>`` , ``<`` , ``>`` , ``<=`` , ``>=`` .
          * **Value** -- Value to be searched for. Values may be numbers, boolean values (true/false) or strings depending on the operand. String values are case sensitive and must be enclosed in single quotes. Special characters must be escaped. Boolean and string values can only be used with the comparators ``=`` and ``<>`` . For example, the following filter expression searches on ``gameSessionName`` : \"``FilterExpression\": \"gameSessionName = \'Matt\\\'s Awesome Game 1\'\"`` .
          To chain multiple conditions in a single expression, use the logical keywords ``AND`` , ``OR`` , and ``NOT`` and parentheses as needed. For example: ``x AND y AND NOT z`` , ``NOT (x OR y)`` .
          Session search evaluates conditions from left to right using the following precedence rules:
          * ``=`` , ``<>`` , ``<`` , ``>`` , ``<=`` , ``>=``
          * Parentheses
          * NOT
          * AND
          * OR
          For example, this filter expression retrieves game sessions hosting at least ten players that have an open player slot: ``\"maximumSessions>=10 AND hasAvailablePlayerSessions=true\"`` .
        :type SortExpression: string
        :param SortExpression:
          Instructions on how to sort the search results. If no sort expression is included, the request returns results in random order. A sort expression consists of the following elements:
          * **Operand** -- Name of a game session attribute. Valid values are ``gameSessionName`` , ``gameSessionId`` , ``gameSessionProperties`` , ``maximumSessions`` , ``creationTimeMillis`` , ``playerSessionCount`` , ``hasAvailablePlayerSessions`` .
          * **Order** -- Valid sort orders are ``ASC`` (ascending) and ``DESC`` (descending).
          For example, this sort expression returns the oldest active sessions first: ``\"SortExpression\": \"creationTimeMillis ASC\"`` . Results with a null value for the sort operand are returned at the end of the list.
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
